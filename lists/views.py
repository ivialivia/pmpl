from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def home_page(request):
	#pass
	return render(request, 'home.html')	

def view_list(request):
	items = Item.objects.all()
	itempribadi =''

	if Item.objects.count()==0 :
		itempribadi = 'yey, waktunya berlibur'
	elif Item.objects.count()<5 :
		itempribadi = 'sibuk tapi santai'
	elif Item.objects.count()>=5 :
		itempribadi = 'oh tidak'
	return render(request, 'list.html', {'items': items, 'itempribadi': itempribadi})
def new_list(request):
	Item.objects.create(text=request.POST['item_text'])
	return redirect('/lists/the-only-list-in-the-world/')
