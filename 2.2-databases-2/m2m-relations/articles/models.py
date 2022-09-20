from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    sections = models.ManyToManyField('Section', related_name='articles', through='ArticleSection')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Section(models.Model):

    section_name = models.CharField(max_length=100, verbose_name='Тематика')

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'

    def __str__(self):
        return self.section_name


class ArticleSection(models.Model):

    articles = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes', verbose_name='Статья')
    sections = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='scopes', verbose_name='Тематика')
    main_section = models.BooleanField(verbose_name='Основной раздел')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статей'

    def __str__(self):
        return f'Тэг; {"Основной" if self.main_section else "Второстепенный"}; {self.sections.section_name}'


