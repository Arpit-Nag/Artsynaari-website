from django.contrib import admin
from .models import MusesImage,Product,yarn,ProductImage,Category,Slot,ProductRequest,Muses
from django.contrib.admin.options import InlineModelAdmin
# Register your models here.
admin.site.register(Category)
# admin.site.register(Slot)
# admin.site.register(ProductRequest)
admin.site.register(yarn)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # fields=['title','price']
    list_display=['title','category','price']
    inlines=[ProductImageAdmin]
    class Meta:
        model=Product
#
# @admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass

class MusesImageAdmin(admin.StackedInline):
    model = MusesImage

@admin.register(Muses)
class MusesAdmin(admin.ModelAdmin):
    inlines=[MusesImageAdmin]
    class Meta:
        model = Muses

# @admin.register(MusesImage)
class MusesImageAdmin(admin.ModelAdmin):
    pass

class SlotAdmin(admin.TabularInline):
    model = Slot
    max_num = 1


@admin.register(ProductRequest)
class ProductRequestAdmin(admin.ModelAdmin):
    inlines=[SlotAdmin]
    class Meta:
        model=ProductRequest

@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    pass
