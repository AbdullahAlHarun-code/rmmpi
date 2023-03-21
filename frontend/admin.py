from django.contrib import admin
from .models import (
    ApplicationForm,
    Category,
    FormOptions,
    WorkExperience,
    AdditionalInformation,
    FormImages,

)
# Register your models here.

@admin.register(ApplicationForm)
class ApplicationFormAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'dob', 'updated', 'timestamp']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','active', 'updated', 'timestamp']

@admin.register(FormOptions)
class FormOptionsAdmin(admin.ModelAdmin):
    list_display = ['name','category']

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['application']

@admin.register(AdditionalInformation)
class AdditionalInformationAdmin(admin.ModelAdmin):
    list_display = ['application','passport_number', 'passport_issue_date', 'passport_expiry_date', 'country', 'mobile_phone']

@admin.register(FormImages)
class FormImagesAdmin(admin.ModelAdmin):
    list_display = ['application','image']