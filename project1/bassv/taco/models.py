from django.db import models

# Create your models here.
class Assignments(models.Model):
    """
    int for AID, String
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    # unique id for each assignment 
    aid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for the Assignment")
    # for stroing the link to the place where the assignment is located.
    assignment_link = models.CharField(max_length=200, help_text="Enter the link to find the Assignment")
    # foregin key to reference the course which the assifnment is for
    cid= models.ForeignKey('Course',on_delete=models.SET_NULL, null=True)
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
	aid= models.ForeignKey('Assignments',on_delete=models.SET_NULL, null=True)
	tid= models.ForeignKey('TA',on_delete=models.SET_NULL, null=True)
	pid= models.ForeignKey('Professor',on_delete=models.SET_NULL, null=True)
