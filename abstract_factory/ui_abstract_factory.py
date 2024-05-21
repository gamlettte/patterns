class AbstractButton:

    def press(self) -> str:
        pass


class MacButton(AbstractButton):

    def press(self) -> str:
        return "Mac button pressed"


class WindowsButton(AbstractButton):

    def press(self) -> str:
        return "Windows button pressed"


class LinuxButton(AbstractButton):

    def press(self) -> str:
        return "Linux button pressed"



class AbstractField:

    def input(self, string: str) -> str:
        pass


class MacField(AbstractField):

    def input(self, string: str) -> str:
        return f"Mac field accepted {string}"


class WindowsField(AbstractField):

    def input(self, string: str) -> str:
        return f"Windows field accepted {string}"


class LinuxField(AbstractField):

    def input(self, string: str) -> str:
        return f"Linux field accepted {string}"


class UiAbstractFactory:

    def create_button(self) -> AbstractButton:
        pass

    def create_field(self) -> AbstractField:
        pass


class MacUiAbstractFactory(UiAbstractFactory):

    def create_button(self) -> MacButton:
        return MacButton()

    def create_field(self) -> MacField:
        return MacField()
 

class WindowsUiAbstractFactory(UiAbstractFactory):

    def create_button(self) -> WindowsButton:
        return WindowsButton()

    def create_field(self) -> WindowsField:
        return WindowsField()
 

class LinuxUiAbstractFactory(UiAbstractFactory):

    def create_button(self) -> LinuxButton:
        return LinuxButton()

    def create_field(self) -> LinuxField:
        return LinuxField()



def client_code(factory: UiAbstractFactory) -> None:
    button = factory.create_button()
    field = factory.create_field()

    print(f"Abstract button pressed: {button.press()}")
    hw = "hello world"
    print(f"Abstract field used with \"hello world\": {field.input(hw)}")


if __name__ == "__main__":
    print("mac client tests ui:")
    client_code(MacUiAbstractFactory())
    print("\n")

    print("windows client tests ui:")
    client_code(WindowsUiAbstractFactory())
    print("\n")

    print("linux client tests ui:")
    client_code(LinuxUiAbstractFactory())
    print("\n")
