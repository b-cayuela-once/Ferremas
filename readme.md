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

