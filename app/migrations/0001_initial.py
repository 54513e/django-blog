# Generated by Django 3.2.11 on 2023-01-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('content', models.TextField(verbose_name='内容')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
            ],
            options={
                'verbose_name': 'ブログ',
                'verbose_name_plural': 'ブログ',
            },
        ),
    ]
