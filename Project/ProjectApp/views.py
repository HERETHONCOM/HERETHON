from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogPost
from .models import Post

# Create your views here.
def main(requests):
    return render(requests,'main.html')

def create(request):
    if request.method == 'POST':
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=True)
            return redirect('gallery')
        return render(request, 'new.html', {'form':form})
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})
      
def art(requests):
    return render(requests,'art.html')
