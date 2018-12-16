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
    return render(request,'app/index.html',{})

# @login_required
# def form_advanced(request):
#     return render(request,'app/form_advanced.html',{})

@login_required
def project_list(request):
    products = product.objects.all()
    return render(request, 'app/form_advanced.html',{
        'products':products
    })

@login_required
def details(request):
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