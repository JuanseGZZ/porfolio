from django.urls import path
from . import views
from .views import contact_view

app_name="portfolio"
urlpatterns = [
    path("", views.index, name="index"),
    path('contact/', views.contact_view, name='contact'),
]
