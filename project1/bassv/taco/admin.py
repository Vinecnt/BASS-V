from django.contrib import admin

# Register your models here.
from .models import Message, Course, AssignmentCommunication, Assignment, TA, Professor, CourseOffering, MessageCommunication

# admin.site.register(Message)
# admin.site.register(Course)
# admin.site.register(TA)
# admin.site.register(Assignment)
# admin.site.register(AssignmentCommunication)
# admin.site.register(Professor)
# admin.site.register(CourseOffering)
# admin.site.register(MessageCommunication)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('mid','mstring')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('cid','cname')

@admin.register(TA)
class TAADmin(admin.ModelAdmin):
    list_display = ('tid','tname')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('aid','assignment_link','cid','aname')

@admin.register(AssignmentCommunication)
class AssignmentCommunicationAdmin(admin.ModelAdmin):
    list_display = ('aid','tid','pid')


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('pid','pname')

@admin.register(CourseOffering)
class CourseOfferingAdmin(admin.ModelAdmin):
    list_display = ('cid', 'cid')


@admin.register(MessageCommunication)
class MessageCommunicationAdmin(admin.ModelAdmin):
    list_display = ('mid','tid','pid')
