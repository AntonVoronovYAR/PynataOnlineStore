# Generated by Django 4.1.7 on 2023-03-25 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_card_service_delete_services_alter_filling_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='filling',
            field=models.ForeignKey(help_text='Наполнение', null=True, on_delete=django.db.models.deletion.CASCADE, to='cards.filling'),
        ),
    ]