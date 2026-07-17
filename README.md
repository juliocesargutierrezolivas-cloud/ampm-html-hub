# AMPM Operations Hub

Repositorio público para publicar herramientas HTML operativas y alimentarlas con archivos Excel almacenados en GitHub.

## Aplicación disponible

- **Control Ejecutivo de Gastos**: mantenimiento, fletes, suministro, viáticos y energía.
- Histórico incluido: enero a julio de 2026.
- Julio 2026 se abre como periodo predeterminado.

## Estructura

```text
apps/gastos/                 Dashboard de gastos
data/gastos/periodos/        Excel por periodo
config/apps.json             Catálogo del portal
tools/build_manifest.py      Genera el catálogo de periodos
.github/workflows/           Publicación automática en GitHub Pages
```

## Nombres obligatorios por periodo

Cada carpeta mensual debe llamarse `AAAA-MM`, por ejemplo `2026-08`, y utilizar:

```text
master.xlsx
maintenance.xlsx
freight.xlsx
supply_travel.xlsx
energy.xlsx                 # opcional
```

## Actualizar un mes existente

1. Abra `data/gastos/periodos/AAAA-MM/`.
2. Reemplace el Excel correspondiente conservando exactamente su nombre.
3. Confirme el cambio con un commit.
4. GitHub Actions genera el manifiesto y vuelve a publicar el sitio.
5. El mismo enlace del dashboard mostrará la versión nueva. Si permanece abierto, revisa cambios cada cinco minutos.

## Agregar un nuevo mes

1. Duplique la carpeta del mes anterior.
2. Renómbrela con el nuevo periodo, por ejemplo `2026-08`.
3. Reemplace los cuatro archivos obligatorios y, cuando exista, `energy.xlsx`.
4. Haga commit y push.
5. El selector de periodos se actualiza automáticamente en el despliegue.

## Publicar en GitHub Pages

1. Cree un repositorio público.
2. Suba todo el contenido de esta carpeta a la rama `main`.
3. En **Settings → Pages**, seleccione **Source: GitHub Actions**.
4. El workflow `Deploy GitHub Pages` publicará el portal.

## Seguridad

Este repositorio y sus Excel serán públicos. No incluya información personal, bancaria, credenciales, API keys ni datos no autorizados para publicación.

## Prueba local

No abra los HTML con doble clic, porque `fetch()` necesita un servidor web.

```bash
python -m http.server 8000
```

Después abra `http://localhost:8000/`.
