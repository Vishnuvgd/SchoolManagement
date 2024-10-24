from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *


# Create your views here.

def index(request):
    return render(request,'index.html')


# ---------------SchoolAdminReg------------------

def Adminreg(request):
    if request.method =='POST':
        a=AdminRegform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['name']
            em=a.cleaned_data['email']
            psw=a.cleaned_data['password']
            b=AdminModelReg(name=nm,email=em,password=psw)
            b.save()
            return redirect(Adminlog)
        else:
            return HttpResponse("failed..")
    return render(request,'AdminReg.html')


def Adminlog(request):
    if request.method=='POST':
        a=AdminLogform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            psw=a.cleaned_data['password']
            b=AdminModelReg.objects.all()
            for i in b:
                id=i.id
                nm=i.name
                if em==i.email and psw==i.password:
                    return render(request,'Adminprofile.html',{'id':id,'nm':nm})
            else:
                 return redirect(Adminlogfail)
    return render(request,'AdminLog.html')



# ------------Adminfail---------------------------------------
def Adminlogfail(request):
    return render(request,'AdminLogfail.html')

#-------------- studentform -------------------------

def student_form(request):
    if request.method=='POST':
        a=Studentform(request.POST)
        if a.is_valid():
            fnm=a.cleaned_data['first_name']
            ln=a.cleaned_data['last_name']
            em=a.cleaned_data['email']
            ph=a.cleaned_data['phone']
            b=StudentModel(first_name=fnm,last_name=ln,email=em,phone=ph)
            b.save()
            return redirect(student_list)
        else:
            return HttpResponse("upload failed..")
    return render(request,'Studentform.html')


def student_list(request):
    students = StudentModel.objects.all()
    return render(request, 'StudentsList.html', {'students': students})

def student_view(request):
    students = StudentModel.objects.all()
    return render(request, 'StudentView.html', {'students': students})

def student_del(request,id):
    a=StudentModel.objects.get(id=id)
    a.delete()
    return redirect(student_list)

# edit

def student_edit(request,id):
    a=StudentModel.objects.get(id=id)
    if request.method == 'POST':
        a.first_name = request.POST.get('first_name')
        a.last_name = request.POST.get('last_name')
        a.address = request.POST.get('address')
        a.email = request.POST.get('email')
        a.phone = request.POST.get('phone')
        a.save()
        return redirect(student_list)
    return render(request,'Studentedit.html',{'a': a})

# fee
def fee_view(request):
    fee = FeesModel.objects.all()
    return render(request, 'Feestatus.html', {'fee': fee})

def fee_list(request):
    fee = FeesModel.objects.all()
    return render(request, 'Feesview.html', {'fee': fee})

# ------------------officestaff----------------------------

def Office_reg(request):
    if request.method =='POST':
        a=OfficeForm(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['name']
            em=a.cleaned_data['email']
            b=OfficeModel(name=nm,email=em)
            b.save()
            return redirect(Office_log)
        else:
            return HttpResponse("failed..")
    return render(request,'OfficeReg.html')

def Office_log(request):
    if request.method=='POST':
        a=OfficeForm(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            psw=a.cleaned_data['password']
            b=OfficeModel.objects.all()
            for i in b:
                id=i.id
                nm=i.name
                if em==i.email and psw==i.password:
                    return render(request,'Officeprofile.html',{'id':id,'nm':nm})
            else:
                 return redirect(Adminlogfail)
    return render(request,'OfficeLog.html')

def office_profile(request):
    return render(request,'Officeprofile.html')

def office_view(request):
    staff = OfficeModel.objects.all()
    return render(request, 'OfficeView.html', {'staff': staff})

def office_list(request):
    staff = OfficeModel.objects.all()
    return render(request, 'Officestaff_list.html', {'staff': staff})

# edit
def staff_edit(request,id):
    a=OfficeModel.objects.get(id=id)
    if request.method == 'POST':
        a.name = request.POST.get('name')
        a.email = request.POST.get('email')
        a.desigination = request.POST.get('desigination')
        a.email = request.POST.get('email')
        a.subject = request.POST.get('subject')
        a.save()
        return redirect(office_view)
    return render(request,'Officestaffedit.html',{'a': a})

def staff_del(request,id):
    a=OfficeModel.objects.get(id=id)
    a.delete()
    return redirect(office_view)

# Add staff
def staff_form(request):
    if request.method=='POST':
        a=OfficeForm(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['name']
            des=a.cleaned_data['desigination']
            em=a.cleaned_data['email']
            sj=a.cleaned_data['subject']
            b=OfficeModel(name=nm,desigination=des,email=em,subject=sj)
            b.save()
            return redirect(office_list)
        else:
            return HttpResponse("upload failed..")
    return render(request,'Officestaff_form.html')
# --------------------------Libraryview-----------------------------

def library_reg(request):
    if request.method =='POST':
        a=Libraryform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            pws=a.cleaned_data['password']
            b=LibraryModel(email=em,password=pws)
            b.save()
            return redirect(library_log)
        else:
            return HttpResponse("failed..")
    return render(request,'LibraryReg.html')

def library_log(request):
    if request.method=='POST':
        a=Libraryform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            pws=a.cleaned_data['password']
            b=LibraryModel.objects.all()
            for i in b:
                id=i.id
                nm=i.student
                if em==i.email and pws==i.password:
                    return render(request,'Libraryprofile.html',{'id':id,'nm':nm})
            else:
                 return redirect(Adminlogfail)
    return render(request,'LibraryLog.html')



def library_view(request):
    library = LibraryModel.objects.all()
    return render(request, 'LibraryView.html', {'library': library})

def library_list(request):
    library = LibraryModel.objects.all()
    return render(request, 'LibraryList.html', {'library': library})

# edit
# def library_edit(request,id):
#     a=LibraryModel.objects.get(id=id)
#     if request.method == 'POST':
#         a.name = request.POST.get('name')
#         a.email = request.POST.get('email')
#         a.desigination = request.POST.get('desigination')
#         a.email = request.POST.get('email')
#         a.subject = request.POST.get('subject')
#         a.save()
#         return redirect(office_view)
#     return render(request,'Libraryedit.html',{'a': a})

def library_del(request,id):
    a=LibraryModel.objects.get(id=id)
    a.delete()
    return redirect(library_view)

def Book_list(request):
    book = LibraryModel.objects.all()
    return render(request, 'BookList.html', {'book': book})