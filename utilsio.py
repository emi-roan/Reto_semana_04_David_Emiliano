import csv

def leer_inventario(ruta):
    """
    Lee el archivo CSV de entrada y devuelve una lista de diccionarios.
    """
    with open(ruta, 'r', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        return list(lector)

def escribir_reporte(productos, ruta):
    """
    Escribe el reporte en la ruta especificada usando la lista de productos.
    """
    with open(ruta, 'w', encoding='utf-8', newline='') as f:
        escritor = csv.writer(f)
        
        # Escribir los encabezados del CSV
        escritor.writerow(["sku", "nombre", "unidades_faltantes", "valor_inventario"])
        
        # Escribir cada producto que necesita reorden
        for p in productos:
            escritor.writerow([
                p.sku, 
                p.nombre, 
                p.unidades_faltantes(), 
                f"{p.valor_inventario():.2f}"
            ])
