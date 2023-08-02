from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length = 128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена',max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг',help_text='Торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table='advertisements'
    
    def __str__(self):
        return f'Advertisement(id={self.pk}, title={self.title}, price={self.price})'
    
    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            s = self.created_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color:green;fon-weight: bold">Сегодня в {}</span>',s)
        return self.created_at.strftime('%d.%m.%Y %H:%M:%S')    
    
    @admin.display(description='Дата обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            s = self.updated_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color:red;fon-weight: bold">Сегодня в {}</span>',s)
        return self.updated_at.strftime('%d.%m.%Y %H:%M:%S')    

