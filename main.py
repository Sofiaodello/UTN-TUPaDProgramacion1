nombre = input("Cliente: ").strip() 


while nombre == "" or not nombre.isalpha():
    print("Error: ingresá un nombre no vacío y solo con letras (sin espacios ni números).")
    nombre = input("Cliente: ").strip()

cantidad_str = input("Cantidad de productos: ").strip()

while not cantidad_str.isdigit() or int(cantidad_str) <= 0:
    print("Error: ingresá un número entero positivo mayor que 0.")
    cantidad_str = input("Cantidad de productos: ").strip()


cantidad = int(cantidad_str)


total_sin_descuento = 0         
total_con_descuento = 0.0        

for i in range(1, cantidad + 1):
    precio_str = input(f"Producto {i} - Precio: ").strip()

    while not precio_str.isdigit() or int(precio_str) <= 0:
        print("Error: ingresá un precio entero positivo (solo números, mayor que 0).")
        precio_str = input(f"Producto {i} - Precio: ").strip()

    precio = int(precio_str)

    desc = input("Descuento (S/N): ").strip().lower()

    while desc not in ("s", "n"):
        print("Error: ingresá 'S' para sí o 'N' para no (se acepta mayúscula o minúscula).")
        desc = input("Descuento (S/N): ").strip().lower()


    total_sin_descuento += precio
    if desc == "s":
        precio_final = precio * 0.90
    else:
        precio_final = float(precio)

    total_con_descuento += precio_final

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad  


print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")