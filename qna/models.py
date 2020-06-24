from django.db import models
import django.utils.timezone as tz
from django.contrib.auth.models import User
from django.utils.text import slugify

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
    is_approved = models.BooleanField(default=False)

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
    if_prof = models.CharField(max_length = 50,blank=True, null=True)

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


class BlogLink(models.Model):
    title = models.CharField(max_length=200)
    short_desc = models.TextField()
    url = models.URLField()
    author = models.CharField(max_length=100, blank=True, null=True)
    website_name = models.CharField(max_length=200)
    time = models.DateTimeField()

    def __str__(self):
        return str(self.title)
    def get_date(self):
        return "{month} {day}, {year}".format(month=self.time.strftime('%B'),day=self.time.day,year=self.time.year)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=100,)
    date = models.DateTimeField()
    slug=models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title)
    def get_date(self):
        return "{month} {day}, {year}".format(month=self.date.strftime('%B'),day=self.date.day,year=self.date.year)
