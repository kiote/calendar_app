from django.contrib import admin
from .models import AddedEvent

@admin.register(AddedEvent)
class EventTemplateAdmin(admin.ModelAdmin):
    readonly_fields = ('summary', 'time_start', 'time_end', 'created_at', 'guser', 'event')
