# Generated by Django 2.0.2 on 2018-02-17 16:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FrequentlyQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(db_index=True, default=True, help_text='show/hide record.', verbose_name='enabled')),
                ('pub_date_start', models.DateTimeField(db_index=True, default=django.utils.timezone.now, help_text='Rocord will be visible form this date.', verbose_name='start date for publication')),
                ('pub_date_end', models.DateTimeField(blank=True, db_index=True, help_text='Rocord will be invisible form this date.', null=True, verbose_name='end date for publication')),
                ('weight', models.PositiveIntegerField(db_index=True, default=0, help_text='Rocord will be first with greate weight.', verbose_name='weight of publication')),
                ('title', models.CharField(max_length=255, verbose_name='question title')),
                ('question', models.TextField(verbose_name='question')),
                ('answer', models.TextField(verbose_name='answer')),
            ],
            options={
                'ordering': ['-weight', '-pub_date_start'],
                'verbose_name': 'frequently question item',
                'verbose_name_plural': 'frequently questions items',
            },
        ),
    ]
