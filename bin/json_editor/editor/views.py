from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.core.servers.basehttp import FileWrapper
# import django.core.files
import json


def home(request):
	args = {}
	args.update(csrf(request))
	original_data = None
	result_data = None
	json_load_error = False
	json_type = ''
	json_content = ''
	tags = ''
	if request.method == 'POST':
		splitted_name = str(request.FILES['uploaded_file']).split('.')
		if splitted_name[-1].lower() != 'json':
			json_load_error = True
		else:
			original_data = request.FILES['uploaded_file'].read()
			json_dict = json.loads(original_data)

			if 'type' in json_dict.keys():
				json_type = json_dict['type']

			if 'content' in json_dict.keys():
				json_content = json_dict['content']

			if 'tags' in json_dict.keys():
				for tag in json_dict['tags']:
					tags = tags + tag + ' '
			args['json_tags'] = tags
			args['json_type'] = json_type
			args['json_content'] = json_content


		
	if request.method == 'GET':
		form_type = request.GET.get('form_type', '')
		form_tags = request.GET.get('form_tags', '')
		form_content = request.GET.get('form_content', '')

		if form_type != '' and form_tags != '' and form_content != '':
			tags = form_tags.split()
			json_dict = {'type':form_type, 'tags':tags, 'content':form_content}
			result_data = json.dumps(json_dict)

	args['original_data'] = original_data
	args['result_data'] = result_data
	args['json_load_error'] = json_load_error
	
	return render_to_response('main.html', args)
