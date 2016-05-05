from django.contrib import admin
from .models import Post, Post_user, Comment, Comment_user, Hospital, Color

admin.site.register(Post)
admin.site.register(Post_user)
admin.site.register(Comment)
admin.site.register(Comment_user)
admin.site.register(Hospital)
admin.site.register(Color)