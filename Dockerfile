# Usa una imagen base de Python
FROM python:3.9-alpine3.17

# Configura variables de entorno para Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crear un usuario no root y establecer permisos de trabaj
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Establece el directorio de trabajo en /code
WORKDIR /code

# Copia solo los archivos necesarios para instalar las dependencias
COPY requirements.txt /code/

# Instala las dependencias del proyecto especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia los archivos y directorios específicos del proyecto
COPY manage.py /code/
COPY auction_app /code/auction_app
COPY drf /code/drf

# Cambia la propiedad de los archivos copiados al usuario no root
RUN chown -R appuser:appgroup /code

# Cambia al usuario no root
USER appuser

# Expone el puerto 8000 para que pueda ser accesible desde fuera del contenedor
EXPOSE 8000

# Define el comando para arrancar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
