from django.contrib import admin

# Register your models here.
from . models import *
class contactAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','message')

admin.site.register(contact,contactAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('cname','cpic','cdate','id')

admin.site.register(category,categoryAdmin)


class profileAdmin(admin.ModelAdmin):
    list_display=('name',"mobile","email","passwd",'ppic','address')
admin.site.register(profile,profileAdmin)

class newsAdmin(admin.ModelAdmin):
    list_display=('id',"city","headlines","subject",'newsdes','newspic','ndate','ncategory')
admin.site.register(news,newsAdmin)

class notificationAdmin(admin.ModelAdmin):
    list_display=('id','npic',"ndes","ndate")
admin.site.register(notification,notificationAdmin)

class videoAdmin(admin.ModelAdmin):
    list_display=('id',"vtitle","vdes","thumb","vlink","vdate")
admin.site.register(video,videoAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display=('id',"stitle","sdes","spic","sdate")
admin.site.register(slider,sliderAdmin)