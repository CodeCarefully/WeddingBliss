from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('default/index.html')
    context = {
        'latest_question_list': '',
    }
    return HttpResponse(template.render(context, request))