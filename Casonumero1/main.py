from Empleado import Empleado

empleado1 = Empleado("Pepito", "perez", 100000, 1)

print(f'el salario del empleado es de: {empleado1.DarSalario()}')

empleado1.CambiarSalario(1500000)
print(f'el nuevo salario del empleado es de: {empleado1.DarSalario()}')

print(f'el salario anual del empleado es de: {empleado1.DarSalarioAnual()}')

print(f'el impuesto anual es de: {empleado1.CalcularImpuestoAnual()}')