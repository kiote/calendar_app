from django.contrib import admin
from .models import EventTemplate


@admin.register(EventTemplate)
class EventTemplateAdmin(admin.ModelAdmin):
    list_display = ('summary', 'link_to_event', 'location', 'description',
                    'time_start', 'time_end')

    readonly_fields = ('event_data_json', )
