# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IUser',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=100)),
                ('birthday', models.DateField(blank=True, verbose_name='birthday', null=True)),
                ('password', models.CharField(max_length=100)),
                ('sex', models.IntegerField(blank=True, default=1, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('tag', models.CharField(blank=True, max_length=200, null=True)),
                ('head_img', models.CharField(blank=True, max_length=100, null=True)),
                ('register_time', models.DateField(blank=True, default=datetime.datetime(2015, 4, 21, 14, 15, 54, 2070, tzinfo=utc), null=True)),
                ('last_time', models.DateField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('song_name', models.CharField(max_length=100)),
                ('album', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.CharField(blank=True, max_length=100, null=True)),
                ('artist', models.CharField(blank=True, max_length=100, null=True)),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('path', models.CharField(blank=True, max_length=100, null=True)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('music_category', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MusicTag',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('tag_time', models.DateField(verbose_name='tag_time', default=datetime.datetime(2015, 4, 21, 14, 15, 54, 10071, tzinfo=utc))),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('play_list_name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlayTime',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('play_time', models.IntegerField(blank=True, default=0, null=True)),
                ('add_date', models.DateTimeField(blank=True, verbose_name='add_date', null=True)),
                ('music', models.ForeignKey(to='user.Music')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecommendHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('latest_recommend_time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecommendItem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('recommend_date', models.DateTimeField(verbose_name='recommend_date', default=django.utils.timezone.now)),
                ('music', models.ForeignKey(to='user.Music')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recommendhistory',
            name='recommend_items',
            field=models.ManyToManyField(blank=True, related_name='recommend_item', to='user.RecommendItem', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recommendhistory',
            name='recommend_user',
            field=models.ForeignKey(to='user.IUser'),
            preserve_default=True,
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
