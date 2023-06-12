from django.db import models

from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Baslik')
    body = models.TextField(verbose_name='Metin')
    date = models.DateField(auto_now_add=True, verbose_name='Tarih')
    author_name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Yazar')
    

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={"pk": self.pk}) 

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Haber", related_name='comments')
    comment = models.CharField(max_length = 200,verbose_name = "Yorum")
    comment_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name = "Isim")
    
    def __str__(self):
        return self.comment

    def get_absolute_url():
        return reverse('article_list')