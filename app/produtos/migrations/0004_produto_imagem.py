# Generated by Django 5.1.3 on 2024-12-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_alter_produto_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produtos/'),
        ),
    ]