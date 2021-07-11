from django.contrib import admin
from insta.models import Post, Tag, Follow, Stream

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Follow)
admin.site.register(Stream)