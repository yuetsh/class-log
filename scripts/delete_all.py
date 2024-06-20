from core.models import Student, Classname


def run():
    Student.objects.all().delete()
    Classname.objects.all().delete()
