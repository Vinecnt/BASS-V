from django.contrib import admin

# Register your models here.
from .models import Update, Course, AssignmentCommunication, Assignment, Ta, Professor, CourseOffering

# admin.site.register(Message)
# admin.site.register(Course)
# admin.site.register(TA)
# admin.site.register(Assignment)
# admin.site.register(AssignmentCommunication)
# admin.site.register(Professor)
# admin.site.register(CourseOffering)
# admin.site.register(MessageCommunication)


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('uid','ustring')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('cname','cdescription','professor','display_ta')

@admin.register(Ta)
class TaADmin(admin.ModelAdmin):
    list_display = ('tid','full_name')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('aid','assignment_link','cid','aname')

@admin.register(AssignmentCommunication)
class AssignmentCommunicationAdmin(admin.ModelAdmin):
    # list_display = ('aid','tid','pid')
    pass


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('pid','pname')

@admin.register(CourseOffering)
class CourseOfferingAdmin(admin.ModelAdmin):
    # list_display = ('cid', 'cid')
    pass


# @admin.register(MessageCommunication)
# class MessageCommunicationAdmin(admin.ModelAdmin):
#     # list_display = ('mid','tid','pid')
#     pass
