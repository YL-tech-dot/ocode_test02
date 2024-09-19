# Generated by Django 3.1.3 on 2024-09-17 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0008_answer_answer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_image',
            field=models.ImageField(blank=True, null=True, upload_to='pybo/answer_image', verbose_name='업로드 이미지'),
        ),
        migrations.AlterField(
            model_name='question',
            name='image1',
            field=models.ImageField(default=1, upload_to='pybo/image1/', verbose_name='업로드 이미지1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='image2',
            field=models.ImageField(default=1, upload_to='pybo/image2/', verbose_name='업로드 이미지2'),
            preserve_default=False,
        ),
    ]
