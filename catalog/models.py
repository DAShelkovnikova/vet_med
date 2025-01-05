from django.db import models


NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        **NULLABLE
    )
    photo = models.ImageField(
        upload_to="product/photo",
        verbose_name="Изображение",
        help_text="Загрузите фото категории",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        **NULLABLE
    )
    price = models.IntegerField(
        verbose_name="Цена", help_text="Укажите цену за покупку", **NULLABLE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию",
        related_name="categories",
        **NULLABLE
    )
    restrictions = models.TextField(
        verbose_name="Ограничения",
        help_text="Укажите любые ограничения на продукт",
        **NULLABLE
    )
    medical_indications = models.TextField(
        verbose_name="Медицинские показания",
        help_text="Укажите медицинские показания",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Название компании",
        help_text="Введите название компании",
    )
    description = models.TextField(
        verbose_name="Описание компании",
        help_text="Введите описание компании",
        **NULLABLE
    )
    photo = models.ImageField(
        upload_to="product/photo",
        verbose_name="Изображение",
        help_text="Загрузите фото компании",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Имя",
        help_text="Введите ваше имя",
    )
    surname = models.CharField(
        max_length=150,
        verbose_name="Фамилия",
        help_text="Введите вашу фамилию",
    )
    patronymic = models.CharField(
        max_length=150,
        verbose_name="Отчество",
        help_text="Введите ваше отчество",
        **NULLABLE
    )
    email = models.EmailField(
        verbose_name="Email",
        help_text="Введите ваш email",
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        help_text="Введите ваш номер телефона",
    )

    token = models.CharField(max_length=100, verbose_name="token", **NULLABLE)

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"

    def __str__(self):
        return self.name
