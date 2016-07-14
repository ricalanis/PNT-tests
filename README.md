# PNT-Tests

Este repositorio busca agrupar las pruebas que debe de responder el SNT con ayuda de Selenium. La idea es que cada prueba que se corra, y si el driver funciona, se reporte el resultado de la prueba automáticamente a un repositorio de resultados en un google spreadsheet.

####  Contenido:
- *tests.py* : Definiciones de los tests a realizar en la plataforma, y por lo tanto, las características a probar de la plataforma de transparencia.
- *run.py*: Corren los tests y reportan resultados a un Google Spreadsheet de resultados compartidos.
- *gsheets.py*: Tools para conectarse a gsheets. ¿Porqué Gsheets? Para que todos hagamos pruebas y unifiquemos resultados a la larga (Más info en la wiki)
- *tools.py*: para herramientas que puedan compartir los scripts de arriba.

### Requisitos

```
selenium
Driver de Chrome para Selenium
```

### Como Contribuir

Pull requests, Issues con comentarios o preguntas no solo bien recibidos, es lo mejor que me va a pasarr en el día.
