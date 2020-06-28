from django import forms
from django.conf import settings
import datetime
from captcha.fields import ReCaptchaField
from captcha import widgets 


class QuestionSubmission(forms.Form):
    text = forms.CharField(max_length=1000,label =False, required=True,widget=forms.Textarea(attrs={
        'class':"form-control",
        'type':"text",
        'id':"question", 
        'name':"question" ,
        'placeholder':"Ask Anything" ,
        'rows':2,
        'cols':10,
        'style':"width:80%; text-align-last: center;margin:auto; "
    }))
    captcha = ReCaptchaField(label =False,widget=widgets.ReCaptchaV2Checkbox(
        attrs={
            'data-theme': 'dark',
            'data-size': '',
            'style':"float:inherit;width:80%;margin:auto;"
        }))


class ReplySubmission(forms.Form):
    text = forms.CharField(max_length=1000,label = False , required=True,widget=forms.Textarea(attrs={
        'class':"form-control",
        'type':"text",
        'id':"reply", 
        'name':"reply" ,
        'placeholder':"Answer" ,
        'rows':2,
        'cols':10,
        'style':"width:80%; text-align-last: center;margin:auto; "
    }))
    hidden = forms.HiddenInput()
    captcha = ReCaptchaField(label =False,widget=widgets.ReCaptchaV2Checkbox(
        attrs={
            'data-theme': 'dark',
            'data-size': '',
            'style':"float:inherit;width:80%;margin:auto;"
    }))
