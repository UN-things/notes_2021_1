# Modelos de aprendizaje supervisado

Los modelos que se verán son los de clasificación y predicción. Ambos permiten hacer análisis supervisado, en ambos se tienen previamente las etiquetas de registros, al llegar nuevos registros se clasifican en las etiquetas a las que más se asemejen. En ambos se van a tener una fórmula matemática, en los que se buscarán los coeficients de una función.

La diferencia entre ellos es la variable que se buscará predecir.

- **Predicción:** Variable continua. No define una clase o categoría, define una cantidad.
- **Clasificación:** Variable categórica. Es una variable que representa una etiqueta.

## ¿Qué es un algorítmo?
- Método estandarizado para entrenar una modelo (regresión lineal o polinomial).
- Mapea una entrada a un set de predicciones.

# Notebook

- predicción: variable continua
  - Es un número que no define clase o categoría sino una cantidad
  - los atributos deben ser continuos
- Clasificación: variable categórica
- var predic - temperatura, var - ob = personas
- error: distancia
- modelo de error mínimo cuadrado
- el fit encuentra coeficientes. entrena el modelo
- R cuadrado que tan bien se comporta el modelo. que también explica los puntos
- t y P que tanto esas variables ayudan a predecir
- intervalo de confianza
- dominio entre cero y uno
- se hace tantos modelos como variables tenga
- no es determinístico porque puede arrojar múltiples líneas, no da el mismo modelo con pesos y coeficientes
- vecinos, tiene los atributos más cercanos a mí, mayoría gana
- modelo que no se vea afectado por atípicos ni que tome todos los puntos
- se busca distancia
- noe s tanto un modelo porque calcula los puntos cercanos
- no converge o se equivoca mucho
- sí es determinístico
- se inventa una dimensión más para separar datos no separables
- regresión logísitca tradicional
- el árbol de desición es generado por el algorítomo
- mira si se divide un dato, se clasifica, con los que queda hace lo mismo
- arbol se acomoda muy bien a los datos de entrenamiento
- no determi puede encontrar reglas distintas o en diferente orden
- profundidad 3
- cuando no son determinísticos.
- debiles se aprenden los datos y no son determinísticos
- bosque aleatorio, varios árboles de desición