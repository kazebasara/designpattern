#! /usr/bin/env python3
from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    """
    The creator class declares the factory method 
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default
        implementation of the factory method 
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now , use the product
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result


class ConcreteCreator1(Creator):
    """
    Note that
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
    The Product interface
    """

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"

def client_code(creator: Creator) -> None:
    """
    The client code
    """

    print(f"Client: I'm no aware of the creator's class, but it still works.\n"
            f"{creator.some_operation()}", end="")
    
if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")
    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
    
