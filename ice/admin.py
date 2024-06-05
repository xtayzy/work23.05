from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.

from ice.models import *

admin.site.register(Dads)
admin.site.register(Moms)
admin.site.register(Children)
admin.site.register(Kiosk)
admin.site.register(IceCream)
