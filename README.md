# Google Calendar API Credentials Setup

This project uses the Google Calendar API to automatically generate events. To enable this functionality, you must set up a Google Cloud project and generate a credentials.json file with desktop application access.

## 1. Create a project in Google Cloud Console

Go to Google Cloud Console:
https://developers.google.com/workspace/guides/create-project

Sign in with your Google account.

Create a new project and assign a name.

Confirm the project creation.

## 2. Enable the Google Calendar API

Open the left sidebar and go to “APIs & Services”.

Select “Library”.

Search for “Google Calendar API”.

Select “Enable”.

## 3. Configure the OAuth consent screen

In “APIs & Services”, select “OAuth consent screen”.

Choose the “External” user type.

Complete the required fields: application name, support email, and domain if applicable.

Save the configuration.

## 4. Create OAuth credentials

Open “APIs & Services”.

Select “Credentials”.

Select “Create Credentials”.

Choose “OAuth Client ID”.

Set the application type to “Desktop App”.

Download the generated JSON file.

## 5. Prepare the credentials file

Rename the downloaded file to credentials.json.

Move it to the root folder of your project where your main script or notebook is located.

Do not modify the content of the file.

After the first successful authentication, a token.json file will be automatically generated.

## 6. Expected project structure
your_project/
│
├── metodos/
│   ├── funcion_autenticacion.py
|   ├── validations.py
│   └── funcion_generar_bloques.py
├── CrearCorreo.ipynb
├── .env
├── .env.example
├── credentials.json   (archivo descargado)
├── README.md
└── token.json         (se crea automáticamente)

## 7. Important Notes

Never upload credentials.json or token.json to a public repository.

Delete token.json if you need to authenticate with another Google account.

If credentials.json is missing or misplaced, you will encounter a FileNotFoundError.



# Configuración de credenciales para Google Calendar API

Este proyecto utiliza la API de Google Calendar para crear eventos automáticamente. Para que funcione correctamente, es necesario configurar un proyecto en Google Cloud y generar un archivo credentials.json con permisos de aplicación de escritorio.

## 1. Crear un proyecto en Google Cloud Console

Accede a Google Cloud Console:
https://developers.google.com/workspace/guides/create-project?hl=es-419

Inicia sesión con tu cuenta de Google.

Crea un proyecto nuevo y asígnale un nombre.

Confirma la creación del proyecto.

## 2. Habilitar la Google Calendar API

En el panel izquierdo, ubica la sección “APIs y servicios”.

Selecciona “Biblioteca de APIs”.

Busca “Google Calendar API”.

Selecciona “Habilitar”.

## 3. Configurar la pantalla de consentimiento OAuth

En “APIs y servicios”, selecciona “Pantalla de consentimiento OAuth”.

Elige el tipo de usuario “Externo”.

Configura los datos mínimos requeridos: nombre de la aplicación, correo de soporte y dominio si aplica.

Guarda la configuración.

## 4. Crear credenciales OAuth

Ve a “APIs y servicios”.

Selecciona “Credenciales”.

Elige “Crear credenciales”.

Selecciona “ID de cliente OAuth”.

En tipo de aplicación, selecciona “Aplicación de escritorio”.

Confirma y descarga el archivo JSON generado.

## 5. Preparar el archivo de credenciales

Cambia el nombre del archivo descargado a credentials.json.

Colócalo en la carpeta raíz de tu proyecto, donde esté tu script principal o notebook.

No modifiques el contenido del archivo.

Una vez que se ejecute la autenticación por primera vez, se generará automáticamente un archivo token.json.


## 6. Archivos esperados en el proyecto
tu_proyecto/
│
├── metodos/
│   ├── funcion_autenticacion.py
|   ├── validations.py
│   └── funcion_generar_bloques.py
├── CrearCorreo.ipynb
├── .env
├── .env.example
├── credentials.json   (archivo descargado)
├── README.md
└── token.json         (se crea automáticamente)

## 7. Notas importantes

No compartas ni subas credentials.json ni token.json a ningún repositorio público.

Si cambias de cuenta, elimina token.json para forzar una nueva autenticación.

Si el archivo credentials.json no está en la ubicación correcta, aparecerá un error FileNotFoundError.


