from django.contrib import admin
from productapp.models import Product
# Register your models here.
#admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','qty','cat','is_available']
    list_filter=('cat','is_available')

admin.site.register(Product,ProductAdmin)
admin.site.site_header="Ekart Dashboard"
admin.site.site_title="Ekart"