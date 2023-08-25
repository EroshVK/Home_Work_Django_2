from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=250, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, )
    price = models.IntegerField(verbose_name='цена')
    creation_date = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    last_modified_date = models.DateTimeField(verbose_name='дата последнего изменения', **NULLABLE)
    owner = models.ForeignKey(User, verbose_name=' пользователь', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.category} - {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='slag', **NULLABLE)
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    creation_date = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    is_publish = models.BooleanField(verbose_name='признак публикации')
    count_of_views = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блоговая запись'
        verbose_name_plural = 'блоговые записи'


class Version(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='Версия продукта', **NULLABLE)
    version_name = models.CharField(max_length=150, verbose_name='Название версии', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Версия активна')

    def __str__(self):
        return f'{self.product.name}: Версия {self.number}'

    class Meta:
        verbose_name = ('Версия продукта')
        verbose_name_plural = ('Версии продукта')
