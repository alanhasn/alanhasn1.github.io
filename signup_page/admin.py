from django.contrib import admin
from .models import Acounts
# Register your models here.


class signup_admin(admin.ModelAdmin): # to show the content of the fields outside

    list_display =['Username','Email','Password'] # what you want to display
    # list_display_links = ['Username','Email','Password'] # to display the item like links
    list_editable = ['Email','Password'] # to can edit the item from outside
    search_fields = ['Username'] # to create the search fields search by the username
    list_filter = ['Username','Email','Password'] # to filter the item by any category you want 
    
admin.site.register(Acounts) # register signup and signup_admin 

