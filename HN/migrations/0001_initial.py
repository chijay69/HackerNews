# Generated by Django 4.1.3 on 2022-12-02 19:25

import HN.models
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('dead', models.BooleanField(blank=True, default=False, null=True)),
                ('deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('kids', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=HN.models.default_thing, null=True, size=None)),
                ('type', models.CharField(choices=[('job', 'Job'), ('story', 'Story'), ('comment', 'Comment'), ('poll', 'Poll'), ('pollopt', 'Pollopt')], default='job', max_length=250, null=True)),
            ],
            options={
                'ordering': ('-time',),
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HN.basemodel')),
                ('parent', models.IntegerField(blank=True)),
                ('text', models.CharField(blank=True, max_length=8192, null=True)),
            ],
            bases=('HN.basemodel',),
        ),
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HN.basemodel')),
                ('text', models.CharField(blank=True, max_length=8192, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
            ],
            bases=('HN.basemodel',),
        ),
        migrations.CreateModel(
            name='PollModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HN.basemodel')),
                ('parts', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=HN.models.default_thing, null=True, size=None)),
                ('descendants', models.IntegerField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('text', models.CharField(blank=True, max_length=8192, null=True)),
            ],
            bases=('HN.basemodel',),
        ),
        migrations.CreateModel(
            name='PolloptModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HN.basemodel')),
                ('parent', models.IntegerField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
            ],
            bases=('HN.basemodel',),
        ),
        migrations.CreateModel(
            name='StoryModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HN.basemodel')),
                ('descendants', models.IntegerField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
            bases=('HN.basemodel',),
        ),
    ]
