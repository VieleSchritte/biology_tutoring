# from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'bioblog_tasks'
urlpatterns = [
    path('', views.view_start_page, name='welcome'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
