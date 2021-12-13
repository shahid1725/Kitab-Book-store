from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
from bookstoreapp.models import Book,Cart,Order
from django.views.generic import TemplateView,ListView
from django.contrib import messages
from django.utils.decorators import method_decorator
from bookstoreapp.decorators import signin_required
from django.db.models import Sum
from bookstoreapp.filters import BookFilter
# Create your views here.

# class BookAddView(CreateView):
#     model = Book
#     success_url =reverse_lazy("listbook")
#     form_class = AddbookForm
#     template_name = "book_add.html"
@method_decorator(signin_required,name="dispatch")
class CustomerView(TemplateView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        context = {"books": books}
        return render(request, 'home.html', context)


class SignUp(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.UserRegistrationForm()
        context = {}
        context["form"] = form
        return render(request, "user_registration.html", context)

    def post(self,request):
        context={}
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("user registered successfully")
            return redirect("signin")
        else:
            context["form"] = form
            return render(request, "user_registration.html", context)

class SignIn(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.LoginForm()
        context = {"form": form}
        return render(request, "logintemp.html", context)

    def post(self,request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if (user):
                login(request, user)
                return redirect("customerview")

            else:
                return render(request, "logintemp.html", {"form": form})

@method_decorator(signin_required,name="dispatch")
class AddToCart(TemplateView):
    model=Cart
    def get(self, request, *args, **kwargs):
        id=kwargs["id"]
        book=Book.objects.get(id=id)
        cart=Cart.objects.create(item=book,user=request.user)
        cart.save()
        messages.success(request,"Item added to cart successfully")
        return redirect("customerview")

@method_decorator(signin_required,name="dispatch")
class ViewMyCart(TemplateView):
    model=Cart
    template_name = "mycart.html"
    def get(self, request, *args, **kwargs):
        context={}
        items=Cart.objects.filter(user=request.user,status="incart")
        context["items"]=items

        total=Cart.objects.filter(user=request.user,status="incart").aggregate(Sum("item__price"))#well defined in Cart model page
        # print(total)
        context["total"]=total['item__price__sum']


        return render(request,self.template_name,context)



@method_decorator(signin_required,name="dispatch")
class RemoveItemCart(TemplateView):
    model=Cart

    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        cart=self.model.objects.get(id=id)
        cart.status="cancelled"
        cart.save()
        messages.success(request,"Item hasbeen removed from your cart")
        return redirect("customerview")

@method_decorator(signin_required,name="dispatch")
class OrderCreateView(TemplateView):
    model=Order
    form_class=forms.OrderForm
    template_name = "ordercreate.html"
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        cart_id=kwargs["id"]
        cart_item=Cart.objects.get(id=cart_id)

        form=self.form_class(request.POST)
        if form.is_valid():
            address=form.cleaned_data["address"]
            user=request.user.username
            item=cart_item.item

            order=self.model.objects.create(
                item=item,
                user=user,
                address=address
            )

            order.save()

            cart_item.status="orderplaced"
            cart_item.save()

            messages.success(request,"Order hasbeen placed")
            return redirect("customerview")


@method_decorator(signin_required,name="dispatch")
class ViewMyOrder(ListView):
    model=Order
    template_name = "myorder.html"
    context_object_name = "orders"

    def get_queryset(self):
        queryset=super().get_queryset()
        queryset=self.model.objects.filter(user=self.request.user)
        return queryset














# def customer_home(request):
#     books = Book.objects.all()
#     context = {"books": books}
#     return render(request, 'home.html', context)


# def signup(request):
#     form=forms.UserRegistrationForm()
#     context={}
#     context["form"]=form
#
#     if request.method=="POST":
#         form=forms.UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("user registered successfully")
#             return redirect("signin")
#         else:
#             context["form"]=form
#             return render(request,"user_registration.html",context)
#
#     return render(request,"user_registration.html",context)

# def signin(request):
#     form=forms.LoginForm()
#     context={"form":form}
#
#     if request.method=="POST":
#         form=forms.LoginForm(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data["username"]
#             password=form.cleaned_data["password"]
#             user=authenticate(request,username=username,password=password)
#             if(user):
#                 login(request,user)
#                 return redirect("customerview")
#
#             else:
#                 return render(request,"login.html",{"form":form})


    # return render(request,"login.html",context)

@signin_required
def signout(request):
    logout(request)
    return redirect("signin")



# CLASS BASED VIEWS
# FUNCTION BASED VIEWS

# from django.views.generic import....... CreateView......


# CREATE(CreateView)=>MODEL,FORM
# UPDATE(UpdateView)=>MODEL,TEMPLATE,INSTANCE,FORM
# LIST(ListView)=>MODEL,TEMPLATE
# DELETE(DeleteView)=>MODEL,INSTANCE
# VIEW(DetialView)=>MODEL,INSTANCE


