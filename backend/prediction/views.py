from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from .models import model_image
from django.contrib.auth.decorators import login_required
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
from .Trained_Model.utilize_model import identify_tumor
from .sendsms import send_mail

@login_required
def home(request):
    usr = request.user
    data = model_image.objects.filter(user = usr)
    context = {
        'data':data
    }
    return render(request,"home.html",context=context)

@login_required
def test(request):
    if request.method=='POST':
        if request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage(location='UI/media/'+str(request.user))
            filename = fs.save(myfile.name, myfile)
            usr = request.user
            url = str(BASE_DIR)+'/media/'+str(request.user)+'/'+filename
            res = identify_tumor(url)
            c=res['class']
            d = res['probablity']
            print(c,d)
            img = model_image()
            img.user = usr
            img.image = filename
            img.symptom = c
            img.accuracy = d
            img.image_url = url
            img.save()
            send_mail(usr.email,c,d)
            return redirect('dashboard')
    return render(request,"test.html")

@login_required
def help(request):
    return render(request,"help.html")