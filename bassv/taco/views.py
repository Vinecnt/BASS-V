from django.shortcuts import render
from .models import *
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from .forms import AddNewAssignmentForm
from django.http import HttpResponse
import json
from django.shortcuts import redirect


# def custom_login(request):
#     if request.user.is_authenticated():
#         return HttpResponseRedirect()
#     else:
#         return login(request)

# Create your views here.
@login_required
def index(request):
    """
    View function for home page of site.
    """
    # # Generate counts of some of the main objects
    # class_iter = Course.objects.all()
    # num_instances = BookInstance.objects.all().count()
    # # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    # num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable
    cr=Course.objects.filter(ta={Ta.full_name})
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

class CourseListView(LoginRequiredMixin, generic.ListView):
    model = Course

class CourseDetailView(LoginRequiredMixin, generic.DetailView):
    model = Course

    # def get_context_data(self, **kwargs):
    #     context= super(Course, self).get_context_data(** kwargs)
    #     return context

class UpdateListView(LoginRequiredMixin, generic.ListView):
    model = Update

def update(request, pk):
  course = get_object_or_404(Course, pk)
  update = CourseReview(
      comment=request.POST['comment'],
      user=request.user,
      Course=Course)
  review.save()
  return HttpResponseRedirect(reverse('course_detail', kwargs=(course.cid,)))

def addAssignment(request):
    if request.method=="POST":
        print("message")
        form= AddNewAssignmentForm(request.POST)
        # if form.is_valid():
        if True:
            print("form valid")
            # assignment=form.save(commit=False)
            assignment = Assignment()
            print(request.POST)
            print("%s, %s, %s" % (request.POST.get('aname'), request.POST.get('assigned_hours'), request.POST.get('cid')))
            assignment.aname=request.POST.get('Assignment')
            assignment.assigned_hours=request.POST.get('assigned_hours')
            assignment.cid = Course.objects.get(cid=request.POST.get('courseid'))
            assignment.tid = (Ta.objects.filter(full_name=request.POST.get('select_form')))[0]
            #assignment.tid = (Ta.objects.get(tid=request.POST.get('select_form')).tid)
            assignment.save()
            return redirect('course-detail', request.POST.get('courseid'))
    else:
        form=AddNewAssignmentForm
    return HttpResponse(
            json.dumps({'status': 'OK'}),
            content_type="application/json"
            )
