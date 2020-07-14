from django.contrib import admin
from .models import *

@admin.register(Question)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('question_text','date','posted_by')

@admin.register(Answer)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('date','answer_text','answered_by')

@admin.register(Upvote)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('upvoted_by','date')