from django.urls import path
from customer import views



urlpatterns=[
    path('home',views.CustomerView.as_view(),name="customerview"),
    path('signup',views.SignUp.as_view(),name="signup"),
    path('signin',views.SignIn.as_view(),name="signin"),
    path('signout',views.signout,name="signout"),
    path('addcart/<int:id>',views.AddToCart.as_view(),name="addcart"),
    path('viewcart',views.ViewMyCart.as_view(),name="viewcart"),
    path('removecart/<int:id>',views.RemoveItemCart.as_view(),name="removecart"),
    path('buynow/<int:id>',views.OrderCreateView.as_view(),name="orderitem"),
    path('myorder',views.ViewMyOrder.as_view(),name="myorder"),


]
