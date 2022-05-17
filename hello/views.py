from django.shortcuts import render
from .models import Friend
from .forms import HelloForm
# Create your views here.

def index( request ):
    data = Friend.objects.all()
    params = {
        'title':'Hello',
        'message':'all friends.',
        'data':[],
        'form':HelloForm()
    }
    num = request.POST['id']
    item = Friend.objects.get(num)
    params['data'].append( item )
    return render( request,"hello/index.html",params)