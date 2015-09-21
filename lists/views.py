from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.
def home_page(request):
	#pass
	return render(request, 'home.html')	

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	items = Item.objects.filter(list=list_)
	itempribadi =''

	if Item.objects.count()==0 :
		itempribadi = 'yey, waktunya berlibur'
	elif Item.objects.count()<5 :
		itempribadi = 'sibuk tapi santai'
	elif Item.objects.count()>=5 :
		itempribadi = 'oh tidak'
	return render(request, 'list.html', {'items': items, 'itempribadi': itempribadi})
def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))
