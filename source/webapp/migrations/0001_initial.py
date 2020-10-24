# Generated by Django 2.2.13 on 2020-10-24 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_img', models.ImageField(upload_to='photos', verbose_name='Картинка')),
                ('signature', models.CharField(max_length=200, verbose_name='Подпись')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_photos', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
    ]
