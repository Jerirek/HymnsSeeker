# HymnsSeeker

Una herramienta web para buscar himnos utilizando inteligencia artificial y búsqueda semántica. Desarrollada para ayudar en la selección de cantos en el culto, permitiendo encontrar himnos que compartan un mismo tema.

## Características

- **Búsqueda semántica**: Utiliza embeddings de transformers para encontrar himnos relevantes por tema.
- **Interfaz web simple**: Fácil de usar con un formulario de búsqueda.
- **Filtrado por himnario**: Permite buscar en himnarios específicos o en todos.
- **Vista previa y expansión**: Muestra una vista previa de la letra y permite expandir para ver el himno completo.
- **Modo oscuro**: Soporte para tema claro y oscuro.
- **Responsive**: Funciona en dispositivos móviles y de escritorio.
- **Restricciones de copyright**: Oculta letras completas de himnarios con restricciones de derechos.

## Tecnologías utilizadas

- **Backend**: Flask (Python)
- **IA**: Sentence Transformers (modelo `paraphrase-multilingual-MiniLM-L12-v2`)
- **Embeddings**: Numpy para cálculos de similitud coseno
- **Frontend**: HTML, CSS, JavaScript puro
- **Despliegue**: Gunicorn, compatible con Heroku y Render

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Jerirek/HymnsSeeker.git
   cd HymnsSeeker
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Asegúrate de que el archivo `himnos_embeddings.json` esté presente en el directorio raíz.

4. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

5. Abre tu navegador en `http://localhost:5000`

## Uso

1. Ingresa un tema o palabras clave en el campo de búsqueda (ej: "gracia en la cruz").
2. Selecciona un himnario específico o deja "Todos" para buscar en todos.
3. Haz clic en "Buscar".
4. Revisa los resultados ordenados por relevancia (Alta, Media).
5. Usa "Ver más" para expandir la letra completa (si está disponible).
6. Usa "Cargar más" para ver más resultados.

## Despliegue

### En Render

El proyecto incluye un archivo `render.yaml` para despliegue fácil en Render:

1. Conecta tu repositorio de GitHub a Render.
2. Render detectará automáticamente la configuración.
3. Despliega la aplicación.

### En Heroku

1. Crea una aplicación en Heroku.
2. Conecta tu repositorio de GitHub.
3. El `Procfile` especifica el comando de inicio: `web: gunicorn app:app`
4. Despliega desde GitHub.

## Estructura del proyecto

```
HymnsSeeker/
├── app.py                    # Aplicación principal de Flask
├── himnos_embeddings.json    # Datos de himnos con embeddings
├── requirements.txt          # Dependencias de Python
├── Procfile                  # Configuración para Heroku
├── render.yaml               # Configuración para Render
├── templates/
│   ├── index.html            # Página principal del buscador
│   └── acerca.html           # Página "Acerca de"
└── README.md                 # Este archivo
```

## Notas importantes

- La herramienta sugiere himnos basados en similitud semántica, pero la selección final debe hacerse con discernimiento considerando el contexto del culto.
- Algunos himnarios tienen restricciones de copyright, por lo que sus letras completas no se muestran.
- Los embeddings se generan previamente y se almacenan en `himnos_embeddings.json` para optimizar el rendimiento.

## Contribuir

Si deseas contribuir al proyecto:

1. Fork el repositorio.
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`).
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`).
4. Push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Autor

Desarrollado por [Jerirek](https://github.com/Jerirek)