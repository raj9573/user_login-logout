from django.shortcuts import render
from django.shortcuts import reverse,redirect
# Create your views here.



from app.forms import *


from django.http import HttpResponse


from django.contrib.auth import authenticate,login,logout


from django.contrib.auth.decorators import login_required

def register(request):

    uf = userform()
    pf = userprofileform()

    if request.method == 'POST' and request.FILES:

        print("post method is activated")

        ufd = userform(request.POST)
        upfd = userprofileform(request.POST,request.FILES)

        if  ufd.is_valid() and upfd.is_valid():

            pw = ufd.cleaned_data['password']

            uo = ufd.save(commit=False)

            uo.set_password(pw)


            uo.save()

            upo  =  upfd.save(commit=False)

            upo.user = uo   


            upo.save()

            return HttpResponse("data saved successfully")

        else:


            return HttpResponse("data is not valid")

    return render(request,'register.html',{'uf':uf,'pf':pf})



def ul(request):


    if request.method == 'POST':


        un = request.POST.get('username')

        pw = request.POST['password']

        user = authenticate(username = un,password = pw)

        print(user)

        if user:
            login(request,user)


            # request.session['user']= user.username

            request.user = user

            return redirect('display_user')
        


    return render(request,'user_login.html')

@login_required
def display_user(request):



    # username = request.session.get('user')
    
    user = request.user

    upo = userprofile.objects.get(user = user)

    return render(request,'user_details.html',{'user':user,'upo':upo}

    )



def get_text(request):




    return HttpResponse("Action attribute called this funtion ")


@login_required
def user_logout(request):

    logout(request)


    return redirect('ul')
