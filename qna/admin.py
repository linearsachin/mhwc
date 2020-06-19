from django.contrib import admin
from .models import (
    Question,
    Reply,
    PublicQuestion,
    PublicReply,
)
# Register your models here.

admin.site.register(Question)
admin.site.register(Reply)
admin.site.register(PublicQuestion)
admin.site.register(PublicReply)
