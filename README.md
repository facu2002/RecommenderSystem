# Sistema de Recomendación : Métodos de filtrado colaborativo
### Daniel Felipe Gómez Aristizabal
### Facundo José García Gallo
#### Universidad de La Laguna - Gestión del Conocimiento en las Organizaciones


### Índice

1. [Instrucciones de uso](#instrucciones-de-uso)
2. [Explicación de ejecución](#explicación-de-ejecución)
3. [Descripción del código](#Descripción-del-código)
4. [Visualización de documentación](#Visualización-de-documentación)

#### Instrucciones de uso

Antes de explicar cómo se debe ejecutar el programa tenemos que detenernos a entender a la perfección qué parámetros se le deben pasar al mismo. Como se explica en el enunciado de la práctica, debíamos haber implementado un sistema de recomendación que calcule las valoraciones de ciertos usuarios siguiendo el método de filtrado colaborativo, para ello se puede llevar a cabo con varias métricas que calculan la similitud de dos usuarios, estas métricas pueden ser de tres tipos: Correlación de Pearson, Distancia Coseno o Distancia Euclídea. Para la elección de una de estas métricas, optamos por la entrada de una variable al estilo POSIX, de este modo, la variable puede tomar solo tres valores: cero (para la Correlación de Pearson), uno (para la Distancia Coseno) y dos (para la Distancia Euclídea).

Por otro lado, aparece el concepto de predicción, que es la función encargada de realizar el cálculo del valor final que se predijo para un usuario y un ítem, esta predicción puede ser de dos tipos: Predicción Simple o Diferencia con la media. Del mismo modo, decidimos realizar la consulta de selección de esta predicción mediante la entrada de una variable al estilo POSIX, pero esta vez, la variable solo puede tomar dos valores: cero (para la Predicción Simple) o uno (para la Diferencia con la media).

Además, debemos hablar del concepto de vecindad, un término que no podemos dejar pasar ya que es inevitable para la realización del cálculo final. La vecindad es el número de vecinos (usuarios con mayor similitud) que se debe tener en cuenta para calcular alguna de las dos predicciones, este valor debe estar en el rango [ 1, n - 1].

Por último, debemos introducir la matriz con los valores de las valoraciones de los usuarios sobre ciertos ítems, en nuestro caso, la matriz será almacenada junto con los límites superiores e inferiores (valores máximos y mínimos de valoración de usuarios) en un archivo con extensión .txt en el subdirectorio /data, aclarar que, si el fichero de entrada no se coloca en este subdirectorio, el programa no funcionará.

Ya explicado cada uno de los parámetros que debe recibir el programa, podemos pasar a un ejemplo de utilización. Para empezar, el programa debe recibir cuatro argumentos de línea de comandos, ni más ni menos. Estos cuatro parámetros deben especificarse de la siguiente manera:
python main.py -f “utility-matrix-5-10-1.txt” -m 0 -p 0 -n 1

Como podemos apreciar, los argumentos vienen precedidos por un identificador, f en el caso del fichero, m en el caso de la métrica, p en el caso de la predicción y n en el caso del número de vecinos. A continuación de estos identificadores debemos colocar los valores previamente explicados.

Por último, podemos hacer uso de un último parámetro, el parámetro de ayuda -h, el cual explica cómo se debe ejecutar el programa en lo que a los argumentos de línea de comandos se refiere.



#### Explicación de ejecución


El resultado de la ejecución del código puede interpretarse desde dos zonas, ya que hemos bifurcado la salida del mismo en dos diferentes áreas, la primera será la propia consola, que tendrá toda la información que se pide en el enunciado de la práctica (matriz de utilidad con la predicción de los elementos faltantes, similitud entre todos los vecinos del usuario del que se está calculando su predicción, los vecinos que se han seleccionado en el proceso de predicción y el cálculo de predicción de la matriz de utilidad en base a los vecinos seleccionados). Mientras que la segunda (que solo tendrá la matriz resultante), será un fichero de salida llamado output.txt ubicado en el directorio raíz del proyecto.


#### Descripción del código


El código se encuentra en la carpeta /src de la raíz del proyecto, a su vez, esta carpeta tiene subdivisiones, /metric y /prediction para cumplir la programación orientada a objetos que se explicó en el informe de esta práctica. En las carpetas /docs y /_build se encuentra el código necesario para el despliegue de la documentación, mientras que en el directorio /data se encuentran los ficheros de entradas de las matrices de valoración.

Si nos metemos en el directorio /src podemos ver tres ficheros, el fichero main.py es el encargado de la ejecución principal del programa, el que se llama a ejecutar en la ejecución total del mismo. El fichero file_system.py contiene los métodos necesarios para sacar la información externa, es decir del fichero que se pasa como argumento de línea de comandos. También se encuentra el fichero Recommender.py, donde se encuentra la clase principal y los métodos de nuestro programa. 

Además, veremos dos directorios, /metric, en el que se encuentra el código necesario para implementar las tres métricas mencionadas anteriormente, así como la clase abstracta de la que cuelgan. Y /prediction, en el que se encuentra el código necesario para la implementación de las fórmulas que predicen la valoración de un usuario, además de la clase abstracta de la que cuelgan.


#### Visualización de documentación


Para la correcta visualización del despliegue de la documentación acceda al link adjunto en el repositorio de GitHub, esto lo llevará directamente a una pestaña del navegador donde puede consultar toda la documentación de nuestro programa.