from django.db import models

# Create your models here.
class Course(models.Model):

    Course_Image=models.ImageField(upload_to="uploads/")
    Course_Name=models.CharField(max_length=200)
    Course_Fee=models.DecimalField(max_digits=12,decimal_places=2)
    Description=models.TextField(max_length=300)
    Course_Brochure=models.FileField(upload_to="brochures/")
    