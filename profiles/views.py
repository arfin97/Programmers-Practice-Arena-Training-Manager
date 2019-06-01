from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from .models import Profile
from django.contrib.auth.models import User
from sheets.models import SheetMember
from solve_activities.models import Solve
# Create your views here.

class Register(CreateView):
    template_name = 'profiles/register.html'
    form_class = forms.RegisterForm
    success_url = reverse_lazy('login')

def profile(request, user_id):
	try:
		user = User.objects.get(pk=user_id)
		profile = user.profile
		sheet_member = SheetMember.objects.get(member=user)
		all_solve = Solve.objects.filter(solver=user)
		return render(request, 'profiles/profile.html', {'profile':profile, 'sheet_member':sheet_member, 'all_solve':all_solve})
	except:
		return render(request, 'profiles/profile.html')

def create_profile(request, user_id):
	if request.method == "POST":
		print("Dhuksi")
		user = User.objects.get(pk=user_id)
		try:
			profile = user.profile
			try:
				profile.image = request.FILES['image']
			except:
				print("Image update korbo na, ager image use korbo")
				

			profile.name = request.POST['name']
			profile.varsity_id = request.POST['varsity_id']
			profile.save()
			print("Profile banani ase, khali profile pic update kore daw")
			return render(request, 'profiles/create_profile.html', {'message': "Updated", 'tag':'success'})

		except:
			print("Profile banani nai")
			try:
				profile = Profile()
				profile.user = User.objects.get(pk=user_id)
				print("Ashalm 2")
				profile.image = request.FILES['image']
				print("Ashalm 3")
				profile.name = request.POST['name']
				profile.varsity_id = request.POST['varsity_id']
				profile.save()
				print("Chobi save korsi")
				return render(request, 'profiles/create_profile.html', {'message': "Updated", 'tag':'success'})
			except NameError:
				print("Cobi dey nai")
				return render(request, 'profiles/create_profile.html', {'message': "Profile Picture Required", 'tag':'danger'})

		return render(request, 'profiles/create_profile.html')
	return render(request, 'profiles/create_profile.html')