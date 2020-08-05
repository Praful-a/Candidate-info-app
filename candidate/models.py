from django.db import models

# Create your models here.
GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

BLOOD = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
)

MARITAL = (
    ('Single', 'Single'),
    ('Married', 'Married')
)

LANGUAGE = (
    ('Hindi', 'Hindi'),
    ('English', 'English'),
    ('Bengali', 'Bengali'),
    ('Telugu', 'Telugu'),
    ('Marathi', 'Marathi'),
    ('Tamil', 'Tamil'),
    ('Gujarati', 'Gujarati'),
    ('Kannada', 'Kannada'),
    ('Malayalam', 'Malayalam'),
    ('Odia', 'Odia'),
    ('Punjabi', 'Punjabi')
)

class Profile(models.Model):
    name = models.CharField(max_length=255)
    Gender = moldes.CharField(choices=GENDER, max_length=10)
    Mother's_Name = models.CharField(max_length=250)
    Father's_Name = models.CharField(max_length=255)
    Blood_Group = models.CharField(choices=BLOOD, max_length=3)
    Marital_Status = models.CharField(choices=MARITAL, max_length=15)
    Aadhar_Card_No. = models.IntegerField()
    Aadhar_Front_Img = models.ImageField()
    Aadhar_Back_Img = models.ImageField()
    Your_Photo = models.ImageField()
    Your_CV = models.ImageField()
    Primary_lang = models.CharField(choices=LANGUAGE)


class Contact(models.Model):
    Mobile = models.IntegerField()
    Alternate_Mobile = models.IntegerField()
    Emergency_Mobile = models.IntegerField()
    Relation_with_Emergency_Contact = models.IntegerField()
    Email = models.EmailField()
    Accept = models.BooleanField(default=False)
