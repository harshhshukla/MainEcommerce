from django.utils import timezone
from unicodedata import category
from django.db.models.base import Model, ModelBase
from django.contrib.auth.models import User


from django.db import models

# Create your models here.
class Mens(models.Model):
    
    mens_id = models.AutoField
    title =  models.CharField(max_length=50)
    Sale_or_not =  models.CharField(max_length=50,default="No Sale")
    price = models.FloatField()
    image = models.ImageField(upload_to="Home\mensimg\images",default="")
    descriptions= models.CharField(max_length=200,default="")
    categoryhai = (
        ("Mens","Mens"),
        ("Womens","Womens"),
        ("Kids","Kids"),
        ("Accessories","Accessories"),
    )
    category =  models.CharField(max_length=50,choices=categoryhai)
    
    subcategoryhai = (
        ("Casual","Casual"),
        ("Athletic","Athletic"),
        ("Sandals","Sandals"),
        ("Clog","Clog"),
    )
    subcategory = models.CharField(max_length=100,choices=subcategoryhai)
       
    def __str__(self):
        return self.title

        
class order(models.Model):
    jsonCart = models.CharField(max_length=1500)
    email = models.CharField(max_length=50,default="")
    first_name =  models.CharField(max_length=50)
    state =  models.CharField(max_length=50)
    isSameBillingAddress = models.BooleanField(default=False)
    last_name =  models.CharField(max_length=50)
    address =  models.CharField(max_length=200)
    zip = models.IntegerField()
    productorder=models.BooleanField(default=False)
    
    CODHai = models.BooleanField(default=True)
    UPIHai = models.BooleanField(default=False)
    order_date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.email
    
    

class detailsqr(models.Model):
    qr_id = models.AutoField(primary_key=True)
    Name =  models.CharField(max_length=50)
    TransactionID = models.IntegerField()
    UPINumber = models.IntegerField()
    UPIIDHAi =  models.CharField(max_length=50,default="none")
    Filehai = models.ImageField(upload_to="Home\qrdetails\images",default="")
    pub_date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.Name
    
class Review(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    mensProduct =  models.ForeignKey(Mens,models.CASCADE)
    comment = models.TextField(max_length=250)
    rate = models.IntegerField(default=5)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)