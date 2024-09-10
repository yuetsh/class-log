from core.models import Classname, Course, Student


def run():
    with open("scripts/students.txt", encoding="utf-8") as f:
        for line in f.read().splitlines():
            name = line.split()[1]
            classname = Classname.objects.get(name=line.split()[5] + "班")
            course = Course.objects.first()
            Student.objects.create(name=name, classname=classname, course=course)