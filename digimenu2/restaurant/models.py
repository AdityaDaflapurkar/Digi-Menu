from django.contrib import admin
from django.db import models
#from PIL import Image 
# Create your models here.
from django import template
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

register = template.Library()

class Cuisine(models.Model):
    cuisine_id=models.AutoField(primary_key = True)
    cuisine_name = models.CharField(max_length=200)
    image_path= models.CharField(max_length=100)

    def __str__(self):
        return self.cuisine_name

#class Image(models.Model):
#	cuisine = models.ForeignKey(Cuisine)
#	image =models.ImageField(upload_to='images',verbose_name='My Photo')

#class InlineImage(admin.TabularInline):
#      model=Image

#class CuisineAdmin(admin.ModelAdmin):
#	inlines=[InlineImage]

admin.site.register(Cuisine)#,CuisineAdmin)   
 
class Menu(models.Model):
    menu_item = models.CharField(primary_key = True , max_length =200)
    price = models.IntegerField()
    description = models.TextField()
    cuisine_id = models.ForeignKey(Cuisine)
    image_path= models.CharField(max_length=100)
    def __str__(self):
        return self.menu_item
   


#class Table(models.Model):
 #   table_no = models.IntegerField(primary_key = True)
  #  def __str__(self):
   #     return "Table Number " + str(self.table_no)
        

class Userprofile(models.Model):
   user = models.ForeignKey(User, unique=True)
   def __str__(self):
        return self.user
    #name = models.CharField(max_length = 30)
    #phone_no = models.IntegerField()
   # table_no = models.ForeignKey(Table)
    #password = models.CharField(primary_key = True ,max_length=7)
   # bill_id = models.IntegerField()

class Cart(models.Model):
 
    item_name = models.CharField(max_length = 200)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField()
    user = models.ForeignKey(Userprofile)
    def __str__(self):
        return self.item_name


    
class Cartitem(models.Model):

    item_name = models.ForeignKey(Cart)
    menu_item = models.ForeignKey(Menu)
    
