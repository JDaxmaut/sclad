from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название организации")
    code = models.CharField(max_length=50, unique=True, verbose_name="Код организации")

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def __str__(self):
        return self.name


class Category(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name="Организация")
    name = models.CharField(max_length=100, verbose_name="Название категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name="Организация")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=200, verbose_name="Товар")
    sku = models.CharField(max_length=50, unique=True, verbose_name="Артикул")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Остаток на складе")
    min_limit = models.PositiveIntegerField(default=5, verbose_name="Минимальный порог")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"{self.name} ({self.sku})"

    @property
    def is_low_stock(self):
        return self.quantity <= self.min_limit