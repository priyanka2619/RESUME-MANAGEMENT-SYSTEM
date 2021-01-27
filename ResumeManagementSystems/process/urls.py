"""RMSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from process import views

urlpatterns = [
    path('',views.showIndex,name='main'),
    path('registration/',views.registration,name='registration'),
    path('user_registration/',views.registration,name='user_registration'),

    path('user_otp/',views.userOTP,name='user_otp'),
    path('validate_otp/',views.validateOtp,name='validate_otp'),

    path('confirmation/',views.confirmation,name='confirmation'),
    path('login/',views.login,name='login'),
    path('login_validate/',views.loginValidate,name='login_validate'),

    path('view_profile/',views.view_profile,name='view_profile'),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('updated_profile_page/',views.updated_profile_page,name='updated_profile_page'),
    path('delete_profile/',views.delete_profile,name='delete_profile'),
    path('delete_profile_page/',views.delete_profile_page,name='delete_profile_page'),


    path('logout/',views.logout,name='logout'),


    path('about/',views.about,name='about'),
    path('contactus/',views.contactUs,name='contactus'),

]

#Consumer application use this --> urls
urlpatterns+= [
    path('api.registration_details/',views.RegistrationDetails.as_view()),
    path('api.profile_details/',views.ProfileDetails.as_view())
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
