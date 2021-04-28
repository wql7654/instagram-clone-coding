from django.shortcuts import render, redirect, get_object_or_404
from .models import Instargram, Comment
from .forms import InstargramForm, CommentForm

#Create your views here.
def first(request):
    if request.user.is_authenticated:
        return redirect('instargram:index')

    else:
        return redirect('accounts:login')

def index(request):
    instargram_list = Instargram.objects.order_by('-pk')
    context = {
        'instargram_list' : instargram_list,
    }
    return render(request,'instargram/index.html', context)


def create(request):
        if request.method == "POST":

            form = InstargramForm(request.POST, request.FILES)

            if form.is_valid():
                article = form.save(commit=False)
                article.user = request.user
                article.save()
                
                return redirect('instargram:detail', article.pk)
        else:
            form = InstargramForm()
        context = {
            'form':form,
        }    
        return render(request,'instargram/create.html',context)


def detail(request, pk):
    article = get_object_or_404(Instargram, pk=pk)
    context = {
        'article': article,
    }    
    return render(request,'instargram/detail.html', context)


def delete(request, pk):
    article = get_object_or_404(Instargram, pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('instargram:index')
    return redirect('instargram:detail', article.pk)    

def update(request, pk):
    article = get_object_or_404(Instargram, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':

            form = InstargramForm(request.POST,request.FILES, instance=article)

            if form.is_valid():
                article = form.save()
                return redirect('instargram:detail', article.pk)
        else:
            form = InstargramForm(instance=article)
    else:
        return redirect('instargram:index')
        # return HttpResponseForbidden()
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'instargram/update.html', context)


def like(request, pk):
    instargram = get_object_or_404(Instargram, pk=pk)

    if instargram.like_users.filter(pk=request.user.pk).exists():
        instargram.like_users.remove(request.user)
    else:
        instargram.like_users.add(request.user)

    return redirect('instargram:index')


def detail_like(request, pk):
    instargram = get_object_or_404(Instargram, pk=pk)

    if instargram.like_users.filter(pk=request.user.pk).exists():
        instargram.like_users.remove(request.user)
    else:
        instargram.like_users.add(request.user)

    return redirect('instargram:detail', pk)
        