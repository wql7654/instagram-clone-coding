from django.shortcuts import render, redirect
from .models import Instargram, Comment
from .forms import InstargramForm, CommentForm

#Create your views here.
def first(request):
    # if request.user.is_authenticated:
    #     pass

    # else:
    return redirect('accounts:login')

def index(request):
    instargram_list = Instargram.objects.order_by('-pk')
    context = {
        'instargram_list' : instargram_list,
    }
    return render(request,'instargram/index.html', context)