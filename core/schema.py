import graphene
from graphene_django import DjangoObjectType
from books.models import Book


# Modelo que indica a GraphQL qué datos debe devolver, está relacionado al models de la app books de Django
class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "description", "created_at", "updated_at")


# Clase para crear registros en la BBDD
class CreateBookMutation(graphene.Mutation):
    # Argumentos que se espera recibir desde el cliente
    class Arguments:
        title = graphene.String()
        description = graphene.String()

    # Retorna la información del registro nuevo almacenado en BBDD
    book = graphene.Field(BookType)

    # Método para registrar los nuevos datos en la BBDD
    def mutate(self, info, title, description):
        book = Book(title=title, description=description)
        book.save()
        return CreateBookMutation(book=book)        # Devuelve la instancia de la ejecución de la clase CreateBookMutation, es decir, los datos nuevos almacenados en la BBDD


# Clase para eliminar registro en la BBDD
class DeleteBookMutation(graphene.Mutation):
    # Argumento que se espera recibir desde el cliente
    class Arguments:
        id = graphene.ID(required=True)

    # # Retorna la información del registro eliminado en BBDD
    # book = graphene.Field(BookType)

    # Retorna un mensaje
    message = graphene.String()

    # Método para eliminar dato en la BBDD
    def mutate(self, info, id):
        book = Book.objects.get(pk=id)
        book.delete()
        return DeleteBookMutation(message="Book deleted")       # Devuelve la instancia de la ejecución de la clase DeleteBookMutation, es decir, el mensaje Book deleted al borrar el registro en la BBDD


# Clase para modificar registro en la BBDD
class UpdateBookMutation(graphene.Mutation):
    # Argumento que se espera recibir desde el cliente
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()

    # Retorna la información del registro modificado en BBDD
    book = graphene.Field(BookType)

    # Método para modificar registro en la BBDD
    def mutate(self, info, id, title, description):
        book = Book.objects.get(pk=id)
        book.title = title
        book.description = description
        book.save()
        return UpdateBookMutation(book=book)        # Devuelve la instancia de la ejecución de la clase UpdateBookMutation, es decir, el registro modificado en la BBDD


# Clase para devolver información del backend al cliente
class Query(graphene.ObjectType):
    """
        Posibles query que se pueden realizar por el cliente:
            hello: devuelve un mensaje de Hello!
            books: devuelve una lista con todos los datos almacenados en la BBDD
            book: devuelve el registro especificado por su id desde la BBDD
    """
    hello = graphene.String(default_value="Hello!")
    books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.ID())

    # Método para devolver al cliente todos los datos almacenados en la BBDD
    def resolve_books(self, info):
        return Book.objects.all()

    # Método para devolver al cliente el dato especificado por su id desde la BBDD
    def resolve_book(self, info, id):
        return Book.objects.get(pk=id)


# Clase para recibir información del cliente al backend
class Mutation(graphene.ObjectType):
    create_book = CreateBookMutation.Field()        # Con Field se convierte en una mutación
    delete_book = DeleteBookMutation.Field()        # Con Field se convierte en una mutación
    update_book = UpdateBookMutation.Field()        # Con Field se convierte en una mutación


# Nuevas query/consultas se deben agregar al Schema
schema = graphene.Schema(query=Query, mutation=Mutation)
