from django.apps import AppConfig
# +

class MainPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_page'


# class SuitConfig(DjangoSuitConfig):# this to change the theme of the admin panel
#     layout = 'vertical' # the theme name   and we will put it in setting 