from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.main, name='home'),
    path('about', views.FAQ, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('authorization', views.authorization, name='authorization'),
    path('delivery', views.delivery, name='delivery'),
    path('payment', views.payment, name='payment'),
    path('offer', views.offer, name='offer'),
    path('favorite', views.favorite, name='favorite'),
    path('shopping', views.shopping, name='shopping'),
    path('productprimer/kostyum/muzhskoy', views.productprimer_kostyum_muzhskoy, name='product-1'),
    path('productprimer/kostyum/zhenskiy', views.productprimer_kostyum_zhenskiy, name='product-2'),
    path('productprimer/noutbuk', views.productprimer_noutbuk, name='product-3'),
    path('productprimer/smartfon', views.productprimer_smartfon, name='product-4'),
    path('productprimer/smart_chasy', views.productprimer_smart_chasy, name='product-5'),
    path('productprimer/ruchka', views.productprimer_ruchka, name='product-6'),
    path('productprimer/stol/rukovoditelya', views.productprimer_stol_rukovoditelya, name='product-7'),
    path('productprimer/kreslo/rukovoditelya', views.productprimer_kreslo_rukovoditelya, name='product-8'),
    path('productprimer/lampa/nastolnaya', views.productprimer_lampa_nastolnaya, name='product-9'),
    path('productprimer/chashka/dlya/kofe', views.productprimer_chashka_dlya_kofe, name='product-10'),
    path('productprimer/kniga/o/biznese', views.productprimer_kniga_o_biznese, name='product-11'),
    path('productprimer/kashpo', views.productprimer_kashpo, name='product-12')
]
