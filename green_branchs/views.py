from django.shortcuts import render

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic_plan, Topic_rec, Topic_prod, Topic_activ, Topic, Entry
from .forms import TopicForm, EntryForm



def index(request):
#"""Домашняя страница приложения green_branchs"""
	return render(request, 'green_branchs/index.html')



def topics_plan(request):
#"""Выводит список планов питания."""	
	topics_plan = Topic_plan.objects.order_by()
	context = {'topics_plan': topics_plan}
	return render(request, 'green_branchs/topics_plan.html', context)
	
def topic_plan(request, topic_plan_id):
#"""Выводит план питания и связанные сним записи."""
	topic_plan = Topic_plan.objects.get(id=topic_plan_id)
	entries_plan = topic_plan.entry_plan_set.order_by()
	context = {'topic_plan': topic_plan, 'entries_plan': entries_plan}
	return render(request, 'green_branchs/topic_plan.html', context)
	


def topics_rec(request):
#"""Выводит список категорий рецептов."""	
	topics_rec = Topic_rec.objects.order_by()
	context = {'topics_rec': topics_rec}
	return render(request, 'green_branchs/topics_rec.html', context)
	
def topic_rec(request, topic_rec_id):
#"""Выводит список рецептов."""
	topic_rec = Topic_rec.objects.get(id=topic_rec_id)
	entries_rec = topic_rec.entry_rec_set.order_by()
	context = {'topic_rec': topic_rec, 'entries_rec': entries_rec}
	return render(request, 'green_branchs/topic_rec.html', context)



def topics_prod(request):
#"""Выводит список категорий продуктов."""	
	topics_prod = Topic_prod.objects.order_by()
	context = {'topics_prod': topics_prod}
	return render(request, 'green_branchs/topics_prod.html', context)
	
def topic_prod(request, topic_prod_id):
#"""Выводит список продуктов."""
	topic_prod = Topic_prod.objects.get(id=topic_prod_id)
	entries_prod = topic_prod.entry_prod_set.order_by()
	context = {'topic_prod': topic_prod, 'entries_prod': entries_prod}
	return render(request, 'green_branchs/topic_prod.html', context)



def topics_activ(request):
#"""Выводит список категорий тренировок."""	
	topics_activ = Topic_activ.objects.order_by()
	context = {'topics_activ': topics_activ}
	return render(request, 'green_branchs/topics_activ.html', context)
	
def topic_activ(request, topic_activ_id):
#"""Выводит список тренировок."""
	topic_activ = Topic_activ.objects.get(id=topic_activ_id)
	entries_activ = topic_activ.entry_activ_set.order_by()
	context = {'topic_activ': topic_activ, 'entries_activ': entries_activ}
	return render(request, 'green_branchs/topic_activ.html', context)



@login_required
def topics(request):
#"""Выводит список тем."""	
	topics = Topic.objects.filter(owner=request.user).order_by()
	context = {'topics': topics}
	return render(request, 'green_branchs/topics.html', context)

@login_required
def topic(request, topic_id):
#"""Выводит одну тему и все ее записи."""
	topic = Topic.objects.get(id=topic_id)
	# Проверка того, что тема принадлежит текущему пользователю.
	if topic.owner != request.user:
		raise Http404
	entries = topic.entry_set.order_by()
	context = {'topic': topic, 'entries': entries}
	return render(request, 'green_branchs/topic.html', context)

@login_required
def new_topic(request):
#"""Определяет новую тему."""
	if request.method != 'POST':
		# Данные не отправлялись; создается пустая форма.
		form = TopicForm()
	else:
		# Отправлены данные POST; обработать данные.
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
#			form.save()
		return HttpResponseRedirect(reverse('green_branchs:topics'))
	context = {'form': form}
	return render(request, 'green_branchs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
#"""Добавляет новую запись по конкретной теме."""
	topic = Topic.objects.get(id=topic_id)
	if request.method != 'POST':
		# Данные не отправлялись; создается пустая форма.
		form = EntryForm()
	else:
		# Отправлены данные POST; обработать данные.
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('green_branchs:topic', args=[topic_id]))
	context = {'topic': topic, 'form': form}
	return render(request, 'green_branchs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
#"""Редактирует существующую запись."""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if topic.owner != request.user:
		raise Http404
	if request.method != 'POST':
		# Исходный запрос; форма заполняется данными текущей записи.
		form = EntryForm(instance=entry)
	else:
		# Отправка данных POST; обработать данные.
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('green_branchs:topic', args=[topic.id]))
	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'green_branchs/edit_entry.html', context)
