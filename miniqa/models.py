from django.db import models
from django.contrib.auth.models import User
import uuid

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question_text = models.TextField()
    
    date = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return(str(self.id) + str(self.date))

class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    answer_text = models.TextField()
    answered_by = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(str(self.id) + str(self.date))

class Upvote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    upvoted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(str(self.id) + str(self.date))
