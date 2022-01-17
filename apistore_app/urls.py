from django.urls import path, include
from .views import purchaseviewset, purchase_view, gen_bill
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', purchaseviewset)
urlpatterns = [
    path('', purchase_view, name='purchase'),
    path('gen/', gen_bill, name='generate'),
    path('api/', include(router.urls))
]
