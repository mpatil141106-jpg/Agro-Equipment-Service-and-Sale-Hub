from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer, Work, Appointment, Payment, Stock, Cart, Order


def Customer_Head(request):
    with open("text.txt", "r") as file:
        name = file.read().strip()
        return render(request, 'customer/customer_head.html', {"name": name})


def Customer_Dashboard(request):
    with open("text.txt", "r") as file:
        name = file.read().strip()
    # Get the total count of customers
    approve_app = Appointment.objects.filter(name=name, status="Approve").count()
    reject_app = Appointment.objects.filter(name=name, status="Reject").count()
    done_task = Appointment.objects.filter(name=name, task_status="Done").count()
    incomplete_task = Appointment.objects.filter(name=name, task_status="Inprogress").count()

    return render(request, 'customer/customer_dashboard.html',
                  {"approve": approve_app, "reject": reject_app, "done": done_task, "incomplete": incomplete_task,
                   "name": name})


def Customer_Appointment(request):
    all_services = Work.objects.all()  # Assuming ServiceModel is your model name
    filter_services = Appointment.objects.filter(status='underprocess') | Appointment.objects.filter(status='Approve')
    unique_works = set()
    unique_services = []

    for service in all_services:

        if service.work not in unique_works:
            unique_works.add(service.work)
            unique_services.append(service)
    return render(request, 'customer/customer_appointment.html',
                  {'all': unique_services, "service": all_services, 'filter': filter_services})


def Customer_Task(request):
    all_task = Appointment.objects.filter(status='Inprogress') | Appointment.objects.filter(status='Done')
    done_task = Appointment.objects.filter(status='Done')
    inprogress_task = Appointment.objects.filter(status='Inprogress')
    return render(request, 'customer/customer_task.html',
                  {'all': all_task, "done": done_task, 'inprogress': inprogress_task})


def Customer_Payment(request):
    return render(request, 'customer/customer_payment.html')


def Customer_View_Stock(request):
    with open("text.txt", "r") as file:
        name = file.read().strip()
    product = Stock.objects.all()
    return render(request, 'customer/customer_view_stock.html', {"product": product, "name": name})


def Customer_Total_Task(request):
    with open("text.txt", "r") as file:
        name = file.read().strip()
    total_task = Appointment.objects.filter(name=name, task_status="Done") | Appointment.objects.filter(name=name,
                                                                                                        task_status="Inprogress")
    return render(request, 'customer/customer_total_task.html', {"task": total_task, "name": name})


def Customer_Payment_History(request):
    with open("text.txt", "r") as file:
        name = file.read().strip()
    all = Payment.objects.filter(customer_name=name)
    return render(request, 'customer/customer_payment_history.html', {"payment": all, "name": name})


def Customer_Appointment_History(request):
    with open("text.txt", "r") as file:
        name = file.read().strip()
    all = Appointment.objects.filter(name=name, status="Approve") | Appointment.objects.filter(name=name,
                                                                                               status="Reject")
    return render(request, 'customer/customer_appointment_history.html', {"all": all, "name": name})


def Customer_Appointment_Request(request):
    with open("text.txt", "r") as file:
        name = file.read().strip()
    all_services = Work.objects.all()  # Assuming ServiceModel is your model name
    unique_works = set()
    unique_services = []

    for service in all_services:
        if service.work not in unique_works:
            unique_works.add(service.work)
            unique_services.append(service)
    return render(request, 'customer/customer_appointment_request.html',
                  {'all': unique_services, "service": all_services, "name": name})


def Customer_Inprogress_Task(request):
    with open("text.txt", "r") as file:
        name = file.read().strip()
    inprogress_task = Appointment.objects.filter(name=name, task_status="Inprogress")
    return render(request, 'customer/customer_inprogress_task.html', {"task": inprogress_task, "name": name})


def Customer_Done_Task(request):
    with open("text.txt", "r") as file:
        name = file.read().strip()
    done_task = Appointment.objects.filter(name=name, task_status="Done")
    return render(request, 'customer/customer_done_task.html', {"task": done_task, "name": name})


def View_Cart(request):
    with open("text.txt", "r") as file:
        name = file.read().strip()
    cart_items = Cart.objects.filter(customer_name=name)  # Assuming Cart model has customer_name field
    products = []
    for item in cart_items:
        product = Stock.objects.filter(
            id=item.cart_id).first()  # Assuming Cart has a field cart_id corresponding to Stock's id
        if product:
            products.append(product)
    return render(request, 'customer/view_cart.html', {"products": products, "name": name})


def myorder(request):
    with open("text.txt", "r") as file:
        name = file.read().strip()
    order=Order.objects.filter(customer_name=name)
    return render(request, 'customer/myorder.html',{"order":order,"name":name})