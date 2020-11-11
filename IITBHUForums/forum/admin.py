from django.contrib import admin
from .models import Post,Group,Comments

admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Comments)