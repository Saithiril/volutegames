from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class New(models.Model):
	caption = models.CharField(max_length=30, verbose_name='Заголовок')
	text_news = models.TextField(max_length=500, verbose_name='Текст')
	pub_date = models.DateTimeField('date published', editable=False)
	author = models.ForeignKey(User, editable=False)
	class Meta:
		verbose_name = "Новость"
		verbose_name_plural = "Новости"