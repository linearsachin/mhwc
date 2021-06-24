from django import forms
from django.conf import settings
import datetime
from captcha.fields import ReCaptchaField
from captcha import widgets 


class QuestionSubmission(forms.Form):
    text = forms.CharField(max_length=1000,label =False, required=True,widget=forms.Textarea(attrs={
        'class':"materialize-textarea black-text",
        'type':"text",
        'id':"question", 
        'name':"question" ,
        'rows':2,
        'cols':10,
        'style':"width:80%; text-align-last: center;margin:auto;background-color:#cedbdb "
    }))
    captcha = ReCaptchaField(label =False,widget=widgets.ReCaptchaV2Checkbox(
        attrs={
            'data-theme': 'light',
            'data-size': '',
            'style':"float:inherit;width:80%;margin:auto;display:none",
            'class':"small",
            'id':"captcha"
        }))


class ReplySubmission(forms.Form):
    text = forms.CharField(max_length=1000,label = False , required=True,widget=forms.Textarea(attrs={
        'class':"materialize-textarea white-text",
        'type':"text",
        'id':"reply", 
        'name':"reply" ,
        'rows':2,
        'cols':10,
        'style':"text-align-last: center;margin:auto;color:black "
    }))
    # hidden = forms.CharField(widget=forms.TextInput(attrs={
    #     'id':"decider", 
    #     'name':"decider" ,
    #     'type':"hidden",
    # }))
    captcha = ReCaptchaField(label =False,widget=widgets.ReCaptchaV2Checkbox(
        attrs={
            'data-theme': 'dark',
            'data-size': 'compact',
            'style':"float:inherit;width:80%;margin:auto;"
    }))
