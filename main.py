from models.producto import Producto
from utils.validators import validar_producto
from utils.io import leer_inventario, escribir_reporte

def crear_objetos_productos(datos_raw):
    productos_validos = []

    for fila in datos_raw:
        sku = fila.get("sku")
        nombre = fila.get("nombre")
        categoria = fila.get("categoria")
        precio = fila.get("precio")
        stock = fila.get("stock")
        stock_minimo = fila.get("stock_minimo")

        es_valido, error = validar_producto(
            sku,
            nombre,
            categoria,
            precio,
            stock,
            stock_minimo
        )

        if not es_valido:
            print(f"Omitiendo registro: {error}")
            continue

        try:
            producto = Producto(
                sku=sku,
                nombre=nombre,
                categoria=categoria,
                precio=float(precio),
                stock=int(stock),
                stock_minimo=int(stock_minimo)
            )

            productos_validos.append(producto)

        except (ValueError, TypeError) as error:
            print(f"Error creando producto {sku}: {error}")

    return productos_validos

def obtener_productos_reorden(productos):
    productos_reorden = [
        producto
        for producto in productos
        if producto.necesita_reorden()
    ]

    productos_reorden.sort(
        key=lambda producto: (
            -producto.unidades_faltantes(),
            producto.nombre.lower()
        )
    )

    return productos_reorden

def main():
    ruta_entrada = "data/inventario.csv"
    ruta_salida = "outputs/reporte_inventario.csv"

    print("--- Iniciando Sistema de Inventario ---")

    try:
        datos_raw = leer_inventario(ruta_entrada)

        if not datos_raw:
            print("No se encontraron datos en el inventario.")
            return

        productos = crear_objetos_productos(datos_raw)

        if not productos:
            print("No hay productos válidos para procesar.")
            return

        productos_reorden = obtener_productos_reorden(productos)

        print(f"Total productos válidos: {len(productos)}")
        print(f"Productos para reorden: {len(productos_reorden)}")

        escribir_reporte(ruta_salida, productos_reorden)

        print(f"Reporte generado exitosamente en: {ruta_salida}")

    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta_entrada}")

    except PermissionError:
        print("No hay permisos suficientes para acceder a los archivos.")

    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")

if __name__ == "__main__":
    main()
