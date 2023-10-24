from django.db import models
# from django.db import migrations

class Member(models.Model):
    First_name=models.CharField(max_length=255)
    Last_name=models.CharField(max_length=255)
    Phone=models.IntegerField(null=True)
    Date_added=models.DateField(null=True)

# class Migration(migrations.Migration):
#     initial=True
    # dependencies=[

    # ]
    # operations=[
    #     migrations.CreateModel(
    #         name='Member',
    #         fields=[
    #             ('id',models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    #             ('First_name', models.CharField(max_length=255)),
    #             ('Last_name',models.CharField(max_length=255)),
    #         ],

    #     ),
    # ]
