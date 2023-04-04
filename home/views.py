from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
from django.contrib  import messages
from django.contrib.auth.models import User
# Create your views here.
def count_cart(request):
    username = request.user.username
    cart_number = Cart.objects.filter( username=username, checkout=False).count()
    return cart_number
class Base(View):
    views = {}
    views['categories'] = Category.objects.all()
    views['brands'] = Brand.objects.all()

class HomeView(Base):
    def get(self,request):
        self.views
        self.views['cart_no'] = count_cart(request)
        self.views['ads'] = Ad.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['hots'] = Product.objects.filter(labels = 'hot')
        self.views['news'] = Product.objects.filter(labels='new')
        self.views['sale'] = Product.objects.filter(labels='sale')
        return render(request,'index.html',self.views)

class CategoryView(Base):
    def get(self,request,slug):
        self.views
        self.views['cart_no'] = count_cart(request)
        ids = Category.objects.get(slug = slug).id
        self.views['product_category'] = Product.objects.filter(category_id = ids)

        return render(request,'category.html',self.views)

class BrandView(Base):
    def get(self,request,slug):
        self.views
        self.views['cart_no'] = count_cart(request)
        ids = Brand.objects.get(slug = slug).id
        self.views['product_brand'] = Product.objects.filter(brand_id = ids)

        return render(request,'brand.html',self.views)

class ProductDetailView(Base):
    def get(self,request,slug):
        self.views
        self.views['cart_no'] = count_cart(request)
        self.views['product_detail'] = Product.objects.filter(slug = slug)
        self.views['product_review'] = ProductReview.objects.filter(slug = slug)
        return render(request,'product-detail.html',self.views)


class SearchView(Base):
    def get(self,request):
        self.views
        self.views['cart_no'] = count_cart(request)
        query = request.GET.get('query')
        if query !='':
            self.views['search_product'] = Product.objects.filter(name__icontains = query)
        else:
            return redirect('/')
        return render(request, 'search.html', self.views)


def productReview(request,slug):
    if request.method == 'POST':
        username = request.user.username
        email = request.user.email
        comment = request.POST['comment']
        star = request.POST['star']
        data = ProductReview.objects.create(
            name = username,
            email = email,
            review = comment,
            star = star,
            slug = slug
        )
        data.save()
    return redirect(f'/product/{slug}')

def signup(request):
    if request.method == 'POST':
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request,'The username is already taken!')
                return redirect('/signup')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'The email is already in use!')
                return redirect('/signup')
            else:
                user = User.objects.create(
                    username = username,
                    email = email,
                    first_name = f_name,
                    last_name = l_name,
                    password = password
                )
                user.save()
                return redirect('/accounts/login')
        else:
            messages.error(request, 'The password and confirm password is not same!')
            return redirect('/signup')

    return render(request,'signup.html')

class CartView(Base):
    def get(self,request):
        self.views
        self.views['cart_no'] = count_cart(request)
        username = request.user.username
        cart_info = Cart.objects.filter(username = username,checkout = False)
        self.views['cart_product'] = cart_info
        all_total = 0
        for i in cart_info:
            print(i)
            all_total = all_total + i.total
        self.views['all_total'] = all_total
        self.views['shipping'] = 50
        self.views['grand_total'] =  all_total + self.views['shipping']

        return render(request,'cart.html',self.views)
def add_to_cart(request,slug):
    username = request.user.username
    if Cart.objects.filter(slug = slug,username=username,checkout = False).exists():
        quantity = Cart.objects.get(slug = slug,username=username,checkout = False).quantity
        price = Product.objects.get(slug=slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price
        if discounted_price > 0:
            original_price = discounted_price
        else:
            original_price = price
        quantity = quantity + 1
        total = quantity * original_price
        Cart.objects.filter(slug=slug, username=username, checkout=False).update(total = total,quantity = quantity)
        return redirect('/cart')
    else:
        price = Product.objects.get(slug=slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price
        if discounted_price > 0:
            total = discounted_price
        else:
            total = price
        data = Cart.objects.create(
            username = username,
            slug = slug,
            items = Product.objects.filter(slug = slug)[0], #[{'price':2000,name:'Apple'}]
            total = total
        )
        data.save()
        return redirect('/cart')

def delete_cart(request,slug):
    username = request.user.username
    Cart.objects.filter(slug=slug, username=username, checkout=False).delete()
    return redirect('/cart')

def reduce_cart(request,slug):
    username = request.user.username
    if Cart.objects.filter(slug = slug,username=username,checkout = False).exists():
        quantity = Cart.objects.get(slug = slug,username=username,checkout = False).quantity
        price = Product.objects.get(slug=slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price
        if discounted_price > 0:
            original_price = discounted_price
        else:
            original_price = price
        if quantity >1:
            quantity = quantity -1
            total = quantity * original_price
            Cart.objects.filter(slug=slug, username=username, checkout=False).update(total = total,quantity = quantity)
            return redirect('/cart')
        else:
            messages.error(request, 'The quantity is already 1')
            return redirect('/cart')