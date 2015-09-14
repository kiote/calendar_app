from django.contrib import admin
from .models import EventTemplate

@admin.register(EventTemplate)
class EventTemplateAdmin(admin.ModelAdmin):
    readonly_fields = ('event_data_json', )
