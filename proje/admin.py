from django.contrib import admin
from proje.models import Mansets, Sample, Comment
# Register your models here.


class ManstesAdmin(admin.ModelAdmin):  
    list_display= ['ustyazi','yazi']
    list_filter = ['ustyazi','yazi']
    list_display_links = ['ustyazi']

    class Meta:

        model = Mansets


admin.site.register(Mansets,ManstesAdmin)

class SampleAdmin(admin.ModelAdmin):
    list_display= ['baslik','blog']
    list_filter = ['baslik','blog']
    list_display_links = ['baslik']


    class Meta:

        model = Sample


admin.site.register(Sample,SampleAdmin)
  





admin.site.register(Comment) 