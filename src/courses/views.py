import imp
from sre_parse import CATEGORIES
from unicodedata import category
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .models import *
from exams.models import *
import random


def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }

    return render(
        request=request,
        template_name='courses/index.html',
        context=context
        )


def course(request, course_id):
    course = Course.objects.get(course_id=course_id)
    context = {
        'course': course,
    }

    return render(
        request=request,
        template_name='courses/course.html',
        context=context
    )

def code(request, course_id):
    course = Course.objects.get(course_id=course_id)
    context = {
        'course': course,
    }
    return render(
        request=request,
        template_name='courses/code.html',
        context=context
    )

def enroll(request, course_id):
    course = Course.objects.get(course_id=course_id)
    student = Student.objects.get(user=request.user)
    student.enrolled_courses.add(course)
    student.save()

    # get a random exam which categories are in the course
    exams = Exam.objects.filter(categories__in=course.category.all())
    # print(list(exams[1].categories.all())[1].category_name)
    exams_cats = [[exams[i].categories.all()[j].category_name for j in range(len(exams[i].categories.all()))] for i in range(len(exams))]
    course_cats = [course.category.all()[i].category_name for i in range(len(course.category.all()))]
    valid_exams = []
    for exam in range(len(exams_cats)):
        if sorted(course_cats) == sorted(exams_cats[exam]):
            valid_exams.append(exams[exam])
    # print(valid_exams)
    random_exam = random.choice(valid_exams)
    # print()
    # print(random_exam)
    # print()
    # student.exams.add(str(random_exam.exam_id))

    send_mail(
        'Enrollment Confirmation',
        'You have been enrolled in the course: ' + course.course_name  + ' Here is your exam code',
        request.user.email,
        [student.student_email],
        fail_silently=False,
    )
    return redirect('code', course_id=course_id)

# def enroll(request):
#     if request.user.is_authenticated():

#     send_mail(
#         'Enrollment Exam Code',
#         'Your exam code is: 12345',
#         'odc.egypt.learning@gmail.com',
#         [f'{Student.student_email}'],
#     )
#     return render(
#         request=request,
#         template_name='courses/code.html'
#     )