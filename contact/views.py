from django.shortcuts import render,redirect

from .models import contact
# Create your views here.

def index(request):
    if  request.method == 'POST':
        sub = request.POST['subject']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contactvar = contact(subject=sub,Name=name,Email=email,Phoneno=phone,Message=message)
        contactvar.save()        
        return redirect('/contact/')
    return render(request, 'contact/contact.html')
