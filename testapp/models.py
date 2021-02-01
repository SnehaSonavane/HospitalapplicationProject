from django.db import models
from django.urls import reverse
# Create your models here.
class Doctor(models.Model):
    doctor_name=models.CharField(max_length=150)
    mobile_no=models.IntegerField()
    shift_choices=(
    ('day shift','Day Shift'),
    ('night shift','Night Shift')
    )
    shift=models.CharField(max_length=30,choices=shift_choices)
    specialization=models.CharField(max_length=100)
    experience=models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('read_data')

    def __str__(self):
        return self.doctor_name


class Patient(models.Model):
    patient_name=models.CharField(max_length=250)
    mobile_number=models.IntegerField()
    age=models.IntegerField()
    gender_choices=(
    ('male','Male'),
    ('female','Female')
    )
    gender=models.CharField(max_length=30,choices=gender_choices)
    address=models.TextField()

    def get_absolute_url(self):
        return reverse('read1_data')

    def __str__(self):
        return self.patient_name


class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True)
    patient=models.OneToOneField(Patient,on_delete=models.CASCADE,null=True)
    disease=models.CharField(max_length=30,null=True)
    date_and_time=models.DateTimeField(null=True)
