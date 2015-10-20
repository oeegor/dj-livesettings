# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LiveSetting',
            fields=[
                ('key', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('key_type', models.CharField(max_length=256, choices=[(b'bool', b'bool'), (b'str', b'str'), (b'int', b'int'), (b'float', b'float'), (b'json', b'json'), (b'yaml', b'yaml')])),
                ('value', models.TextField()),
            ],
        ),
    ]
