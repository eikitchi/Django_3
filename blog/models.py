from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Post(models.Model):
    name = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='URL')
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='images/', verbose_name='изображение', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    published = models.BooleanField(verbose_name='признак публикации', default=True)
    view_count = models.PositiveIntegerField(verbose_name='количество просмотров', default=0)

    def __str__(self):
        return f'{self.name} {self.slug}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('created_at',)

    def increase_view_count(self):
        """
        Увеличивает просмотры поста на 1.
        """
        self.view_count += 1
        self.save()