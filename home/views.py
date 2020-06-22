from django.shortcuts import render
from .models import Book
from users.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):

	context = {
		'books': Book.objects.all()[:3],
		'adventure': Book.objects.filter(genre = 'Adventure'),
		'selfhelp': Book.objects.filter(genre = 'Self-Help'),		
	}
	print(context)
	return render(request, 'home/home.html', context)

@login_required
def profile(request):
	basic_info = User.objects.get(username = request.user.username)
	more_details = UserProfile.objects.get(user = basic_info)
	return render(request, 'home/profile.html', {'basic_info': basic_info,'more_details':more_details})

def genre_search(request,genretype):
	q = Book.objects.filter(genre = genretype)
	return render(request, 'home/genre.html', {'books':q})