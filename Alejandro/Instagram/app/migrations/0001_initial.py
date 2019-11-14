# Generated by Django 2.2.7 on 2019-11-14 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='app/publicaciones/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='app/usuarios/')),
            ],
        ),
        migrations.CreateModel(
            name='PubSave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pub')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
        migrations.CreateModel(
            name='PubLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pub')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
        migrations.CreateModel(
            name='PubComentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField()),
                ('id_publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pub')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
        migrations.AddField(
            model_name='pub',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='app/historias/')),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_usuario', to='app.User')),
                ('id_usuario_seguido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_usuario_seguido', to='app.User')),
            ],
        ),
    ]