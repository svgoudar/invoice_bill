from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse, redirect
from rest_framework import serializers, viewsets, decorators, response
from django.contrib import messages

from .models import items
from .serializer import ItemtSerializer
from rest_framework import viewsets
from .forms import purchaseForm
from django.http import JsonResponse
from django.contrib.auth.models import User
import inspect
from rest_framework.authentication import SessionAuthentication
# from .custompermissions import MyPermission
from django.views import View
from django.shortcuts import reverse
from datetime import datetime

import os
import requests


def gen_bill(request):
    return render(request, 'apistore_app/invoice.html')


class purchaseviewset(viewsets.GenericViewSet):
    http_method_names = ['get']
    lookup_field = 'pk'
    tax = {'Medicine': 5, 'Food': 5, 'Music': 3, 'Total': 5, 'Imported': 18}

    queryset = items.objects.all()
    serializer_class = ItemtSerializer


    def get_amount(self, key, value):
        return float(value * (1 + float(self.tax.get(key, 0) / 100)))

    def get_bill(self, value_list):
        for i in value_list:
            i['final_price'] = round(self.get_amount(i.get('item_category', 0), i['price']), 4)
            i['applied_tax'] = self.tax.get(i.get('item_category'), 0)
            i['purchased_date'] = datetime.fromisoformat(str(i.get("purchased_date"))).ctime()

        return value_list

    def get_queryset(self):
        user = self.request.user
        user = get_object_or_404(User, id=user.id)
        return items.objects.filter(customer=user)

    @decorators.action(methods=['get'], detail=False)
    def generate_bill(self, request):
        api_data = list(self.get_queryset().values())
        total_before_tax = sum(map(lambda x: x.get('final_price'), self.get_bill(api_data)))
        total = self.get_amount('Total', total_before_tax) if round(total_before_tax) >= 2000 else total_before_tax

        api_data.append({'total': round(total_before_tax),
                  'applied_tax_on_total_amount': self.tax.get('Total') if total_before_tax >= 2000 else 0,
                  'final_total':round(total)})
       
        return JsonResponse(api_data, safe=False)


@login_required(login_url='/login/')
def purchase_view(request):
    user = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        form = purchaseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            inter_form = form.save(commit=False)
            inter_form.customer = user
            inter_form.save()
            messages.success(request, f'Congrats !! You have purchased {inter_form.item} !!')
            return redirect('purchase')

    else:
        form = purchaseForm()
    return render(request, 'apistore_app/index.html', {'form': form})
