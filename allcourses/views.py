from django.shortcuts import render, get_object_or_404
from course.models import Course

# Create your views here.
def home(request):
    course_items = Course.objects
    return render(request, 'allcourses/home.html',{'all_course_items':course_items})

def details(request, course_id):
    detail_course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course/course_details.html',{'detailcourse':detail_course})
