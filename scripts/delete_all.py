from core.models import Student, Classname, Log
from django.contrib.auth.models import User


def run():
    User.objects.all().delete()
    Student.objects.all().delete()
    Classname.objects.all().delete()
    Log.objects.all().delete()
