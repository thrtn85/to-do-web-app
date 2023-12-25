from django.shortcuts import render, redirect
from django.contrib import messages

# import todo form and models

from .forms import ToDoForm
from .models import ToDo

###############################################


def index(request):

	item_list = ToDo.objects.order_by("-create_date")
	if request.method == "POST":
		form = ToDoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todo')
	form = ToDoForm()

	page = {
		"form": form,
		"list": item_list,
		"title": "TODO LIST",
	}
	return render(request, 'todo/todo.html', page)


### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
	item = ToDo.objects.get(id=item_id)
	item.delete()
	messages.info(request, "item removed !!!")
	return redirect('todo')
