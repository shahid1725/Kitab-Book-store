import django_filters
from .models import Book,Order

class BookFilter(django_filters.FilterSet):
    class Meta:
        model=Book
        fields=["name","author","price","copies"]

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model=Order
        fields=["item","user","order_date","status"]

