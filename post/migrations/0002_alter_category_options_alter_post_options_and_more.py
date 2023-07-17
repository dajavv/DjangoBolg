# Generated by Django 4.2.3 on 2023-07-15 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '类别'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': '帖子'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': '标签'},
        ),
        migrations.AddField(
            model_name='post',
            name='photos',
            field=models.CharField(default=1, max_length=200, verbose_name='封面图片'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='words',
            field=models.CharField(default=1, max_length=15, verbose_name='字数'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='cname',
            field=models.CharField(max_length=30, unique=True, verbose_name='类别名称'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.category', verbose_name='所属类别'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='类别内容'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发帖时间'),
        ),
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.CharField(max_length=200, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='post',
            name='isdelete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='post.tag', verbose_name='所属标签'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tname',
            field=models.CharField(max_length=20, unique=True, verbose_name='标签'),
        ),
    ]