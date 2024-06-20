from django.contrib import admin
from django.core.paginator import Paginator

from .models import Log, Reason
from .models import Classname, Course, Student

admin.site.site_header = "徐越的课堂记录管理"
admin.site.site_index = "徐越的课堂记录管理"
admin.site.site_title = "徐越的课堂记录管理"


class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "classname"]
    search_fields = ["name", "classname__name"]
    list_filter = ["classname__name", "course"]
    list_per_page = 20
    paginator = Paginator


admin.site.register(Student, StudentAdmin)
admin.site.register(Reason)
admin.site.register(Course)
admin.site.register(Classname, list_display=["name", "head_teacher"])


class LogAdmin(admin.ModelAdmin):
    search_fields = ["student__name", "student__classname__name"]
    list_filter = ["student__classname__name"]
    list_per_page = 20
    paginator = Paginator
    autocomplete_fields = ["student"]


admin.site.register(Log, LogAdmin)
