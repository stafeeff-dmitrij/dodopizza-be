# Generated by Django 5.1.4 on 2025-03-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: list[tuple[str, str]] = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessByIP',
            fields=[
                ('ip', models.GenericIPAddressField(primary_key=True, serialize=False, verbose_name='ip адрес')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('comment', models.TextField(verbose_name='комментарий')),
                ('period', models.CharField(blank=True, choices=[('10m', '10 минут'), ('30m', '30 минут'), ('1h', '1 час'), ('2h', '2 часа'), ('6h', '6 часов'), (
                    '12h', '12 часов'), ('1d', '1 день'), ('1w', '1 неделя'), ('1M', '1 месяц'), ('always', 'Всегда')], null=True, verbose_name='период доступа')),
                ('access_to', models.DateTimeField(blank=True, null=True, verbose_name='доступ до')),
            ],
            options={
                'verbose_name': 'Доступ по IP',
                'verbose_name_plural': 'Доступ по IP',
                'db_table': 'access_by_ip',
            },
        ),
    ]
