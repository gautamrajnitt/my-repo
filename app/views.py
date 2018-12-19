from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import productform
from .models import product

class Home(TemplateView):
    template_name='index.html'

def upload(request):
    context={}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

@login_required
def index(request):
    # return HttpResponse("<h1>welcome</h1>")
    products = product.objects.all()
    return render(request,'app/index.html',{
        'products':products
    })

# @login_required
# def form_advanced(request):
#     return render(request,'app/form_advanced.html',{})

@login_required
def media_gallery(request):
    products = product.objects.all()
    return render(request, 'app/media_gallery.html',{
        'products':products
    })

@login_required
def liked_projects(request):
    products = product.objects.all()
    return render(request, 'app/liked_projects.html',{
        'products':products
    })

@login_required
def details(request, product_id):
        print(product_id)
        products = product.objects.all()
        return render(request, 'app/details.html',{
            'products':products
        })
        
@login_required
def upload_project(request):
    if request.method == 'POST':
        form = productform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # subject = 'Thank you for registering to our site'
            # message = ' it  means a world to us '
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = ['gautam.raj.nitt@gmail.com',]
            # send_mail( subject, message, email_from, recipient_list )
            # messages.success(request, 'Project details Updated.')
            return redirect('/dashboard/projects')
    else:
        form = productform()
        products = product.objects.all()
        return render(request, 'app/form_advanced.html',{
            'products':products
        })
    return render(request, 'app/form_advanced.html',{
        'form': form
    })

@login_required
def profile(request):
    return render(request, 'app/profile.html')