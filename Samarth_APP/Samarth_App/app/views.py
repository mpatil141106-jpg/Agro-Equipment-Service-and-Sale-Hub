import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Customer, Work, Appointment, Payment, Stock, Cart, Order
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
import os
from django.conf import settings
from django.shortcuts import get_object_or_404


def Home(request):
    file_path = 'text.txt'  # Update with your file path
    if os.path.exists(file_path):
        return redirect('customer_dashboard')  # Redirect to dashboard if file exists
    else:
        return render(request, 'includes/home.html')


def About(request):
    return render(request, 'includes/about.html')


def Contact(request):
    return render(request, 'includes/contact.html')


def Login(request):
    return render(request, 'includes/login.html')


def Registration(request):
    return render(request, 'includes/registration.html')


def Service(request):
    return render(request, 'includes/service.html')


def doLogin(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        # Attempt authentication for admin
        if username == 'gendrajpatil45@gmail.com' and password == 'patil1234':
            return redirect('dashboard')

        # Attempt authentication for customer
        else:
            try:
                # Retrieve customer from database based on email
                customer = Customer.objects.get(email=username)
                member = customer
                # Check if customer exists and verify password
                if customer is not None:
                    file1 = open("text.txt", "w")
                    file1.write(customer.name)
                    file1.close()
                    email = customer.email
                    passwd = customer.password
                    if username == email and check_password(password, passwd):
                        return redirect('customer_dashboard')
                    else:
                        # Authentication failed
                        return render(request, 'includes/login.html', {'error_message': 'Authentication failed'})
                else:
                    # Password doesn't match
                    return render(request, 'includes/login.html', {'error_message': 'Invalid credentials'})
            except Customer.DoesNotExist:
                # Customer not found
                print("Customer not found")
                return render(request, 'includes/login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'login.html')


def doRegistration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobileno')
        password = request.POST.get('pass')
        password = make_password(password)
        city = request.POST.get('city')
        gender = request.POST.get('gender')

        profile_image = request.FILES.get('profile_img')

        if profile_image:
            # Save the image file to the media directory
            file_path = os.path.join(settings.MEDIA_ROOT, 'profile_images', profile_image.name)
            with open(file_path, 'wb') as destination:
                for chunk in profile_image.chunks():
                    destination.write(chunk)

        else:
            profile_image_path = None

        # Create Customer object and save it to the database
        user_profile = Customer(
            name=name,
            email=email,
            mobileno=mobile_no,
            password=password,
            city=city,
            profile_image=os.path.join('profile_images', profile_image.name),
            gender=gender
        )
        user_profile.save()

        messages.success(request, 'Registration successful. Please login to continue.')
        # Redirect to a success page or any other page
        return redirect('login')
    else:
        return render(request, 'registration_form.html')


def addService(request):
    if request.method == "POST":
        service_name = request.POST.get('service')  # Use 'service_name' instead of 'name'
        service_type = request.POST.get('service_type')
        service_price = request.POST.get('service_price')
        if service_type is None:
            service_type = 'Na'

        existing_work = Work.objects.filter(work=service_name, work_type=service_type).exists()
        if not existing_work:
            work_profile = Work(
                work=service_name,  # Use 'service_name' instead of 'name'
                work_type=service_type,
                work_price=service_price
            )
            work_profile.save()

            # Redirect to a success page or any other page
            return redirect('add_service')  # Replace 'service' with your actual URL name
        else:
            return redirect('add_service')
    else:
        return redirect('add_service')


def get_work_types(request):
    selected_work = request.GET.get('work')
    types = Work.objects.filter(work=selected_work).values_list('work_type', flat=True)
    return JsonResponse(list(types), safe=False)


def make_Appointment(request):
    if request.method == 'POST':
        work_name = request.POST.get('work')
        work_Type = request.POST.get('type')
        date = request.POST.get('date')
        time = request.POST.get('time')
        name = open("text.txt", "r")
        pay = Work.objects.get(work_type=work_Type)
        a = pay.work_price
        appointment_profile = Appointment(
            name=name.read(),
            reason=work_name,
            reason_type=work_Type,
            date=date,
            time=time,
            status="underprocess",
            task_status='Na',
            pay=a
        )
        appointment_profile.save()
        messages.success(request, 'Appointment created successfully!')
        # Redirect to a success page or any other page
        return redirect('customer_appointment_request')


def customer_logout(request):
    file = os.path.exists("text.txt")
    if file:
        os.remove("text.txt")
    return redirect('home')


def deleteService(request):
    if request.method == 'POST':
        work = request.POST.get('work')
        type = request.POST.get('type')

        Work.objects.filter(work=work, work_type=type).delete()
    return redirect('manage_service')


def update_status(request):
    if request.method == "POST":
        appointment_id = request.POST.get("appointment_id")
        action = request.POST.get("action")

        if action == "approve":
            x = Appointment.objects.get(appointment_id=appointment_id)
            x.status = 'Approve'
            x.save()
            return redirect('appointment_request')
        elif action == "reject":
            x = Appointment.objects.get(appointment_id=appointment_id)
            x.status = 'Reject'
            x.save()
            return redirect('appointment_request')
        else:
            return redirect('appointment_request')


def update_task(request):
    if request.method == "POST":
        appointment_id = request.POST.get("appointment_id")
        action = request.POST.get("action")
        if action == "inprogress":
            x = Appointment.objects.get(appointment_id=appointment_id)
            x.task_status = 'Inprogress'
            x.save()
            return redirect('manage_task')
        elif action == "done":
            x = Appointment.objects.get(appointment_id=appointment_id)
            x.task_status = 'Done'
            x.save()
            return redirect('manage_task')
        else:
            return redirect('manage_task')


def search_form(request):
    if request.method == "POST":
        id = request.POST.get("appn_id")
        x = Appointment.objects.get(appointment_id=id)
        return render(request, 'owner/payment.html', {'all': x, 'id': id})
    else:
        return redirect('payment')


def pay_payment(request):
    if request.method == "POST":
        pay_id = request.POST.get("appointment_id")
        name = request.POST.get("input_name")
        service = request.POST.get("input_service")
        service_type = request.POST.get("input_service_type")
        total_payment = float(request.POST.get("input_total_payment"))
        pay_payment = float(request.POST.get("pay_payment"))
        remaining = total_payment - pay_payment
        payment_profile = Payment(
            appointment_id=pay_id,
            customer_name=name,
            service_name=service,
            service_type=service_type,
            total_amount=total_payment,
            pay_payment=pay_payment,
            remaining_payment=remaining
        )
        payment_profile.save()

        return redirect('payment')
    else:
        return redirect('payment')


def delete_customer(request, id):
    Customer.objects.filter(id=id).delete()
    return redirect('manage_customer')


def InsertStock(request):
    if request.method == 'POST':
        name = request.POST.get('product_name')
        price = request.POST.get('product_price')
        description = request.POST.get('product_discription')
        quantity = request.POST.get('quantity')
        # Get the uploaded image file
        img_file = request.FILES.get('product_img')

        if img_file:
            # Save the image file to the media directory
            file_path = os.path.join(settings.MEDIA_ROOT, 'product_images', img_file.name)
            with open(file_path, 'wb') as destination:
                for chunk in img_file.chunks():
                    destination.write(chunk)

            # Create a Stock object and save it to the database
            stock_profile = Stock(
                name=name,
                price=price,
                description=description,
                img=os.path.join('product_images', img_file.name),
                quantity=quantity
            )
            stock_profile.save()

            return redirect('add_stock')  # Redirect to the add_stock page after successful upload
        else:
            # Handle the case when no image is uploaded
            return render(request, 'error.html', {'message': 'No image uploaded'})
    else:
        return redirect('add_stock')


def add_to_cart(request):
    if request.method == 'POST':
        with open("text.txt", "r") as file:
            name = file.read().strip()
        id = Customer.objects.get(name=name)
        product_id = request.POST.get('product_id')
        print(product_id)
        cart_profile = Cart(
            cart_id=product_id,
            customer_name=name,
            customer_id=id.id
        )
        cart_profile.save()
        return redirect('view_cart')
    else:
        return redirect('customer_view_stock')


def place_order(request):
    if request.method == 'POST':
        with open("text.txt", "r") as file:
            name = file.read().strip()
        id = request.POST.get('id')
        quantity_ = int(request.POST.get('quantity'))  # Convert to int
        product = get_object_or_404(Stock, id=id)

        # Checking if requested quantity is available
        if product.quantity < quantity_:
            # Handle case where requested quantity exceeds available quantity
            # You can render an error message or redirect to an error page
            return HttpResponse("Requested quantity not available.")

        order_profile = Order(
            customer_name=name,
            product_id=id,
            product_name=product.name,
            product_price=product.price,
            quantity=quantity_,
            img=product.img
        )
        order_profile.save()

        # Updating product quantity
        product.quantity -= quantity_
        product.save()

        return redirect('view_cart')
    else:
        return redirect('view_cart')
