from django.shortcuts import render,redirect
from bookstoreapp.forms import AddbookForm,OrderUpdateForm
# from bookstoreapp import forms
from bookstoreapp.models import Book,Order
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView,TemplateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from bookstoreapp.decorators import signin_required,admin_permission_required
from .filters import BookFilter,OrderFilter
# Create your views here.


# def Add_book(request):
#     if request.method=="GET":
#
#         form=AddbookForm
#
#         context={}
#         context["form"]=form
#
#         return render(request,"book_add.html",context)
#
#     if request.method=="POST":
#         form=AddbookForm(request.POST,request.FILES)
#         if form.is_valid():
#
#             form.save()                 #model form
#
#             # print(form.cleaned_data)
#             # book_name=form.cleaned_data["BOOK_NAME"]
#             # book_author=form.cleaned_data["AUTHOR"]
#             # book_price=form.cleaned_data["PRICE"]
#             # book_copies=form.cleaned_data["COPIES"]
#             #
#             # book=Book.objects.create(name=book_name,author=book_author,price=book_price,copies=book_copies)
#             # book.save()
#             print("BOOK SAVED")
#
#
#
#             return redirect("listbook")  #from url
#
#         else:
#             return render(request,"book_add.html",{'form':form})

# @method_decorator(admin_permission_required,name="dispatch")
class BookAddView(CreateView):
    model = Book
    success_url =reverse_lazy("listbook")
    form_class = AddbookForm
    template_name = "book_add.html"


#
# def list_book(request):
#     books=Book.objects.all()
#     context={}
#     context["books"]=books
#
#     return render(request,"book_list.html",context)

# @method_decorator(signin_required,name="dispatch")
class ListBookView(ListView):
    model=Book
    template_name = "book_list.html"
    context_object_name = "books"



# def remove_book(request,id):
#     books=Book.objects.get(id=id)
#     books.delete()
#
#     return redirect("listbook")

# @method_decorator(admin_permission_required,name="dispatch")
class BookDeleteView(DeleteView):
    model = Book
    template_name = "bookdelete.html"
    success_url = reverse_lazy("listbook")
    pk_url_kwarg = "id"


# def change_book(request,id):
#     book=Book.objects.get(id=id)
#     if request.method=="GET":
#
#
#         form=AddbookForm(instance=book)
#
#
#         # form=AddbookForm(initial={
#         #     "BOOK_NAME":book.name,
#         #     "AUTHOR":book.author,
#         #     "PRICE":book.price,
#         #     "COPIES": book.copies,
#         #
#         # })
#
#         context={}
#         context["form"]=form
#
#         return render(request,"book_edit.html",context)
#     if request.method=="POST":
#         form=AddbookForm(request.POST,instance=book)
#         if form.is_valid():
#
#             form.save()
#
#             # book.name=form.cleaned_data["BOOK_NAME"]
#             # book.author=form.cleaned_data["AUTHOR"]
#             # book.price=form.cleaned_data["PRICE"]
#             # book.copies=form.cleaned_data["COPIES"]
#             # book.save()
#             return redirect("listbook")
#
#
# # def bookview(request,id):
# #     book=Book.objects.get(id=id)
# #
# #     context={}
# #     context["book"]=book
# #
# #     return render(request,"bookview.html",context)

# @method_decorator(admin_permission_required,name="dispatch")
class BookUpdateView(UpdateView):
    model = Book
    form_class = AddbookForm
    success_url = reverse_lazy("listbook")
    pk_url_kwarg = "id"
    template_name = "book_edit.html"



# @method_decorator(signin_required,name="dispatch")
class BookDetialView(DetailView):
    model=Book
    template_name = "bookview.html"
    context_object_name = "books"
    pk_url_kwarg = "id"

# @method_decorator(admin_permission_required,name="dispatch")
class ViewCustomerOrders(ListView):
    model=Order
    template_name = "customer_orders.html"
    context_object_name = "orders"

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)

        neworders=self.model.objects.filter(status="order placed")
        context["neworders"]=neworders

        deliveredorders=self.model.objects.filter(status="Delivered")
        context["deliveredorder"]=deliveredorders

        context["neworder_count"]=neworders.count()
        context["deliveredorder_count"]=deliveredorders.count()

        return context

class CustomerOrderDetials(DetailView):
    model=Order
    template_name = "customerorderdetials.html"
    pk_url_kwarg = "id"
    context_object_name = "vieworder"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)

        order_detials=self.model.objects.filter(status="order placed")
        context["orderdetials"]=order_detials

        return context

class OrderUpdateView(UpdateView):
    model=Order
    form_class =OrderUpdateForm
    template_name = "orderupdate.html"
    pk_url_kwarg = "id"
    # success_url = reverse_lazy("bookview")


class BookSearchView(TemplateView):
    template_name = "books.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        f = BookFilter(self.request.GET, queryset=Book.objects.all())
        context["filter"] = f

        return context

class OrderSearchView(TemplateView):
    template_name = "ordersearch.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        f=OrderFilter(self.request.GET,queryset=Order.objects.all())
        context["filter"]=f

        return context