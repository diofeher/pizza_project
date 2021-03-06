# Generated by Django 2.1.4 on 2018-12-03 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.CharField(max_length=32)),
                ('customer_address', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('size', models.IntegerField(choices=[(30, '30cm'), (50, '50cm')], default=30)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Pizza'),
        ),
    ]
