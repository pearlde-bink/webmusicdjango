# Generated by Django 4.2.6 on 2023-10-16 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_rename_voabulary_music_vocabulary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vocab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng', models.CharField(max_length=100)),
                ('meaning', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='music',
            name='vocabs',
            field=models.ManyToManyField(related_name='music', to='music.vocab'),
        ),
    ]
