from django.db import models

from accounts.models import User


class Shop(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    url = models.URLField(verbose_name='Ссылка', null=True, blank=True)
    user = models.OneToOneField(User, verbose_name='Пользователь', related_name='shop',
                                blank=True, null=True,
                                on_delete=models.CASCADE)
    state = models.BooleanField(verbose_name='статус получения заказов', default=True)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = "Магазины"
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название')
    shops = models.ManyToManyField(Shop, verbose_name='Магазины', related_name='categories',
                                   blank=True, related_query_name='shops')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"
        ordering = ('-name',)

    def __str__(self):
        return self.name


# class Product(models.Model):
#     name = models.CharField(max_length=80, verbose_name='Название')
#     category = models.ForeignKey(Category, verbose_name='Категория', related_name='products', blank=True,
#                                  on_delete=models.CASCADE)
#     model = models.CharField(max_length=80, verbose_name='Модель', blank=True)
#     external_id = models.PositiveIntegerField(verbose_name='Внешний ИД')
#     shop = models.ForeignKey(Shop, verbose_name='Магазин', related_name='products_info', blank=True,
#                              on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(verbose_name='Количество')
#     price = models.PositiveIntegerField(verbose_name='Цена')
#     price_rrc = models.PositiveIntegerField(verbose_name='Рекомендуемая розничная цена')
#
#     class Meta:
#         verbose_name = 'Продукт'
#         verbose_name_plural = "Продукты"
#         ordering = ('category', '-name')
#         constraints = [
#             models.UniqueConstraint(fields=['shop', 'category', 'external_id'], name='unique_product_info'),
#         ]
#
#     def __str__(self):
#         return self.name


# class ProductInfo(models.Model):
#     model = models.CharField(max_length=80, verbose_name='Модель', blank=True)
#     external_id = models.PositiveIntegerField(verbose_name='Внешний ИД')
#     product = models.ForeignKey(Product, verbose_name='Продукт', related_name='product_infos', blank=True,
#                                 on_delete=models.CASCADE)
#     shop = models.ForeignKey(Shop, verbose_name='Магазин', related_name='product_info', blank=True,
#                              on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(verbose_name='Количество')
#     price = models.PositiveIntegerField(verbose_name='Цена')
#     price_rrc = models.PositiveIntegerField(verbose_name='Рекомендуемая розничная цена')
#
#     class Meta:
#         verbose_name = 'Информация о продукте'
#         verbose_name_plural = "Информация о продуктах"
#         constraints = [
#             models.UniqueConstraint(fields=['product', 'shop', 'external_id'], name='unique_product_info'),
#         ]
#
#     def __str__(self):
#         return self.product.name


# class Parameter(models.Model):
#     name = models.CharField(max_length=40, verbose_name='Название')
#
#     class Meta:
#         verbose_name = 'Имя параметра'
#         verbose_name_plural = "Имена параметров"
#         ordering = ('-name',)
#
#     def __str__(self):
#         return self.name


# class ProductParameter(models.Model):
#     product_info = models.ForeignKey(Product, verbose_name='Информация о продукте',
#                                      related_name='product_parameters', blank=True,
#                                      on_delete=models.CASCADE)
#     parameter = models.ForeignKey(Parameter, verbose_name='Параметр', related_name='product_parameters', blank=True,
#                                   on_delete=models.CASCADE)
#     value = models.CharField(verbose_name='Значение', max_length=100)
#
#     class Meta:
#         verbose_name = 'Параметр'
#         verbose_name_plural = "Параметры"
#         constraints = [
#             models.UniqueConstraint(fields=['product_info', 'parameter'], name='unique_product_parameter'),
#         ]
