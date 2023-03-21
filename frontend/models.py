from django.db import models

AVAILABILITY =[
    ('full-time','Full Time'),
    ('part-time','Part Time'),
    ('contract','Contract'),
]
class Category(models.Model):
    name = models.CharField(max_length=50)
    active          = models.BooleanField(default=True)
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class FormOptions(models.Model):
    name = models.CharField(max_length=100)
    category   = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Create your models here.
class ApplicationForm(models.Model):
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    active          = models.BooleanField(default=True)
    dob             = models.CharField(max_length=100)
    availability    = models.OneToOneField(FormOptions, on_delete=models.CASCADE)
    languages        = models.ManyToManyField(FormOptions, related_name='person_languages')
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)




# language        = models.ManyToManyField(FormOptions)

class WorkExperience(models.Model):
    application = models.ForeignKey(ApplicationForm, on_delete=models.CASCADE)
    experience = models.ManyToManyField(FormOptions)
    

    def __str__(self):
        return self.application.last_name

class AdditionalInformation(models.Model):
    application = models.ForeignKey(ApplicationForm, on_delete=models.CASCADE)
    passport_number = models.CharField(max_length=50)
    passport_issue_date = models.DateTimeField(auto_now_add=False)
    passport_expiry_date = models.DateTimeField(auto_now_add=False)
    address = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    mobile_phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    ppsn = models.CharField(max_length=50)
    profile = models.CharField(max_length=50)

    def __str__(self):
        return self.passport_number

class FormImages(models.Model):
    application = models.ForeignKey(ApplicationForm, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.passport_number
