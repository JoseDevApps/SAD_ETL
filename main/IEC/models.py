from django.db import models

class Instrumento(models.Model):
    instrumento = models.CharField(max_length=200)
    variable = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.instrumento

class Ubicacion(models.Model):
    latitud = models.FloatField(blank=True)
    longitud = models.FloatField(blank=True)
    altura = models.FloatField(blank=True)
    direccion = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.direccion

class Sensor(models.Model):
    fabricante = models.CharField(max_length= 200)
    especificaciones = models.FileField(upload_to='especificaciones', blank=True)
    instrumentoID= models.ForeignKey(Instrumento, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.fabricante

class SensorMed(models.Model):
    sensorID = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=False)
    mean = models.FloatField()
    max = models.FloatField(blank=True)
    min = models.FloatField(blank=True)
    std = models.FloatField(blank=True)
    unidad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    def __str__(self) -> str:
        return str(self.sensorID)

class TorreMet(models.Model):
    SensoresID = models.ManyToManyField(Sensor)
    ubicacionID = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, verbose_name="Descripcion Torre")
    def __str__(self) -> str:
        return str(self.SensoresID)

class parque_eolico(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self) -> str:
        return str(self.nombre)

class Aerogenerador(models.Model):
    nombre = models.CharField(max_length=200)
    parque = models.ForeignKey(parque_eolico, on_delete=models.CASCADE)
    potencia_nominal = models.FloatField()
    diametro_rotor = models.FloatField()
    altura_buje = models.FloatField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    def __str__(self) -> str:
        return self.nombre

class DescripcionMedi(models.Model):
    aerogeneradorID= models.ForeignKey(Aerogenerador, on_delete=models.CASCADE)
    scatter_power = models.FileField(upload_to='AG_POWER', blank=True)
    scatter_wind = models.FileField(upload_to='AG_WIND', blank=True)
    scatter_turbulence = models.FileField(upload_to='AG_TUR', blank=True)
    special_data = models.FileField(upload_to='AG_SPECIAL', blank=True)
    scatter_rot_PA = models.FileField(upload_to='AG_PITCH', blank=True)
    status_signals = models.FileField(upload_to='AG_SIGNALS', blank=True)
    scatter_air_den = models.FileField(upload_to='AG_AIR', blank=True)
    scatter_wind_shear = models.FileField(upload_to='AG_SHEAR', blank=True)
    scatter_wind_shear_TC = models.FileField(upload_to='AG_SHEAR_TC', blank=True)
    wind_shear_correction = models.FloatField(blank=True)
    avg_air_density = models.FloatField(blank=True)
    def __str__(self) -> str:
        return str(self.aerogeneradorID)

class AG_identificacion(models.Model):
    aerogeneradorID = models.ForeignKey(Aerogenerador, on_delete=models.CASCADE)
    fabricante = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    numeroSerie = models.CharField(max_length=200)
    anoProduccion = models.DateTimeField(blank=True)
    def __str__(self) -> str:
        return self.numeroSerie

class descripcion_sitio(models.Model):
    aerogeneradorID = models.ForeignKey(Aerogenerador, on_delete=models.CASCADE)
    fotografias = models.FileField(upload_to='AG_SITIO', blank=True)
    mapa = models.FileField(upload_to='AG_MAPA', blank=True)
    limites = models.FileField(upload_to='AG_LIMITES', blank=True)
    calibracion = models.FileField(upload_to='AG_CALIBRACION', blank=True)
    ubicacion = models.FileField(upload_to='AG_UBICACION', blank=True)
    def __str__(self) -> str:
        return str(self.aerogeneradorID)

class descripcion_equipamiento(models.Model):
    aerogeneradorID = models.ForeignKey(Aerogenerador, on_delete=models.CASCADE)
    esquema_met = models.FileField(upload_to='AG_MET', blank=True)
    documentacion = models.FileField(upload_to='AG_DOC', blank=True)
    def __str__(self) -> str:
        return str(self.aerogeneradorID)
    
# Serie de tiempos
class aerogenerador_st(models.Model):
    ag_ID = models.ForeignKey(Aerogenerador, on_delete=models.CASCADE)
    time = models.DateTimeField(blank=True)
    viento_avg = models.FloatField(blank=True)
    viento_max = models.FloatField(blank=True)
    viento_min = models.FloatField(blank=True)
    viento_std = models.FloatField(blank=True)
    p_avg = models.FloatField(blank=True)
    p_max = models.FloatField(blank=True)
    p_min = models.FloatField(blank=True)
    p_std = models.FloatField(blank=True)
    posicion = models.FloatField(blank=True)
    posicion_min = models.FloatField(blank=True)
    posicion_max = models.FloatField(blank=True)
    posicion_std = models.FloatField(blank=True)
    pteo_avg = models.FloatField(blank=True)
    pteo_min = models.FloatField(blank=True)
    pteo_max = models.FloatField(blank=True)
    pteo_std = models.FloatField(blank=True)

    def __str__(self) -> str:
        return str(self.ag_ID)

class NonStrippingCharField(models.CharField):
    def formfield(self, **kwargs):
        kwargs['strip'] = False
        return super(NonStrippingCharField, self).formfield(**kwargs)

class ag_conf(models.Model, NonStrippingCharField):
    nombre = models.CharField(max_length=200)
    aerogenerador = models.ForeignKey(Aerogenerador, on_delete=models.CASCADE)
    # Velocidad de viento a la altura del buje del aerogenerador
    ws_avg = NonStrippingCharField(max_length=200)
    ws_min = NonStrippingCharField(max_length=200, blank=True)
    ws_max = NonStrippingCharField(max_length=200, blank=True)
    ws_std = NonStrippingCharField(max_length=200, blank=True)
    # Direccion de viento a la altura del buje del aerogenerador
    wd_avg = NonStrippingCharField(max_length=200)
    wd_min = NonStrippingCharField(max_length=200, blank=True)
    wd_max = NonStrippingCharField(max_length=200, blank=True)
    wd_std = NonStrippingCharField(max_length=200, blank=True)
    # Potencia activa generada por el aerogenerador
    pins_avg = NonStrippingCharField(max_length=200)
    pins_min = NonStrippingCharField(max_length=200, blank=True)
    pins_max = NonStrippingCharField(max_length=200, blank=True)
    pins_std = NonStrippingCharField(max_length=200, blank=True)
    # Potencia teorica proveniente por el fabricante
    p_teo_avg = NonStrippingCharField(max_length=200)
    p_teo_min = NonStrippingCharField(max_length=200, blank=True)
    p_teo_max = NonStrippingCharField(max_length=200, blank=True)
    p_teo_std = NonStrippingCharField(max_length=200, blank=True)
    # Columnas de identificacion
    date = NonStrippingCharField(max_length=200, blank=True)
    no_serie = NonStrippingCharField(max_length=200, blank=True)
    label_col = models.BooleanField(default=True,blank=True)

    def __str__(self) -> str:
        return str(self.nombre)
    
class parque_conf(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200,blank=True)
    aerogeneradores = models.ManyToManyField(ag_conf)
    def __str__(self) -> str:
        return str(self.nombre)