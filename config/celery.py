import os
from celery import Celery
from celery.schedules import crontab

# Указываем Django settings модуль для Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Имя приложения должно совпадать с именем папки!
app = Celery('config',broker='redis://localhost:6379/0')

# Загружаем настройки из Django, все настройки Celery должны начинаться с CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим tasks.py в приложениях
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


app.conf.beat_schedule = {
    'auto-publish-news-every-5-minutes': {
        'task': 'newsapp.tasks.publish_all_news', 
        'schedule': crontab(minute='*/5'), 
    },
}

app.conf.timezone='Asia/Tashkent'