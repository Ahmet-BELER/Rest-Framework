from django.contrib import admin
from news.models import Article,Author,Comments
# Register your models here.

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Comments) 