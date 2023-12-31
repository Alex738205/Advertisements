from dataclasses import fields
from email.mime import image
from django.contrib import admin
from .models import Advertisement
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description', 
        'price', 
        'auction',
        'created_date',
        'updated_date',
        'image_small'
    ]
    
    list_filter = [
        'auction',
        'created_at'
    ]
    
    actions = [
        'make_action_as_false',
        'make_action_as_true'
    ]
    
    fieldsets = (
        (
            'Общие', {
                'fields': ('title', 'description','image'), 
            }
        ),
        (
            'Финансы', {
                'fields': ('price', 'auction'),
                'classes': ['collapse']
            }
        )
    )
    
    @admin.action(description='Убрать возможность торга')
    def make_action_as_false(self,request,queryset):
        queryset.update(auction=False)
        
    @admin.action(description='Дoбавить возможность торга')
    def make_action_as_true(self,request,queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement,AdvertisementAdmin)
