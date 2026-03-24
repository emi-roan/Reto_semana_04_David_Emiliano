def validar_producto(sku, nombre, categoria, precio, stock, stock_minimo):
    try:
        if not sku or not str(sku).strip(): return False, "SKU inválido"
        if not nombre or not str(nombre).strip(): return False, "Nombre vacío"
        if float(precio) < 0: return False, "Precio negativo"
        if int(stock) < 0: return False, "Stock negativo"
        if int(stock_minimo) < 0: return False, "Stock mínimo negativo"
        return True, None
    except (ValueError, TypeError):
        return False, "Error de tipo de dato (No numérico)"