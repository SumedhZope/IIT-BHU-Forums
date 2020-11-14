from django.contrib import admin
from .models import Post,Group,Comments,like,Role,Role_choices

admin.site.register(like)
admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Comments)
admin.site.register(Role)
admin.site.register(Role_choices)