from django.db import models

class Textbox(models.Model):

    code = models.CharField(max_length=10, null=False, unique=True)
    content = models.TextField(null=True)

    class Meta:
        db_table = "textbox"