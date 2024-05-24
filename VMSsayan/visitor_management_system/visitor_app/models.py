


from django.db import models
from django.contrib.auth.models import User

class Enterprise(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    tel_no = models.CharField(max_length=15)
    fax_no = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField()

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Staff(models.Model):
    name = models.CharField(max_length=100)
    staff_id = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=15)
    tel_no = models.CharField(max_length=15)
    extn = models.CharField(max_length=10)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    role_choices = [
        ('Admin', 'Admin'),
        ('User', 'User'),
        ('Security', 'Security'),
    ]
    role = models.CharField(max_length=10, choices=role_choices)

    
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # Note: In a real-world scenario, use proper encryption techniques for passwords
    confirmed_password = models.CharField(max_length=100)  # For confirming the password

class PostalService(models.Model):
    type = models.CharField(max_length=50)
    reg_date_time = models.DateTimeField()
    from_address = models.TextField()
    to_address = models.TextField()
    through = models.CharField(max_length=50)
    ref_number = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)


class Visitor(models.Model):
    pass_type_choices = [
        ('Single Day', 'Single Day'),
        ('Multiple Days', 'Multiple Days'),
    ]
    pass_type = models.CharField(max_length=20, choices=pass_type_choices,null=True)
    valid_day = models.IntegerField(blank=True, null=True)
    
    # Define category choices
    CATEGORY_CHOICES = [
        ('Software', 'Software'),
        ('HR', 'HR'),
        ('IT', 'IT'),
    ]
    
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,null=True)
    DEPARTMENT_CHOICES = [
        ('DevOps', 'DevOps'),
        ('Python Full Stack', 'Python Full Stack'),
        # Add more choices as needed
    ]
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES,null=True)

    staff = models.ForeignKey(Staff,max_length=50, on_delete=models.CASCADE,null=True)
    visitor_name = models.CharField(max_length=100,null=True)
    
    # Define gender choices
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,null=True)
    company_name = models.CharField(max_length=100,null=True)
    address = models.TextField(max_length=50,null=True)
    in_date_time = models.DateTimeField(max_length=50,null=True)
    purpose = models.CharField(max_length=255,null=True)


class VisitorLog(models.Model):
    barcode_no = models.CharField(max_length=50)

    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    vehicle_no = models.CharField(max_length=20)
    item_carried = models.CharField(max_length=255)
    item_issued = models.CharField(max_length=255)
    badge_no = models.CharField(max_length=20)
    item_deposited = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)

# Add more models as per your requirements
