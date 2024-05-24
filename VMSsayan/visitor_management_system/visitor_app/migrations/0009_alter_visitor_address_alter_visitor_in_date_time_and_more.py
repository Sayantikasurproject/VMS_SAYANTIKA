# Generated by Django 4.0.3 on 2024-02-28 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitor_app', '0008_alter_visitor_address_alter_visitor_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='address',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='in_date_time',
            field=models.DateTimeField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='staff',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='visitor_app.staff'),
        ),
    ]