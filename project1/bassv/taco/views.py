from django.shortcuts import render
from .models import *
from django.views import generic

# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    # # Generate counts of some of the main objects
    class_iter = Course.objects.all()
    # num_instances = BookInstance.objects.all().count()
    # # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    # num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable
    context = dict()
    # for item in class_iter:
    #     context[str(item)] = item.cname

    return render(
        request,
        'index.html',
    #     context={'num_books': num_books, 'num_instances': num_instances,
    #              'num_instances_available': num_instances_available, 'num_authors': num_authors},
        context,
    )

class CourseListView(generic.ListView):
    model = Course

class CourseDetailView(generic.DetailView):
    model = Course


class MessageListView(generic.ListView):
    model = Message