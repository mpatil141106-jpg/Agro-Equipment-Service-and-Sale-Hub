from django.db import models


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    mobileno = models.CharField(max_length=15, default='')
    password = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    gender = models.CharField(max_length=10, default='')


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default='')
    reason = models.CharField(max_length=100, default='')
    reason_type = models.CharField(max_length=50, default='')
    date = models.DateField(max_length=20, default='')
    time = models.TimeField(max_length=10, default='')
    status = models.CharField(max_length=20, default='')
    task_status = models.CharField(max_length=20, default='')
    appointment_date = models.DateField(auto_now_add=True)
    pay = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class Work(models.Model):
    service_id = models.AutoField(primary_key=True)
    work = models.CharField(max_length=50)
    work_type = models.CharField(max_length=50)
    work_price = models.DecimalField(max_digits=10, decimal_places=2)


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    appointment_id = models.IntegerField()
    customer_name = models.CharField(max_length=20, default='')
    service_name = models.CharField(max_length=100, default='')
    service_type = models.CharField(max_length=50, default='')
    payment_date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_payment = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_payment = models.DecimalField(max_digits=10, decimal_places=2)


class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=15)
    description = models.CharField(max_length=500)
    img = models.ImageField(upload_to='media/product_images/', null=True, blank=True)
    quantity = models.IntegerField()


class Cart(models.Model):
    cart_id = models.IntegerField()
    customer_name = models.CharField(max_length=100, default='')
    customer_id = models.IntegerField(default=1)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100, default='')
    product_id = models.IntegerField(default=1)
    product_name = models.CharField(max_length=50)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='media/order_images/', null=True, blank=True)
    quantity = models.IntegerField(default=1)
