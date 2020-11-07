from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group, User
from django import forms
# class myUserCreationForm_bus(forms.ModelForm):
#     class Meta:
#         model = bus
#         fields = ('routeId','locationNo','plateNo')

class busAdmin(admin.ModelAdmin):
    # change_form = myUserCreationForm_bus
    # def get_form(self, request, obj=None, **kwargs):
    #     self.form = self.change_form
    #     return super(busAdmin, self).get_form(request, obj, **kwargs)
    #
    # def has_add_permission(self, request):
    #     return True
    list_display = ['버스번호','번호판','현재위치','routeId']

admin.site.register(bus,busAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)