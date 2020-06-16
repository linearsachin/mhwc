from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.TextField()
    slug = models.SlugField(max_length=20)
    def __str__(self):
        return str(self.question_text)[:20]+"..."

class Reply(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,blank=True, null=True)
    reply_text = models.TextField()
    

    def __str__(self):
        return str(self.reply_text)[:20]+"..."

