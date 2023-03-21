from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.files.storage import FileSystemStorage
import json
from .forms import FormApplication
import pycountry

# Create your views here.

def page_404(request):
    context = {
        'title':'404 page'
    }
    return render(request, "frontend/page_404.html", context)
    
def index(request):
    context = {
        'title':'Home page'
    }
    return render(request, "frontend/index.html", context)

# upload cv module
def upload_cv(request):
    title = 'Upload Your Application Form'
    form = FormApplication(request.POST or None)
    # print(pycountry.countries)
    # for country in pycountry.countries:
    #     print(country.name)
    if request.method == 'POST':
        upload_file = request.FILES['upload_cv']
        fs = FileSystemStorage()
        #print('filename: ', upload_file['upload_cv'].name)
        fs.save(upload_file.name, upload_file)
        
        # recapcha
        # clientKey = request.POST['g-recapcha-response']
        # secretKey = ''
        # capchaData = {
        #     'secret':secretKey,
        #     'response':clientKey,
        # }
        # r = request.post('', data=capchaData)
        # response = json.loads(r.text)
        # verify = response['success']
        # if verify:
        #     title = '! Your CV uploaded successfully.'
        title = '! Your Application Form uploaded successfully.'

    context = {
        'title':title,
        'form': form
    }
    return render(request, "frontend/upload-cv.html", context)
