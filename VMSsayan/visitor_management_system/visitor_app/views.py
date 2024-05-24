from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .forms import VisitorRegistrationForm,VisitorLogoutForm
from .models import Visitor, VisitorLog, Category, Department, Staff, Enterprise, PostalService
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import PostalService  # Import the PostalService model
from .models import PostalService
from .models import UserProfile
from django.contrib import messages
from .models import Category

from .models import Visitor, Category
from django.shortcuts import get_object_or_404
# views.py

from django.shortcuts import render
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from .models import Enterprise, Staff, VisitorLog

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

import sys
print(sys.path)

    

def visitorlogout_poojitha(request):
    
    # Implement logic for displaying all data
    return render(request, 'visitorlogout.html')
def smday(request):
    return render(request, 'smday.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect to alldata.html after successful login
            return redirect('visitor_app:all_data')
        else:
            # Authentication failed
            # Add your logic to handle authentication failure, such as displaying an error message
            pass
    return render(request, 'login.html')

def all_data(request):
    
    # Implement logic for displaying all data
    return render(request, 'alldata.html')


def anusha(request):
    
    # Implement logic for displaying all data
    return render(request, 'exisitingvisitor.html')


def barcode(request):
    # Implement barcode-related logic
    return render(request, 'barcode.html')



def category(request):
    # Implement logic for managing categories
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})

def save_category(request):
    
    if request.method == 'POST':
        name = request.POST.get('Category')
        description = request.POST.get('Description')
        
        # Create a new Category object and save it to the database
        category = Category.objects.create(name=name, description=description)
        category.save()
    
    return render(request, 'category.html')
def department(request):
    # Implement logic for managing departments
    departments = Department.objects.all()
    return render(request, 'department.html', {'departments': departments})
def save_department(request):
    if request.method == 'POST':
        name = request.POST.get('Department')
        description = request.POST.get('Description')
        
        # Create a new Department object and save it to the database
        department = Department.objects.create(name=name, description=description)
        department.save()
        
    
    return render(request, 'department.html')
def enterprise(request):
    # Implement logic for managing enterprise details
    enterprise_details = Enterprise.objects.all()
    return render(request, 'enterprise1.html', {'enterprise_details': enterprise_details})
def save_enterprise(request):
    if request.method == "POST":
     
        # Extract form data
         name = request.POST.get('enterpriseName')
         address = request.POST.get('address1')
         city = request.POST.get('city')
         state = request.POST.get('state')
         pincode = request.POST.get('pincode')
         tel_no = request.POST.get('phoneNumber')
         email = request.POST.get('email')
         website = request.POST.get('website')

        # Create and save Enterprise object
         enterprise = Enterprise(
            name=name,
            address=address,
            city=city,
            state=state,
            pincode=pincode,
            tel_no=tel_no,
            email=email,
            website=website
        )
         enterprise.save()


    # Handle GET request if needed
    return render(request, 'enterprise.html')
   
    
def postal_service(request):
    # Retrieve postal entries from the database
    postal_entries = PostalService.objects.all()

    # Pass postal_entries to the template context
    return render(request, 'postal.html', {'postal_entries': postal_entries})
def saveEnquiry(request):
    if request.method == "POST":
        type = request.POST.get('type')
        regDateTime = request.POST.get('regDateTime')
        from_value = request.POST.get('from')
        to = request.POST.get('to')
        through = request.POST.get('through')
        refNumber = request.POST.get('refNumber')
        contactPerson = request.POST.get('contactPerson')
        mobileNumber = request.POST.get('mobileNumber')
        
        en=PostalService(type=type,reg_date_time=regDateTime,from_address=from_value,to_address=to,through=through,ref_number=refNumber,contact_person=contactPerson,mobile_no=mobileNumber)
        en.save()
    
    return render(request, "postal.html")
def reports(request):
    # Implement logic for generating reports
    return render(request, 'Reports.html')

def staff_master(request):
    # Implement logic for managing staff details
    staff_members = Staff.objects.all()
    return render(request, 'staffmaster.html', {'staff_members': staff_members})

def save_staff_master(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        name = request.POST.get('name')
        staff_id = request.POST.get('staffid')
        department_name = request.POST.get('deptname')
        mobile_no = request.POST.get('mobileno')
        tel_no = request.POST.get('telno')
        extn = request.POST.get('extn')
        # Assuming Department object is already created based on the selected department name
        # Fetch the department object based on the selected name
        # try:
        #     department = Department.objects.get(name=department_name)
        # except Department.DoesNotExist:
            # Handle the case where department does not exist
            # return HttpResponse("Department does not exist", status=404)

        # Create a new Staff object and save it to the database
        sf = Staff(
            name=name,
            staff_id=staff_id,
            department=department_name,
            mobile_no=mobile_no,
            tel_no=tel_no,
            extn=extn
        )
        sf.save()
        # Optionally, you can redirect the user to a different page after saving the data
        # return redirect('success_page')  # Replace 'success_page' with your actual URL name
    
    # Handle cases where the request method is not POST
    # return HttpResponse("Method not allowed", status=405)

        return render(request, "staffmaster.html")

    
def run(request):
    return render(request, 'multiple.html')

def multilogin(request):
    return render(request, 'multilogin.html')


def user_master(request):
    # Implement logic for managing user accounts
    # For example:
    users = User.objects.all()
    return render(request, 'usermaster.html', {'users': users})
def save_user_master(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        role = request.POST.get('role')
        
        # Check if passwords match
        if password != confirmpassword:
            # Handle password mismatch error (Redirect, render error message, etc.)
            pass  # For now, we'll just pass
            
        # Create or get the User instance
        user, created = User.objects.get_or_create(username=username)
        if created:
            user.set_password(password)
            user.save()
        
        # Check if a UserProfile already exists for the user
        try:
            profile = UserProfile.objects.get(user=user)
            # If UserProfile exists, update it with new data
            profile.name = name
            profile.role = role
            profile.save()
        except UserProfile.DoesNotExist:
            # If UserProfile doesn't exist, create a new one
            profile = UserProfile.objects.create(user=user, name=name, role=role)
        
        # Redirect or render success message
        # return redirect('user_master')  # Redirect to the appropriate page after saving
    
    return render(request, 'usermaster.html')




def visitor_registration(request):
    # Implement logic for visitor registration
    if request.method == 'POST':
        form = VisitorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record inserted successfully!')
            return redirect('visitor_registration')
        else:
            messages.error(request, 'Error in form submission. Please check your input.')
    else:
        form = VisitorRegistrationForm()
    
    return render(request, 'visitorregistration.html', {'form': form})


            
def save_visitor_registration(request):
    if request.method == 'POST':
        pass_type = request.POST.get('pass_type')  
        valid_day = request.POST.get('valid_day')
        category = request.POST.get('category')
        department = request.POST.get('department')
        staff = request.POST.get('staff')
        visitor_name = request.POST.get('visitor_name')
        gender = request.POST.get('gender')
        company_name = request.POST.get('company_name')
        address = request.POST.get('address')
        in_date_time = request.POST.get('in_date_time')
        purpose = request.POST.get('purpose')
        print(request.POST)
        if not pass_type:
            print("pass_type field is empty or not submitted correctly")

        visitor = Visitor(
            pass_type=pass_type,
            valid_day=valid_day,
            category=category,
            department=department,
            staff=staff,
            visitor_name=visitor_name,
            gender=gender,
            company_name=company_name,
            address=address,
            in_date_time=in_date_time,
            purpose=purpose
        )
        visitor.save()

        messages.success(request, 'Visitor registered successfully!')
        return redirect('visitor_app:visitor_registration')
    else:
        messages.error(request, 'Error in form submission. Please check your input.')
        form = VisitorRegistrationForm()
    
    return render(request, 'visitorregistration.html')




def visitor_logout(request):
    # Implement logic for visitor logout
    if request.method == 'POST':
        form = VisitorLogoutForm(request.POST)
        if form.is_valid():
            # Handle visitor logout
            # ...
            messages.success(request, 'User logged out successfully!')
            return redirect('visitor_logout')
        else:
            messages.error(request, 'Error in form submission. Please check your input.')
    else:
        form = VisitorLogoutForm()

    return render(request, 'visitorlogout.html', {'form': form})

"""def generate_pdf_report(request):
    # Retrieve data based on form submission
    dept_name = request.POST.get('deptname')
    staff_name = request.POST.get('staffname')
    from_date = request.POST.get('from_date')
    to_date = request.POST.get('to_date')

    # Fetch data from the database based on the form inputs
    enterprises = Enterprise.objects.all()
    
    # Fetch department and category data
    departments = Department.objects.all()
    categories = Category.objects.all()

    # Create a response object
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # Create a PDF document
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Add data to the PDF document
    elements.append(Paragraph('Enterprise Details:', getSampleStyleSheet()['Heading1']))
    enterprise_data = [
        [enterprise.name, enterprise.address, enterprise.city, enterprise.state, enterprise.pincode, enterprise.tel_no, enterprise.fax_no, enterprise.email, enterprise.website]
        for enterprise in enterprises
    ]
    enterprise_table = Table(data=enterprise_data, style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
    elements.append(enterprise_table)

    elements.append(Paragraph('Department Details:', getSampleStyleSheet()['Heading1']))
    department_data = [
        [department.name, department.description]
        for department in departments
    ]
    department_table = Table(data=department_data, style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
    elements.append(department_table)

    elements.append(Paragraph('Category Details:', getSampleStyleSheet()['Heading1']))
    category_data = [
        [category.name, category.description]
        for category in categories
    ]
    category_table = Table(data=category_data, style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
    elements.append(category_table)

    # Build PDF document
    doc.build(elements)

    return response
"""
def generate_pdf_report(request):
    # Fetch data from the database based on the form inputs
    enterprises = Enterprise.objects.all()
    departments = Department.objects.all()
    categories = Category.objects.all()
    user_profiles = UserProfile.objects.all()
    postal_services = PostalService.objects.all()

    # Create a response object
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # Create a PDF document
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Add data to the PDF document
    styles = getSampleStyleSheet()
    
    # Add Enterprise Details
    elements.append(Paragraph('Enterprise Details:', styles['Heading1']))
    enterprise_data = [
        [enterprise.name, enterprise.address, enterprise.city, enterprise.state, enterprise.pincode, enterprise.tel_no, enterprise.fax_no, enterprise.email, enterprise.website]
        for enterprise in enterprises
    ]
    enterprise_table = Table(data=enterprise_data, style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
    elements.append(enterprise_table)

    # Add Department Details
    elements.append(Paragraph('Department Details:', styles['Heading1']))
    department_data = [
        [department.name, department.description]
        for department in departments
    ]
    department_table = Table(data=department_data, style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
    elements.append(department_table)

    # Add Category Details
    elements.append(Paragraph('Category Details:', styles['Heading1']))
    category_data = [
        [category.name, category.description]
        for category in categories
    ]
    category_table = Table(data=category_data, style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
    elements.append(category_table)

    # Add User Profile Details
    elements.append(Paragraph('User Profile Details:', styles['Heading1']))
    user_profile_data = [
        [profile.name, profile.user.username, profile.role]
        for profile in user_profiles
    ]
    user_profile_table = Table(data=user_profile_data, style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
    elements.append(user_profile_table)

    # Add Postal Service Details
    elements.append(Paragraph('Postal Service Details:', styles['Heading1']))
    postal_service_data = [
        [service.type, service.reg_date_time, service.from_address, service.to_address, service.through, service.ref_number, service.contact_person, service.mobile_no]
        for service in postal_services
    ]
    postal_service_table = Table(data=postal_service_data, style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
    elements.append(postal_service_table)

    # Build PDF document
    doc.build(elements)

    return response
