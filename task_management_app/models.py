from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateTimeField()
    completed=models.BooleanField(default=False)
    description=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

