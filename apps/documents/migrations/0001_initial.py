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
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(db_index=True, default=True, help_text='show/hide record.', verbose_name='enabled')),
                ('pub_date_start', models.DateTimeField(db_index=True, default=django.utils.timezone.now, help_text='Rocord will be visible form this date.', verbose_name='start date for publication')),
                ('pub_date_end', models.DateTimeField(blank=True, db_index=True, help_text='Rocord will be invisible form this date.', null=True, verbose_name='end date for publication')),
                ('weight', models.PositiveIntegerField(db_index=True, default=0, help_text='Rocord will be first with greate weight.', verbose_name='weight of publication')),
                ('title', models.CharField(max_length=255, verbose_name='document title')),
                ('document', models.FileField(upload_to='documents', verbose_name='document file')),
            ],
            options={
                'ordering': ['-weight', 'pub_date_start'],
                'verbose_name': 'document',
                'verbose_name_plural': 'documents',
            },
        ),
        migrations.CreateModel(
            name='DocumentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(db_index=True, default=True, help_text='show/hide record.', verbose_name='enabled')),
                ('pub_date_start', models.DateTimeField(db_index=True, default=django.utils.timezone.now, help_text='Rocord will be visible form this date.', verbose_name='start date for publication')),
                ('pub_date_end', models.DateTimeField(blank=True, db_index=True, help_text='Rocord will be invisible form this date.', null=True, verbose_name='end date for publication')),
                ('weight', models.PositiveIntegerField(db_index=True, default=0, help_text='Rocord will be first with greate weight.', verbose_name='weight of publication')),
                ('title', models.CharField(max_length=255, verbose_name='document category title')),
                ('description', models.TextField(blank=True, verbose_name='document category description')),
            ],
            options={
                'ordering': ['-weight', 'pub_date_start'],
                'verbose_name': 'document category item',
                'verbose_name_plural': 'document category items',
            },
        ),
        migrations.CreateModel(
            name='DocumentCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_date', models.DateTimeField(auto_now=True, verbose_name='access date')),
                ('client_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='client ip address')),
                ('user_agent', models.TextField(blank=True, verbose_name='user agent')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.Document', verbose_name='document')),
            ],
            options={
                'ordering': ['access_date'],
                'verbose_name': 'document counter',
                'verbose_name_plural': 'documents counter items',
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='doctype title')),
                ('description', models.TextField(verbose_name='doctype description')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'document type',
                'verbose_name_plural': 'documents types',
            },
        ),
        migrations.AddField(
            model_name='document',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.DocumentCategory', verbose_name='document category item'),
        ),
        migrations.AddField(
            model_name='document',
            name='doc_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.DocumentType', verbose_name='document type'),
        ),
    ]
