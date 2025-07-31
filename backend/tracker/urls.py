from django.urls import path
from . import views
from .views import FoodUploadView
from django.contrib.auth.views import LogoutView
from .views import logout_view
urlpatterns = [
    path('', views.welcome_page, name='welcome'),  # Show welcome.html when root URL is hit
    path('test/', views.test_api, name='test'),
    path('example/', views.example_view, name='example'),
    path('upload/', FoodUploadView.as_view(), name='upload'),
    path('home/', views.home, name='home'),  # Use if you want a /home/ page later
    path('signup/', views.signup_view, name='signup'),
    path('verify/', views.verify_otp_view, name='verify_otp'),
    path('login/', views.login_view, name='login'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('verify-reset-otp/', views.verify_reset_otp_view, name='verify_reset_otp'),
    path('reset-password/', views.reset_password_view, name='reset_password'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('open-camera/', views.open_camera, name='open_camera'),
    path('logout/', logout_view, name='logout'),
    path('food-history/', views.food_history, name='food_history'),
    path('add-item/', views.add_item, name='add_item'),
    path('food-history/delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('run-expiry-check/', views.run_expiry_check, name='run_expiry_check'),
    path('api/scan-barcode/', views.scan_barcode, name='scan_barcode'),
    path('api/scan-label/', views.scan_label_ocr, name='scan_label_ocr'),
    
]
