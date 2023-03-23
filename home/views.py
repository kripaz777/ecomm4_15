from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
# Create your views here.
class Base(View):
    views = {}
    views['categories'] = Category.objects.all()
    views['brands'] = Brand.objects.all()

class HomeView(Base):
    def get(self,request):
        self.views
        self.views['ads'] = Ad.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['hots'] = Product.objects.filter(labels = 'hot')
        self.views['news'] = Product.objects.filter(labels='new')
        self.views['sale'] = Product.objects.filter(labels='sale')
        return render(request,'index.html',self.views)

class CategoryView(Base):
    def get(self,request,slug):
        self.views
        ids = Category.objects.get(slug = slug).id
        self.views['product_category'] = Product.objects.filter(category_id = ids)

        return render(request,'category.html',self.views)

class BrandView(Base):
    def get(self,request,slug):
        self.views
        ids = Brand.objects.get(slug = slug).id
        self.views['product_brand'] = Product.objects.filter(brand_id = ids)

        return render(request,'brand.html',self.views)

class ProductDetailView(Base):
    def get(self,request,slug):
        self.views
        self.views['product_detail'] = Product.objects.filter(slug = slug)

        return render(request,'product-detail.html',self.views)


class SearchView(Base):
    def get(self,request):
        self.views
        query = request.GET.get('query')
        if query !='':
            self.views['search_product'] = Product.objects.filter(name__icontains = query)
        else:
            return redirect('/')
        return render(request, 'search.html', self.views)