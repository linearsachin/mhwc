from django.shortcuts import render,redirect
from django.utils.text import slugify
from django.views.generic import View ,ListView
from django.http import HttpResponse
from .models import (
    # Question,
    # Reply,
    PublicQuestion,
    PublicReply,
    RepliesReply,
    Blog,
    BlogLink,
)
from django.db.models import F

import os  
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

import smtplib
import csv
import django.utils.timezone as tz
from .filters import ( 
    # QuestionFilter,
    PublicQuestionFilter
)
import datetime 
import random
import string
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import QuestionSubmission,ReplySubmission

from ratelimit.mixins import  RatelimitMixin
from ratelimit.decorators import ratelimit




def randomString(stringLength=15):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


# class ForumAuthView(View):
#     def get(self, request,forum_id, *args, **kwargs):
#         forum = User.objects.get(username=forum_id)
#         context ={
#             "forumid":forum.username,
#             "forumcode":forum.password,
#         }
#         return render(request ,'qna/forum-auth.html',context)

#     def post(self, request, *args, **kwargs):
#         forum_id = self.request.POST.get('forumid')
#         forum_code = self.request.POST.get('forumcode')
#         forum = authenticate(username = forum_id,password=forum_code)
#         if forum is not None:
#             return redirect('forum',forum_id)
#         else:
#             messages.warning(request,f'Wrong Forum Code for {forum_id}')
#             return redirect('forum-auth',forum_id)



# def generateForum(request):
#     if not request.user.is_authenticated:
#         forumId = randomString(10)
#         forumCode = str(random.randint(100000,99999999)) + randomString(4)
#         User.objects.create_user(
#             username = forumId,
#             password  =forumCode,
#         )
#         messages.success(request, f"Your forum Id is: {forumId}")
#         messages.success(request, f"Remeber This Code for further login: {forumCode}")
#         return redirect("forum-auth")
#     else:
#         messages.warning(request,'You are already in a forum')
#         return redirect('home')



# class ForumView(View):
#     def get(self, request, *args, **kwargs):
#         try:
#             forum = User.objects.get(username=request.user.username)
#             questions = Question.objects.filter(forum=forum).order_by('-time')
#             question_filter = QuestionFilter(request.GET, queryset=questions)
#             qForm = QuestionSubmission()
#             qoute = get_qoute()
#             context = {
#                 'questions':question_filter,
#                 'qForm':qForm,
#                 'qoute':qoute,
#                 "forumid":forum.username,  
#             }
#             return render(request ,'qna/forum.html',context)
#         except:
#             return render(request ,'qna/forum.html')

#     def post(self,request,*args, **kwargs):
#         form = QuestionSubmission(self.request.POST or None)
#         try:
#             if form.is_valid():
#                 forum_id =request.user.username
#                 forum = User.objects.get(username=forum_id)
#                 ques = form.cleaned_data.get('text')
#                 trun = random.randint(20, 30)
#                 slug_  =slugify(ques[:trun]+""+randomString(3))
#                 time = tz.now()
#                 Question.objects.create(
#                     forum = forum,
#                     question_text = ques,
#                     slug = slug_,
#                     time= time,
#                 )
#             return redirect("question",slug=slug_,)
#         except:
#             return redirect("home")


def get_qoute():
    with open('qoutes.csv',encoding='UTF-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # try:
        for row in csv_reader:
            if row[1]==str(datetime.date.today()):
                return row[0]
        # except:
        #     return "“Shame dies when stories are told in safe places.” ― Ann Voskamp"
        
class HomeView(View):
    def get(self, request):
        questions = PublicQuestion.objects.filter(is_approved=True).order_by('-time')
        question_filter = PublicQuestionFilter(request.GET, queryset=questions)
        qForm = QuestionSubmission()
        qoute = get_qoute()
        if request.user.is_authenticated:
            forumid = request.user.username
        else:
            forumid=''

        context = {
            'questions':question_filter,
            'qForm':qForm,
            'qoute':qoute,
            'forumid':forumid,
            
        }
        return render(request ,'qna/home.html',context)

    def post(self,request):
        form = QuestionSubmission(self.request.POST or None)
        try:
            if form.is_valid():
                ques = form.cleaned_data.get('text')
                trun = random.randint(20, 30)
                slug_= slugify(ques[:trun]+" "+randomString(3))
                time = tz.now()
                PublicQuestion.objects.create(
                    question_text = ques,
                    slug = slug_,
                    time= time,
                )
                send_mail('email_mods.csv',[slug_],True)
            url = 'https://peer-space.herokuapp.com/public-question/'+str(slug_)
            messages.success(request,"Your question has been submitted for review, It will be approved ASAP\ncheck back at {url}".format(url=url))
            return redirect("home")
        except:
            messages.warning(request,"There was a problem adding your Question.\nPlease try again")            
            return redirect("home")

def listToString(s):  
    str1 =  "" 
    for ele in s:  
        str1 +=( ele + "\n")  
    return str1  

def send_mail(filename,question_slugs,is_to_mod=True):     
    gmail_user = os.environ['gmail_id']
    gmail_password = os.environ['gmail_pw']

    sent_from = gmail_user
    with open(filename,encoding='UTF-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            to = row
    url=[]
    for slug in question_slugs:
        url.append('https://peer-space.herokuapp.com/public-question/{question}'.format(question=slug))
    url = listToString(url)
    subject = 'Question(s) Added to Public Forum'
    if is_to_mod:
        body = "Question(s) was added to the forum.\nPlease Approve it ASAP:\n{URL}\nThank You.".format(URL = url)
    else:
        body = "Question(s) was added to the forum.\nHelp them by visiting:\n{URL}\nThank You.".format(URL = url)

    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
    except:
        print( 'Something went wrong...')



class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'qna/about.html')

class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'qna/contactus.html')



class QuestionView(View):
    def get(self, request,slug, *args, **kwargs):
        try:
            forum = User.objects.get(username = request.user.username)
            question = Question.objects.get(slug = slug,forum=forum)
            replies = Reply.objects.filter(question=question).order_by('-time')
            rForm = ReplySubmission()
            context = {
                'question':question,
                'replies': replies,
                'rForm':rForm,
            }
            return render(request ,'qna/question.html',context)
        except:
            return redirect('home')
       

    def post(self, request, *args, **kwargs):
        form = ReplySubmission(self.request.POST or None)
        try:
            if form.is_valid():
                reply = form.cleaned_data.get('text')
                qpk = self.request.POST.get('question_pk')
                question = Question.objects.get(pk = qpk)
                time = tz.now()
                Reply.objects.create(
                    reply_text = reply,
                    question  = question,
                    time=time,
                    
                )
            return redirect("question",slug=question.slug)
        except:
            return redirect("home")


class PublicQuestionView(View):
    def get(self, request,slug, *args, **kwargs):
        try:
            question = PublicQuestion.objects.get(slug = slug,is_approved=True)
            replies = PublicReply.objects.filter(question=question).order_by('-time')
            allreplies= []
            for reply in replies:
                allreplies.append((reply,(RepliesReply.objects.filter(question=reply).order_by('-time'))))

            rForm = ReplySubmission()
            context = {
                'question':question,
                'replies': replies,
                'rForm':rForm,
                'allreplies':allreplies,
            }
            return render(request ,'qna/question.html',context)
        except:
            messages.warning(request,"Error!")
            return redirect('home')
       

    def post(self, request, *args, **kwargs):
        form = ReplySubmission(self.request.POST or None)
        print(self.request.POST)
        try:
            if form.is_valid():
                reply = form.cleaned_data.get('text')
                qpk = self.request.POST.get('question_pk')
                question_id = self.request.POST.get('question_id')
                decider = self.request.POST.get('decider')
                if request.user.username == 'sachin':
                    is_prof = 'Moderator'
                elif request.user.username == 'kikstartz':
                    is_prof= 'Professional'
                else:
                    is_prof=''
                time = tz.now()
                if decider == "Reply":
                    question = PublicQuestion.objects.get(pk = qpk)
                    question.n_of_replies = F('n_of_replies') + 1
                    question.save()
                    PublicReply.objects.create(
                        reply_text = reply,
                        question  = question,
                        time=time,
                        if_prof=is_prof,
                    )
                    messages.success(request,"Your reply was added")
                    return redirect("publicquestion",slug=question.slug)
                else:
                    reply_ = PublicReply.objects.get(pk = qpk)
                    question = PublicQuestion.objects.get(pk = question_id)

                    RepliesReply.objects.create(
                        reply_text = reply,
                        question  = reply_,
                        time=time,
                        if_prof=is_prof,
                    )
                    messages.success(request,"Your reply was added")
                    return redirect("publicquestion",slug=question.slug)
        except:
            messages.warning(request,"There was a problem adding your reply")
            return redirect("home")



class BlogLinksView(ListView):
    model = BlogLink
    paginate_by = 5
    template_name = 'qna/blog_list.html'
    ordering = ['-time']


class BlogView(View):
    def get(self, request,blog_slug, *args, **kwargs):
        blog = Blog.objects.get(slug=blog_slug)
        recent_blog = Blog.objects.exclude(slug=blog_slug).order_by('-date')[:3]
        context={
            'blog':blog,
            'recent':recent_blog
        }
        return render(request,'qna/blog.html',context)




def handler404(request,exception=404):
    return render(request, 'qna/404.html', status=404)
def handler500(request,exception=404):
    return render(request, 'qna/500.html', status=500)