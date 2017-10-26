from django.db import models
import uuid

# Create your models here.


class Assignment(models.Model):
	"""
    int for AID, String
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
	# unique id for each assignment
	aid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for the Assignment")
	# for stroing the link to the place where the assignment is located.
	assignment_link = models.CharField(max_length=200, help_text="Enter the link to find the Assignment")
	# foregin key to reference the course which the assifnment is for
	cid = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
	# Assignment Name for referencing the assignment
	aname = models.CharField(max_length=200, help_text="Entera name for the Assignment")

	def __str__(self):
		"""
        String for representing the Model object (in Admin site etc.)
        Returns the name of the Assignment
        """
		return self.aname


class AssignmentCommunication(models.Model):
	"""
	making foreign keys for these
	AssignID
	TA ID
	PROFESSOR ID
	"""
	aid = models.ForeignKey('Assignment', on_delete=models.SET_NULL, null=True)
	tid = models.ForeignKey('TA', on_delete=models.SET_NULL, null=True)
	pid = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True)


class Course(models.Model):
	# unique id for each assignment
	cid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for the Course")
	cname = models.CharField(max_length=200, help_text="Enter Course Name")


class TA(models.Model):
	# unique id for each assignment
	tid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for the TA")
	tname = models.CharField(max_length=200, help_text="Enter First Name")
	courseOfferingID = models.ManyToManyField(Course, help_text="Select a course assigned to TA")

	def display_course(self):
		"""
        Creates a string for the courses. This is required to display courses for TA.
        """
		return ', '.join([courseOfferingID.name for courseOfferingID in self.courseOfferingID.all()[:3]])
		display_course.short_description = 'Courses assigned to this TA'

	def __str__(self):
		"""
        String for representing the Model object.
        Returns the name of the TA and their unique ID.
        """
		return '%s, %s' % (self.tname, self.tid)


class Professor(models.Model):
	pid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for the Professor")
	pname = models.CharField(max_length=200, help_text="Enter Professor's Name")
	courseOfferingID = models.ManyToManyField(Course, help_text="Select a course by this Professor")

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
		return '%s, %s' % (self.pname, self.id)


class CourseOffering(models.Model):
	cid = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
	tid = models.ForeignKey('TA', on_delete=models.SET_NULL, null=True)
	pid = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True)


class Message(models.Model):
	mid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for the Message")
	mstring = models.CharField(max_length=200, help_text="Enter the Message")


class MessageCommunication(models.Model):
	# I dont know how to reference two foreign keys to the same attribute so to make
	# it easier for the time being we just have TA and PID
	# also worst come worst we can hard code what we want our application to do

	mid = models.ForeignKey('Message', on_delete=models.SET_NULL, null=True)
	tid = models.ForeignKey('TA', on_delete=models.SET_NULL, null=True)
	pid = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True)
