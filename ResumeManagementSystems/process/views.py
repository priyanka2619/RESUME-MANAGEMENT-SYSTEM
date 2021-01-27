from django.contrib import messages
from django.shortcuts import render,redirect
from process.forms import RegistrationForm,ProfileForm
from process.models import RegistrationModel,ProfileModel,IndustriesModel
from django.contrib.messages import success

from rest_framework.generics import ListAPIView
from process.serializer import RegistrationSerializer,ProfileSerializer


def showIndex(request):
    return render(request,"process_templates/main_page.html")


def registration(request):

    rf = RegistrationForm(request.POST)

    if request.method == "POST":
        if rf.is_valid():
            rf.save()
            return redirect('user_otp')
        else:
            return render(request, "process_templates/registration.html", {"form": rf})
    else:
        return render(request,"process_templates/registration.html",{"form":rf})


def userOTP(request):
    return render(request,"process_templates/otp.html")


def validateOtp(request):
    cno = request.POST.get("t1")
    u_otp = request.POST.get("t2")
    try:
        result = RegistrationModel.objects.get(contact=cno,otp=u_otp)
        if result.status == "pending":
            result.status = "approved"  #updating the record
            result.save()
            success(request, "Thanks For your Registration")
            return redirect('confirmation')
        elif result.status == "approved":
            success(request,"Your Registration is already approved.")
            return redirect('confirmation')
    except RegistrationModel.DoesNotExist:
        mess = "Invalid User...Please Try again"
        return render(request,"process_templates/otp.html",{"message":mess})


def confirmation(request):
    return render(request,"process_templates/confirmation.html")


def login(request):
    return render(request,"process_templates/login.html")

def loginValidate(request):
    e_mail = request.POST.get("n1")
    passw = request.POST.get("n2")
    try:
        result = RegistrationModel.objects.get(email=e_mail,password=passw)
        if result.status == "pending":
            return render(request,"process_templates/login.html",{"message":"Your Registration is not Approved"})
        if result.status == "closed":
            return render(request, "process_templates/login.html", {"message": "Sorry! Your Account is closed"})
        request.session["contact"] = result.contact
        request.session["name"] = result.name
        request.session["rno"] = result.rno
        return redirect('view_profile')
    except RegistrationModel.DoesNotExist:
        return render(request,"process_templates/login.html",{"message":"Invalid User"})


def view_profile(request):
    try:
        r_no = request.session["rno"]
        print(r_no)
        try:
           result = ProfileModel.objects.get(person_id=r_no)
           print(result)
           status = True
        except ProfileModel.DoesNotExist:
             status = False
        return render(request, "process_templates/view_profile.html",
                      {"status": status, "rdata": RegistrationModel.objects.all(), "pdata": ProfileModel.objects.all()})

    except KeyError:
        # messages.success(request,"Without Login you cannot access View Profile")
        return render(request,"process_templates/view_profile.html")

def update_profile(request):
    pf = ProfileForm()
    return render(request,"process_templates/update_profile.html",{"form":pf,"rform":RegistrationForm(),"pdata":ProfileModel.objects.all(),"idata":IndustriesModel.objects.all(),"rdata":RegistrationModel.objects.all()})

def updated_profile_page(request):
    person = request.POST.get("p1")
    edu = request.POST.get("education")
    img = request.FILES.get("photo")
    cv = request.FILES.get("resume")
    in_type = request.POST.get("i1")
    result = ProfileModel(person_id=person,education=edu,photo=img,resume=cv,itype_id=in_type)
    result.save()
    return redirect('main')

def delete_profile(request):
    return render(request,"process_templates/delete_profile.html",{"data":ProfileModel.objects.all()})

def delete_profile_page(request):
    try:
        del request.session["contact"]
        del request.session["name"]
        del request.session["rno"]
        res = ProfileModel.objects.get(pno=request.POST.get("pno"))
        res.delete()
        return redirect('main')
    except ProfileModel.DoesNotExist:
         return render(request,"process_templates/login.html",{"message":"Your Profile is deleted"})

def logout(request):
    try:
        del request.session["contact"]
        del request.session["name"]
        del request.session["rno"]
        return redirect('main')
    except KeyError:
        return render(request,"process_templates/login.html",{"message":"Sorry..Please do Login ..Without Login you cannot access logout"})

def about(request):
    return render(request,"process_templates/about.html")


def contactUs(request):
    return render(request,"process_templates/contactus.html")

#Consumer

class RegistrationDetails(ListAPIView):
    queryset = RegistrationModel.objects.all()
    serializer_class = RegistrationSerializer


class ProfileDetails(ListAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer