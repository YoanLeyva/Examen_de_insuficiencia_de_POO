class Prestado:
    def entregar(self):
        self.prestado = True

    def devolver(self):
        self.prestado = False

    def isPrestado(self):
        return self.prestado


class Libro(Prestado):
    def __init__(self, titulo, escritor, genero=None, numero_paginas=100):
        self.titulo = titulo
        self.escritor = escritor
        self.genero = genero
        self.numero_paginas = numero_paginas
        self.prestado = False

    def __str__(self):
        return f"Libro: {self.titulo} ({self.escritor}), {self.numero_paginas} páginas"

    def get_titulo(self):
        return self.titulo

    def get_escritor(self):
        return self.escritor

    def get_genero(self):
        return self.genero

    def get_numero_paginas(self):
        return self.numero_paginas

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_escritor(self, escritor):
        self.escritor = escritor

    def set_genero(self, genero):
        self.genero = genero

    def set_numero_paginas(self, numero_paginas):
        self.numero_paginas = numero_paginas


class Revista(Prestado):
    def __init__(self, titulo, publicacion, genero=None, numero_paginas=50):
        self.titulo = titulo
        self.publicacion = publicacion
        self.genero = genero
        self.numero_paginas = numero_paginas
        self.prestado = False

    def __str__(self):
        return f"Revista: {self.titulo} ({self.publicacion}), {self.numero_paginas} páginas"

    def get_titulo(self):
        return self.titulo

    def get_publicacion(self):
        return self.publicacion

    def get_genero(self):
        return self.genero

    def get_numero_paginas(self):
        return self.numero_paginas

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_publicacion(self, publicacion):
        self.publicacion = publicacion

    def set_genero(self, genero):
        self.genero = genero

    def set_numero_paginas(self, numero_paginas):
        self.numero_paginas = numero_paginas


# Crear arrays de libros y revistas
libros = [
    Libro("El son entero", "Nicolás Guillén", genero="Poesía", numero_paginas=180),
    Libro("Cecilia Valdés o La Loma del Ángel", "Cirilo Villaverde", genero="Romántico", numero_paginas=328),
    Libro("Los pasos perdidos", "Alejo Carpentier", genero="Realismo mágico"),
    Libro("Paradiso", "José Lezama Lima", genero="Experimental", numero_paginas=320)
]

revistas = [
    Revista("Álbum cubano de lo bueno y lo bello", "Febrero 2024", genero="Arte, cultura y estilo de vida"),
    Revista("Revista Cubana de Salud Pública", "Marzo 2024", genero="Científico y de salud pública"),
    Revista("Revista Habanera de Ciencias Médicas", "Enero 2024", genero="Médicos y científicos", numero_paginas=60),
    Revista("Conrado", "Abril 2024", genero="Ensayos, poesía, narrativa y crítica literaria")
]

# Entregar algunos libros y revistas
libros[0].entregar()
libros[2].entregar()
revistas[1].entregar()

# Contar libros y revistas entregados
libros_entregados = sum(libro.isPrestado() for libro in libros)# Esta linea de codigo itera sobre todos los libros y luego suma todos los que estan en True
revistas_entregadas = sum(revista.isPrestado() for revista in revistas)

print(f"Libros entregados: {libros_entregados}")
print(f"Revistas entregadas: {revistas_entregadas}")

# Encontrar el libro con más páginas
libro_mas_paginas = max(libros, key=lambda libro: libro.get_numero_paginas()) # extrae el número de páginas de cada libro utilizando el método get_numero_paginas()
print(f"Libro con más páginas:\n{libro_mas_paginas}")

