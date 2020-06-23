from django.contrib import admin
from .models import (
    Question,
    Reply,
    PublicQuestion,
    PublicReply,
    Blog
)
from .views import send_mail
# Register your models here.
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('question_text','is_approved','time')
    list_filter = ['is_approved','time']
    actions = ['approve_questions', ]
    def approve_questions(self,request,queryset):
        queryset.update(is_approved=True)
        slugs=[]
        for question in queryset:
            slugs.append(question.slug)
        send_mail('email.csv',slugs,False)



admin.site.register(Question)
admin.site.register(Reply)
admin.site.register(PublicQuestion,QuestionsAdmin)
admin.site.register(PublicReply)
admin.site.register(Blog)

