from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required



from django.conf.urls import url
from .views import home_view, signup_view, activation_sent_view, activate

urlpatterns = [
    path('<int:pk>', home_view, name="home"),
    path('new/', views.createIdc, name='createIdc'),
    path('profile/', views.person, name='person'),
    path('signup/', signup_view, name="signup"),
    path('sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]


# urlpatterns = [
#     path('', views.index, name = 'index'),
#     # path("register/", views.register, name="register"),
#     # # path(' ', LoginView.as_view()),
#     # path('logout/', LogoutView.as_view()),
#     # path('accounts/', include('django.contrib.auth.urls')),
#     #    accounts/ login/ [name='login']
# 	# accounts/ logout/ [name='logout']
# 	# accounts/ password_change/ [name='password_change']
# 	# accounts/ password_change/done/ [name='password_change_done']
# 	# accounts/ password_reset/ [name='password_reset']
# 	# accounts/ password_reset/done/ [name='password_reset_done']
# 	# accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# 	# accounts/ reset/done/ [name='password_reset_complete']
#     # path('backoffice/', login_required(TemplateView.as_view(template_name='backoffice/index.html'))),


# ]
