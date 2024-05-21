from __future__ import annotations
from abc import ABC, abstractmethod

class State:

    def get_context(self) -> Context:
        return self._context

    def set_context(self, context: Context) -> None:
        self._context = context

    def handle_reset(self) -> None:
        pass

    def handle_coin_insertion(self) -> None:
        pass
    
    def handle_beverage_selected(self) -> None:
        pass

    def handle_red_button_pressed(self) -> None:
        pass


class InitialState(State):
    def handle_coin_insertion(self) -> None:
        print("Coin Inserted")
        self._context.transition_to(CoinInsertedState())

class CoinInsertedState(State):
    def handle_beverage_selected(self) -> None:
        print("Beverage Selected")
        self._context.transition_to(BeverageSelectedState())

class BeverageSelectedState(State):
    def handle_red_button_pressed(self) -> None:
        print("Red Button Pressed (Beverage output assumed)")
        self._context.transition_to(RedButtonPressedState())


class RedButtonPressedState(State):
    def handle_reset(self) -> None:
        print("State Machine Reset")
        self._context.transition_to(InitialState())



class Context:
    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.set_context(self)

    def request_reset(self):
        self._state.handle_reset()

    def request_coin_insertion(self):
        self._state.handle_coin_insertion()

    def request_beverage_selection(self):
        self._state.handle_beverage_selected()

    def request_red_button_press(self):
        self._state.handle_red_button_pressed()
        print("drink is expected to be vended here")
        self._state.handle_reset()        


class Vending_machine:
    # states: initial, coin_inserted, beverage_selected, red_button_pressed
    def __init__(self):
        self._context = Context(InitialState()) 

    def reset(self):
        self._context.request_reset()

    def insert_coin(self):
        self._context.request_coin_insertion()

    def select_beverage(self):
        self._context.request_beverage_selection()

    def press_red_button(self):
        self._context.request_red_button_press()


if __name__ == "__main__":
    m = Vending_machine()

    m.insert_coin()

    m.select_beverage()

    m.press_red_button()
