from django.shortcuts import render
from django.views.generic import View
from .models import *
# Create your views here.
class Base(View):
    views = {}

class HomeView(Base):
    def get(self,request):
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['hots'] = Product.objects.filter(labels = 'hot')
        self.views['news'] = Product.objects.filter(labels='new')
        self.views['sale'] = Product.objects.filter(labels='sale')
        return render(request,'index.html',self.views)