class Product():

    def get_parts_str(self) -> str:
        pass


class SomeScreen(Product):

    def __init__(self) -> None:
        self._parts = []

    def add(self, part: any) -> None:
        self._parts.append(part)

    def get_parts_str(self) -> str:
        return f"Product parts: {', '.join(self._parts)}"


class Builder:

    def release_product(self) -> Product:
        pass

    def add_initial_screen(self) -> None:
        pass

    def add_corner_menu(self) -> None:
        pass

    def add_specific_button(self) -> None:
        pass



class SpecificBuilder(Builder):

    def reset(self) -> None:
        self._screen = SomeScreen()

    def __init__(self) -> None:
        self.reset()

    def release_product(self) -> SomeScreen:
        screen = self._screen
        self.reset()
        return screen

    def add_initial_screen(self) -> None:
        self._screen.add("initial screen")

    def add_corner_menu(self) -> None:
        self._screen.add("corner menu")

    def add_specific_button(self) -> None:
        return self._screen.add("specific button")



class Director:

    def __init__(self) -> None:
        pass

    def set_builder(self, builder: Builder) -> None:
        self._builder = builder

    def get_builder(self) -> Builder:
        return self._builder

    def build_minimal_usable_ui(self) -> None:
        self._builder.add_initial_screen()

    def build_full_featured_ui(self) -> None:
        self._builder.add_initial_screen()
        self._builder.add_corner_menu()
        self._builder.add_specific_button()


if __name__ == "__main__":

    screen_director = Director()
    screen_builder = SpecificBuilder()
    screen_director.set_builder(screen_builder)

    print("Simplest product: ")
    screen_director.build_minimal_usable_ui()
    print(screen_director.get_builder()
                         .release_product()
                         .get_parts_str())
    print("\n")

    print("Full featured product: ")
    screen_director.build_full_featured_ui()
    print(screen_director.get_builder()
                         .release_product()
                         .get_parts_str())
    print("\n")

    print("Builder custom product: ")
    screen_builder.add_initial_screen()
    screen_builder.add_specific_button()
    print(screen_builder.release_product().get_parts_str())
    print("\n")
