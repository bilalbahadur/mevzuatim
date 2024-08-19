
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from proje.views import index, redirect_hakkimizda, redirect_mansetler, redirect_blog, redirect_iletisim, redirect_manset_detail





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('hakkimizda', redirect_hakkimizda, name='hakkimizda'),
    path('mansetler', redirect_mansetler, name='mansetler'),
    path('blog', redirect_blog, name='blog'),
    path('iletisim', redirect_iletisim, name='iletisim'),

    path('mansetler/<int:manset_id>/', redirect_manset_detail, name='manset_detail'),
    
  path('hakkimizda.html', redirect_hakkimizda),
    path('mansetler.html', redirect_mansetler),
    path('blog.html', redirect_blog),
    path('iletisim.html', redirect_iletisim),
     path('manset/<int:manset_id>/', redirect_manset_detail, name='redirect_manset_detail'),
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)