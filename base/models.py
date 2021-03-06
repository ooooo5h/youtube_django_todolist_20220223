from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# DB에 저장하기 위해 클래스를 정의해야함
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):   # 자기자신을 어떻게 표현할건지? title로 표현하겠다.
        return self.title
    
    class Meta:
        ordering = ['complete']