from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    telefono = models.CharField(max_length=20)
    fecnac = models.DateField()

    class Meta:
        permissions = [
            ("can_access_special_feature", "Can access special feature"),
            # Otros permisos personalizados
        ]

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('Permisos de usuario'),
        blank=True,
        related_name='permisos_usario_personalizado'  # Cambiar a un nombre único
    )
    
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('Grupos'),
        blank=True,
        related_name='grupos_usuario_personalizado'  # Cambiar a un nombre único
    )

    @property
    def edad(self):
        today = date.today()
        age = today.year - self.fecnac.year - ((today.month, today.day) < (self.fecnac.month, self.fecnac.day))
        return age
