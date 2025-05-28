______________________________________
LEEME.
______________________________________
ARCHIVOS:
paginaweb:
Codigo fuente de nuestra Aplicación.
Nucleo de la aplicación.

venv:
Entorno virtual de nuestra Aplicación.

db.sqlite3:
Base de datos integrada de Django.

manage.py:
Nos ayuda a poder ejecutar comandos administrativos, por ejemplo, ejecutar un servidor desarrollo (runserver).

requirements.txt:
Dependencias/Librerias del proyecto.
______________________________________
// CLONAR EL REPOSITORIO DESDE 0.

(Posterior a la instalación de GIT)

* Configurar Git:
git config --global user.name "Tu Nombre"
git config --global user.email "tunombre@ejemplo.com"

* Clonar repositorio:
git clone https://github.com/b-cayuela-once/Ferremas.git
______________________________________
COMANDOS ENTORNO:
// DESPUES DE CLONAR EL REPOSITORIO.

* Crear entorno virtual:
python -m venv venv

* Activar entorno virtual:
.\venv\Scripts\Activate.ps1

* Instalar dependencias (requirements.txt)
pip install -r requirements.txt

* Este comando crea los requerimientos/librerias actuales del proyecto.
pip freeze > requirements.txt

______________________________________
COMANDOS SERVIDOR DE DESARROLLO (Django):

* Arrancar servidor:
python manage.py runserver

* Crear Aplicación:
python manage.py startapp "nombre app"

* Cargar datos: (guarda regiones, comunas, tipo de usuarios en la base de datos)
python cargar_datos.py

______________________________________
COMANDOS DE GITHUB:
* Estado del repositorio:
git status

* Agregar todos los archivos modificados:
git add .

* Comitear:
git commit -m "Actualizado HTML con nuevos cambios"

* Pushear:
git push

______________________________________
PASO A PASO:
* Crear directorio (carpeta donde clonaste el repositorio)

* Clonar repositorio:
git clone https://github.com/b-cayuela-once/Ferremas.git

* Actualizar pip
python.exe -m pip install --upgrade pip

* Crear entorno virtual:
python -m venv venv

* Activar entorno virtual:
.\venv\Scripts\Activate.ps1

* Instalar dependencias (requirements.txt)
pip install -r requirements.txt

* Realizar migraciones pendientes.
python manage.py makemigrations

* Migrar:
python manage.py migrate

* Subir datos a la base de datos.
python cargar_datos.py