from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer, Work, Appointment, Payment, Stock,Order


def Dashboard(request):
    count = Customer.objects.all().count()
    appointment = Appointment.objects.filter(status="underprocess").count()
    task = Appointment.objects.filter(status="Approve").count() | Appointment.objects.filter(
        task_status="Done").count() | Appointment.objects.filter(task_status="Inprogress").count()
    done = Appointment.objects.filter(task_status="Done").count()
    incomplete = Appointment.objects.filter(task_status="Inprogress").count()

    return render(request, 'owner/dashboard.html',
                  {'co': count, 'app': appointment, 'task': task, 'done': done, 'inc': incomplete})


def Dashborad_Customer(request):
    all_members = Customer.objects.all
    return render(request, 'owner/customer.html', {'all': all_members})


def Dashboard_Appointment(request):
    all_members = Appointment.objects.filter(status='underprocess').values()
    all = Appointment.objects.filter(status="Approve") | Appointment.objects.filter(status="Reject")
    return render(request, 'owner/dashboard_appointment.html', {'all': all_members, "filter": all})


def Service(request):
    all_services = Work.objects.all()
    unique_works = set()
    unique_services = []

    for service in all_services:
        if service.work not in unique_works:
            unique_works.add(service.work)
            unique_services.append(service)
    return render(request, 'owner/dashboard_service.html', {'all': unique_services})


def Task(request):
    all = Appointment.objects.filter(status="Approve")
    return render(request, 'owner/dashboard_task.html', {"filter": all})


def Update(request):
    return render(request, 'owner/dashboard_update.html')


def view_customer(request):
    all_members = Customer.objects.all
    return render(request, 'owner/view_customer.html', {'all': all_members})


def manage_customer(request):
    all_members = Customer.objects.all
    return render(request, 'owner/manage_customer.html', {'all': all_members})


def add_service(request):
    return render(request, 'owner/add_service.html')


def manage_service(request):
    all_services = Work.objects.all()
    unique_works = set()
    unique_services = []

    for service in all_services:
        if service.work not in unique_works:
            unique_works.add(service.work)
            unique_services.append(service)
    return render(request, 'owner/manage_service.html', {'all': unique_services})


def manage_task(request):
    all = Appointment.objects.filter(status="Approve", task_status='Na')
    return render(request, 'owner/manage_task.html', {"filter": all})


def inprogress_task(request):
    all = Appointment.objects.filter(task_status="Inprogress")
    return render(request, 'owner/inprogress_task.html', {"filter_done": all})


def done_task(request):
    all = Appointment.objects.filter(task_status="Done")
    return render(request, 'owner/done_task.html', {"filter_done": all})


def appointment_request(request):
    all_members = Appointment.objects.filter(status='underprocess').values()
    return render(request, 'owner/appointment_request.html', {'all': all_members})


def appointment_history(request):
    all = Appointment.objects.filter(status="Approve") | Appointment.objects.filter(status="Reject")
    return render(request, 'owner/appointment_history.html', {"filter": all})


def payment(request):
    all = Payment.objects.all()
    return render(request, 'owner/payment.html', {'all': all})


def payment_history(request):
    all = Payment.objects.all()
    return render(request, 'owner/payment_history.html', {'payment': all})


def add_stock(request):
    return render(request, 'owner/add_stock.html')


def view_stock(request):
    all = Stock.objects.all()
    for i in all:
        print(i.name)
    return render(request, 'owner/view_stock.html', {'product': all})


def notification_view(request):
    low_stock_products = Stock.objects.filter(quantity__lt=5)
    return render(request, 'owner/notification.html', {"low_stock_products": low_stock_products})


def order_product(request):
    order=Order.objects.all()
    return render(request,'owner/order_product.html',{"order":order})