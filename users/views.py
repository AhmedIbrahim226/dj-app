from django.shortcuts import render
from django.http import HttpResponse
from decouple import config
from utils.db import db
import redis
from .models import *
import os


def home_view(request):
	rd = redis.Redis(
		host=config('REDIS_HOST', default='redis'),
		port=6379,
		db=0
	)

	rd.set('cache_key', 'cache_value', 5)
	cached_key = rd.get('cache_key')
	print(cached_key)
	print(config('KEY'))
	print(config('KEY1'))
	print(config('KEY2'))
	categories = db(collection='category').get_collection.find()
	print(f"\nFrom MONGO DB ==> \n {list(categories)}\n")

	print(f"\nFrom POSTGRES DB ==> \n {Course.objects.all()}\n")

	print("Traffic from container", os.uname().nodename)
	return render(request, 'users/home.html', {})


def profile_view(request):
	return HttpResponse("<h1>Ahmed</h1><h2>Ibrahim</h2><h3>Hemid2</h3>")
	return HttpResponse("<h1>Ahmed</h1><h2>Ibrahim</h2><h3>Hemid</h3>")


