from uuid import UUID

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.views.generic import TemplateView, View
from invite.models import Weddingevent, Party, Guest
from django.shortcuts import get_object_or_404
from django.db.models import Q

def validate_uuid4(uuid_string):

    try:
        val = UUID(uuid_string, version=4)
    except ValueError:
        # If it's a value error, then the string
        # is not a valid hex code for a UUID.
        return False

    return True

class HomepageView(TemplateView):
    model = Weddingevent
    template_name = 'weddingchooser.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weddings'] = [(obj.slug, obj.person1, obj.person2) for obj in Weddingevent.objects.all()]
        return context


class WeddingView(View):
    model = Weddingevent

    def get(self, request, *args, **kwargs):
        weddingobj =  get_object_or_404(Weddingevent, slug=kwargs['wed_slug'])
        templatename = weddingobj.template_name
        return render(request, templatename+"/index.html", {'wedding': weddingobj})


class InviteView(View):
    model = Weddingevent

    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        if code is None:
            raise Http404('Invalid Code')

        if validate_uuid4(code):
            try:
                partyobj = Party.objects.get(invite_code_long=code)
            except Party.DoesNotExist:
                raise Http404("Invalid code - Try to type again?")

        else:
            try:
                partyobj = Party.objects.get(invite_code_short=code)
            except Party.DoesNotExist:
                raise Http404("Invalid code - Try to type again?")

        weddingobj = get_object_or_404(Weddingevent, slug=kwargs['wed_slug'])
        templatename = weddingobj.template_name

        if partyobj is None:
            raise Http404('Invalid code - Try to type again?')
        return render(request, templatename + "/invite.html", {'wedding': weddingobj, 'party': partyobj})

    def post(self, request, *args, **kwargs):
        code = request.GET.get('code')
        if code is None:
            raise Http404('Invalid Code')

        if validate_uuid4(code):
            try:
                partyobj = Party.objects.get(invite_code_long=code)
            except Party.DoesNotExist:
                raise Http404("Invalid code - Try to type again?")

        else:
            try:
                partyobj = Party.objects.get(invite_code_short=code)
            except Party.DoesNotExist:
                raise Http404("Invalid code - Try to type again?")

        request.POST.get("people[]")
        request.POST.get("transpeople")
        request.POST.get("email")
        request.POST.get("freetext")
        request.POST.get("code")

        weddingobj = get_object_or_404(Weddingevent, slug=kwargs['wed_slug'])
        templatename = weddingobj.template_name

        if partyobj is None:
            raise Http404('Invalid code - Try to type again?')

        #put save code here
        return render(request, templatename + "/invite.html", {'wedding': weddingobj, 'party': partyobj, 'RSVP': request.POST})


