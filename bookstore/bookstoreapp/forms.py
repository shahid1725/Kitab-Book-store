from django import forms
from django.forms import ModelForm

from bookstoreapp.models import Book, Order


# class AddbookForm(forms.Form):
#     BOOK_NAME=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     AUTHOR=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     PRICE=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     COPIES=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#
#     def clean(self):
#         cleaned_data=super().clean()
#         PRICE=cleaned_data["PRICE"]
#         COPIES=cleaned_data["COPIES"]
#
#         if PRICE<0:
#
#             msg="Invalid price"
#             self.add_error("PRICE",msg)
#
#         if COPIES < 0:
#             msg="invalid copies"
#             self.add_error("COPIES",msg)


class AddbookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["name", "author", "price", "copies", "image"]  # modelile fields  or "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "copies": forms.NumberInput(attrs={"class": "form-control"})
        }

        labels = {
            'name': 'BOOK NAME',
            'author': 'AUTHOR',
            "price": "PRICE",
            "copies": "COPIES"

        }

class OrderUpdateForm(ModelForm):
    class Meta:
        model = Order
        fields = ["status", "expected_delivery_date"]
        widgets = {
            "status": forms.Select(attrs={"class": "form-select"}),
            "expected_delivery_date": forms.DateInput(attrs={"type":"date"})
        }
