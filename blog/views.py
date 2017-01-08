from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Post

# Create your views here.
def view_posts(request):
	post_list = Post.objects.all().order_by("create_time");
	paginator = Paginator(post_list, 5) # Show 5 posts per page

	page = request.GET.get('page')
	try:
	    posts = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    posts = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    posts = paginator.page(paginator.num_pages)

	return render(request, 'posts.html', {'posts': posts});

def view_post(request, pk):
	post = Post.objects.get(pk=pk);
	return render(request, 'post.html', {'post': post});