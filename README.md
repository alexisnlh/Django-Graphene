# [![Django](https://skillicons.dev/icons?i=django,graphql&perline=3)](https://skillicons.dev) Django GraphQL tutorial con Graphene (CRUD)

> ℹ️ Aplicación basada en el [tutorial](https://www.youtube.com/watch?v=cultgNYc1DE&t=1980s) impartido por Fazt Code

API sencilla con operaciones CRUD utilizando un modelo de Python llamado Graphene. La aplicación será relacionada a libros donde se pueden realizar las siguientes consultas:
* Consultar todos los libros registrados devolviendo el *id*, el *título del libro*, la *descripción*, la *fecha de creación* y de *modificación*.
* Consultar un libro específico indicando su *id* y devolviendo la información completa de este o la especificada.
* Crear un libro nuevo indicando el *título* y la *descripción*, devolviendo su información completa.
* Eliminar un libro indicando su *id*, devolviendo un mensaje general.
* Modificar un libro indicando su *id*, el *título* y la *descripción*, devolviendo su información completa.

### Estructura del código
> *Dentro del código se puede encontrar comentarios para cada línea o proceso que es importante mencionar su utilidad.*

La API consta de un schema de GraphQL ubicado en el directorio core/schema.py. Es en este schema que se encuentran todas las clases/models relacionados a las query permitidas por la API.

Se ha utilizado un sistema de gestión de bases de datos SQLite.

Las posibles query se ubican en el Query_example.txt