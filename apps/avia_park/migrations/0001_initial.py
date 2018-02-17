# Generated by Django 2.0.2 on 2018-02-17 16:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Craft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(db_index=True, default=True, help_text='show/hide record.', verbose_name='enabled')),
                ('pub_date_start', models.DateTimeField(db_index=True, default=django.utils.timezone.now, help_text='Rocord will be visible form this date.', verbose_name='start date for publication')),
                ('pub_date_end', models.DateTimeField(blank=True, db_index=True, help_text='Rocord will be invisible form this date.', null=True, verbose_name='end date for publication')),
                ('weight', models.PositiveIntegerField(db_index=True, default=0, help_text='Rocord will be first with greate weight.', verbose_name='weight of publication')),
                ('title', models.CharField(max_length=255, verbose_name='craft title')),
                ('description', models.TextField(blank=True, verbose_name='craft description')),
                ('image', models.ImageField(upload_to='avia_park', verbose_name='craft image')),
                ('slug', models.CharField(max_length=255, unique=True, verbose_name='craft slug')),
            ],
            options={
                'ordering': ['-weight', '-pub_date_start'],
                'verbose_name': 'craft',
                'verbose_name_plural': 'crafts',
            },
        ),
        migrations.CreateModel(
            name='CraftImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='avia_park', verbose_name='craft image')),
                ('craft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avia_park.Craft', verbose_name='craft')),
            ],
            options={
                'ordering': ['craft__title'],
                'verbose_name': 'craft image',
                'verbose_name_plural': 'crafts images',
            },
        ),
    ]
