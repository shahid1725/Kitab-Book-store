from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=120,unique=True)
    author=models.CharField(max_length=120)
    price=models.PositiveIntegerField(default=0)
    copies=models.PositiveIntegerField(default=0)
    image=models.ImageField(upload_to="bookimages",null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    item=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    options=(("incart","incart"),("cancelled","cancelled"),("ordered","ordered"))
    status=models.CharField(max_length=120,choices=options,default="incart")



class Order(models.Model):
    item=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.CharField(max_length=40)
    address=models.CharField(max_length=120)
    order_date=models.DateField(auto_now_add=True)

    options=(
        ("order placed","order placed"),
        ("Dispatched","Dispatched"),
        ("Cancelled","Cancelled"),
        ("Delivered","Delivered")
    )
    status=models.CharField(max_length=120,choices=options,default="order placed")
    expected_delivery_date=models.DateField(null=True,blank=True)

#TOTAL AMOUNT IN CART --SHELL
#  from bookstoreapp.models import Book,Cart
#  from django.db.models import Sum
# total=Cart.objects.filter(user__username="shahid",status="incart").aggregate(Sum("item__price"))





#ORM

#CREATE

    # ref_name=Model name(field1="value1",field2="value2")
    # ref_name.save()

#fetch all books

    # ref_name=Model name.Objects.all()

#(lte-lessthanequal,lt=lessthan,gte,gt)

#price below 350

    # ref_name=Model name.objects.filter(price__lte=350)
    # ref name

#copies 6 above

    # ref_name=model name.objects.filter(copies__gt=6)
    # ref name

#print prices and name of book

    # ref name= model name.objects.all()
    # for xyz in ref name:
            #print(xyz.price,xyz.name)

#price bw 300 to 600

    # ref name=model name.objects.filter(price__gt=300,price__lt=600)
    # ref name

#Detials of specific book

    # ref name= model name.objects.filter(name="AADU JEEVITHAM")
    # for xyz in ref name:
        #print(xyz.price),rint(xyz,author)



    #--->for case sensitive

    # ref name=model name.objects.filter(name__iexact="aadujeevitham")
    # ref name

    #contains

    #to check similiar books(eg:indulekha,india)
        # ref name=model name.objects.filter(name__contains="IND")
        # ref name


#TO DELETE

    # ref name=model name.objects.get(name="test")
    # ref name.delete()

#UPDATE

    # ref name=model name.objects.get(id=3)
    # ref name.price=1000,ref name.copies=3000
    # ref name .save()

#for getting id

    # ref name=model name.objects.all().values('id','name')





