##Nombre del estudiante: Edwin Usgame Alarcón
##Grupo: 213022_893
##Programa: Ingeniería de sistemas
##Código Fuente: Creado por el estudiante.

## Función que calcula la suma de horas semanales y clasifica la jornada.
def calculo_semana(total_horas, max_horas_semana):
    if total_horas > max_horas_semana:
        return f"Sobretiempo (+{total_horas - max_horas_semana:.2f})"
    elif total_horas < max_horas_semana:
        return f"Menor al horario (-{max_horas_semana - total_horas:.2f})"
    else:
        return "Horario estandar"

## Datos almacenados 
max_horas_semana = 40
## Arreglo para nombres empleados.
nombres = ["Julieth", "Alexandra", "Nicolas", "Samantha"]
## Matriz horas por día.
horas_dia = [
    [8,8,8,8,7],
    [8,9,7,9,8],
    [9,9,9,8,6],
    [8,6,10,7,9]
]

## Pregunta inicial.
while True:
    print("\nSISTEMA DE GESTIÓN DE HORAS")
    opcion = input("¿Desea ingresar nuevos datos? (Si/No)\nADVERTENCIA: Al seleccionar 'Si' deberá ingresar todos los datos manualmente, al seleccionar 'No' se utilizarán los datos predefinidos:\n> ").lower()

    if opcion == "si" or opcion == "no":
        break  
    else:
        print("\n¡ALERTA! Por favor responda únicamente 'Si' o 'No'.")

## Modulo para el Si.
if opcion == "si":
    ## Se hace reset a la matriz con datso para que se puedan ingresar los nuevos.
    nombres = []
    horas_dia = []
    
    # MOdulo para validar la cantidad de empleados que se van a registrar.
    while True:
        try:
            cantidad = int(input("¿Cuántos empleados desea registrar? (Máximo 100): "))
            
            if 1 <= cantidad <= 100:
                break 
            else:
                print("¡ALERTA! La cantidad de empleados debe ser entre 1 y 100.")
        except ValueError:
            print("¡ALERTA! Por favor ingrese un número entero válido.")
    
    # Modulo para rellenar los datos de los empleados.
    for e in range(cantidad):
        nombre = input(f"\nNombre del empleado {e+1}: ")
        nombres.append(nombre)
        
        horas_empleado = []
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        
        for dia in dias:
            while True: 
                try:
                    h = float(input(f"  Horas del {dia}: "))
                    if 0 <= h <= 12:
                        horas_empleado.append(h)
                        break 
                    else:
                        print("  ¡ALERTA! Las horas no pueden ser negativas ni mayores a 12.")
                except ValueError:
                    print("  ¡ALERTA! Por favor ingrese un número válido.")
        
        horas_dia.append(horas_empleado)

## Modulo para organizar los resultados. si se selecciona NO salta directamente a este modulo.
print("\n")
print("Resultados:")
print()
print(f"{'Empleado':<12} | {'Horas':<10} | {'Tipo de Jornada'}")
print("-" * 55)

##Modulo que procesa los datos de la matriz y da los resultados.
for i in range(len(nombres)):
    suma_horas_semana = 0
    for j in range(len(horas_dia[i])):
        suma_horas_semana += horas_dia[i][j]

    total_semana = calculo_semana(suma_horas_semana, max_horas_semana)    
    print(f"{nombres[i]:<12} | {suma_horas_semana:<10.2f} | {total_semana}")

print("\n")