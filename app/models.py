from django.db import models

# Create your models here.


#Model created 
class Teacher(models.Model):
    Firstname =models.CharField( max_length=50)
    Lastname = models.CharField( max_length=50)
    Email = models.EmailField( max_length=254)
    Contact = models.CharField(max_length=50)
    
    
    
   
   #This function is used for converting object into string
    def __str__(self) -> str:
        return self.Firstname 
    
    
class Student(models.Model):
    Firstname =models.CharField( max_length=50)
    Lastname = models.CharField( max_length=50)
    Email = models.EmailField( max_length=254)
    Contact = models.CharField(max_length=50)
    
    def __str__(stu) -> str:
        return stu.Firstname 
    
