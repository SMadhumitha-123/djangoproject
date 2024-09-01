import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='id',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='user',
        ),
        
        migrations.AddField(
            model_name='employees',
            name='name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]