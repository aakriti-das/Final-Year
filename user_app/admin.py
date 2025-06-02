from django.contrib import admin

# Register your models here.
from user_app.models import Record,Station,Vehicle

admin.site.register(Record)
admin.site.register(Station)
admin.site.register(Vehicle)