from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserProfileForm
from django.contrib import messages

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		user_profile_form = UserProfileForm(request.POST,request.FILES)
		if form.is_valid() and user_profile_form.is_valid():
			user = form.save()

			profile = user_profile_form.save(commit=False)
			
			profile.user = user

			profile.save()

			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}')
			return redirect('login')

	else:
		form = UserRegisterForm()
		user_profile_form = UserProfileForm()
	return render(request, 'users/register.html', {'form':form, 'profile_form':user_profile_form})