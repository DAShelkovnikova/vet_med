from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите фото категории",
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
        blank=True,
        null=True,
    )
    price = models.IntegerField(
        blank=True, null=True, verbose_name="Цена", help_text="Укажите цену за покупку"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию",
        null=True,
        blank=True,
        related_name="categories",
    )
    restrictions = models.TextField(
        verbose_name="Ограничения",
        help_text="Укажите любые ограничения на продукт",
        blank=True,
        null=True,
    )
    medical_indications = models.TextField(
        verbose_name="Медицинские показания",
        help_text="Укажите медицинские показания",
        blank=True,
        null=True,
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
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите фото компании",
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
        blank=True,
        null=True,
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
    appointment = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        verbose_name="Запись вашего питомца на прием",
        help_text="Введите, куда вы хотите записаться",
        null=True,
        blank=True,
    )
    token = models.CharField(
        max_length=100, verbose_name="token", blank=True, null=True
    )

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"

    def __str__(self):
        return self.name



