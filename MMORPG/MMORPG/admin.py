from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'post', 'created_on', 'author')
    list_filter = ('active','created_on')
    search_fields = ('post', 'text', 'author')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)