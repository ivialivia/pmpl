from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/')
	
	items = Item.objects.all()
	itempribadi =''
	
	if Item.objects.count()==0 :
		itempribadi = 'yey, waktunya berlibur'
	elif Item.objects.count()<5 :
		itempribadi = 'sibuk tapi santai'
	elif Item.objects.count()>=5 :
		itempribadi = 'oh tidak'
	return render(request, 'home.html', {'items': items, 'itempribadi': itempribadi})
