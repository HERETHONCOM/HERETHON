from django.contrib import admin
from django.urls import path, include
from ProjectApp import views
from django.conf.urls. static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main,name='main'),
    path('accounts/', include('allauth.urls')),
    path('new/', views.create, name="new"),
    path('art/',views.art,name='art'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)