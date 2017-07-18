from django.contrib import admin
from myapp.models import *

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Topic)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'in_stock', 'numpages')

class CourseAdmin(admin.ModelAdmin) :
    list_display = ('title', 'textBook', 'course_no')

class StudentAdmin(admin.ModelAdmin) :
    list_display = ('first_name', 'last_name')