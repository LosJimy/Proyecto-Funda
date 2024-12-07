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
Código fuente: int a = 5;
Tokens: [Keyword:int, Identifier:a, Operator:=, Number:5, Delimiter:;]


### Cómo Funciona el Analizador Léxico


Lectura del Código: El analizador comienza leyendo el archivo de código fuente carácter por carácter.
Formación de Tokens: Usa un conjunto de reglas basadas en expresiones regulares para reconocer patrones, como:
Letras seguidas de dígitos o guiones bajos se interpretan como identificadores (x).
Caracteres como + o = son reconocidos como operadores.
Números enteros o decimales se reconocen como literales numéricos.
Clasificación: Cada token identificado se clasifica según su tipo y se almacena en una lista que se pasará a la fase siguiente.

Características propias del lenguaje
===================

Nuestro código cuenta con una nueva funcionalidad relacionada con escribir palabras invertidas.


Al imprimir un string tambien escribe el reverso de la cadena de caracteres: hola | aloh


Esto también sucede para llamar desde codigo a una palabra clave, es decir, para llamar print, if, else, elif, for, while, in, range, true, false, es de la siguiente manera tnirp, fi, esle, file, rof, elihw, ni, egnar, eurt, eslaf

