from rest_framework import serializers
from .models import UsuarioModel
class RegistroSerializer(serializers.ModelSerializer):

    def save(self):
        usuarioNombre = self.validated_data.get('usuarioNombre')
        usuarioApellido = self.validated_data.get('usuarioApellido')
        usuarioCorreo = self.validated_data.get('usuarioCorreo')
        usuarioTipo = self.validated_data.get('usuarioTipo')
        password = self.validated_data.get('password')

        nuevoUsuario = UsuarioModel(usuarioNombre=usuarioNombre, usuarioApellido=usuarioApellido,
                                    usuarioCorreo=usuarioCorreo, usuarioTipo=usuarioTipo)

        nuevoUsuario.set_password(password)

        nuevoUsuario.save()
        return nuevoUsuario

    class Meta:
        model = UsuarioModel
        # fields = '__all__'
        exclude = ['groups', 'user_permissions', 'is_superuser',
                   'last_login', 'is_active', 'is_staff']
        # forma 2
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }