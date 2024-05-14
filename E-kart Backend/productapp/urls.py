from django.urls import path
from productapp import views
urlpatterns = [
    path('home',views.homepage),
    path('addproduct',views.add_product),
    path('productdash',views.product_dashboard),
    path('delete/<pid>',views.delete_product),
    path('edit/<pid>',views.update_product),


]