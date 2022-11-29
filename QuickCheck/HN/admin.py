from django.contrib import admin

# Register your models here.
from .models import *


# @admin.register(BaseModel)
# class BaseAdmin(admin.ModelAdmin):
#     list_display = ('by', 'type', 'text', 'url', 'title', 'parts')
#     search_fields = ('title', 'text')
#     date_hierarchy = 'time'
#     ordering = ('type', 'by')


admin.site.register(JobModel)

admin.site.register(StoryModel)

admin.site.register(CommentModel)

admin.site.register(PolloptModel)

admin.site.register(PollModel)

admin.site.register(BaseModel)
