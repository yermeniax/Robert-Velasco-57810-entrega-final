from django.db import models

# Modelo para el Equipo
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    estadio = models.CharField(max_length=100)
    fundacion = models.DateField()  # Fecha de fundación del equipo
    
    def __str__(self):
        return self.nombre

# Modelo para el Profesor (DT)
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    categoria = models.CharField(max_length=100)  # Campo para la categoría que maneja el profesor
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

# Modelo para el Jugador
class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)  # Relación con Equipo
    posicion = models.CharField(max_length=50)
    numero_camiseta = models.PositiveIntegerField()
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)  # Campo para el DNI
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True)  # Relación con Profesor

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Pago(models.Model):
    TIPO_PAGO_CHOICES = [
        ('M', 'Mensualidad'),
        ('I', 'Inscripción'),
    ]
    MES_CHOICES = [
        ('01', 'Enero'),
        ('02', 'Febrero'),
        ('03', 'Marzo'),
        ('04', 'Abril'),
        ('05', 'Mayo'),
        ('06', 'Junio'),
        ('07', 'Julio'),
        ('08', 'Agosto'),
        ('09', 'Septiembre'),
        ('10', 'Octubre'),
        ('11', 'Noviembre'),
        ('12', 'Diciembre'),
    ]
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    tipo_pago = models.CharField(max_length=1, choices=TIPO_PAGO_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    mes = models.CharField(max_length=2, choices=MES_CHOICES, blank=True, null=True)

    def __str__(self):
        return f'{self.jugador} - {self.get_tipo_pago_display()} - {self.fecha_pago}'



