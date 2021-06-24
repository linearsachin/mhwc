from django.contrib import admin
from .models import (
    # Question,
    # Reply,
    PublicQuestion,
    PublicReply,
    BlogLink,
    Blog,
    RepliesReply,
    MoodCheck,
    MoodQ,
)
from .views import send_mail
# Register your models here.
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('question_text','is_approved','n_of_replies','time')
    list_filter = ['is_approved','n_of_replies','time']
    actions = ['approve_questions', ]
    def approve_questions(self,request,queryset):
        queryset.update(is_approved=True)
        slugs=[]
        for question in queryset:
            slugs.append(question.slug)
        send_mail('email.csv',slugs,False)

class ReplyAdmin(admin.ModelAdmin):
    list_display = ('question','time','if_prof')
    list_filter = ['question','time','if_prof']

def listToString(s):  
    str1 =  "" 
    for ele in s:  
        str1 +=( ele + "\n")  
    return str1  


class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title','author','date')
    list_filter = ['title','date']
    actions = ['add_to_bloglinks', ]
    def add_to_bloglinks(self,request,queryset):
        for blog in queryset:
            BlogLink.objects.create(
                title = blog.title,
                short_desc = blog.text[:200],
                url = "https://peer-space.herokuapp.com/blog/"+blog.slug,
                author = blog.author,
                website_name = "PeerSpace",
                time = blog.date,
            )



# admin.site.register(Question)
# admin.site.register(Reply)
admin.site.register(PublicQuestion,QuestionsAdmin)
admin.site.register(PublicReply,ReplyAdmin)
admin.site.register(BlogLink)
admin.site.register(RepliesReply)

admin.site.register(Blog,BlogsAdmin)
admin.site.register(MoodCheck)
admin.site.register(MoodQ)

