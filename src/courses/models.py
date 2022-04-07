from django.db import models
from django.contrib.auth.models import User
# from exams.models import Exam


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    category_id = models.AutoField(
        verbose_name='Category ID',
        primary_key=True,
        unique=True,
        auto_created=True,
    )
    category_name = models.CharField(
        verbose_name='Category Name',
        max_length=200,
        blank=False,
        editable=True,
        default=None
    )
    created_at = models.DateTimeField(
        verbose_name='Created At',
        auto_now=True
    )

    def __str__(self) -> str:
        return self.category_name


class Course(models.Model):
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    course_id = models.AutoField(
        verbose_name='Course ID',
        primary_key=True,
        unique=True,
        auto_created=True,
    )
    course_name = models.CharField(
        verbose_name='Course Name',
        max_length=200,
        blank=False,
        editable=True
    )
    course_level = models.CharField(
        verbose_name='Course Level',
        max_length=255,
        blank=False,
        editable=True,
        choices=(
            ('Beginner', 'Beginner'),
            ('Intermediate', 'Intermediate'),
            ('Advanced', 'Advanced')
        )
    )
    course_description = models.TextField(
        verbose_name='Course Description',
        blank=False,
        editable=True,
        default=None,
    )
    # category_id = models.IntegerField(
    #     verbose_name='Category ID',
    #     blank=False,
    #     editable=True,
    #     choices=(
    #         (1, 1),
    #         (2, 2),
    #         (3, 3),
    #         (4, 4),
    #         (5, 5),
    #         (6, 6),
    #         (7, 7),
    #         (8, 8),
    #         (9, 9),
    #         (10, 10),
    #         (11, 11)
    #     )
    # )
    category = models.ManyToManyField(
        Category,
        verbose_name='Categories',
        blank=False,
        editable=True,
    )    
    created_at = models.DateTimeField(
        verbose_name='Created At',
        auto_now=True
    )

    def __str__(self) -> str:
        return f'Course: {self.course_id} | {self.course_name}'


class Student(models.Model):
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    user = models.OneToOneField(
        User,
        verbose_name='User',
        on_delete=models.CASCADE
    )
    student_id = models.AutoField(
        verbose_name='Student ID',
        primary_key=True,
        unique=True,
        auto_created=True,
    )
    student_name = models.CharField(
        verbose_name='Student Name',
        max_length=55,
        blank=False,
        editable=True
    )
    student_email = models.EmailField(
        verbose_name='Student Email',
        max_length=50,
        blank=False,
        editable=True,
        default=None
    )
    student_phone = models.CharField(
        verbose_name='Student Phone',
        max_length=55,
        blank=False,
        editable=True,
        default=None,
    )
    student_address = models.CharField(
        verbose_name='Student Address',
        max_length=100,
        blank=False,
        editable=True,
        default=None
    )
    student_college = models.CharField(
        verbose_name='Student College',
        max_length=44,
        blank=False,
        editable=True,
        default=None
    )
    enrolled_courses = models.ManyToManyField(
        Course,
        verbose_name='Enrolled Courses',
        blank=True,
        editable=True
    )
    # exams = models.ForeignKey(
    #     Exam,
    #     verbose_name='Student Exams',
    #     blank=True,
    #     editable=True
    # )
    exams = models.CharField(
        max_length=200,
        verbose_name='Exam Code',
        blank=True,
        editable=True
    )
    created_at = models.DateTimeField(
        verbose_name='Created At',
        auto_now=True
    )

    def __str__(self) -> str:
        return f'Student: {self.student_id}'