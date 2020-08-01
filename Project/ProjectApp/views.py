from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogPost
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def main(request):
    posts = Post.objects
    post_list=Post.objects.all()
    paginator = Paginator(post_list, 2) # 페이지 나누기 (객체 3개씩)
    page = request.GET.get('page') # 요청한 페이지 값
    pages = paginator.get_page(page) # 해당 페이지 가져오기
    return render(request, 'main.html', {'posts':posts, 'pages':pages})

def create(request):
    if request.method == 'POST':
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=True)
            return redirect('main')
        return render(request, 'new.html', {'form':form})
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})
      
def art(requests):
    return render(requests,'art.html')
