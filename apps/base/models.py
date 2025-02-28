import uuid

from django.db import models

class LabUUID(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class Base(models.Model):
    nome = models.CharField('Nome', max_length=254, db_index=True)
    descricao = models.CharField(max_length=254, null=True, blank=True)
    ativo = models.BooleanField(default=False)

    class Meta:
        abstract = True