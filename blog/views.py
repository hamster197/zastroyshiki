from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import StavkiEditForm, NewPostHodStrForm
from .models import stavki_ip, blog_hod_st


# Create your views here.
@login_required
def StavkiPrEditView(request):
    st = get_object_or_404(stavki_ip, pk=1)
    if request.POST:
        form = StavkiEditForm(request.POST, instance=st)
        if form.is_valid():
            form.save()
    else:
        form = StavkiEditForm(instance=st)
    return render(request, 'blog/stavkiedit.htm', {'tform':form})

@login_required
def NewPostHodStrView(request):
    if request.POST:
        form = NewPostHodStrForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            print(form.errors)
            form.save()
    else:
        form = NewPostHodStrForm()
    return render(request,'blog/hodstblogedit.htm',{'tform':form,})

@login_required
def EditPostHodStrView(request, idd):
    post = get_object_or_404(blog_hod_st, pk=idd)
    if request.POST:
        form = NewPostHodStrForm(request.POST, request.FILES, instance=post)
        print(form.errors)
        if form.is_valid():
            print(form.errors)
            form.save()
            return redirect('blog:hodstroy')
    else:
        form = NewPostHodStrForm(instance=post)
    return render(request,'blog/hodstblogedit.htm',{'tform':form,})

def IndexHodStView(request):
    post = blog_hod_st.objects.all().order_by('-date_sozd')
    return render(request,'main/hodstroy.html',{'tpost':post})
