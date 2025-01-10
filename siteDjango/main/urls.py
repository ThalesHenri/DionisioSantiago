from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('comprarProduto/<int:produto_id>/', views.comprarProduto, name='comprarProduto'),
    path('contato/', views.contato, name='contato'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)