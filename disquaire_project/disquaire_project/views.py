from django.http import HttpResponse

def accueil(request):
	message=('<h1>Hello world</h1><br/><h3>Welcome on my first page</h3>')
	return HttpResponse(message)