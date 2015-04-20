__author__ = 'Administrator'
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('index.html', RequestContext(request, {}))


def genres(request):
    return render_to_response('genres.html', RequestContext(request, {}))


def listen(request):
    return render_to_response('listen.html', RequestContext(request, {}))


def not_found(request):
    return render_to_response('404.html', RequestContext(request, {}))


