from django.contrib import admin
from .models import Table, MenuItem, Order, OrderItem

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'qr_code')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_editable = ('price', 'available')
    search_fields = ('name',)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'table', 'created_at', 'is_completed')
    list_filter = ('is_completed', 'created_at')
    inlines = [OrderItemInline]
    readonly_fields = ('created_at',)
