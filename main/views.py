# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import serializers

from .models import Questions

def index(request):
	obj = Questions.objects.all()[:20]
	serialized = serializers.serialize('json', obj)
	return render_to_response('index.html', {
		'posts': obj,
        'posts_json': serialized,
    }, context_instance=RequestContext(request))