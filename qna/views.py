from django.shortcuts import render,redirect
from django.utils.text import slugify
from django.views.generic import View 
from django.http import HttpResponse
from .models import (
    Question,
    Reply,
)
import random
from .forms import QuestionSubmission,ReplySubmission
# Create your views here.

class HomeView(View):
    def get(self, request):
        questions = Question.objects.all()
        replies = Reply.objects.all()
        qForm = QuestionSubmission()
        rForm = ReplySubmission()
        context = {
            'questions':questions,
            'reply': replies,
            'qForm':qForm,
            'rForm':rForm,
        }
        return render(request ,'qna/home.html',context)



    def post(self,request):
        form = QuestionSubmission(self.request.POST or None)
        rform = ReplySubmission(self.request.POST or None)
        try:
            if form.is_valid():
                ques = form.cleaned_data.get('text')
                trun = random.randint(20, 30)
                slug_  =slugify(ques[:trun])
                Question.objects.create(
                    question_text = ques,
                    slug = slug_,
                )
            return redirect("question",slug=slug_)
        except:
            return redirect("home")
       


class QuestionView(View):
    def get(self, request,slug, *args, **kwargs):
        question = Question.objects.get(slug = slug)
        replies = Reply.objects.filter(question=question)
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
                print(question.slug)
                # slug_  =slugify(reply)
                Reply.objects.create(
                    reply_text = reply,
                    question  = question,
                    # slug = slug_,
                )
            return redirect("question",slug=question.slug)
        except:
            return redirect("home")