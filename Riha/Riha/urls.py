from django.contrib import admin
from django.urls import path, include
from idcomplete.views import home_view, signup_view
# from idcomplete.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('idcomplete/',include('idcomplete.urls')),
    path('', home_view, name="home"),
    path('signup/', signup_view, name="signup")
]
