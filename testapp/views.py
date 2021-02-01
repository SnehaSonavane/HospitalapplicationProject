from django.shortcuts import render

from testapp.models import Doctor,Patient,Appointment

from django.core.paginator import Paginator
from testapp.forms import DoctorForm,PatientForm
from django.views.generic import CreateView
# Create your views here.
def home_view(request):
   return render(request,"home.html")

def doctor_read_view(request):
    doc_list=Doctor.objects.all()

    paginator=Paginator(doc_list,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    dname=request.GET.get('dname')
    if dname!='' and dname is not None:
        page_obj=doc_list.filter(doctor_name__contains=dname)

    my_dict={'page_obj':page_obj}
    return render(request,'doctorread.html',my_dict)



class doctor_form_view(CreateView):
    model=Doctor
    #fields="__all__"
    form_class=DoctorForm


def patient_read_view(request):
    pat_list=Patient.objects.all()

    paginator=Paginator(pat_list,4)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    name=request.GET.get('pname')#vinny
    if name!='' and name is not None:
        page_obj=pat_list.filter(patient_name__exact=name)




    my_dict={'page_obj':page_obj}
    return render(request,'patientread.html',my_dict)




class patient_form_view(CreateView):
    model=Patient
    #fields="__all__"
    form_class=PatientForm

def appointment_details_view(request,id):
   if request.method=='POST':
    app_list=Appointment.objects.get(id=id)

    my_dict={'app_list':app_list}
    return render(request,'appdetail.html',my_dict)
