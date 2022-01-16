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


class purchaseviewset(viewsets.GenericViewSet):
    http_method_names = ['get']
    lookup_field = 'pk'
    tax = {'Medicine': 5, 'Food': 5, 'music': 3, 'Total': 5, 'Imported': 18}

    queryset = items.objects.all()
    serializer_class = ItemtSerializer

    # def retreive(self,request,pk=None):

    def get_amount(self, key, value):
        # print("float(value * (1 + float(tax.get(key, 0) / 100)) ", float(value * (1 + float(self.tax.get(key, 0) / 100))))
        return float(value * (1 + float(self.tax.get(key, 0) / 100)))

    # total = sum(map(lambda x: , g))
    # print("Before sum   ", sum(map(lambda x: x.get('price', 0), g)))

    # print(get_amount('imported', 3000))

    def get_bill(self, value_list):
        for i in value_list:
            i['final_price'] = round(self.get_amount(i.get('item_category', 0), i['price']), 4)
            i['applied_tax'] = self.tax.get(i.get('item_category'), 0)
        return value_list

    def get_queryset(self):
        user = self.request.user
        user = get_object_or_404(User, id=user.id)
        return items.objects.filter(customer=user)

    @decorators.action(methods=['get'], detail=False)
    def generate_bill(self, request):
        # user = User.objects.get(username=request.user.username)
        # print("self.get_queryse: ",self.get_object())
        # for j in list(self.queryset):
        #     print(j)
        # print(list(self.get_queryset().values()))
        # return self.queryset
        # print(s())
        # print("self.get_queryset(): ",list(self.queryset))
        # d = dict(inspect.getmembers(self.get_queryset()))

        model_fields = list(map(lambda x: x.name, self.get_serializer_class().Meta.model._meta.get_fields()))
        print("fields : ", model_fields)
        # values = []
        f = list(self.get_queryset().values())
        tax = {'medicines': 5, 'Food': 5, 'music': 3, 'total': 5, 'imported': 18}

        # print(qs)
        # f = [x.i for x, i in (self.get_queryset(), model_fields)]
        # print(f)
        # for i in model_fields:

        # print("Model class : ",dict(inspect.signature(self.get_queryset().model).parameters))

        # print("fields : ",[x.name for x in m._meta.get_fields()])
        # print("d:  ",dict(d).get('__dict__'))
        v = list(self.get_queryset().values())
        total_before_tax = sum(map(lambda x: x.get('final_price'), self.get_bill(v)))
        # print(" total:  ", total)
        # print(int(total) >= 2000)
        total = self.get_amount('Total', total_before_tax) if int(total_before_tax) >= 2000 else total_before_tax

        v.append({'total': round(total_before_tax),
                  'applied_tax_on_total_amount': self.tax.get('Total') if total_before_tax >> 2000 else 0,
                  'final_total':round(total)})
        print("Total: ", total)
        print("list(self.get_queryset().values()) ", list(self.get_queryset().values()))
        return JsonResponse(v, safe=False)
        # return JsonResponse(list(self.get_queryset().values()), safe=False)


import os
import requests


def get_droplets():
    url = "https://127.0.0.1:8000/api/generate_bill"
    r = requests.get(url, verify=False)
    droplets = r.json()
    return droplets
    # print(droplets)
    # droplet_list = []
    # for i in range(len(droplets['droplets'])):
    #     droplet_list.append(droplets['droplets'][i])
    # return droplet_list


@login_required(login_url='/login/')
def purchase_view(request):
    user = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        form = purchaseForm(request.POST)
        if form.is_valid():
            # fields = ["item", "item_category", "quantity", "price"]

            data = form.cleaned_data
            # fields = {"item":data['item'],"item_category":data['item_category'],"quantity":data['quantity'],"price":data['price']}
            inter_form = form.save(commit=False)
            inter_form.customer = user
            # inter_form.customer.create(**fields)
            # print("choice name ",form.ord.label)
            inter_form.save()
            messages.success(request, f'Congrats !! You have purchased {inter_form.item} !!')
            return redirect('purchase')
            # return HttpResponse("<h1>Success</h1>")

    else:
        form = purchaseForm()
    return render(request, 'apistore_app/index.html', {'form': form})


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = items.objects.all()
    # serializer_class = StudentSerializer
    # authentication_classes = [SessionAuthentication]

    # permission_classes = [MyPermission]


from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)  # , link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def gen_bill(request):
    return render(request, 'apistore_app/invoice.html')


class GenerateInvoice(View):
    def get(self, request, pk, *args, **kwargs):
        try:
            user = get_object_or_404(User, id=request.user.id)
            order_db = items.objects.get(cutomer=user)  # you can filter using order_id as well
        except:
            return HttpResponse("505 Not Found")
        data = {
            'order_id': user.id,
            'user_email': user.email or 'noemail@mail.com',
            'date': str(user.last_login),
            'amount': order_db.total_amount,
        }
        pdf = render_to_pdf('firstapp/payment/invoice.html', data)
        # return HttpResponse(pdf, content_type='application/pdf')

        # force download
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % (data['order_id'])
            content = "inline; filename='%s'" % (filename)
            # download = request.GET.get("download")
            # if download:
            content = "attachment; filename=%s" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
