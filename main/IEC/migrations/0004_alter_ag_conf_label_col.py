# Generated by Django 4.1 on 2024-04-03 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("IEC", "0003_alter_ag_conf_label_col"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ag_conf",
            name="label_col",
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
