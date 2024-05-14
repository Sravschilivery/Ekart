from django.urls import path
from storeapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('home',views.homepage),
    # path('contact',views.contactpage),
    # path('about',views.aboutpage),
    # path('edit/<id>',views.edit),
    # path('delete/<id>',views.delete),
    # path('addition/<x>/<y>',views.addition),
    path('',views.home),
    path('pdetails/<pid>',views.product_details),
    path('about',views.about),
    path('cart',views.cart),
    path('contact',views.contact),
    path('catfilter/<catv>',views.cat_filter),
    path('pricerange',views.pricerange),
    path('sort',views.sort),
    path('search',views.search),
    path('cart/<prod_id>',views.addtocart),
    path('removecart/<cid>',views.remove_cart),
    path('changeqty/<cid>',views.changeqty),
    path('placeorder',views.place_order),
    path('removeitem/<oid>',views.cancelorder),
    path('makepayment',views.make_payment),
    path('sendmail',views.sendmail)
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)