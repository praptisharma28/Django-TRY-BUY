from django.contrib import admin

# Register your models here.
from home.models import Contact
from authentication.models import Login,Signup
# Register your models here.
admin.site.register(Contact)
admin.site.register(Login)
admin.site.register(Signup)









