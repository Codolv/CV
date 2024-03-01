from django.contrib import admin
from .models import Person, Contact, Address, Skill, Education

# Register your models here.
admin.site.register(Person)
admin.site.register(Contact)
admin.site.register(Address)
admin.site.register(Skill)
admin.site.register(Education)
