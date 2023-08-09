# Generated by Django 4.2.3 on 2023-07-28 00:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnologias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tecnologia', models.CharField(max_length=50, verbose_name='Nombre de Tecnologia')),
            ],
            options={
                'verbose_name': 'Tecnologia',
                'verbose_name_plural': 'Tecnologias',
            },
        ),
        migrations.CreateModel(
            name='ProyectosDev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de Proyecto')),
                ('link', models.URLField(max_length=100, verbose_name='Link de Proyecto')),
                ('anio_creacion', models.DateField(blank=True, null=True, verbose_name='Año de Terminacion')),
                ('descripcion', models.TextField(verbose_name='Descripcion de Proyecto')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado el')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tecnologia', models.ManyToManyField(to='curriculum.tecnologias', verbose_name='Tecnologias utilizadas')),
            ],
            options={
                'verbose_name': 'Proyecto Desarrollado',
                'verbose_name_plural': 'Proyectos Desarrollados',
            },
        ),
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=100, verbose_name='Habilidad')),
                ('nivel', models.CharField(choices=[('Basico', 'Basico'), ('Intermedio', 'Intermedio'), ('Alto', 'Alto'), ('Avanzado', 'Avanzado')], max_length=100, verbose_name='Nivel')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado el')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
            },
        ),
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra', models.CharField(max_length=100, verbose_name='Extra, Hobbies y demas')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado el')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Extra',
                'verbose_name_plural': 'Extras',
            },
        ),
        migrations.CreateModel(
            name='ExperienciaLb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiencia', models.BooleanField(default=False)),
                ('empresa', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado el')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Experiencia Laboral',
                'verbose_name_plural': 'Experiencias Laborales',
            },
        ),
        migrations.CreateModel(
            name='Estudios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudio', models.CharField(blank=True, choices=[('Primaria', 'Primaria'), ('Secundaria', 'Secundaria'), ('Tecnico', 'Tecnico'), ('Tecnologo', 'Tecnologo'), ('Profesional', 'Profesional'), ('Posgrados', 'Posgrados')], max_length=100, null=True, verbose_name='Tipo de Estudio')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo Obtenido')),
                ('institucion', models.CharField(max_length=100, verbose_name='Institución')),
                ('on_course', models.BooleanField(default=False, verbose_name='En Curso')),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado el')),
                ('id_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Estudio',
                'verbose_name_plural': 'Estudios',
            },
        ),
    ]
