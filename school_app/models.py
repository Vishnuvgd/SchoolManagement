from django.db import models

# Create your models here.

class AdminModelReg(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class StudentModel(models.Model):
    first_name = models.CharField(max_length=50)  
    last_name = models.CharField(max_length=50)  
    address = models.TextField(null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    
    def __str__(self):
        return self.first_name
    
class FeesModel(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=50)  
    
    def __str__(self):
        return self.status    

class OfficeModel(models.Model):
    name = models.CharField(max_length=25)  
    email = models.EmailField() 
    password = models.CharField(max_length=20)  
    desigination = models.CharField(max_length=25)    
    subject = models.CharField(max_length=25)  
    
    def __str__(self):
        return self.name
      

class LibraryModel(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    book_title = models.CharField(max_length=200)
    stock = models.IntegerField()
    book_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.book_title
    

