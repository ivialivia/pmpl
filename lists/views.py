from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.
def home_page(request):
	#pass
	itempribadi='yey, waktunya berlibur'
	return render(request, 'home.html', {'itempribadi': itempribadi})	

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	itempribadi =''

	if Item.objects.filter(list_id=list_id).count()==0 :
		itempribadi = 'yey, waktunya berlibur'
	elif Item.objects.filter(list_id=list_id).count()<5 :
		itempribadi = 'sibuk tapi santai'
	elif Item.objects.filter(list_id=list_id).count()>=5 :
		itempribadi = 'oh tidak'
	return render(request, 'list.html', {'list': list_, 'itempribadi': itempribadi})
def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))
def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))	
