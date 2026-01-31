from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Appointment)
admin.site.register(Work)
admin.site.register(Payment)
admin.site.register(Stock)
admin.site.register(Cart)
admin.site.register(Order)