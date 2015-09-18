from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext
from django.contrib import messages
from django.shortcuts import redirect

from .models import EventTemplate

class ListView(TemplateView):
    def get(self, request):
        events = EventTemplate.objects.all()
        context = RequestContext(request, {'events': events})
        return render(request, 'event_template/index.html', context)

class SingleView(TemplateView):
    def get(self, request, event_id):
        messages.success(request, 'Event has been added to your calendar.')
        return redirect('list')