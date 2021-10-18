from django.db import models
from django.contrib.auth.models import User

class Topic_plan(models.Model):
	#"""Тема готовых планов питания"""
	text = models.CharField(max_length=200)
	cover = models.ImageField(upload_to='images/')
	def __str__(self):
		#"""Возвращает строковое представление модели."""
		return self.text

class Entry_plan(models.Model):
	#"""Планы питания"""
	topic = models.ForeignKey(Topic_plan, on_delete = models.CASCADE)
	cover = models.ImageField(upload_to='images/')
	text = models.TextField()
	
	class Meta:
		verbose_name_plural = 'entries_plan'
	def __str__(self):
		#"""Возвращает строковое представление модели."""
		return self.text



class Topic_rec(models.Model):
	#"""Тема рецептов"""
	text = models.CharField(max_length=200)
	cover = models.ImageField(upload_to='images/')
	def __str__(self):
		#"""Возвращает строковое представление модели."""
		return self.text

class Entry_rec(models.Model):
	#"""Рецепты"""
	topic = models.ForeignKey(Topic_rec, on_delete = models.CASCADE)
	cover = models.ImageField(upload_to='images/')
	text = models.TextField()
	
	class Meta:
		verbose_name_plural = 'entries_rec'
	def __str__(self):
		#"""Возвращает строковое представление модели."""
		return self.text



class Topic_prod(models.Model):
	#"""Тема продуктов"""
	text = models.CharField(max_length=200)
	cover = models.ImageField(upload_to='images/')
	def __str__(self):
		#"""Возвращает строковое представление модели."""
		return self.text

class Entry_prod(models.Model):
	#"""Продукты"""
	topic = models.ForeignKey(Topic_prod, on_delete = models.CASCADE)
	cover = models.ImageField(upload_to='images/')
	text = models.TextField()
	
	class Meta:
		verbose_name_plural = 'entries_prod'
	def __str__(self):
		#"""Возвращает строковое представление модели."""
		return self.text



class Topic_activ(models.Model):
	#"""Тема тренировок"""
	text = models.CharField(max_length=200)
	cover = models.ImageField(upload_to='images/')
	def __str__(self):
		#"""Возвращает строковое представление модели."""
		return self.text

class Entry_activ(models.Model):
	#"""Тренировки"""
	topic = models.ForeignKey(Topic_activ, on_delete = models.CASCADE)
	cover = models.ImageField(upload_to='images/')
	text = models.TextField()
	
	class Meta:
		verbose_name_plural = 'entries_activ'
	def __str__(self):
		#"""Возвращает строковое представление модели."""
		return self.text

class Topic(models.Model):
	#"""Тема, которую изучает пользователь"""
	text = models.CharField(max_length=200)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
	#"""Возвращает строковое представление модели."""
		return self.text
#	@transaction.commit_on_success
#    def save(self, *args, **kwargs):
#       if not self.entry_id:
#            self.entry_id, _ = Entry.objects.get_or_create(text='_course_' + self.id)
#
#        super(Topic, self).save(*args, **kwargs)

class Entry(models.Model):
	topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
	text = models.TextField()
	
	class Meta:
		verbose_name_plural = 'entries'
	def __str__(self):
		return self.text[:50] + "..."
