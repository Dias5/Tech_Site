from django.shortcuts import render

def main(request):
    return render(request, 'main/home.html')

def FAQ(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def authorization(request):
    return render(request, 'main/authorization.html')

def delivery(request):
    return render(request, 'main/delivery.html')

def payment(request):
    return render(request, 'main/payment.html')

def offer(request):
    return render(request, 'main/offer.html')

def favorite(request):
    return render(request, 'main/favorite.html')

def shopping(request):
    return render(request, 'main/shopping.html')

def productprimer_kostyum_muzhskoy(request):
    return render(request, 'main/product/productprimer-kostyum-muzhskoy.html')

def productprimer_kostyum_zhenskiy(request):
    return render(request, 'main/product/productprimer-kostyum-zhenskiy.html')

def productprimer_noutbuk(request):
    return render(request, 'main/product/productprimer-noutbuk.html')

def productprimer_smartfon(request):
    return render(request, 'main/product/productprimer-smartfon.html')

def productprimer_smart_chasy(request):
    return render(request, 'main/product/productprimer-smart-chasy.html')

def productprimer_ruchka(request):
    return render(request, 'main/product/productprimer-ruchka.html')

def productprimer_stol_rukovoditelya(request):
    return render(request, 'main/product/productprimer-stol-rukovoditelya.html')

def productprimer_kreslo_rukovoditelya(request):
    return render(request, 'main/product/productprimer-kreslo-rukovoditelya.html')

def productprimer_lampa_nastolnaya(request):
    return render(request, 'main/product/productprimer-lampa-nastolnaya.html')

def productprimer_chashka_dlya_kofe(request):
    return render(request, 'main/product/productprimer-chashka-dlya-kofe.html')

def productprimer_kniga_o_biznese(request):
    return render(request, 'main/product/productprimer-kniga-o-biznese.html')

def productprimer_kashpo(request):
    return render(request, 'main/product/productprimer-kashpo.html')