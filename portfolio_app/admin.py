from django.contrib import admin

from portfolio_app.models import Comment, Post

admin.site.register(Post)
admin.site.register(Comment)