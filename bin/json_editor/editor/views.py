from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.core.servers.basehttp import FileWrapper
# import django.core.files
import json


def home(request):
	args = {}
	args.update(csrf(request))

	if request.method == 'POST':
		json_data = request.FILES['uploaded_file'].read()
		json_dict = json.loads(json_data)
		args['json_type'] = json_dict['type']
		args['json_content'] = json_dict['content']
		tags = ''
		for tag in json_dict['tags']:
			tags = tags + tag + ' '
		args['json_tags'] = tags
		args['original_data'] = json_data
		return render_to_response('editor.html', args)

	if request.method == 'GET':
		form_type = request.GET.get('form_type', '')
		form_tags = request.GET.get('form_tags', '')
		form_content = request.GET.get('form_content', '')

		tags = form_tags.split()
		json_dict = {'type':form_type, 'tags':tags, 'content':form_content}
		data = json.dumps(json_dict)
		args['result_data'] = data

	return render_to_response('main.html', args)
