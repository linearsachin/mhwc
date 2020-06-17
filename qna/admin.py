from django.contrib import admin
from .models import (
    Forum,
    Question,
    Reply,
)
# Register your models here.
admin.site.register(Forum)

admin.site.register(Question)
admin.site.register(Reply)