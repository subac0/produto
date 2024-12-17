from django.contrib import admin
from django.urls import path, include
from produtos.views import listar_produtos, custom_login, custom_logout, custom_cadastro
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', custom_login, name='login'),  
    path('logout/', custom_logout, name='logout'),
    path('signup/', custom_cadastro, name='signup'),
    path('produtos/', include('produtos.urls')), 
    path('', listar_produtos, name='listar_produtos'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)