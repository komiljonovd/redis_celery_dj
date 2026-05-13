from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'News'
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']