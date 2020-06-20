from django.db import models
import django.utils.timezone as tz
from django.contrib.auth.models import User

class Question(models.Model):
    forum = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    question_text = models.TextField()
    slug = models.SlugField(max_length=50)
    time = models.DateTimeField()
    def __str__(self):
        return str(self.question_text)[:20]+"..."
    def get_time_diff(self):
        if self.time:
            now = tz.now()
            timediff = now - self.time
            hours =  round(timediff.total_seconds()//3600)
            if hours < 1:
                return "now"
            elif hours < 2 and hours >= 1:
                return "1 hour ago"
            elif hours >= 2 and hours < 24:
                return "{hours} hours ago".format(hours=hours)
            elif hours >= 24 and hours < 48 :
                return "{days} day ago".format(days=round(hours/24))
            elif hours >=48:
                return "{days} days ago".format(days=round(hours/24))
            else:
                return ""

class PublicQuestion(models.Model):
    question_text = models.TextField()
    slug = models.SlugField(max_length=50)
    time = models.DateTimeField()
    def __str__(self):
        return str(self.question_text)[:20]+"..."
    def get_time_diff(self):
        if self.time:
            now = tz.now()
            timediff = now - self.time
            hours =  round(timediff.total_seconds()//3600)
            if hours < 1:
                return "now"
            elif hours < 2 and hours >= 1:
                return "1 hour ago"
            elif hours >= 2 and hours < 24:
                return "{hours} hours ago".format(hours=hours)
            elif hours >= 24 and hours < 48 :
                return "{days} day ago".format(days=round(hours/24))
            elif hours >=48:
                return "{days} days ago".format(days=round(hours/24))
            else:
                return ""
            

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
            hours =  round(timediff.total_seconds()//3600)
            if hours < 1:
                return "now"
            elif hours < 2 and hours >= 1:
                return "1 hour ago"
            elif hours >= 2 and hours < 24:
                return "{hours} hours ago".format(hours=hours)
            elif hours >= 24 and hours < 48 :
                return "{days} day ago".format(days=round(hours/24))
            elif hours >=48:
                return "{days} days ago".format(days=round(hours/24))
            else:
                return ""

class PublicReply(models.Model):
    question = models.ForeignKey(PublicQuestion,on_delete=models.CASCADE,blank=True, null=True)
    reply_text = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return str(self.reply_text)[:20]+"..."
    def get_time_diff(self):
        if self.time:
            now = tz.now()
            timediff = now - self.time
            hours =  round(timediff.total_seconds()//3600)
            if hours < 1:
                return "now"
            elif hours < 2 and hours >= 1:
                return "1 hour ago"
            elif hours >= 2 and hours < 24:
                return "{hours} hours ago".format(hours=hours)
            elif hours >= 24 and hours < 48 :
                return "{days} day ago".format(days=round(hours/24))
            elif hours >=48:
                return "{days} days ago".format(days=round(hours/24))
            else:
                return ""