from django.db import models

NULLABLE = {"blank": True, "null": True}


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    avatar = models.ImageField(upload_to="students/", verbose_name="Аватар", **NULLABLE)

    email = models.CharField(max_length=150, verbose_name='email', unique=True, null=True, blank=True)

    is_activ = models.BooleanField(default=True, verbose_name="учится")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "студент"
        verbose_name_plural = "студенты"
        ordering = ("last_name",)


class Subject(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
