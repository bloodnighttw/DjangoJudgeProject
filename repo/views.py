from django.shortcuts import render, redirect
from django.http import HttpResponse
from repo.repos import repos 
# Create your views here.

def test(request,id):
	for repo in repos:
		if repo.get('id') == id:
			return render(request , 'questionRepo/Repo.html',{'repo' : repo })
	return redirect('index/')


