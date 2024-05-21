# electronics, clothes, books

class Product:

    def operation(self) -> str:
        pass


class Electronics(Product):

    def operation(self) -> str:
        return "result of operation in electronics"


class Clothes(Product):

    def operation(self) -> str:
        return "result of operation in clothes"


class Books(Product):

    def operation(self) -> str:
        return "result of operation in books"



class Creator:

    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()

        result = f"creator: operation done with: {product.operation()}"
        return result


class ElectronicsCreator(Creator):

    def factory_method(self) -> Product:
        return Electronics()


class ClothesCreator(Creator):

    def factory_method(self) -> Product:
        return Clothes()


class BooksCreator(Creator):

    def factory_method(self) -> Product:
        return Books()


def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("Main code: Books creation.")
    client_code(BooksCreator())
    print("\n")

    print("Main code: Electronics creation.")
    client_code(ElectronicsCreator())
    print("\n")

