from django.db import models
from django.utils.crypto import get_random_string

from apps.base.models import *
from apps.colaborador.models import *


class Departamento(LabUUID, Base):

    class Meta:
        verbose_name = 'Departamento'

    def __str__(self):
        return self.nome

