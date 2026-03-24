import csv

def escribir_reporte(productos, ruta):
    with open(ruta, 'w', encoding='utf-8', newline='') as f:
        escritor = csv.writer(f)
        escritor.writerow(["sku", "nombre", "unidades_faltantes", "valor_inventario"])
        for p in productos:
            escritor.writerow([
                p.sku, 
                p.nombre, 
                p.unidades_faltantes(), 
                f"{p.valor_inventario():.2f}"
            ])