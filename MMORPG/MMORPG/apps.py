from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MMORPG'
  #  def ready(self):
  #     import news.signals

