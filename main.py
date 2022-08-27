from utils import wrong_choice
from rot13_decoder import Rot13
from caesar_decoder import Caesar

def exit_decoder() -> str:
    return "Niestety wychodzimy z programu. Do widzenia!"


# Wszystko co wykonalismy to -> wzorzec projektowy fasada
def main_executor() -> None:
    while True:
        # User inputs
        cipher_choice: str = input("1.ROT13\n2.Cesar\n3.Exit\n")
        #text_to_decode: str = input("Provide text: ")

        available_ciphers = {
            "1": Rot13().show_menu,
            "2": Caesar().show_menu,
            "3": exit_decoder
        }

        print(available_ciphers.get(cipher_choice, wrong_choice)())

if __name__ == '__main__':
    main_executor()

