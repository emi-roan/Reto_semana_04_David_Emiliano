Arquitectura Modular para Gestión de Inventarios Desarrollador

Alumno: David Emiliano Rodríguez Anduiza

Carrera: Ciencia de Datos - ESCOM (IPN)

Introducción y Paradigma de Programación Este proyecto no es solo un script lineal; es una aplicación diseñada bajo el paradigma de Programación Orientada a Objetos (POO) y Modularización. El objetivo principal fue separar las responsabilidades del sistema para cumplir con el principio de Single Responsibility (Responsabilidad Única), asegurando que el código sea mantenible, escalable y fácil de testear.

Desglose Arquitectónico (Módulos y Paquetes) A. Capa de Modelado de Datos (models/) En este paquete centralizamos la "esencia" del negocio. El archivo producto.py contiene la clase Producto, que actúa como el plano (blueprint) para cada artículo del inventario.

Encapsulamiento: Cada atributo (sku, precio, stock, etc.) se agrupa en una entidad lógica.

Lógica de Negocio: Implementamos métodos de instancia como necesita_reorden(). Este método encapsula la regla de decisión: if stock < stock_minimo. Al estar dentro de la clase, cualquier cambio en la política de reabastecimiento solo se edita en un lugar.

Cálculos Dinámicos: El método unidades_faltantes() calcula el déficit exacto, mientras que valor_inventario() genera métricas financieras en tiempo real.

B. Capa de Utilidades y Servicios (utils/) Aquí es donde ocurre la "magia" técnica que soporta a la lógica principal:

Validación de Datos (validators.py): En Ciencia de Datos, la limpieza de datos es el 80% del trabajo. Este módulo actúa como un filtro de seguridad. Antes de intentar crear un objeto Producto, verificamos que los datos del CSV sean íntegros. Si un precio viene como texto no numérico o un stock es negativo, el validador lo marca como error, evitando que el programa colapse por una ValueError.

Gestión de I/O (io.py): Este módulo abstrae la complejidad de interactuar con el sistema de archivos.

Lectura: Utiliza la librería nativa csv para mapear las filas del archivo data/inventario.csv a diccionarios de Python.

Escritura: Genera el reporte final en la carpeta outputs/. Se configuró específicamente con newline='' para evitar saltos de línea extra en sistemas Windows y con codificación utf-8 para soportar caracteres especiales.

Flujo de Ejecución (Pipeline de Datos) El archivo main.py funciona como el Orquestador Central. El flujo sigue estos pasos críticos:
Carga: Se invoca a leer_inventario para traer los datos crudos a memoria.

Limpieza y Transformación: Se recorre cada registro del CSV. Cada fila pasa por el filtro de validar_producto. Si es válida, se "instancia" un objeto de la clase Producto.

Procesamiento de Inteligencia: Se genera una nueva lista llamada reorden usando una List Comprehension. Aquí filtramos solo aquellos objetos que el método necesita_reorden() marque como True.

Optimización y Ordenamiento: Para que el reporte sea útil, aplicamos un método de ordenamiento sort() con una función lambda. Los productos con mayor déficit de unidades se colocan al principio del archivo (Orden descendente), permitiendo una toma de decisiones inmediata.

Persistencia: Finalmente, se envían los datos procesados a escribir_reporte para generar el entregable final.

Gestión de Estructura y Git Para este reto, se implementó una estructura de directorios profesional:
init.py: Archivos esenciales que transforman simples carpetas en paquetes de Python, permitiendo importaciones absolutas y relativas.

data/ vs outputs/: Separación física entre datos de entrada (fuente de verdad) y datos de salida (resultados procesados), una práctica estándar en pipelines de ingeniería de datos.

Control de Versiones: Se utilizó Git para el seguimiento de cambios, asegurando que cada etapa del desarrollo (limpieza, modularización y documentación) quedara registrada en el historial del repositorio.

Conclusión Técnica La implementación de este sistema demuestra el dominio de conceptos avanzados como la abstracción de funciones, el manejo de excepciones y la organización de código en módulos independientes. Esta arquitectura permite que, en el futuro, podamos cambiar la base de datos de un CSV a una SQL o una API sin necesidad de reescribir la lógica de los productos o las validaciones.
