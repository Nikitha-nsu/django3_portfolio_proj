from django.shortcuts import render
from .models import BlogModel

def blogsmodel(request):
    blogobjs = BlogModel.objects.order_by('-date')[:]
    return render(request,'blogmodel/blogsmodel.html', {'blogobjs': blogobjs})
# Create your views here.
