from itertools import chain

from django.contrib import admin

from .models import Article, Section, ArticleSection


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image',]# 'get_sections']
    list_filter = ['published_at',] # 'get_sections']

    # @admin.display(description='Article Section', ordering='sections__section_name')
    # def get_sections(self, obj):
    #     return obj.sections.section_name


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id',]
    # 'section_name']


@admin.register(ArticleSection)
class ArticleSection(admin.ModelAdmin):
    list_display = ['id']

