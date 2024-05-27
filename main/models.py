from django.db import models

# Create your models here.
from django.db import models


class Dengue(models.Model):
    fecha_actualizacion = models.TextField(db_column='FECHA_ACTUALIZACION', blank=True, null=True)  # Field name made lowercase.
    id_registro = models.IntegerField(db_column='ID_REGISTRO', blank=True, null=True)  # Field name made lowercase.
    sexo = models.IntegerField(db_column='SEXO', blank=True, null=True)  # Field name made lowercase.
    edad_anos = models.IntegerField(db_column='EDAD_ANOS', blank=True, null=True)  # Field name made lowercase.
    entidad_res = models.IntegerField(db_column='ENTIDAD_RES', blank=True, null=True)  # Field name made lowercase.
    municipio_res = models.IntegerField(db_column='MUNICIPIO_RES', blank=True, null=True)  # Field name made lowercase.
    habla_lengua_indig = models.IntegerField(db_column='HABLA_LENGUA_INDIG', blank=True, null=True)  # Field name made lowercase.
    indigena = models.IntegerField(db_column='INDIGENA', blank=True, null=True)  # Field name made lowercase.
    entidad_um_notif = models.IntegerField(db_column='ENTIDAD_UM_NOTIF', blank=True, null=True)  # Field name made lowercase.
    municipio_um_notif = models.IntegerField(db_column='MUNICIPIO_UM_NOTIF', blank=True, null=True)  # Field name made lowercase.
    institucion_um_notif = models.IntegerField(db_column='INSTITUCION_UM_NOTIF', blank=True, null=True)  # Field name made lowercase.
    fecha_sign_sintomas = models.TextField(db_column='FECHA_SIGN_SINTOMAS', blank=True, null=True)  # Field name made lowercase.
    tipo_paciente = models.IntegerField(db_column='TIPO_PACIENTE', blank=True, null=True)  # Field name made lowercase.
    hemorragicos = models.IntegerField(db_column='HEMORRAGICOS', blank=True, null=True)  # Field name made lowercase.
    diabetes = models.IntegerField(db_column='DIABETES', blank=True, null=True)  # Field name made lowercase.
    hipertension = models.IntegerField(db_column='HIPERTENSION', blank=True, null=True)  # Field name made lowercase.
    enfermedad_ulc_peptica = models.IntegerField(db_column='ENFERMEDAD_ULC_PEPTICA', blank=True, null=True)  # Field name made lowercase.
    enfermedad_renal = models.IntegerField(db_column='ENFERMEDAD_RENAL', blank=True, null=True)  # Field name made lowercase.
    inmunosupr = models.IntegerField(db_column='INMUNOSUPR', blank=True, null=True)  # Field name made lowercase.
    cirrosis_hepatica = models.IntegerField(db_column='CIRROSIS_HEPATICA', blank=True, null=True)  # Field name made lowercase.
    embarazo = models.IntegerField(db_column='EMBARAZO', blank=True, null=True)  # Field name made lowercase.
    defuncion = models.IntegerField(db_column='DEFUNCION', blank=True, null=True)  # Field name made lowercase.
    dictamen = models.IntegerField(db_column='DICTAMEN', blank=True, null=True)  # Field name made lowercase.
    toma_muestra = models.IntegerField(db_column='TOMA_MUESTRA', blank=True, null=True)  # Field name made lowercase.
    resultado_pcr = models.IntegerField(db_column='RESULTADO_PCR', blank=True, null=True)  # Field name made lowercase.
    estatus_caso = models.IntegerField(db_column='ESTATUS_CASO', blank=True, null=True)  # Field name made lowercase.
    entidad_asig = models.IntegerField(db_column='ENTIDAD_ASIG', blank=True, null=True)  # Field name made lowercase.
    municipio_asig = models.IntegerField(db_column='MUNICIPIO_ASIG', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        fila = "Titulo: " + str(self.id_registro) + " - " + "Estado :" + str(self.entidad_res)
        return fila
    def ObtenerAtributos(self):
        #atributos = ["fecha_actualizacion","sexo","edad"]
        atributos = ["Hermosillo", 'Nogales', 'Obregon', 'Navojoa']
        return atributos
    class Meta:
        managed = False
        db_table = 'dengue_abierto'