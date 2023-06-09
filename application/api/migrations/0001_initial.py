# Generated by Django 4.2 on 2023-05-19 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patent",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=150, unique=True)),
                ("c", models.FloatField(blank=True, null=True)),
                ("cr", models.FloatField(blank=True, null=True)),
                ("co", models.FloatField(blank=True, null=True)),
                ("mo", models.FloatField(blank=True, null=True)),
                ("w", models.FloatField(blank=True, null=True)),
                ("ti", models.FloatField(blank=True, null=True)),
                ("al", models.FloatField(blank=True, null=True)),
                ("nb", models.FloatField(blank=True, null=True)),
                ("ta", models.FloatField(blank=True, null=True)),
                ("b", models.FloatField(blank=True, null=True)),
                ("zr", models.FloatField(blank=True, null=True)),
                ("hf", models.FloatField(blank=True, null=True)),
                ("v", models.FloatField(blank=True, null=True)),
                ("re", models.FloatField(blank=True, null=True)),
                ("ru", models.FloatField(blank=True, null=True)),
                ("ir", models.FloatField(blank=True, null=True)),
                ("ce", models.FloatField(blank=True, null=True)),
                ("la", models.FloatField(blank=True, null=True)),
                ("nd", models.FloatField(blank=True, null=True)),
                ("y", models.FloatField(blank=True, null=True)),
                ("link", models.CharField(max_length=250)),
                ("doclink", models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                "db_table": "Patent",
            },
        ),
    ]
