# Generated by Django 5.1.4 on 2025-01-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "owner_name",
                    models.CharField(
                        help_text="Как зовут владельца животного",
                        max_length=150,
                        verbose_name="Имя владельца животного",
                    ),
                ),
                (
                    "pet_name",
                    models.CharField(
                        help_text="Как зовут вашего питомца",
                        max_length=150,
                        verbose_name="Кличка питомца",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        help_text="Введите вид животного",
                        max_length=150,
                        verbose_name="Вид животного",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        help_text="Какого пола ваш питомец",
                        max_length=150,
                        verbose_name="Пол вашего питомца",
                    ),
                ),
                (
                    "age",
                    models.CharField(
                        help_text="Какого возраста ваш питомец",
                        max_length=150,
                        verbose_name="Возраст питомца",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        help_text="По каком телефону можно с вами связаться",
                        max_length=150,
                        verbose_name="Телефон для связи",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Введите ваш email",
                        max_length=150,
                        verbose_name="Ваш email",
                    ),
                ),
                (
                    "appointment_date",
                    models.DateField(
                        help_text="Выберите желаемую дату записи",
                        verbose_name="Желаемая дата записи",
                    ),
                ),
            ],
            options={
                "verbose_name": "Запись",
                "verbose_name_plural": "Записи",
            },
        ),
    ]
