# Proyecto compilador
Taller de fundamentos de ciencias de la computación 

Benjamin Erazo, 21.340.552-7

Clerians Márquez, 20.717.942-6

Valentina López, 21.392.825-2

Descripción de la gramatica del lenguaje
===================

### Palabras clave: 
fi (if), esle (else), rof (for), break, tnirp (print), empty, file (elif), elihw (while), ni (in), egnar (range)

### Tipos de datos: 
int : Números enteros

float : Números decimales

string : Cadena de texto delimitada por comillas dobles ("")

boolean : Valores lógicos (eurt (true),eslaf (false))

### Operadores:
Operadores aritméticos: +, -, *, /, %

Operadores relacionales: ==, !=, >, <, >=, <=

Operadores lógicos: &&, ||, !

Operadores de asignación: =

Paréntesis: (, )

Estructura interna del compilador
===================

El compilador sigue la estructura clásica, dividida en varias fases:


### Análisis Léxico
El análisis léxico es la primera fase del compilador. Su propósito es leer el código fuente y dividirlo en componentes básicos llamados tokens, que son las unidades mínimas de significado en el lenguaje. Esta etapa actúa como un puente entre el código fuente y el análisis sintáctico, asegurándose de que el texto sea interpretable para las fases posteriores.


Ejemplo de tokenización, declaracion de una variable:
Código fuente: a = 5
Tokens: [Identifier:a, Operator:=, Number:5]


### Cómo Funciona el Analizador Léxico


Lectura del Código: El analizador comienza leyendo el archivo de código fuente carácter por carácter.

Formación de Tokens: Usa un conjunto de reglas basadas en expresiones regulares para reconocer patrones, como:
Letras seguidas de dígitos o guiones bajos se interpretan como identificadores (x).

Caracteres como + o = son reconocidos como operadores.

Números enteros o decimales se reconocen como literales numéricos.

Clasificación: Cada token identificado se clasifica según su tipo y se almacena en una lista que se pasará a la fase siguiente.

### Análisis Sintáctico

El análisis sintáctico, también conocido como parsing, es la segunda fase del compilador. Su objetivo es verificar que los tokens generados por el analizador léxico sigan las reglas gramaticales del lenguaje y construir una representación estructurada del programa, comúnmente llamada Árbol de Sintaxis Abstracta (AST). 


### Función Principal

Validación de la Gramática: Comprueba si los tokens forman estructuras válidas según las reglas de la gramática.

Construcción del AST: Representa la estructura jerárquica del programa para que las siguientes fases puedan interpretarlo.

Detección de Errores Sintácticos: Identifica errores como paréntesis no balanceados, secuencias de tokens mal formadas o estructuras incompletas.

### Análisis Semántico

El análisis semántico es la tercera fase del compilador. Su propósito es verificar que las construcciones del programa tengan sentido desde el punto de vista lógico y semántico, garantizando que las operaciones y los datos sean coherentes entre sí. Mientras que el análisis sintáctico verifica la forma del programa, el análisis semántico valida su significado.

### Función Principal 

Verificar Tipos de Datos: Asegura que las operaciones y asignaciones sean compatibles con los tipos de datos.

Detectar Variables No Declaradas: Comprueba que todas las variables usadas hayan sido previamente declaradas.

Chequear Reglas de Alcance: Verifica que las variables y funciones sean accesibles en el contexto en el que se utilizan.

Validar Otras Reglas Lógicas: Incluye la validación de límites, conversiones de tipos y operaciones ilegales.


Características propias del lenguaje
===================

Nuestro código cuenta con una nueva funcionalidad relacionada con escribir palabras invertidas.


Al imprimir un string tambien escribe el reverso de la cadena de caracteres: hola | aloh


Esto también sucede para llamar desde codigo a una palabra clave, es decir, para llamar print, if, else, elif, for, while, in, range, true, false, es de la siguiente manera tnirp, fi, esle, file, rof, elihw, ni, egnar, eurt, eslaf

