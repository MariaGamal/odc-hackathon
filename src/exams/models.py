from django.db import models
from courses.models import Category

# Create your models here.
class Question(models.Model):
    question_id = models.AutoField(
        verbose_name='Question ID',
        primary_key=True,
        unique=True,
        auto_created=True,
    )     
    content = models.TextField(
        verbose_name='Question Content',
        blank=False,
        editable=True,
        default=None,
    )
    right_choice = models.CharField(
        verbose_name='Right Choice',
        max_length=10,
        blank=False,
        editable=True
    )
    wrong_1 = models.CharField(
        verbose_name='Wrong Choice',
        max_length=10,
        blank=False,
        editable=True
    )
    wrong_2 = models.CharField(
        verbose_name='Wrong Choice',
        max_length=10,
        blank=False,
        editable=True
    )

    def __str__(self) -> str:
        return f'Q{self.question_id}: {self.content}'


class Exam(models.Model):
    class Meta:
        verbose_name = "Exam"

    exam_id = models.AutoField(
        verbose_name='Exam ID',
        primary_key=True,
        unique=True,
        auto_created=True,
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name='Categories',
        blank=False,
        editable=True,
    )
    questions = models.ManyToManyField(
        Question,
        verbose_name='Questions',
        blank=False,
        editable=True,
    )
    def __str__(self) -> str:
        return f'Exam: {self.exam_id}'
