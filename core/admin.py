from django.contrib import admin
from django.core.paginator import Paginator

from .models import Log, Reason
from .models import Classname, Course, Student

admin.site.site_header = "徐越的课堂记录管理"
admin.site.site_index = "徐越的课堂记录管理"
admin.site.site_title = "徐越的课堂记录管理"


class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "classname", "course"]
    search_fields = ["name", "classname__name", "pinyin", "pinyin_shortcut"]
    list_filter = ["classname__name"]
    list_per_page = 20
    paginator = Paginator


admin.site.register(Student, StudentAdmin)
admin.site.register(Reason)
admin.site.register(Course)


class ClassnameAdmin(admin.ModelAdmin):
    list_display = ["name", "head_teacher"]


admin.site.register(Classname, ClassnameAdmin)


class LogAdmin(admin.ModelAdmin):
    list_display = ["__str__", "created_at"]
    search_fields = [
        "student__name",
        "student__classname__name",
        "student__pinyin",
        "student__pinyin_shortcut",
    ]
    list_filter = ["student__classname__name"]
    list_per_page = 20
    paginator = Paginator
    autocomplete_fields = ["student"]


admin.site.register(Log, LogAdmin)
