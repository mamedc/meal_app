from django.shortcuts import render
from .models import Post

posts_toy = [
	{
		'author': 'Corey', 
		'title': 'Blog Post 1', 
		'content': 'First content', 
		'date_posted': 'August 27, 2018'
	}, 
	{
		'author': 'Jane', 
		'title': 'Blog Post 2', 
		'content': '2nd content', 
		'date_posted': 'August 28, 2018'
	}, 
]


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})