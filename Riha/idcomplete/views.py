from django.shortcuts import  render, redirect, reverse, get_object_or_404
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
# from .tokens import account_activation_token
from django.template.loader import render_to_string
from .models import *
from .forms import *

def home_view(request, pk, template_name = 'idcomplete/index.html'):
	id    =   get_object_or_404(IdentiteComplete, pk = pk)
	return render(request, template_name, {'id': id })


def createIdc(request):
    if request.method == "POST":
        form = IdentiteCompleteForm(request.POST)
        if form.is_valid():
            identite = form.save(commit=False)
            identite.author = request.user
            identite.save()
            return redirect('http://127.0.0.1:8000/idcomplete', pk=identite.pk)
    else:
        form = IdentiteCompleteForm()
    return render(request, 'idcomplete/form.html', {'form': form})

def  person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            identite = form.save(commit=False)
            identite.save()
            return redirect('http://127.0.0.1:8000/profile', pk=identite.pk)
    else:
        form = PersonForm()
    return render(request, 'idcomplete/profile.html', {'form': form})


def activation_sent_view(request):
    return render(request, 'idcomplete/activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true 
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'idcomplete/activation_invalid.html')

def signup_view(request):
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            # user can't login until link confirmed
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            # load a template like get_template() 
            # and calls its render() method immediately.
            message = render_to_string('activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'idcomplete/signup.html', {'form': form})




















































































































































































































































# from django.shortcuts import render
# from django.contrib.auth import authenticate, login, logout
# from django.http import *
# from .models import *
# from django.views.generic import TemplateView
# from django.conf import settings
# from .forms import RegisterForm

# class LoginView(TemplateView):

#   template_name = 'idcomplete/index.html'

#   def post(self, request, **kwargs):

#     username = request.POST.get('username', False)
#     password = request.POST.get('password', False)
#     user = authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         login(request, user)
#         return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )

#     return render(request, self.template_name)


# class LogoutView(TemplateView):

#   template_name = 'idcomplete/index.html'

#   def get(self, request, **kwargs):

#     logout(request)

#     return render(request, self.template_name)


# def register(response):
# 	if response.method == "POST":
# 		form = RegisterForm(response.POST)
# 		if form.is_valid():
# 			form.save()

# 		return redirect("/home")
# 	else:
# 		form = RegisterForm()

# 	return render(response, "register/register.html", {"form":form})



