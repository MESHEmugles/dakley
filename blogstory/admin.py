from django.contrib import admin

from  embed_video.admin  import  AdminVideoMixin
from . models import *
from . address import *

# Register your models here.

class TutorialAdmin(AdminVideoMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    pass

admin.site.register(Tutorial, TutorialAdmin)

class CategoryAdmin(AdminVideoMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

admin.site.register([TutorialNumber, TutorialComment, Address])



