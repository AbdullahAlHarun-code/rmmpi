from django import forms 
from .models import ApplicationForm, Category, FormOptions
import pycountry
#  python manage.py runserver
class FormApplication(forms.ModelForm):
    COUNTRY = []
    for country in pycountry.countries:
        COUNTRY.append((str(country.name),str(country.name)))
    first_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}))
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}))
    dob= forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': '12/03/2003'}))
    availability= forms.ModelChoiceField(queryset=FormOptions.objects.all().filter(category=Category.objects.all().filter(name='Availability')[0].id), empty_label='Please Select', widget=forms.Select(attrs={'class': 'form-control'}))
    languages= forms.ModelChoiceField(queryset=FormOptions.objects.all().filter(category=Category.objects.all().filter(name='Languages')[0].id), empty_label='Please Select', widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    work_experience= forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Butcher: cutting and boning. He has 15 years of experience'}))
    passport_number= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex.IE44784555BG'}))
    passport_issue_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': '12/03/2003'}))
    passport_expiry_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': '12/03/2003'}))
    address= forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    post_code= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: E23 OEB'}))
    country= forms.ChoiceField(choices=COUNTRY, widget=forms.Select(attrs={'class': 'form-control'}))
    mobile_number= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+353 8956874558'}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'eg: test@gmail.com'}))
    ppsn= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg: 45781245PU'}))
    profile= forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'I’m a fast learner, reliable and hard working person, enthusiastic, communicative, charismatic , energetic, personable, and willing to learn and develop new skills.'}))
    class Meta:
        model = ApplicationForm 
        fields = (
            'first_name',
            'last_name', 
            'dob', 
            'availability', 
            'languages', 
            'work_experience', 
            'passport_number', 
            'passport_issue_date', 
            'passport_expiry_date',
            'address',
            'post_code',
            'country',
            'mobile_number',
            'email',
            'ppsn',
            'profile',
        )




    
 