from django.contrib import admin

# Register your models here.
from .models import Message, Course, AssignmentCommunication, Assignment, TA, Professor, CourseOffering, MessageCommunication

admin.site.register(Message)
admin.site.register(Course)
admin.site.register(TA)
admin.site.register(Assignment)
admin.site.register(AssignmentCommunication)
admin.site.register(Professor)
admin.site.register(CourseOffering)
admin.site.register(MessageCommunication)