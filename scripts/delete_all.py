from core.models import Student, Classname, Log


def run():
    Student.objects.all().delete()
    Classname.objects.all().delete()
    Log.objects.all().delete()
