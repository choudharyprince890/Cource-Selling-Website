from django.contrib import admin
from .models.cource import Cource,Hashtag,Learning,Prerequisite
from .models.videos import Videos
from .models.payment import Payment
from .models.user_cource import UserCource
# Register your models here.


class HashtagAdmin(admin.TabularInline):
    model = Hashtag

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class VideoAdmin(admin.TabularInline):
    model = Videos

class CourceAdmin(admin.ModelAdmin):
    inlines = [HashtagAdmin, LearningAdmin, PrerequisiteAdmin, VideoAdmin]

admin.site.register(Cource, CourceAdmin)
admin.site.register(Videos)
admin.site.register(Payment)
admin.site.register(UserCource)
