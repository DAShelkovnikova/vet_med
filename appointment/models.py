from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Appointment(models.Model):
    owner_name = models.CharField(
        max_length=150,
        verbose_name="Имя владельца животного",
        help_text="Как зовут владельца животного",
    )
    pet_name = models.CharField(
        max_length=150,
        verbose_name="Кличка питомца",
        help_text="Как зовут вашего питомца",
    )
    type = models.CharField(
        max_length=150, verbose_name="Вид животного", help_text="Введите вид животного"
    )
    gender = models.CharField(
        max_length=150,
        verbose_name="Пол вашего питомца",
        help_text="Какого пола ваш питомец",
    )
    age = models.CharField(
        max_length=150,
        verbose_name="Возраст питомца",
        help_text="Какого возраста ваш питомец",
    )
    phone = models.CharField(
        max_length=150,
        verbose_name="Телефон для связи",
        help_text="По каком телефону можно с вами связаться",
    )
    email = models.EmailField(
        max_length=150, verbose_name="Ваш email", help_text="Введите ваш email"
    )


    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return self.name
