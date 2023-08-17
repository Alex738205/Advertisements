from django.db import models
from django.contrib import admin
from django.forms import ValidationError
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()

class TitleField(models.CharField):
    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if len(value) > 0 and value[0] == '?':
            raise ValidationError('Заголовок не может начинаться свопросительного знака')
class Advertisement(models.Model):
    title = TitleField('Заголовок', max_length = 128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена',max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг',help_text='Торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name = "Пользователь", on_delete = models.CASCADE)
    image = models.ImageField("Изображение", upload_to="advertisements/")
    
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
    
    @admin.display(description='Иконка')
    def image_small(self):
        if self.image != '':
            return format_html('<img src="{}" alt="Иконка" style="object-fit:cover;width:32px;height:32px"></img>', self.image.url)
        return ''    
