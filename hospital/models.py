import email
from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('doctor', 'doctor'),
    ('patient', 'patient'),
)
class register_doctor(models.Model):
    #model for entered details
    user_type=models.CharField(choices=GENDER_CHOICES,max_length=10,default='doctor')
    first_name=models.CharField(max_length=25,null=True,blank=True)
    last_name = models.CharField(max_length=25,null=True)
    user_name = models.CharField(max_length=25,null=True)
    profile_pic = models.ImageField(upload_to='images/',null=True)
    address_line1=models.CharField(max_length=75,null=True)
    city=models.CharField(max_length=25,null=True,blank=True)
    state=models.CharField(max_length=25,null=True)
    pincode=models.IntegerField(null=True)
    email=models.EmailField(max_length=25,null=True)
    password=models.CharField(max_length=25,null=True)
    password2=models.CharField(max_length=25,null=True)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'register_doctor'







