from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publishing_date', 'content']  # post listesinde gozuken alanlar
    list_display_links = ['title', 'publishing_date']  # post icine girebilmek icin linkler
    list_filter = ['publishing_date']  # filtre olusturur
    search_fields = ['title', 'content']
    actions_on_bottom = True
    actions_on_top = False
    actions_selection_counter = False
    #date_hierarchy = 'publishing_date'
    # list_editable = ['title']                           #buraya yazdigimiz alanlar display linkste olmamali !

# admin.site.register(Post, PostAdmin)
