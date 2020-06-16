from django import forms
from django.conf import settings
import datetime

class QuestionSubmission(forms.Form):
    text = forms.CharField(max_length=240,label = "Ask you question:", required=True,widget=forms.Textarea(attrs={
        'class':"form-control",
        'type':"text",
        'id':"question", 
        'name':"question" ,
        'placeholder':"Ask Anything" ,
        'rows':2,
        'cols':6,
        'style':"width:70%; text-align-last: center;margin:auto; "
    }))


class ReplySubmission(forms.Form):
    text = forms.CharField(max_length=240,label = False , required=True,widget=forms.Textarea(attrs={
        'class':"form-control",
        'type':"text",
        'id':"reply", 
        'name':"reply" ,
        'placeholder':"Answer" ,
        'rows':2,
        'cols':6,
        'style':"width:70%; text-align-last: center;margin:auto; "
    }))
    hidden = forms.HiddenInput()