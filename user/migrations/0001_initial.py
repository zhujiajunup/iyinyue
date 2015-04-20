# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('user_name', models.CharField(max_length=100)),
                ('birthday', models.DateField(blank=True, verbose_name='birthday', null=True)),
                ('password', models.CharField(max_length=100)),
                ('sex', models.IntegerField(blank=True, default=1, null=True)),
                ('email', models.EmailField(blank=True, null=True, max_length=100)),
                ('tag', models.CharField(blank=True, null=True, max_length=200)),
                ('head_img', models.CharField(blank=True, null=True, max_length=100)),
                ('register_time', models.DateField(blank=True, default=datetime.datetime(2015, 4, 20, 12, 18, 54, 327838, tzinfo=utc), null=True)),
                ('last_time', models.DateField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('song_name', models.CharField(max_length=100)),
                ('album', models.CharField(blank=True, null=True, max_length=100)),
                ('year', models.CharField(blank=True, null=True, max_length=100)),
                ('artist', models.CharField(blank=True, null=True, max_length=100)),
                ('comment', models.CharField(blank=True, null=True, max_length=100)),
                ('genre', models.CharField(blank=True, null=True, max_length=100)),
                ('path', models.CharField(blank=True, null=True, max_length=100)),
                ('popular', models.IntegerField(default=0)),
                ('unpopular', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MusicCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('music_category', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MusicTag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('tag_time', models.DateField(default=datetime.datetime(2015, 4, 20, 12, 18, 54, 333839, tzinfo=utc), verbose_name='tag_time')),
                ('tag_content', models.CharField(max_length=100)),
                ('tag_music', models.ForeignKey(to='user.Music')),
                ('tag_user', models.ForeignKey(to='user.IUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('operation_time', models.DateField(verbose_name='operation_time')),
                ('operation_type', models.CharField(max_length=50)),
                ('operation_music', models.ForeignKey(to='user.Music')),
                ('operation_user', models.ForeignKey(to='user.IUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('play_list_name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlayTime',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('play_time', models.IntegerField(blank=True, default=0, null=True)),
                ('add_date', models.DateTimeField(blank=True, verbose_name='add_date', null=True)),
                ('music', models.ForeignKey(to='user.Music')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='playlist',
            name='play_time',
            field=models.ManyToManyField(blank=True, related_name='musics', to='user.PlayTime', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='music',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='category', to='user.MusicCategory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='dislike_songs',
            field=models.ManyToManyField(blank=True, related_name='dislike_songs', to='user.Music', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='favorite_songs',
            field=models.ManyToManyField(blank=True, related_name='favorite_songs', to='user.PlayTime', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='friends_rel_+', to='user.IUser', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='play_list',
            field=models.ManyToManyField(blank=True, related_name='play_list', to='user.PlayList', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='play_recorded',
            field=models.ManyToManyField(blank=True, related_name='play_recorded', to='user.PlayTime', null=True),
            preserve_default=True,
        ),
    ]
