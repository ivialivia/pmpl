from django.http import HttpResponse

# Create your views here.
def home_page(request):
	return HttpResponse('<html><title>Alivia Khaira 1206277464</title><body>Halaman milik Alivia</body></html>')
