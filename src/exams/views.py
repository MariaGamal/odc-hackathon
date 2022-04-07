from django.shortcuts import render
from .models import *

# def enroll(request, course_id):
#     course = Course.objects.get(course_id=course_id)
#     student = Student.objects.get(user=request.user)
#     student.enrolled_courses.add(course)
#     student.save()

#     # get a random exam which categories are in the course
#     exams = Exam.objects.filter(categories__in=course.category.all())
#     # print(list(exams[1].categories.all())[1].category_name)
#     exams_cats = [[exams[i].categories.all()[j].category_name for j in range(len(exams[i].categories.all()))] for i in range(len(exams))]
#     course_cats = [course.category.all()[i].category_name for i in range(len(course.category.all()))]
#     valid_exams = []
#     for exam in range(len(exams_cats)):
#         if sorted(course_cats) == sorted(exams_cats[exam]):
#             valid_exams.append(exams[exam])
#     print(valid_exams)


# Takes exam_id from enroll function in courses/views.py
def exam(request, exam_id):
    exam = Exam.objects.get(exam_id=exam_id)
    context = {
        'exam': exam,
    }

    return render(
        request=request,
        template_name='courses/exam.html',
        context=context
    )