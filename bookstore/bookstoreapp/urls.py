from django.urls import path
from bookstoreapp import views

urlpatterns=[
    path("add",views.BookAddView.as_view(),name="addbook"),
    path("list",views.ListBookView.as_view(),name="listbook"),
    path("remove/<int:id>",views.BookDeleteView.as_view(),name="removebook"),
    path("change/<int:id>",views.BookUpdateView.as_view(),name="changebook"),
    path("view/<int:id>",views.BookDetialView.as_view(),name="bookview"),
    path("customer/order",views.ViewCustomerOrders.as_view(),name="customerorder"),
    path("customer/orderdetials/<int:id>",views.CustomerOrderDetials.as_view(),name="customerorderdetials"),
    path("orders/update/<int:id>",views.OrderUpdateView.as_view(),name="orderupdate"),
    path("findbook",views.BookSearchView.as_view(),name="findbook"),
    path("findorder",views.OrderSearchView.as_view(),name="findorder")
]