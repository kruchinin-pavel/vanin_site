import datetime
from django.db import models

from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField('название статьи', max_length=100)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField("дата публикации")

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    outer_name = models.CharField('автор коментария', max_length=60)
    comment_text = models.CharField('текст коменарий', max_length=300)

    def __str__(self):
        return self.outer_name

    class Meta:
        verbose_name = 'коментарий'
        verbose_name_plural = 'коментарии'
