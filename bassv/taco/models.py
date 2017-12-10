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
	# for stroing the link to the place where the assignment is located.
	# assignment_link = models.CharField(max_length=200, help_text="Enter the link to find the Assignment")
	# foregin key to reference the course which the assifnment is for
	cid = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
	# Assignment Name for referencing the assignment
	aname = models.CharField(max_length=200, help_text="Enter a name for the Assignment")
	assigned_hours = models.IntegerField(default=0, help_text="number of assigned hours")
	#user = models.ForeignKey(User, default=1, limit_choices_to={"groups":1})
	tid = models.ForeignKey('TA', on_delete=models.SET_NULL, null=True)


	def __str__(self):
		"""
        String for representing the Model object (in Admin site etc.)
        Returns the name of the Assignment
        """
		return self.aname

	def get_assignments(self, cid_name):

		return Assignment.objects.filter(cid=cid_name)




class AssignmentCommunication(models.Model):
	"""
	making foreign keys for these
	AssignID
	TA ID
	PROFESSOR ID
	"""
	aid = models.ForeignKey('Assignment', on_delete=models.SET_NULL, null=True)
	# pid = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True)

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
	# unique id for each assignment
	cid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for the Course")
	cname = models.CharField(max_length=200, help_text="Enter Course Name")
	cdescription=models.TextField(max_length=1000, help_text="Enter a brief description of the course")
	professor=models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True)
	ta=models.ManyToManyField(Ta, help_text="Select a TA for this course")
	#assignment = models.ManyToManyField(Assignment, help_text="pick an assignment for the course")

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
	# courseOfferingID = models.ManyToManyField(Course, help_text="Select a course by this Professor")

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



class CourseOffering(models.Model):
	cid = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
	#tid = models.ForeignKey('TA', on_delete=models.SET_NULL, null=True)
#	pid = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True)
	def __str__(self):
		"""
        String for representing the Model object.
        Returns the name of the professor and their unique ID.
        """
		return '%s' % (self.cid)





class Update(models.Model):
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class CourseUpdate(Update):
    course = models.ForeignKey(Course)
