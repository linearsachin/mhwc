from django.shortcuts import render,redirect
from django.utils.text import slugify
from django.views.generic import View ,ListView
from django.http import HttpResponse
from .models import (
    Forum,
    Question,
    Reply,
)
import csv
import django.utils.timezone as tz
from .filters import QuestionFilter
import random
import string
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import QuestionSubmission,ReplySubmission
# Create your views here.
def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


class ForumAuthView(View):
    def get(self, request,forum_id, *args, **kwargs):
        forum = User.objects.get(username=forum_id)
        context ={
            "forumid":forum.username,
            "forumcode":forum.password,
        }
        return render(request ,'qna/forum-auth.html',context)

    def post(self, request, *args, **kwargs):
        forum_id = self.request.POST.get('forumid')
        forum_code = self.request.POST.get('forumcode')
        forum = authenticate(username = forum_id,password=forum_code)
        if forum is not None:
            return redirect('forum',forum_id)
        else:
            return redirect('forum-auth',forum_id)

def generateForum(request):
    forumId = randomString(10)
    forumCode = random.randint(100000,999999)
    User.objects.create_user(
        username = forumId,
        password  =forumCode,
    )
    messages.success(request, f"Your forum Id is: {forumId}")
    messages.success(request, f"Remeber This Code for further login: {forumCode}")
    return redirect("forum-auth")


class ForumView(View):
    def get(self, request,forum_id, *args, **kwargs):
        forum = User.objects.get(username=forum_id)
        print(request.user)
        context ={
            "forumid":forum.username,
            # "forumcode":forum.forum_code,
        }

        return render(request ,'qna/forum.html',context)

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')

class HomeView(View):
    def get(self, request):
        questions = Question.objects.all().order_by('-time')
        question_filter = QuestionFilter(request.GET, queryset=questions)
        qForm = QuestionSubmission()
        rForm = ReplySubmission()
        qoute = get_qoute()
        print(qoute)
        context = {
            'questions':question_filter,
            'qForm':qForm,
            'rForm':rForm,
            'qoute':qoute
            
        }
        return render(request ,'qna/home.html',context)

def get_qoute():
    with open('qoutes.csv',encoding='UTF-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if row[1]==tz.now():
                return row[0]
            else:
                return "a qoute"
        
class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'qna/about.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
    def post(self,request):
        form = QuestionSubmission(self.request.POST or None)
        try:
            if form.is_valid():
                ques = form.cleaned_data.get('text')
                trun = random.randint(20, 30)
                slug_  =slugify(ques[:trun])
                time = tz.now()
                Question.objects.create(
                    question_text = ques,
                    slug = slug_,
                    time= time,
                )
            return redirect("question",slug=slug_)
        except:
            return redirect("home")
       


class QuestionView(View):
    def get(self, request,slug, *args, **kwargs):
        question = Question.objects.get(slug = slug)
        replies = Reply.objects.filter(question=question).order_by('-time')
        rForm = ReplySubmission()
        context = {
            'question':question,
            'replies': replies,
            'rForm':rForm,
        }
        return render(request ,'qna/question.html',context)
       

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


# class SearchView(ListView):
#     model = Question
#     template_name = 'search.html'
#     context_object_name = 'all_search_results'

#     def get_queryset(self):
#        result = super(SearchView, self).get_queryset()
#        query = self.request.GET.get('search')
#        print(query)
#        if query:
#           postresult = Question.objects.filter(title__contains=query)
#           print(postresult)
#           result = postresult
#        else:
#            print('none')
#            result = None
#        return result


def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'search/user_list.html', {'filter': user_filter})