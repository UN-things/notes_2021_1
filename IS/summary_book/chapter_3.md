# Índice
- [Índice](#índice)
- [Resolver problemas mediante búsqueda](#resolver-problemas-mediante-búsqueda)
	- [Agentes resolvente-problemas](#agentes-resolvente-problemas)
		- [Problemas y soluciones bien definidos](#problemas-y-soluciones-bien-definidos)
		- [Formular los problemas](#formular-los-problemas)
	- [Ejemplos de Problemas](#ejemplos-de-problemas)
		- [Problemas de juguete](#problemas-de-juguete)
		- [Problemas del Mundo Real](#problemas-del-mundo-real)
	- [Búsqueda de Soluciones](#búsqueda-de-soluciones)
	- [Medir el rendimiento de la resolución del problema](#medir-el-rendimiento-de-la-resolución-del-problema)
	- [Estrategias de búsqueda no informada](#estrategias-de-búsqueda-no-informada)
		- [Búsqueda primero en Anchura](#búsqueda-primero-en-anchura)
		- [Búsqueda de costo uniforme](#búsqueda-de-costo-uniforme)

# Resolver problemas mediante búsqueda

_Cómo un agente puede encontrar una secuencia de acciones que alcance sus
objetivos, cuando ninguna acción simple lo hará._

Los agentes basados en objetivos pueden tener éxito considerando las acciones
futuras y lo deseable de sus resultados. Los agentes resolventes-problemas deciden
qué hacer para encontrar secuencias de acciones que conduzcan a los estados
eseables.

Algoritmos de propósito general para resolver estos problemas:

- **No informados:** No dan información sobre el problema, salvo su definición.
- **Informados:** Tienen cierta idea de dónde buscar las soluciones.

## Agentes resolvente-problemas

Los objetivos ayudan a organizar su comportamiento, limitando las metas que
intenta alcanzar el agente. El primer paso para solucionar un problema es la
**formulación del objetivo** (conjunto de estados que satisfacen el objetivo),
basado en la situación actual y la medida de rendimiento del agente.

Dado un objetivo, la **formulación del problema** es el proceso de decidir qué
acciones y estados tenemos que considerar.

_Un agente con distintas opciones inmediatas de valores desconocidos puede
decidir qué hacer, examinando las diferentes secuencias posibles de acciones que
le conduzcan a estados de valores conocidos, y entonces escoger la mejor secuencia_


Este proceso de hallar esta secuencia se llama **búsqueda**. Un algoritmo de
búsqueda toma como entrada un problema y devuelve una solución de la forma
secuencia de acciones. Luego se procede a ejecutar las acciones que ésta
recomienda. Esta es la llamada fase de **ejecución**. Una vez ejecutada la
solución, el agente formula un nuevo objetivo.

![Agente resolvente-problemas](../images/III00.png)

Los agentes que realizan sus planes con los ojos cerrados, por así decirlo, deben
estar absolutamente seguros de lo que pasa (los teóricos de control lo llaman
sistema de **lazo abierto**, porque ignorar las percepciones rompe el lazo entre
el agente y el entorno).

### Problemas y soluciones bien definidos

Un problema puede definirse, formalmente, por cuatro componentes:
- **Estado inicial:** Dónde comienza el agente.
- **Función sucesor:** Una descripción de las posibles acciones disponibles por el
  agente. La formulación 3 más común utiliza una función sucesor. Dado un estado
  particular $x$, $SUCESOR-FN(x)$ devuelve un conjunto de pares ordenados $<acción, sucesor>$.
  Implícitamente el estado inicial y la función sucesor definen el **espacio de
  estados** del problema (el conjunto de todos los estados alcanzables desde el
  estado inicial). El espacio de estados forma un grafo en el cual los nodos son
  estados y los arcos entre los nodos son acciones. Un **camino** en el espacio de
  estados es una secuencia de estados conectados por una secuencia
  de acciones.
- **Test objetivo:** Determina si un estado es un estado objetivo.
- Una función **costo del camino** que asigna un costo numérico a cada camino.
  El **costo individual** de una acción $a$ que va desde un estado $x$ al estado
  $y$ se denota por $c(x,a,y)$.

Una **solución** de un problema es un camino desde el estado inicial a un estado
objetivo. La calidad de la solución se mide por la función costo del camino, y una
**solución óptima** tiene el costo más pequeño del camino entre todas las
soluciones.

### Formular los problemas

Al proceso de eliminar detalles de una representación se le llama **abstracción**.
La abstracción es válida si podemos ampliar cualquier solución abstracta a una
solución en el mundo más detallado, y es útil si al realizar cada una de las
acciones en la solución es más fácil que en el problema original.

## Ejemplos de Problemas

Diferencias entre _problemas de juguete_ y _problemas del mundo real_:
- Un **problema de juguete** se utiliza para ilustrar o ejercitar los métodos de
  resolución de problemas. Éstos se pueden describir de forma exacta y concisa.
- Un **problema del mundo-real** es aquel en el que la gente se preocupa por sus
  soluciones.

### Problemas de juguete

Problema de la Aspiradora:

- **Estados:** el agente está en una de dos localizaciones, cada una de las cuales
  puede o no contener suciedad. Así, hay $2 \cdot 2^2 = 8$ posibles estados del mundo.
- **Estado inicial:** cualquier estado puede designarse como un estado inicial.
- **Función sucesor:** ésta genera los estados legales que resultan al intentar
  las tresacciones (Izquierda, Derecha y Aspirar). En la Figura 3.3 se muestra el
  espacio de estados completo.
- **Test objetivo:** comprueba si todos los cuadrados están limpios.
- **Costo del camino:** cada costo individual es 1, así que el costo del camino es
  el número de pasos que lo compone.

![Espacio de estados - Aspiradora](../images/III01.png)

### Problemas del Mundo Real

El **problema de búsqueda de una ruta** está definido en términos de posiciones y
transiciones a lo largo de ellas:

- **Estados:** cada estado está representado por una localización (por ejemplo, un
  aeropuerto) y la hora actual.
- **Estado inicial:** especificado por el problema.
- **Función sucesor:** devuelve los estados que resultan de tomar cualquier vuelo
  programado (quizá más especificado por la clase de asiento y su posición) desde
  el aeropuerto actual a otro, que salgan a la hora actual más el tiempo de
  tránsito del aeropuerto.
- **Test objetivo:** ¿tenemos nuestro destino para una cierta hora especificada?
- **Costo del camino:** esto depende del costo en dinero, tiempo de espera, tiempo
  del vuelo, costumbres y procedimientos de la inmigración, calidad del asiento,
  hora, tipo de avión, kilometraje del aviador experto, etcétera.

El **problema del viajante de comercio (PVC)** es un problema de ruta en la que
cada ciudad es visitada exactamente una vez. La tarea principal es encontrar el
viaje más corto. El problema es de tipo NP duro.

Los **problemas turísticos** están estrechamente relacionados con los problemas de
búsqueda de una ruta, pero con una importante diferencia: cada estado debe incluir
no sólo la localización actual sino también las ciudades que el agente ha visitado.

## Búsqueda de Soluciones

Este capítulo se ocupa de las técnicas de búsqueda que utilizan un **árbol de
búsqueda** explícito generado por el estado inicial y la función sucesor,
definiendo así el espacio de estados. La raíz del árbol de búsqueda es el **nodo de
búsqueda** que corresponde al estado inicial. Como no estamos en un estado
objetivo, tenemos que considerar otros estados, esto se hace **expandiendo** el
estado actual; es decir aplicando la función sucesor al estado actual y generar
así un nuevo conjunto de estados. El estado a expandir está determinado por la
**estrategia de búsqueda**.

Un nodo es una estructura de datos con cinco componentes:
- **Estado:** el estado, del espacio de estados, que corresponde con el nodo.
- **Nodo padre:** El nodo en el árbol de búsqueda que ha generado este nodo.
- **Acción:** La acción que se aplicará al padre para generar el nodo.
- **Costo del camino:** Tradicionalmente denotado por $g(n)$, de un camino desde
  el estado inicial al nodo, indicado por los punteros a los padres.
- **Profundidad:** El número de pasos a los largo del camino desde el estado
  inicial.

La conexión de nodos que se han generado pero no expandido, se conoce como **frontera**, cada elemento de la frontera es un nodo hoja, no se ha expandido.

Las operaciones en una **Cola** son:
- `createQueue(element)`: Crea una cola con los elementos dados.
- `isEmpty(queue)`: Devuelve Verdadero si no hay ningún elemento en la cola
- `first(queue)`: Devuelve el primer elemento de la cola.
- `deleteFirst(queue)`: Devuelve `first(queue)` y lo borra de la cola.
- `insert(element, queue)`: Inserta elemento en la cola y devuelve la cola
  resultado
- `insertAll(elements, queue)`: Inserta un conjunto de elemenntos en la cola y
  devuelve la cola resultado.

![Algoritmmo general - busqueda árboles](../images/III02.png)

## Medir el rendimiento de la resolución del problema

Evaluaremos el rendimiento de un algoritmo de cuatro formas:
- **Completitud:** ¿Está garantizado que el algoritmo encuentre una solución cuando
  esta exista?
- **Optimización:** ¿Encuentra la solución óptima?
- **Complejidad en tiempo:** ¿Cuánto tarda en encontrar una solución?
- **Complejidad en espacio:** ¿Cuánta memoria se necesita para el funcionamiento de
  la búsqueda?

La **complejidad** se expresa en terminos de 3 cantidades:
- **b:** Factor de ramificación, es el máximo de sucesores de
  cualquier nodo.
- **d:**  La profundidad el nodo objetivo más superficial.
- **m:** La longitud máxima de cualquier camino en el espacio de estados.

Para valorar la eficacia de un algoritmo de búsqueda, podemos considerar el
**costo de la búsqueda** (que depende típicamente de la complejidad en tiempo pero
puede incluir también un término para el uso de la memoria) o podemos utilizar el
**coste total**, que combina el costo de la búsqueda y el costo del camino
solución encontrado.

## Estrategias de búsqueda no informada

El nombre de **busqueda no informada** hace referencia a que ellas no tienen
información adicional acerca de los estados más allá de la que proporciona la
definición del problema. Todo lo que ellas pueden hacer es generar los sucesores y
distinguir entre un estado objetivo de uno que no lo es.

### Búsqueda primero en Anchura

Se expande primero el nodo raíz, a continuación se expanden todos los sucesores
del nodo raíz, después sus sucesores, etc. En general, se expanden todos los nodos
a una profundidad en el árbol de búsqueda antes de expandir cualquier nodo del
próximo nivel.

la `SEARCH-TREE(problem,QUEUE-FIFO())` resulta una búsqueda primero en anchura. La
cola FIFO pone todos los nuevos sucesores generados al final de la cola, lo que
significa que los nodos más superficiales se expanden antes que los nodos más
profundos.

El nodo objetivo más superficial no es necesariamente el óptimo. La búsqueda
primero en anchura es óptima si el costo del camino es una función no decreciente
de la profundidad del nodo (por ejemplo, cuando todas las acciones tienen el mismo
coste).

![Búsqueda por anchur](../images/III03.png)

**Importante:**
- Son un problema más grande los requisitos de memoria para la búsqueda primero en 
  anchura que el tiempo de ejecución.
- Los problemas de búsqueda de complejidad exponencial no pueden resolverse por 
  métodos sin información, salvo casos pequeños.

### Búsqueda de costo uniforme

