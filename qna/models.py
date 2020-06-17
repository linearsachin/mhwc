from django.db import models
import django.utils.timezone as tz



# Create your models here.

class Forum(models.Model):
    forum_id = models.CharField(max_length=50,unique=True)
    forum_code = models.CharField(max_length=10,)
    is_public = models.BooleanField(default=False)
    def __str__(self):
        return str(self.forum_id)






class Question(models.Model):
    question_text = models.TextField()
    slug = models.SlugField(max_length=50)
    time = models.DateTimeField()
    def __str__(self):
        return str(self.question_text)[:20]+"..."
    def get_time_diff(self):
        if self.time:
            now = tz.now()
            timediff = now - self.time
            return round(timediff.total_seconds()//3600)

class Reply(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,blank=True, null=True)
    reply_text = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return str(self.reply_text)[:20]+"..."
    def get_time_diff(self):
        if self.time:
            now = tz.now()
            timediff = now - self.time
            return int(round(timediff.total_seconds()//3600))

