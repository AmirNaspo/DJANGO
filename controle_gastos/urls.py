from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from contas.views import *
from controle_gastos import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'url_home'),
    path('update/<int:pk>/', update, name = 'url_update'),
    path('listagem/', listagem, name = 'url_listagem'),
    path('delete/<int:pk>/', delete, name = 'url_delete'),
    path('individual/<int:pk>/', individual, name = 'url_individual'),
    path('Diretoria/', diretoria, name = 'url_diretoria'),
    path('blabla/',blabla, name = 'url_blabla'),
    path('accounts/', include('accounts.urls')),
    path ('accounts/', include('django.contrib.auth.urls')),
    path('perfil/', perfil, name = 'url_perfil'),
    path('upload-csv/', upload, name='upload.url'),
    path('render/pdf/', Pdf.as_view()),
    path('pont/',pont, name = 'url_pont'),
    #path('pont2/<int:pk>/',pont2, name = 'url_pont2'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

