from django.contrib import admin
from stabilo.models import Category, Keyword

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('label',)}

class KeywordAdmin(admin.ModelAdmin):
    list_display = ('category', 'keyword')
    list_filter = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Keyword, KeywordAdmin)
