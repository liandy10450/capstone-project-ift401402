from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import bin
from .models import customer
from .models import department
from .models import employee
from .models import hazard
from .models import job
from .models import location
from .models import vendor
from .models import product
from .models import Order
from .models import order_status

admin.site.register(bin)
admin.site.register(customer)
admin.site.register(department)
admin.site.register(employee)
admin.site.register(hazard)
admin.site.register(job)
admin.site.register(location)
admin.site.register(vendor)
admin.site.register(product)
#admin.site.register(Order)
admin.site.register(order_status)

@admin.register(Order)
class ViewAdmin(ImportExportModelAdmin):
    pass