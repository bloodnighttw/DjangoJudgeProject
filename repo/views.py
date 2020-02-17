from django.shortcuts import render, redirect
from django.http import HttpResponse
from repo.repos import repos 
# Create your views here.


def questionRepo(request,id):
	for repo in repos:
		if repo.get('id') == id:
			return render(request , 'questionRepo/Repo.html',{'repo' : repo })
	return redirect('index/')

def question(request,id,title):
	for repo in repos:
		if repo.get('id') == id:
			for q in  repo.get('questions'):
				if q.get('title') == title :
					return render(request , 'questionRepo/question.html',{'question':q})
	return redirect('/index')

