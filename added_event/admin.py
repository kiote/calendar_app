from django.contrib import admin
from .models import AddedEvent


@admin.register(AddedEvent)
class EventTemplateAdmin(admin.ModelAdmin):
    exclude = ('summary', 'time_start', 'time_end', 'credentials')

    readonly_fields = ('checked', 'time_start_changed_to',
                       'created_at', 'updated_at', 'guser',
                       'event', 'changed', 'google_event_id')
