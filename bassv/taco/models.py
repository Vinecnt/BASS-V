from django.db import models
import uuid
from django.urls import reverse
from django.contrib.auth.models import User, Group
from datetime import date


# Create your models here.




class Assignment(models.Model):
	"""
    int for AID, String
    """
	# unique id for each assignment
	aid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for the Assignment")
	tid = models.ForeignKey('TA', on_delete=models.SET_NULL, null=True)
	cid = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
	# Assignment Name for referencing the assignment
	aname = models.CharField(max_length=200, help_text="Enter a name for the Assignment")
	assigned_hours = models.IntegerField(default=0, help_text="number of assigned hours")


	def __str__(self):
		"""
        String for representing the Model object (in Admin site etc.)
        Returns the name of the Assignment
        """
		return self.aname

class Ta(models.Model):
	# unique id for each assignment
	tid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for the TA")
	full_name = models.CharField(max_length=200, help_text="Enter Full Name")
	# last_name = models.CharField(max_length=200, help_text="Enter Last Name")


	# def display_course(self):
	# 	"""
    #     Creates a string for the courses. This is required to display courses for TA.
    #     """
	# 	return ', '.join([courseOfferingID.name for courseOfferingID in self.courseOfferingID.all()[:3]])
	# 	display_course.short_description = 'Courses assigned to this TA'

	# def get_absolute_url(self):
	# 	return reverse('ta-detail', args=[str(self.id)])

	def __str__(self):
		"""
        String for representing the Model object.
        Returns the name of the TA and their unique ID.
        """
		return '%s' % (self.full_name)




class Course(models.Model):
	cid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for the Course")
	professor=models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True)
	ta=models.ManyToManyField(Ta, help_text="Select a TA for this course")
	cname = models.CharField(max_length=200, help_text="Enter Course Name")
	cdescription=models.TextField(max_length=1000, help_text="Enter a brief description of the course")

	def get_absolute_url(self):
		 return reverse('course-detail', args=[str(self.cid)])

	def __str__(self):
		return self.cname

	def display_ta(self):
		return ', '.join([ ta.full_name for ta in self.ta.all()[:3]])
		display_ta.short_description = 'Ta'

	def get_assignments(self):
		return Assignment.objects.filter(cid = self.cid).all()







class Professor(models.Model):
	pid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for the Professor")
	pname = models.CharField(max_length=200, help_text="Enter Professor's Name")

	def display_course(self):
		"""
        Creates a string for the courses. This is required to display courses in Admin.
        """
		return ', '.join([courseOfferingID.name for courseOfferingID in self.courseOfferingID.all()[:3]])
		display_course.short_description = 'Courses taught by this Professor'

	def __str__(self):
		"""
        String for representing the Model object.
        Returns the name of the professor and their unique ID.
        """
		return '%s' % (self.pname)


class Update(models.Model):
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class CourseUpdate(Update):
    course = models.ForeignKey(Course)
