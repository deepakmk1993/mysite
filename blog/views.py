from django.shortcuts import render
from .models import Post

# Create your views here.
def view_posts(request):
	posts = Post.objects.all().order_by("create_time");
	return render(request, 'posts.html', {'posts': posts});

def view_post(request, pk):
	post = Post.objects.get(pk=pk);
	return render(request, 'post.html', {'post': post});