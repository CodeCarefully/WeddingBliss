from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from invite.models import Weddingevent


class HomepageView(TemplateView):
    model = Weddingevent
    template_name = 'weddingchooser.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weddings'] = [(obj.slug, obj.person1, obj.person2) for obj in Weddingevent.objects.all()]
        return context

