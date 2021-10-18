"""Определяет схемы URL для green_branchs."""

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'green_branchs'
urlpatterns = [
	# Домашняя страница.
	path('', views.index, name='index'),

	# Вывод всех тем для планов питания.
	path(r'^topics_plan/$', views.topics_plan, name='topics_plan'),
	# Страница с подробной информацией по отдельному плану питания
	path(r'^topics_plan/(?P<topic_plan_id>\d+)/$', views.topic_plan, name='topic_plan'),

	# Вывод всех тем рецептов.
	path(r'^topics_rec/$', views.topics_rec, name='topics_rec'),
	# Страница со списком рецептов.
	path(r'^topics_rec/(?P<topic_rec_id>\d+)/$', views.topic_rec, name='topic_rec'),
	
	# Вывод всех тем продуктов.
	path(r'^topics_prod/$', views.topics_prod, name='topics_prod'),
	# Страница со списком продутов.
	path(r'^topics_prod/(?P<topic_prod_id>\d+)/$', views.topic_prod, name='topic_prod'),
	
	# Вывод всех тем для тренировок.
	path(r'^topics_activ/$', views.topics_activ, name='topics_activ'),
	# Страница со списком тренировок.
	path(r'^topics_activ/(?P<topic_activ_id>\d+)/$', views.topic_activ, name='topic_activ'),
	
	# Вывод всех тем.
	path(r'^topics/$', views.topics, name='topics'),
	# Страница с подробной информацией по отдельной теме
	path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
	# Страница для добавления новой темы
	path(r'^new_topic/$', views.new_topic, name='new_topic'),
	# Страница для добавления новой записи
	path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
	# Страница для редактирования записи
	path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,name='edit_entry'),
	
]
# включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
