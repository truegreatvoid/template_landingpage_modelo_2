import datetime as dt
from storages.backends.s3boto3 import S3Boto3Storage

from django.db import models
from django.utils.crypto import get_random_string

from apps.base.models import *
from apps.colaborador.models import *


def build_upload_path(base_path, filename, created=None):
    created = created or dt.datetime.now()
    return f"{base_path}/{created.year}/{filename}"

def colaboradores_upload_path(instance, filename):
    return build_upload_path(
        base_path="eas/images/colaboradores/",
        filename=filename
    )

def eventos_upload_path(instance, filename):
    return build_upload_path(
        base_path="eas/images/eventos/",
        filename=filename
    )

def eventos_upload_path(instance, filename):
    return build_upload_path(
        base_path="eas/images/eventos/",
        filename=filename
    )

def oferecemos_upload_path(instance, filename):
    return build_upload_path(
        base_path="eas/images/oferecemos/",
        filename=filename
    )

def programas_upload_path(instance, filename):
    return build_upload_path(
        base_path="eas/images/programas/",
        filename=filename
    )

def eas_upload_path(instance, filename):
    return build_upload_path(
        base_path="eas/images/base/",
        filename=filename
    )

class LandingPage(LabUUID, Base):
    principal_texto = models.CharField(max_length=254, null=True, blank=True)
    image = models.FileField('Imagem', storage=S3Boto3Storage(), upload_to=eas_upload_path, blank=True, null=True)
    video = models.CharField(max_length=200, null=True, blank=True)
    aniversario = models.DateField('Aniversário', blank=True, null=True)

    endereco = models.CharField('Endereço', max_length=200, blank=True)
    complemento = models.CharField('Complemento', max_length=100, blank=True)
    bairro = models.CharField('Bairro', max_length=100, blank=True)
    cidade = models.CharField('Cidade', max_length=100, blank=True)
    cep = models.CharField('CEP', max_length=12, blank=True)
    uf = models.CharField('UF', max_length=2, default='PE')

    contato = models.CharField(max_length=30, blank=True, null=True)

    email = models.EmailField('E-mail', max_length=254, blank=True, null=True, unique=True, db_index=True)

    facebook = models.CharField(max_length=354, blank=True, null=True)
    x = models.CharField(max_length=354, blank=True, null=True)
    instagram = models.CharField(max_length=354, blank=True, null=True)
    linkedin = models.CharField(max_length=354, blank=True, null=True)

    missao_valor_titulo = models.CharField(max_length=254, null=True, blank=True)
    missao_valor_complemento = models.TextField(blank=True, default='')
    missao_valor_item_1 = models.CharField(max_length=254, null=True, blank=True)
    missao_valor_item_2 = models.CharField(max_length=254, null=True, blank=True)
    missao_valor_item_3 = models.CharField(max_length=254, null=True, blank=True)
    missao_valor_item_4 = models.CharField(max_length=254, null=True, blank=True)
    missao_valor_item_5 = models.CharField(max_length=254, null=True, blank=True)
    missao_valor_item_6 = models.CharField(max_length=254, null=True, blank=True)

    funcionamento_seg = models.CharField(max_length=254, null=True, blank=True)
    funcionamento_ter = models.CharField(max_length=254, null=True, blank=True)
    funcionamento_qua = models.CharField(max_length=254, null=True, blank=True)
    funcionamento_qui = models.CharField(max_length=254, null=True, blank=True)
    funcionamento_sex = models.CharField(max_length=254, null=True, blank=True)
    funcionamento_sab = models.CharField(max_length=254, null=True, blank=True)
    funcionamento_dom = models.CharField(max_length=254, null=True, blank=True)

    footer_descricao = models.TextField(blank=True, default='')
    ano = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Landing Page'

    def __str__(self):
        return self.nome


class Programas(LabUUID, Base):
    image = models.FileField('Imagem', storage=S3Boto3Storage(), upload_to=programas_upload_path, blank=True, null=True)
    descricao_1 = models.CharField(max_length=254, null=True, blank=True)
    descricao_2 = models.CharField(max_length=254, null=True, blank=True)
    descricao_2 = models.CharField(max_length=254, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Programas'

    def __str__(self):
        return self.nome
    
class Oferecemos(LabUUID, Base):
    image = models.FileField('Imagem', storage=S3Boto3Storage(), upload_to=oferecemos_upload_path, blank=True, null=True)
    descricao_1 = models.CharField(max_length=254, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Oferecemos'

    def __str__(self):
        return self.nome
    
class Eventos(LabUUID, Base):
    image = models.FileField('Imagem', storage=S3Boto3Storage(), upload_to=eventos_upload_path, blank=True, null=True)
    evento = models.DateField(null=True, blank=True)
    horario_inicio = models.TimeField('Horário Início', null=True, blank=True)
    horario_fim = models.TimeField('Horário Fim', null=True, blank=True)
    localizacao = models.CharField('Localização', max_length=254, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Eventos'

    def __str__(self):
        return self.nome
    

class Colaboradores(LabUUID, Base):
    image = models.FileField('Imagem', storage=S3Boto3Storage(), upload_to=colaboradores_upload_path, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Colaboradores'

    def __str__(self):
        return self.nome