# Generated by Django 4.0.4 on 2022-05-31 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cogscinet', '0004_alter_verein_membership_alter_verein_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='verein',
            name='company',
            field=models.CharField(blank=True, max_length=128, verbose_name='Company name (if applicable)'),
        ),
        migrations.AlterField(
            model_name='verein',
            name='plan',
            field=models.CharField(choices=[('R', 'Reduced (21€)'), ('N', 'Regular (42€)'), ('S', 'Senior (84€)'), ('I', 'Company, silver member (420€)'), ('G', 'Company, gold member (42 * 42€ = 1.764€)'), ('L', 'Individual amount > 84€ for individuals, > 1764€ for companys, given below)')], max_length=1, verbose_name='Membership type (non-binding, has to be declared after final decision)'),
        ),
    ]
