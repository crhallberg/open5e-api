# Generated by Django 3.2.20 on 2023-10-29 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0010_rename_type_creature_deprecated_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatureType',
            fields=[
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('desc', models.TextField(help_text='Description of the game content item. Markdown.')),
                ('key', models.CharField(help_text='Unique key for the Item.', max_length=100, primary_key=True, serialize=False)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v2.document')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CreatureSet',
            fields=[
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('key', models.CharField(help_text='Unique key for the Item.', max_length=100, primary_key=True, serialize=False)),
                ('creatures', models.ManyToManyField(help_text='The set of creatures.', related_name='creaturesets', to='api_v2.Creature')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v2.document')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]