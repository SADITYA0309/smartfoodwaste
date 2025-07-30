from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .models import FoodItem
from .serializers import FoodItemSerializer
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
@api_view(['GET'])
def test_api(request):
    return Response({"message": "Smart Food Tracker API working!"})

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from tracker!")
from django.http import JsonResponse

def example_view(request):
    return JsonResponse({'message': 'It works!'})

class FoodUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        serializer = FoodItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Later, insert image recognition logic here
            return Response({'message': 'Uploaded successfully', 'data': serializer.data})
        return Response(serializer.errors, status=400)
def home(request):
    return render(request, 'tracker/home.html')

def test_api(request):
    return JsonResponse({"message": "API is working!"})
def welcome_page(request):
    return render(request, 'tracker/welcome.html')



from django.contrib.auth.models import User
from django.contrib import messages

import random
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        otp = random.randint(100000, 999999)
        request.session['signup_data'] = {
            'email': email,
            'username': username,
            'password': password,
            'otp': str(otp)
        }

        send_mail(
            'Your OTP for Smart Food Tracker',
            f'Your OTP is {otp}',
            'your_email@gmail.com',
            [email],
            fail_silently=False,
        )
        return redirect('verify_otp')
    return render(request, 'tracker/signup.html')


def verify_otp_view(request):
    if request.method == 'POST':
        user_otp = request.POST['otp']
        saved_data = request.session.get('signup_data')
        if saved_data and user_otp == saved_data['otp']:
            user = User.objects.create_user(
                username=saved_data['username'],
                email=saved_data['email'],
                password=saved_data['password']
            )
            del request.session['signup_data']
            messages.success(request, 'Signup successful!')
            return redirect('login')
        else:
            messages.error(request, 'Invalid OTP')
    return render(request, 'tracker/verify_otp.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Replace with your dashboard URL name
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'tracker/login.html')

def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.filter(email=email).first()
            otp = random.randint(100000, 999999)
            request.session['reset_email'] = email
            request.session['reset_otp'] = str(otp)
            send_mail(
                'Reset Password OTP',
                f'Your OTP is {otp}',
                'your_email@gmail.com',
                [email],
                fail_silently=False,
            )
            return redirect('verify_reset_otp')
        except User.DoesNotExist:
            messages.error(request, "Email not found")
    return render(request, 'tracker/forgot_password.html')


def verify_reset_otp_view(request):
    if request.method == 'POST':
        entered_otp = request.POST['otp']
        if entered_otp == request.session.get('reset_otp'):
            return redirect('reset_password')
        else:
            messages.error(request, "Invalid OTP")
    return render(request, 'tracker/verify_reset_otp.html')


def reset_password_view(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
        else:
            email = request.session.get('reset_email')
            user = User.objects.filter(email=email).first()
            user.set_password(password)
            user.save()
            messages.success(request, "Password reset successful. Please log in.")
            return redirect('login')
    return render(request, 'tracker/reset_password.html')
@login_required
def dashboard(request):
    if request.user.is_authenticated:
        history_items = FoodItem.objects.filter(user=request.user)
        return render(request, 'tracker/dashboard.html', {'history_items': history_items})
    else:
        return redirect('login')
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile
@login_required
def edit_profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)  # <-- This line fixes it

    if request.method == 'POST':
        full_name = request.POST.get('first_name')
        email = request.POST.get('email')
        profile_picture = request.FILES.get('profile_picture')

        user.first_name = full_name
        user.email = email
        user.save()

        if profile_picture:
            profile.profile_picture = profile_picture
            profile.save()

        return redirect('dashboard')

    return render(request, 'tracker/edit_profile.html', {'user': user, 'profile': profile})
@login_required
def open_camera(request):
    return render(request, 'tracker/open_camera.html')
from django.contrib.auth import logout
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
@login_required
def food_history(request):
    items = FoodHistory.objects.filter(user=request.user).order_by('-purchase_date')
    return render(request, 'tracker/food_history.html', {'items': items})


from django import forms
from .models import Item
from .forms import AddItemForm
from .models import FoodHistory
@login_required
def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.user = request.user
            food.save()
            return redirect('food_history')
    else:
        form = AddItemForm()
    return render(request, 'tracker/add_item.html', {'form': form})
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

@require_POST
@login_required
def delete_item(request, item_id):
    item = get_object_or_404(FoodHistory, id=item_id, user=request.user)
    item.delete()
    return redirect('food_history')
<<<<<<< HEAD

# tasks.py or in your views.py temporarily
from datetime import date, timedelta
from django.core.mail import send_mail
from .models import FoodItem

def check_expiring_items():
    today = date.today()
    notify_date = today + timedelta(days=2)

    items = FoodItem.objects.filter(expiry_date=notify_date, alert_sent=False)

    for item in items:
        # Email notification
        if item.user.email:
            send_mail(
                subject=f"⚠️ Your '{item.name}' is expiring soon!",
                message=f"Hi {item.user.username},\n\nYour '{item.name}' is going to expire on {item.expiry_date}.",
                from_email="companioncareeplus@gmail.com",
                recipient_list=[item.user.email],
                fail_silently=False,
            )

        item.alert_sent = True
        item.save()
from django.http import JsonResponse

@login_required
def run_expiry_check(request):
    check_expiring_items()
    return JsonResponse({'status': 'Check complete, emails sent if needed'})
=======
>>>>>>> b3f9822bebec3b90f8b8c02c56acc278ad26fcad
