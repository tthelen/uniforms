# Generated by Django 4.0.4 on 2022-04-30 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Verein',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=128)),
                ('lastname', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('membership', models.CharField(choices=[('A', 'Already member'), ('N', 'New membership'), ('L', 'Planned for later')], max_length=1)),
                ('iban', models.CharField(max_length=32, verbose_name='IBAN')),
                ('plan', models.CharField(choices=[('R', 'Reduced (21€)'), ('N', 'Regular (42€)'), ('S', 'Senior (84€)'), ('I', 'Company, silver member (420€)'), ('G', 'Company, gold member (1.764€)')], max_length=1)),
                ('extra_fee', models.IntegerField(verbose_name='Optional: Higher membership fee per year')),
                ('suggested_name', models.CharField(max_length=128, verbose_name='Suggested name for the association')),
                ('notes', models.TextField(blank=True)),
                ('validation_id', models.UUIDField(editable=False)),
                ('validated', models.BooleanField(default=False, editable=False)),
                ('mkdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
