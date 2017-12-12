from django.contrib import admin

# Register your models here.
from .models import Update, Course, Assignment, Ta, Professor, CourseUpdate

# admin.site.register(Course)
# admin.site.register(TA)
# admin.site.register(Assignment)
# admin.site.register(Professor)
# @admin.register(Update)

# class UpdateAdmin(admin.ModelAdmin):
#     list_display = ('uid','ustring')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('cname','cdescription','professor','display_ta')

@admin.register(Ta)
class TaADmin(admin.ModelAdmin):
    list_display = ('tid','full_name')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('aid','cid','aname')

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('pid','pname')


@admin.register(CourseUpdate)
class CourseUpdateAdmin(admin.ModelAdmin):
    # list_display = ('mid','tid','pid')
    pass
