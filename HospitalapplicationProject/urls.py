"""HospitalapplicationProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_view),
    path('read/', views.doctor_read_view,name='read_data'),
    path('form/', views.doctor_form_view.as_view()),
    path('read1/', views.patient_read_view,name='read1_data'),
    path('form1/', views.patient_form_view.as_view()),
    path('appointment/<int:id>/', views.appointment_details_view),
]
