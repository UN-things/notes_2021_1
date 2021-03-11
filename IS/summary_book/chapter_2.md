# Índice
- [Índice](#índice)
- [Agentes inteligentes](#agentes-inteligentes)
	- [Agentes y su entorno](#agentes-y-su-entorno)
	- [Buen comportamiento: el concepto de racionalidad](#buen-comportamiento-el-concepto-de-racionalidad)
		- [Medidas de rendimiento](#medidas-de-rendimiento)
		- [Racionalidad](#racionalidad)
		- [Omnisciencia, aprendizaje y autonomía](#omnisciencia-aprendizaje-y-autonomía)
	- [Agente Racional](#agente-racional)
	- [La naturaleza del entorno](#la-naturaleza-del-entorno)
		- [Especificación del entorno de trabajo](#especificación-del-entorno-de-trabajo)
			- [Propiedades de los entornos de trabajo](#propiedades-de-los-entornos-de-trabajo)
	- [Estructuras de los agentes](#estructuras-de-los-agentes)
		- [Programas de los agentes](#programas-de-los-agentes)
			- [Agentes reactivos simples](#agentes-reactivos-simples)
			- [Agentes reactivos basados en modelos](#agentes-reactivos-basados-en-modelos)
			- [Agentes basados en objetivos](#agentes-basados-en-objetivos)
			- [Agentes basados en utilidad](#agentes-basados-en-utilidad)
			- [Agentes que aprenden](#agentes-que-aprenden)

# Agentes inteligentes

## Agentes y su entorno

![Partes del agente](./../images/II00.png)

- **Agente:** es cualquier cosa capaz de percibir su **Medioambiente** con la
  ayuda de **sensores** y actuar en ese medio utilizando **actuadores**.
  Cada agente puede percibir sus propias acciones (pero no siempre sus efectos).
  El comportamiento de un agente viene dado por la **función agente**.
- **Percepción:** El agente puede recibir entradas en cualquier instante.
- **Secuencia de percepciones:** refleja el historial completo de lo que el
  agente ha recibido. _Un agente tomará una desición en un momento dado
  dependiendo de la secuencia completa de percepciones hasta ese instante_.
- **Función agente:** Proyecta una percepción dada, en una acción. Se
  implementará mediante el **programa del agente**. La función del agente es una
  descripción matemática abstracta; el programa del agente es una implementación
  completa, que se ejecuta sobre la arquitectura del agente.

## Buen comportamiento: el concepto de racionalidad

Un agente racional es aquel que hace lo correcto. Hacer lo correcto es aquello
que permite al agente obtener un resultado mejor. Por lo tanto, se necesita
determinar una forma de medir el éxito. Ello, junto a la descripción del entorno
y de los sensores y actuadores del agente, proporcionará una especificación
completa de la tarea que desempeña el agente.

### Medidas de rendimiento

Incluyen los criterios que determinan el éxito en el comportameinto del agente.
Cuando se sitúa un agente en un medio, éste genera una secuencia de acciones de
acuerdo con las percepciones recibidas. Si la secuencia es la deseada, entonces
el agente habrá actuado correctamente.

_Como regla general, es mejor diseñar medidas de utilidad de acuerdo con lo que
se quiere para el entorno, más que de acuerdo con cómo se cree que el agente
debe comportarse_.

### Racionalidad

Depende de 4 factores:

- La medida de rendimiento que define el criterio de éxito.
- El conocimiento del medio en el que habita, acumulado por el agente.
- Las acciones que el agente puede llevar a cabo.
- La secuencia de percepciones del agente hasta este momento.

_En cada posible secuencia de percepciones, un agente racional deberá emprender
aquella acción que supuestamente maximice su medida de rendimiento, basándose en
las evidencias aportadas por la secuencia de percepciones y en el conocimiento
que el agente mantiene almacenado_

### Omnisciencia, aprendizaje y autonomía

Un agente omnisciente conoce el resultado de su acción y actúa de acuerdo con
él; sin embargo, en realidad la omnisciencia no es posible. La **recopilación de
información** busca llevar a cabo acciones con la intención de modificar las
percepciones futuras. No es suficiente con recopilar la información, el agente
debe **aprender** lo máximo porsible de lo que está percibiendo.
Se dice que un agente carece de **autonomía** cuando se apoya más en el
conocimiento inicial que le proporciona su diseñador que en sus propias
percepciones. Un agente racional debe ser autónomo, debe saber aprender a
determinar cómo tiene que compensar el conocimiento incompleto o parcial inicial

## Agente Racional

Entidad que percibe algo y actúa. Un agente racional es aquel que hace lo correcto
a partir de lo que conocen y perciben.

$$
F: P^* \rightarrow A
$$

- $P:$ Percepción.
- $P^*:$ Todo lo que ha percibido desde que ha existido.
- $A:$ Acción que devuelve el agente, maximisa o minimisa una medida de
  rendimiento.

Dado que no se tiene infinita capacidad de cálculo, memoria ni tiempo, hacer un
agente perfectamente racional, es imposible para todo problema (en general).

## La naturaleza del entorno

Son esencialmente los **problemas** para los que los agentes racionales son las
**soluciones**.

### Especificación del entorno de trabajo

**REAS** (**R**endimiento, **E**ntorno, **A**ctuadores, **S**ensores).

![Ejemplo del entorno de trabajo](./../images/II01.png)
![Ejemplo del entorno de trabajo](./../images/II02.png)

#### Propiedades de los entornos de trabajo

Estas dimensiones determinan, hasta cierto punto, el diseño más adecuado para el
agente y la utilización de cada una de las familias principales de técnicas en
la implementación del agente.

- **Totalmente observable** vs. **Parcialmente observable**

Si los sensores del agente le proporcionan acceso al estado completo del medio
en cada momento, entonces se dice que el entorno de trabajo es totalmente
observable. Estos son convenientes ya que el agente no necesita mantener ningún
estado interno para saber qué sucede en el mundo. Un entorno puede ser
parcialmente observable debido al ruido, por sensores poco exactos o porque los
sensores no reciben información de parte del sistema.

- **Determinista** vs. **Estocástico**

Si el siguiente estado del medio está totalmente determinado por el estado
actual y la acción ejecutada por el agente, entonces se dice que el entorno
es determinista; de otra forma es estocástico. Si el medio es parcialmente
observable entonces puede _parecer_ estocástico. Es mejor pensar en entornos
deterministas o estocásticos _desde el punto de vista del agente_.
Si el medio es deterinista, excepto para las acciones de otros agentes, decimos
que el medio es **estratégico**.

- **Episódico** vs. **Secuencial**

En un entorno de trabajo episódico, la experiencia del agente se divide en
episodios atómicos. Cada episodio consiste en la percepción del agente y la
realización de una única acción posterior. El siguiente episodio **no** depende
de las acciones en episiodios previos. Este es más fácil ya que el agente no
necesita pensar con tiempo.

En entornos secuenciales, la decisión presente puede afectar a decisiones
futuras.

- **Estático** vs. **Dinámico**

Si el entorno puede cambiar cuando el agente está deliberando, entonces se dice
que el entorno es dinámico para el agente; de otra forma se dice que es
estático. Si el entorno no cambia con el paso del tiempo, pero el rendimiento
del agente cambia, se dice que el medio es **semidinámico**.

- **Discreto** vs. **Continuo**

La distinción entre discreto y continuo se puede aplicar al estado del medio,
a la forma en la que se maneja el tiempo y a las percepciones y acciones del
agente. Por ejemplo, un medio con estados discretos como el del juego del
ajedrez tiene un número finito de estados distintos.

- **Agente individual** vs. **Multiagente**

Se ha descrito que una entidad puede percibirse como un agente, pero no se ha
explicado qué entidades se deben considerar agentes. ¿Tiene el agente A (por
ejemplo el agente taxista) que tratar un objeto B (otro vehículo) como un
agente, o puede tratarse méramente como un objeto con un comportamiento
estocástico? La distinción clave está en identificar si el comportamiento de B
está mejor descrito por la maximización de una medida de rendimiento cuyo valor
depende del comportamiento de A.

Por ejemplo, en el ajedrez, la entidad oponente B intenta maximizar su medida de
rendimiento, la cual, según las reglas, minimiza la medida de rendimiento del
agente A. Por tanto, el ajedrez es un entorno multiagente **competitivo**.
Por otro lado, en el medio definido por el taxista circulando, el evitar
colisiones maximiza la medida de rendimiento de todos los agentes, así pues es
un entorno multiagente parcialmente **cooperativo**.

![Ejemplos de entornos](./../images/II03.png)

## Estructuras de los agentes

El trabajo de la IA es diseñar el **programa del agente** que implemente la
función del agente que proyecta las percepciones en las acciones. Se asume que
este programa se ejecutará en algún tipo de computador con sensores físicos y
actuadores, lo que se conoce como **arquitectura**.

$$
Arquitectura = sensores + actuadores + \textup{\textit{máquina dónde se ejecuta el
programa agente}}\\
Agente = arquitectura + programa
$$

La arquitectura y el programa deben ser compatibles. Si el programa tiene
recomendaciones como _Caminar_, la arquitectura tiene que tener piernas.

### Programas de los agentes

Hay que tener en cuenta la diferencia entre los programas de los agentes, que
toman la percepción actual como entrada, y la función agente, que recibe la
percepción histórica completa.

![Programa Agente dirigido mediante tabla](../images/II04.png)

El programa de agente dirigido mediante tabla está condenado al fracaso, ya que
este tendrá que tener una tabla de búsqueda muy grande para devolver una acción
dadas las percepciones recibidas:

- $P:$ Conjunto de posibles percepciones.
- $T:$ Tiempo de vida del agente
- Entradas de la tabla = $\sum_{t=1}^{T}{|P|}^t$

#### Agentes reactivos simples

Estos agentes seleccionan las acciones sobre la base de las percepciones actuales,
ignorando el resto de las percepciones históricas.

![Diagrama agente reactivo simple](../images/II05.png)

![Función agente reactivo simple](../images/II06.png)

El agente sólo funcionará si se puede tomar la decisión correcta sobre la base de
la percepción actual, lo cual es posible sólo si el entorno es totalmente
observable. Un agente reactivo simple con capacidad para elegir acciones de manera
aleatoria puede mejorar los resultados que proporciona un agente reactivo simple
determinista (está sujeto a caer en bucles infinitos).

#### Agentes reactivos basados en modelos

El agente debe mantener algún tipo de **estado interno** que dependa de la
historia percibida y que de ese modo refleje por lo menos alguno de los aspectos
no observables del estado actual.

La actualización de la información de estado interno según pasa el tiempo requiere
codificar dos tipos de conocimiento en el programa del agente:

1. Se necesita alguna información acerca de cómo evoluciona el mundo
   independientemente del agente.
2. Se necesita más información sobre cómo afectan al mundo las acciones del agente

Este conocimiento acerca de <<cómo funciona el mundo>>, se denomina modelo.

![Diagrama agente reactivo basado en modelos](../images/II07.png)

![Programa agente basado en modelos](../images/II08.png)

#### Agentes basados en objetivos

Además de la descripción del estado actual, el agente necesita algún tipo de
información sobre su **meta** que describa las situaciones que son deseables.

El programa del agente se puede combinar con información sobre los resultados
de las acciones posibles, para elegir aquellas que le permitan alcanzar su
objetivo.

![Agente basado en objetivos](../images/II09.png)

La selección de acciones basadas en objetivos es directa, cuando alcanzar los
objetivos es el resultado inmediato de una acción individual. En otras ocaciones
puede ser más complicado, cuando debe conciderar secuencias complejas para alcanzar
su objetivo. La **Búsqueda** y la **planificación** son los subcampos de la IA
centrados en encontrar secuencias de acciones que permitan a los agentes alcanzar
sus metas.

Aunque el agente basado en objetivos pueda parecer menos eficiente, es más
flexible ya que el conocimiento que soporta su decisión está representado
explícitamente y puede modificarse. El comportamiento del agente basado en
objetivos puede cambiarse fácilmente, un agente reactivo requeriría modificaciones
mayores.

#### Agentes basados en utilidad

Las metas sólo proporcionan una cruda distinción binaria entre los estados de
«felicidad» y «tristeza», mientras que una medida de eficiencia más general
debería permitir una comparación entre estados del mundo diferentes de acuerdo al
nivel exacto de felicidad que el agente alcance cuando se llegue a un estado u
otro. Un estado del mundo tienen diferentes grados de **utilidad** para el agente.

Una **función de utilidad** proyecta un estado (o secuencia de estados) en un
número real, que representa el nivel de felicidad, esta permite tomar desiciones
racionales en dos tipos de casos:

1. Cuando haya **objetivos conflictivos** y sólo se pueda alcanzar alguno de ellos.
2. Cuando haya **varios objetivos** por los que se pueda guiar el agente, y
   **ninguno de ellos se pueda alcanzar con certeza**, la utilidad proporciona un
   mecanismo para ponderar la probabilidad de éxito en función de la importancia
   de los objetivos.

![Agente basado en utilidad](../images/II0A.png)

#### Agentes que aprenden

El aprendizaje permite que el agente opere en medios inicialmente desconocidos y
que sea más competente que si sólo utilizase su conocimiento inicial. El
aprendizaje está por fuera de la inteligencia, es una cualidad más compleja

![Agentes que aprenden](../images/II0B.png)

- **Elemento de aprendizaje:** Es el responsable de hacer mejoras. Se
  retroalimenta con las cŕiticas sobre la actuación del agente y determina cómo se
  debe modificar el elemento de actuación para proporcionar mejores resultados.
- **Elemento de actuación:** Es responsable de seleccionar acciones externas. Es
  lo que anteriormente se concideraba como agente completo (recibe estímulos y
  determina qué acción realizar)
- **Crítica:** Indica al elemento de aprendizaje qué tal lo está haciendo el
  agente con respecto a un nivel de actuación fijo. Es necesaria porque las
  percepciones por sí mismas no prevén una indicación del éxito del agente.
- **Generador de problemas:** Es responsable de sugerir acciones nuevas que lo
  guiarán hacia experiencias nuevas e informativas. Si el agente está dispuesto a
  explorar un poco, y llevar a cabo acciones que no sean totalmente óptimas a
  corto plazo, puede descubrir acciones mejores a largo plazo.
- _Nivel de actuación:_ Conceptualmente se debe tratar como si estuviese fuera del
  agente, ya que este no debe modificarlo para su propio interés. Identifica parte
  de las percepciones entrantes como **recompensas** o **penalizaciones**.

Cuando se intenta diseñar un agente que tenga capacidad de aprender, la primera
cuestión a solucionar no es ¿cómo se puede enseñar a aprender?, sino ¿qué tipo de
elemento de actuación necesita el agente para llevar a cabo su objetivo, cuando
haya aprendido cómo hacerlo? Dado un diseño para un agente, se pueden construir
los mecanismos de aprendizaje necesarios para mejorar cada una de las partes del
agente.

El aprendizaje en el campo de los agentes inteligentes puede definirse como el
proceso de modificación de cada componente del agente, lo cual permite a cada
componente comportarse más en consonancia con la información que se recibe, lo que
por tanto permite mejorar el nivel medio de actuación del agente.