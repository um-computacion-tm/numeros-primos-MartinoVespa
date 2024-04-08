# README 

### AUTOR
#### VESPA MARTINO

## DESCRIPCIÓN 

Lo que hace este código es  definir una función llamada is_primo(value) que verifica si un número dado value es primo o no.

Lo primero que hace es comprobar si el número es igual a 1. Si es igual a 1, devuelve False, ya que 1 no se considera un número primo.

Despues de comprobar si el número es igual a 1 comienza un bucle while con la variable num_div iniciada en 2, se utilizará para probar si value se puede dividir por algún número menor que él mismo.

Dentro del bucle, se verifica si value es divisible por num_div utilizando el operador módulo (%). Si lo es, devuelve False, eso indica que el número no es primo.

El bucle continúa incrementando num_div hasta que sea igual a value. Si value no se divide por ningún número menor que él mismo, la función devuelve True, indicando que el número es primo.
