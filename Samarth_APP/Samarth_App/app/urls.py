from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views, customer, owner

urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('login/', views.Login, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('customer_logout/', views.customer_logout, name='customer_logout'),
    path('registration/', views.Registration, name='registration'),
    path('doRegistration/', views.doRegistration, name='doRegistration'),
    path('service/', views.Service, name='service'),
    path('delete_service/', views.deleteService, name='delete_service'),
    path('owner/addService/', views.addService, name='addService'),
    path('get_work_types/', views.get_work_types, name='get_work_types'),
    path('owner/customer/', owner.Dashborad_Customer, name='customer'),
    path('place_order/', views.place_order, name='place_order'),

    # Owner module
    path('owner/dashboard/', owner.Dashboard, name='dashboard'),
    path('owner/view_customer/', owner.view_customer, name='view_customer'),
    path('owner/manage_customer/', owner.manage_customer, name='manage_customer'),
    path('delete_customer/<int:id>/', views.delete_customer, name='delete_customer'),
    path('owner/add_service/', owner.add_service, name='add_service'),
    path('owner/manage_service/', owner.manage_service, name='manage_service'),
    path('owner/manage_task/', owner.manage_task, name='manage_task'),
    path('owner/inprogress_task/', owner.inprogress_task, name='inprogress_task'),
    path('owner/done_task/', owner.done_task, name='done_task'),
    path('owner/appointment_request/', owner.appointment_request, name='appointment_request'),
    path('update_status/', views.update_status, name='update_status'),
    path('update_task/', views.update_task, name='update_task'),
    path('owner/appointment_history/', owner.appointment_history, name='appointment_history'),
    path('owner/payment/', owner.payment, name='payment'),
    path('pay_payment/', views.pay_payment, name='pay_payment'),
    path('owner/payment_history/', owner.payment_history, name='payment_history'),
    path('owner/add_stock/', owner.add_stock, name='add_stock'),
    path('owner/insert_stock/', views.InsertStock, name='insert_stock'),
    path('owner/view_stock/', owner.view_stock, name='view_stock'),
    path('owner/notification_view/', owner.notification_view, name='notification_view'),
    path('owner/order_product/', owner.order_product, name='order_product'),
    path('search_form/', views.search_form, name='search_form'),

    path('customer/customer_dashboard/', customer.Customer_Dashboard, name='customer_dashboard'),
    path('customer/customer_appointment/', customer.Customer_Appointment, name='customer_appointment'),
    path('make_appointment/', views.make_Appointment, name='make_appointment'),
    path('customer/customer_total_task/', customer.Customer_Total_Task, name='customer_total_task'),
    path('customer/customer_done_task/', customer.Customer_Done_Task, name='customer_done_task'),
    path('customer/customer_inprogress_task/', customer.Customer_Inprogress_Task,
         name='customer_inprogress_task'),
    path('customer/customer_appointment_request/', customer.Customer_Appointment_Request,
         name='customer_appointment_request'),
    path('customer/customer_appointment_history/', customer.Customer_Appointment_History,
         name='customer_appointment_history'),
    path('customer/customer_payment_history/', customer.Customer_Payment_History,
         name='customer_payment_history'),
    path('customer/customer_view_stock/', customer.Customer_View_Stock, name='customer_view_stock'),
    path('customer/view_cart/', customer.View_Cart, name='view_cart'),
    path('customer/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('customer/customer_head/', customer.Customer_Head, name='customer_head'),
    path('customer/myorder/', customer.myorder, name='myorder')

]
