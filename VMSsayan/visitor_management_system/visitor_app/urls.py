from django.urls import path
from . import views




app_name = 'visitor_app'

urlpatterns = [
    path('smday/', views.smday, name='smday'),
    path('login/', views.login, name='login'),
    path('visitorlogout_poojitha/', views.visitorlogout_poojitha, name='visitorlogout_poojitha'),
    path('run/', views.run, name='run'),
    path('anusha/', views.anusha, name='anusha'),

    path('multilogin/', views.multilogin,name='multilogin'),

    path('all_data/', views.all_data, name='all_data'),
    path('barcode/', views.barcode, name='barcode'),
    path('category/', views.category, name='category'),
    path('save_category/', views.save_category, name='save_category'),
    path('department/', views.department, name='department'),
    path('save_department/', views.save_department, name='save_department'),
    path('enterprise/', views.enterprise, name='enterprise'),
    path('save_enterprise/', views.save_enterprise, name='save_enterprise'),

    
    path('postal_service/', views.postal_service, name='postal_service'),
    
    path('save_enquiry/', views.saveEnquiry, name='save_enquiry'),
    path('reports/', views.reports, name='reports'),
    path('staff_master/', views.staff_master, name='staff_master'),
    path('save_staff_master/', views.save_staff_master, name='save_staff_master'),
    
    path('user_master/', views.user_master, name='user_master'),  # Define URL pattern
    path('save_user_master/', views.save_user_master, name='save_user_master'),

    path('visitor_registration/', views.visitor_registration, name='visitor_registration'),
    path('save_visitor_registration/', views.save_visitor_registration, name='save_visitor_registration'),
    path('visitor_logout/', views.visitor_logout, name='visitor_logout'),
    
    path('generate-pdf/', views.generate_pdf_report, name='generate_pdf_report'),  # Update URL pattern name


    # Add more paths for other views as needed
]
