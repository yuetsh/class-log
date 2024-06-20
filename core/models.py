import datetime

from django.db import models


def current_year():
    return datetime.date.today().year


def year_choices():
    cur = current_year()
    return [(r, r) for r in range(cur - 1, cur + 2)]


class Semester(models.TextChoices):
    FALL = "FA", "秋季"
    SPRING = "SP", "春季"


class ClassCategory(models.TextChoices):
    ZhongBen = "ZB", "中本班"
    ShiYan = "SY", "实验班"
    ZhongZhi = "ZZ", "中职班"
    PuTong = "PT", "普通班"


class Course(models.Model):
    name = models.CharField(max_length=20, default="Python", verbose_name="课程名称")
    year = models.PositiveIntegerField(
        choices=year_choices,
        default=current_year,
        verbose_name="年份",
    )
    semester = models.CharField(
        max_length=2,
        choices=Semester.choices,
        default=Semester.FALL,
        verbose_name="学期",
    )

    class Meta:
        verbose_name_plural = "课程"
        verbose_name = "课程"
        ordering = ["year", "semester"]

    def __str__(self):
        return f"{self.year} {self.name} {self.semester}"


class Classname(models.Model):
    name = models.CharField(max_length=20, verbose_name="班级名称")
    head_teacher = models.CharField(max_length=20, verbose_name="班主任")
    category = models.CharField(
        max_length=2,
        choices=ClassCategory.choices,
        default=ClassCategory.ZhongZhi,
        verbose_name="班级类型",
    )

    class Meta:
        verbose_name = "班级"
        verbose_name_plural = "班级"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=10, db_index=True, verbose_name="姓名")
    classname = models.ForeignKey(
        Classname,
        on_delete=models.CASCADE,
        verbose_name="班级",
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    is_active = models.BooleanField(default=True, verbose_name="是否激活")

    class Meta:
        verbose_name_plural = "学生"
        verbose_name = "学生"
        ordering = ["classname__name", "name"]

    def __str__(self) -> str:
        return f"{self.classname} {self.name}"


class Reason(models.Model):
    name = models.CharField(max_length=100, verbose_name="加/减分的原因")
    is_add = models.BooleanField(default=True, verbose_name="是否是加分")
    score = models.PositiveSmallIntegerField(default=1, verbose_name="分值")

    class Meta:
        verbose_name_plural = "原因"
        verbose_name = "原因"

    def __str__(self):
        return f"{self.name}{"加" if self.is_add else "减"}{self.score}分"


class Log(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="学生")
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE, verbose_name="原因")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "记录"
        verbose_name = "记录"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.student.classname} {self.student.name} {self.reason.name}"
