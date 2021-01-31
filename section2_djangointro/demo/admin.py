from django.contrib import admin
from .models import Book

#admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #fields = ['title','description']
    list_display = ['title','description']
    list_filter = ['published']
    search_field = ['title']
