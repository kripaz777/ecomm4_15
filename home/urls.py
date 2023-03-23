from .views import *
from django.urls import path
app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
    path('brand/<slug>', BrandView.as_view(), name='brand'),
    path('product/<slug>', ProductDetailView.as_view(), name='product'),
    path('search', SearchView.as_view(), name='search'),
]