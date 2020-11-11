from django.contrib import admin
from .models import Post,Group,Comments,like

admin.site.register(like)
admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Comments)