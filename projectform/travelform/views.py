from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Move_Request
from datetime import datetime


@login_required(login_url='login')
def homepage(request):
    data = Move_Request.objects.all()  # Fetch all instances of the MoveRequest model
    return render(request, 'form.html', {'data': data})


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('Form')

        else:

            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


def form(request):
    if request.method == 'POST':
        p_no = request.POST.get('p_no')
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        division = request.POST.get('division')
        payscale = request.POST.get('payscale')
        cnic_no = request.POST.get('cnic_no')
        passport = request.POST.get('passport')
        mobile = request.POST.get('mobile')
        project = request.POST.get('project')
        time_of_move = request.POST.get('time_of_move')
        time_of_return = request.POST.get('time_of_return')
        mode_of_travel = request.POST.get('mode_of_travel')
        date_of_moves = datetime.strptime(request.POST.get('date_of_moves'), '%Y-%m-%d').date()
        date_of_return = datetime.strptime(request.POST.get('date_of_return'), '%Y-%m-%d').date()
        route = request.POST.get('route')
        destination = request.POST.get('destination')
        category = request.POST.get('category')
        pov = request.POST.get('pov')
        duration_days = request.POST.get('duration_days')
        duration_nights = request.POST.get('duration_nights')
        relatedpro = request.POST.get('relatedpro')
        fundingsources = request.POST.get('fundingsources')
        advance = request.POST.get('advance')

        # Create a new instance of the home model
        en = Move_Request(p_no=p_no, name=name, designation=designation, division=division, payscale=payscale,
                         cnic_no=cnic_no,
                         passport=passport, mobile=mobile, project=project, time_of_move=time_of_move,
                         time_of_return=time_of_return, mode_of_travel=mode_of_travel, date_of_moves=date_of_moves,
                         date_of_return=date_of_return, route=route, destination=destination,
                         category=category, pov=pov, duration_days=duration_days,
                         duration_nights=duration_nights, relatedpro=relatedpro, fundingsources=fundingsources,
                         advance=advance)

        en.save()

        try:
            existing_data = Move_Request.objects.get(p_no=p_no)
        except Move_Request.DoesNotExist:
            existing_data = None
            move_request, created = Move_Request.objects.get_or_create(
                p_no=p_no,
                defaults={
                    'name': name,
                    'designation': designation,
                    'division': division,
                    'payscale': payscale,
                    'cnic_no': cnic_no,
                    'passport': passport,
                    'mobile': mobile,
                    'project': project,
                    'time_of_move': time_of_move,
                    'time_of_return': time_of_return,
                    'mode_of_travel': mode_of_travel,
                    'date_of_moves': date_of_moves,
                    'date_of_return': date_of_return,
                    'route': route,
                    'destination': destination,
                    'category': category,
                    'pov': pov,
                    'duration_days': duration_days,
                    'duration_nights': duration_nights,
                    'relatedpro': relatedpro,
                    'fundingsources': fundingsources,
                    'advance': advance
                }
            )
            return redirect('Form')
    return render(request, 'form.html')