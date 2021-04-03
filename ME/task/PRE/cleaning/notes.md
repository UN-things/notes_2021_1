
## Conceptos Globales
- **Inteligencia Artificial:**
- **Machine Learning:** Algoritmos para indicarle a una máquina que aprenda sin necesidad de indicarselo explicitamente
- **Deep Learning:** Aprendizaje basado en redes neuronales, tiene una complejidad más elevada.

## ¿Qué es?
- Sistemas que encuentran patrones, relaciones y regularidades sobre los datos y aplicarlos para construir modelos descriptivos y predictivos.

## ¿Qué se puede hacer?

- **Aprendizaje no supervisado:** Se encuentran patrones similares entre los datos.
- **Aprendizaje Supervisado:** Cada punto tiene una etiqueta, la máquina encuentra patrones y al llegar un nuevo punto le asigna una etiqueta apartir de lo aprendido.

## Machine Learning

- Con la programación tradicional
- Con machine learning, se obtienen reglas, una ecuación que permita describir el comportamiento deseado de la mayor cantidad de datos posibles, esta ecuación se basa en los parámetros de entrada a los cuales se les asigna unos pesos específicos que puedan describir un resultado deseado.

## Más Variables
- Estandarizar/Normalizar:
  - Variables en el mismo rango
  - Lo más común: Restar la media.
    - Media = 0
    - Varianza = 1
  - Definir un rango [0,1], [-1,1]
  - No es necesario normalizar todas la variables.
  - Ya existen librerías para hacer esto (Python y R).
- Variables Categóricas
  - Describe algo del registro
  - Se pueden convertir en variables numéricas
  - Se pueden convertir en la cantidad de columnas como valores puedan tomar estas varibales categóricas.
  - En el ejemplo hay una variable categórica "Mes" y es transformada en 11 columnas, se toma 1 dato menos de lo valores posibles para evitar redundancia.
- Series de Tiempo
  - Hay datos que requieren el valor del registro previo al mismo.

## ¿Qué es un modelo?

Es una representación de los datos. El modelo generaliza y da un valor aproximado que representa alguna característica de los datos.
- El dataset se divide en dos, una parte para entrenar el algoritmo y otra para calcular los resultados deseados. La partición de datos debe ser aleatoria.
- Al modelo se le da un set de datos de entrenamientos para que el programa identifiue patrones, define coeficientes de la ecuación. Entre más datos de entrenamiento, más preciso será el modelo.
- Se le ingresan nuevos registros al modelo que ha sido previamente entrenado.

# Notebook

- Se tienen varios atributos de vinos y se desea saber la calidad del vino
- Limpiar datos
- Evaluar calidad de datos, datos faltantes, atípicos
- pandas -> datos como dataframe
- np datos matemáticos
- seaborn y matplot -> gráficas
- cantidad de datos válidos, media y desviación estándar, min, max, cuartiles
- Distribución de cada una de las variables
- correlación inversa. ïndice de co
- Sirven variables fuertemente relacionadas
- correlación no es causación