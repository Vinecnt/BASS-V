from django.contrib import admin

# Register your models here.

from .models import Assignments, AssignmentCommunication, Course, TA, Professor,  CourseOffering, Message, MessageCommunication

# admin.site.register(Book)
# admin.site.register(Author)

# class BooksInstanceInline(admin.TabularInline):
#     model = BookInstance
#     extra = 0
#
# class BookInline(admin.TabularInline):
#     model = Book
#     extra = 0
#
@admin.register(Assignments)
class AssignmentAdmin(admin.ModelAdmin):
    list_display =  ('aid','aname')


@admin.register(AssignmentCommunication)
class AssignmentCommunicationAdmin(admin.ModelAdmin):
    pass

# admin.site.register(BookInstance)
#
# # Register the Admin classes for Book using the decorator
#

# Register the Admin classes for BookInstance using the decorator

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(CourseOffering)
class CourseOfferingAdmin(admin.ModelAdmin):
    pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass

@admin.register(MessageCommunication)
class MessageCommunication(admin.ModelAdmin):
    pass

# admin.site.register(AssignmentCommunication)
# admin.site.register(Assignments)
# admin.site.register(Course)
# admin.site.register(TA)
# admin.site.register(Professor)
# admin.site.register(CourseOffering)
# admin.site.register(MessageCommunication)
# admin.site.register(Message)