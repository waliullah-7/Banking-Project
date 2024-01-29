from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm,UserProfileForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

class SignUpView(FormView):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = '/login/'  
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def user_login(request):
    if request.user.is_authenticated:
     if request.method=="POST":
        fm= AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user= authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/bank/dashboard/')
     else:           
            fm= AuthenticationForm()
     return render(request,'accounts/login.html',{'form':fm})    


@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')  
    else:
        form = UserProfileForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)
    return render(request, 'accounts/profile.html', {'name': request.user, 'form': form, 'password_form': password_form})    


@login_required
def user_profile_view(request):
    user = request.user
    data = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
    }
    return JsonResponse(data)
   
@login_required
def user_logout(request):
      logout(request)
      return HttpResponseRedirect('/login/')
