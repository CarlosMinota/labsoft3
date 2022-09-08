# Generated by Django 2.2.5 on 2022-05-07 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controlProyecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carrito',
            options={'ordering': ['id_carrito'], 'verbose_name': 'Carrito', 'verbose_name_plural': 'Carritos'},
        ),
        migrations.AlterModelOptions(
            name='ciudad',
            options={'ordering': ['nombre_ciudad'], 'verbose_name': 'Ciudad', 'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['nombre_cliente'], 'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='compra',
            options={'ordering': ['id_compra'], 'verbose_name': 'Compra', 'verbose_name_plural': 'Compras'},
        ),
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['nombre_departamento'], 'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamentos'},
        ),
        migrations.AlterModelOptions(
            name='descuento',
            options={'ordering': ['id_descuento'], 'verbose_name': 'Descuento', 'verbose_name_plural': 'Descuentos'},
        ),
        migrations.AlterModelOptions(
            name='envio',
            options={'ordering': ['id_envio'], 'verbose_name': 'Envio', 'verbose_name_plural': 'Envios'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['nombre_producto'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='nombreCliente',
            new_name='nombre_cliente',
        ),
        migrations.AlterField(
            model_name='carrito',
            name='compra_id_compra',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='controlProyecto.Compra'),
        ),
        migrations.AlterField(
            model_name='envio',
            name='compra_id_compra',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='controlProyecto.Compra'),
        ),
    ]
