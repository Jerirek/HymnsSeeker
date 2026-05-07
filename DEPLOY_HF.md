# Guía Rápida: Desplegar en Hugging Face Spaces

## 1. Crear Space en HF
- Ve a https://huggingface.co/spaces
- "Create new Space"
- **Nombre**: himnosseeker (o el que quieras)
- **SDK**: Docker
- **Hardware**: CPU (gratuito)

## 2. Clonar el repositorio de HF
```bash
git clone https://huggingface.co/spaces/[tu-usuario]/himnosseeker
cd himnosseeker
```

## 3. Copiar archivos
Copia estos archivos al directorio:
- `app.py`
- `requirements.txt`
- `himnos_embeddings.json`
- `Dockerfile`
- `.dockerignore`
- `templates/` (carpeta completa)

## 4. Push a Hugging Face
```bash
git add .
git commit -m "Despliegue de HymnsSeeker"
git push
```

## 5. Esperar construcción
- HF Spaces construirá automáticamente la imagen Docker
- Verás el progreso en la página del Space
- Cuando esté listo, tu app estará disponible en: https://huggingface.co/spaces/[tu-usuario]/himnosseeker

## Ventajas de esta configuración:
✅ Gratis y sin límites de tiempo
✅ Más estable que Render
✅ URL permanente
✅ Tu interfaz original intacta
✅ Actualizaciones automáticas al hacer push
