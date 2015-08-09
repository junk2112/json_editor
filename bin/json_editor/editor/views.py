#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.core.servers.basehttp import FileWrapper
# import django.core.files
import json


def home(request):
	args = {}
	args.update(csrf(request))

	# json_path = "/Users/andrew/git/json_editor/multipliers.json"
	json_path = "/home/transfer/multipliers.json"
	json_file = open(json_path, "r")
	jdict = json.loads(json_file.read())
	json_file.close()

	russian_names = {
		"vechevaya": 	"Вещевая",
		"dixi": 		"Дикси",
		"nahabino": 	"Нахабино",
		"taganka": 		"Таганка",
		"himki": 		"Химки",
		"trehgorka": 	"Трехгорка",
		"ryazanka": 	"Рязанка",
		"topolek": 		"Тополек",
		"test": 		"Вещевая",
		"lublino": 		"Люблино"
	}

	points = []
	for item in jdict:
		points.append(
			{
				"penalty": jdict[item]["penalty"],
				"penalty_input_name": "penalty_" + item,
				"penalty_usd": jdict[item]["penalty_usd"],
				"penalty_usd_input_name": "penalty_usd_" + item,
				"max": jdict[item]["max"],
				"max_input_name": "max_" + item,
				"russian_name": russian_names[item],
				"name":item
			})
		
	if request.method == 'POST':
		post_data = {}
		for p in points:
			post_data[p["name"]] = {}
			post_data[p["name"]]["penalty"] = 		float(request.POST.get(p["penalty_input_name"], 0))
			post_data[p["name"]]["penalty_usd"] = 	float(request.POST.get(p["penalty_usd_input_name"], 0))
			post_data[p["name"]]["max"] = 			float(request.POST.get(p["max_input_name"], 0))

		for item in jdict:
			jdict[item]["penalty"] = post_data[item]["penalty"]
			jdict[item]["penalty_usd"] = post_data[item]["penalty_usd"]
			jdict[item]["max"] = post_data[item]["max"]
		
		json_file = open(json_path, "w")
		json_file.write(str(jdict).replace("u\'", "\'").replace("\'", "\""))
		json_file.close()

		points = []
		for item in jdict:
			points.append(
				{
					"penalty": jdict[item]["penalty"],
					"penalty_input_name": "penalty_" + item,
					"penalty_usd": jdict[item]["penalty_usd"],
					"penalty_usd_input_name": "penalty_usd_" + item,
					"max": jdict[item]["max"],
					"max_input_name": "max_" + item,
					"russian_name": russian_names[item],
					"name":item
				})

	args["data"] = points
	
	return render_to_response('main.html', args)
