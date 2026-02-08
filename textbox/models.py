from django.db import models

class Textbox(models.Model):

    content = models.TextField(null=False, unique=True)
    code = models.CharField(max_length=10, null=False)
    
    class Meta:
        db_table = "textbox"