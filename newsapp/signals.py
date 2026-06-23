from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import News
from .tasks import publish_news
from django.db import transaction


@receiver([post_save, post_delete], sender=News)
def clear_news_cache(sender, instance,created,**kwargs):
    
    transaction.on_commit(lambda: publish_news(instance.id))
       
    cache.delete_pattern('*news_api_list*')
    print('CACHE IS DELETED')
