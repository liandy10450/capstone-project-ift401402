from django.conf import settings
from django.db import models
from django.utils import timezone


class Order(models.Model):
    status = (
        ('New', 'New'),
        ('processed', 'processed'),
        ('being delivered', 'being delivered'),
        ('completed', 'completed'),
        ('cancelled', 'cancelled'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #order_id = models.IntegerField(primary_key=True)
    order_id = models.AutoField(primary_key=True)
    quantity = models.CharField(max_length=3)
    bin_id = models.ForeignKey(
        'Bin',
        on_delete=models.CASCADE,
    )
    deliver_to_whse = models.CharField(max_length=12)
    customer_phone = models.CharField(max_length=12)
    deliver_to_location = models.CharField(max_length=12)
    customer_id = models.ForeignKey(
        'customer',
        on_delete=models.CASCADE,
    )
    deliver_date = models.CharField(max_length=12,default='')
    emp_id = models.ForeignKey(
        'employee',
        on_delete=models.CASCADE,
    )
    vendor_id = models.ForeignKey(
        'vendor',
        on_delete=models.CASCADE,
    )
    product_id = models.ForeignKey(
        'product',
        on_delete=models.CASCADE,
    )

    created_date = models.CharField(max_length=12,default='')
    #created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.CharField(max_length=12,default='')
    #published_date = models.DateTimeField(auto_now=True)
    order_status_id=models.ForeignKey(
        'order_status',
        on_delete=models.CASCADE,
        default='0'
    )

    selected = models.BooleanField(default=False)

    #does not work. no str in Order table
    #def __str__(self):
    #    return self.str(order_id)
    
    def __str__(self):
        return self.product_id.name

class job(models.Model):
    job_id = models.IntegerField(primary_key=True)
    job_title = models.CharField(max_length=50)
    salary = models.CharField(max_length=10)
    def __str__(self):
        return self.job_title

class department(models.Model):
    dep_id = models.IntegerField(primary_key=True)
    dep_name = models.CharField(max_length=50)
    location_id = models.ForeignKey(
        'location',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.dep_name

class employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_fname = models.CharField(max_length=30)
    emp_lname = models.CharField(max_length=30)
    emp_phone = models.CharField(max_length=30)
    emp_email = models.CharField(max_length=50)
    hire_date = models.CharField(max_length=30)
    dep_id = models.ForeignKey(
        'department',
        on_delete=models.CASCADE,
    )
    job_id = models.ForeignKey(
        'job',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.emp_lname + ", " + self.emp_fname

class vendor(models.Model):
    vendor_id = models.IntegerField(primary_key=True)
    vendor_name = models.CharField(max_length=50)
    location_id = models.ForeignKey(
        'location',
        on_delete=models.CASCADE,
    )
    phone = models.CharField(max_length=30)
    def __str__(self):
        return self.vendor_name

class location(models.Model):
    location_id = models.IntegerField(primary_key=True)
    location_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    street = models.CharField(max_length=100)
    def __str__(self):
        return self.location_name

class product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    description = models.TextField(blank=True)
    hazard_id = models.ForeignKey(
        'hazard',
        on_delete=models.CASCADE,
    )
    unit_of_measurement = models.CharField(max_length=10)
    cost = models.CharField(max_length=10)
    contract_limit = models.CharField(max_length=10)
    qty_stock = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    hazard_rating = models.CharField(max_length=50, default='0')
    def __str__(self):
        return self.name

class customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_fname = models.CharField(max_length=50)
    customer_lname = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=50)
    location_id = models.ForeignKey(
        'location',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.customer_lname + ", " + self.customer_fname

class bin(models.Model):
    bin_id = models.IntegerField(primary_key=True)
    number_of_items = models.CharField(max_length=10)
    hazard_id = models.ForeignKey(
        'hazard',
        on_delete=models.CASCADE,
    )
    hazard_rating = models.CharField(max_length=50, default='0')
    def __str__(self):
        return str(self.bin_id)

class hazard(models.Model):
    hazard_id = models.IntegerField(primary_key=True)
    hazard_type = models.CharField(max_length=50)
    def __str__(self):
        return self.hazard_type

class order_status(models.Model):
    status_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=50, default='0')
    def __str__(self):
        return self.status