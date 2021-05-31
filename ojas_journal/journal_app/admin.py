from django.contrib import admin
from journal_app.models import Post, Tag,Contact

admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Tag)
