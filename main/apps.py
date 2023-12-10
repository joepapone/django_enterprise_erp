from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

class Menu():
    def __init__(self, link, text):
        self.link = link
        self.text = text
    
    def __repr__(self):
        return f'Link: {self.link}, Text: {self.text}'

