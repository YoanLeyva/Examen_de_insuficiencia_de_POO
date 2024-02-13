Examen de insuficiencia de Programación orientada a objetos 1er año de Ingeniería Informática.

Crearemos una clase llamada Libro con las siguientes características:

• Sus atributos son titulo, número de páginas, prestado, genero y escritor.
• Por defecto, el número de páginas es de 100 páginas y prestado false. El resto de atributos 
serán valores por defecto según el tipo del atributo.

• Los constructores que se implementaran serán: 
o Un constructor por defecto.
o Un constructor con el titulo y escritor. El resto por defecto.
o Un constructor con todos los atributos, excepto de prestado.

• Los métodos que se implementara serán: 
o Métodos get de todos los atributos, excepto de prestado.
o Métodos set de todos los atributos, excepto de prestado.
o Sobrescribe los métodos toString.

Crearemos una clase Revista con las siguientes características:
• Sus atributos son titulo, número de páginas, prestado, genero y publicación.
• Por defecto, el número de páginas es de 50 páginas y prestado false. El resto de atributos 
serán valores por defecto según el tipo del atributo.

• Los constructores que se implementaran serán: 
o Un constructor por defecto.
o Un constructor con el titulo y número de páginas. El resto por defecto.
o Un constructor con todos los atributos, excepto de prestado.

• Los métodos que se implementara serán: 
o Métodos get de todos los atributos, excepto de prestado.
o Métodos set de todos los atributos, excepto de prestado.
o Sobrescribe los métodos toString.

Como vemos, en principio, las clases anteriores no son padre-hija, pero si tienen en común, por 
eso vamos a hacer una interfaz llamada Prestado con los siguientes métodos:
• entregar(): cambia el atributo prestado a true.
• devolver(): cambia el atributo prestado a false.
• isPrestado(): devuelve el estado del atributo prestado.
• Método compareTo (Object a), compara los números de páginas en las revistas y en los 
libros.

Implementa los anteriores métodos en las clases Revista y Libro. Ahora crea una aplicación 
ejecutable y realiza lo siguiente:
• Crea dos arrays, uno de Libro y otro de Revista, de 4 posiciones cada uno.
• Crea un objeto en cada posición del array, con los valores que desees, puedes usar distintos 
constructores.
• Entrega algunas Revistas y Libros con el método entregar().
• Cuenta cuántos Libros y Revistas hay entregados. Al contarlos, devuélvelos.
• Por último, indica el Libro con más número de páginas. Muéstralos en pantalla con toda su 
información (usa el método toString()).