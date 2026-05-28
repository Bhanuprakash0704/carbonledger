from django.contrib import admin
from .models import Tenant, Source, EmissionRecord


admin.site.register(Tenant)
admin.site.register(Source)
admin.site.register(EmissionRecord)