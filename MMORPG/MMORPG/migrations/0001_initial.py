# Generated by Django 4.0.2 on 2022-02-27 09:11

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
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(choices=[('T', 'Tanks'), ('H', 'Hills'), ('D', 'Dealer'), ('GM', 'Gildmaster'), ('QG', 'Questgiver'), ('SM', 'Smith'), ('L', 'Leathers'), ('PM', 'Poisonmaker'), ('SM', 'Spellmaster')], default=None, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date_created', models.DateField(auto_now_add=True)),
                ('post_detailed_data_created', models.TimeField(auto_now_add=True)),
                ('head_of_post', models.CharField(max_length=255)),
                ('article_text', models.TextField()),
                ('image', models.FileField(blank=True, upload_to='')),
                ('video', models.FileField(blank=True, upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MMORPG.category')),
                ('post_author', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='MMORPG.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='videos/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MMORPG.post')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MMORPG.post')),
            ],
        ),
    ]
