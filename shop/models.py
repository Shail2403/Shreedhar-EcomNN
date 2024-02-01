from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50,default="")
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=1500)
    pub_date=models.DateField()
    image =models.ImageField( upload_to="shop/images",default="")
    def __str__(self):
        return self.product_name
    
class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=500,default="")
    
class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=17)
    amount=models.FloatField(default=0)
    email=models.CharField(max_length=30)
    address=models.CharField(max_length=90)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=20)
    zip_code=models.CharField(max_length=90)
    phone=models.CharField(max_length=90,default="")
    zip_code=models.CharField(max_length=90)

class Partner(models.Model):
    partner_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default="")
    cpname=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=50,default="")
    partnershipType=models.CharField(max_length=20,default="")
    additionalComments=models.CharField(max_length=500,default="")



class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.update_desc[0:7]+"..."