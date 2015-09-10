from django.http import HttpResponse

# Create your views here.
def home_page(request):
	return HttpResponse('<html><title>To-Do Lists</title><body><h1>To-Do Lists for today </h1></body></html>')
