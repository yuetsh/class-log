from django.contrib.auth.models import User

from core.models import Classname, Course, Log, Reason, Student


def run():
    User.objects.create_superuser(
        email="test@example.com",
        username="test",
        password="123456",
    )

    Reason.objects.create(name="积极回答问题")
    Reason.objects.create(name="认真完成作业")
    Reason.objects.create(name="上课违规上网", is_add=False)
    Reason.objects.create(name="上课睡觉", is_add=False)
    Reason.objects.create(name="上课随意讲话", is_add=False)

    Course.objects.create(name="Python")

    with open("scripts/classname.txt", encoding="utf-8") as f:
        for line in f.read().splitlines():
            name = line.split()[0]
            head = line.split()[1]
            Classname.objects.create(name=name, head_teacher=head)

    with open("scripts/students.txt", encoding="utf-8") as f:
        for line in f.read().splitlines():
            name = line.split()[1]
            classname = Classname.objects.get(name=line.split()[3] + "班")
            course = Course.objects.first()
            Student.objects.create(name=name, classname=classname, course=course)

    for _ in range(1000):
        stu = Student.objects.all().order_by("?")[:1][0]
        r = Reason.objects.all().order_by("?")[:1][0]
        log = Log(student=stu, reason=r)
        log.save()
