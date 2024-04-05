from django.contrib import admin
from IEC.models import *

admin.site.register(Instrumento)
admin.site.register(Ubicacion)
admin.site.register(Sensor)
admin.site.register(SensorMed)
admin.site.register(TorreMet)
admin.site.register(Aerogenerador)
admin.site.register(DescripcionMedi)
admin.site.register(AG_identificacion)
admin.site.register(descripcion_sitio)
admin.site.register(descripcion_equipamiento)
admin.site.register(ag_conf)
admin.site.register(parque_conf)
admin.site.register(parque_eolico)
admin.site.register(aerogenerador_st)