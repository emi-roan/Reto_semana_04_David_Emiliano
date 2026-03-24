from models.producto import Producto
from utils.validators import validar_producto
from utils.io import leer_inventario, escribir_reporte

def main():
    try:
        # 1. Leer datos
        datos = leer_inventario("data/inventario.csv")
        validos = []
        
        # 2. Validar y Crear Objetos
        for d in datos:
            ok, err = validar_producto(d['sku'], d['nombre'], d['categoria'], d['precio'], d['stock'], d['stock_minimo'])
            if ok:
                p = Producto(d['sku'], d['nombre'], d['categoria'], d['precio'], d['stock'], d['stock_minimo'])
                validos.append(p)
        
        # 3. Filtrar los que necesitan reorden
        reorden = [p for p in validos if p.necesita_reorden()]
        
        # 4. Ordenar (Opcional pero recomendado)
        reorden.sort(key=lambda x: x.unidades_faltantes(), reverse=True)
        
        # 5. ESCRIBIR EL ARCHIVO (Paso crítico)
        escribir_reporte(reorden, "outputs/reporte_inventario.csv")
        print("✅ ¡Éxito! El archivo se creó en la carpeta 'outputs'.")
        
    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")

if __name__ == "__main__":
    main()