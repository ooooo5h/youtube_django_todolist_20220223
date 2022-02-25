from django.contrib import admin
from .models import Task

# ADMIN사이트에서 수정해야하는 Task를 추가하기
admin.site.register(Task)