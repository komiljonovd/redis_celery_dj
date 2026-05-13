from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import News

@receiver([post_save, post_delete], sender=News)
def clear_news_cache(sender, instance, **kwargs):
    cache.delete_pattern('*news_api_list*')
    print('CACHE IS DELETED')
