from django.contrib import admin
from .models import Advice

@admin.register(Advice)
class AdviceAdmin(admin.ModelAdmin):
    list_display = ('profile__user__username', 'content', 'created')