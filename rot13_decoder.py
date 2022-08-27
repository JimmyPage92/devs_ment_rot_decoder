"""The program 'rot-decoder' is used for encoding and decoding the text given by the user according to the operation of
the so-called Caesar's cipher, i.e. the replacement of a particular character in the Latin alphabet by a character
occurring 13 places after it"""
import sys

from utils import wrong_choice
from inspect import cleandoc


# print(cleandoc(
#     """
#     HELLO
#     HELLO
#     """))

class Rot13:
    """Class that will handle the text decoding according to the ROT13 code rule.

    Attributes:
        output_msg: Decoded message provided by user.
    """

    def __init__(self) -> None:
        self.output_msg: str = ""

    def describe_rot13(self) -> str:

        return cleandoc(
            """
            -----Hello user! Now You are in a program called 'rot-decoder' which is used to decode and decode
            text according to the operation of the so-called ROT-13-----
            ************************************************************
            ROT-13 cipher involves replacing a particular character in the Latin alphabet with
            character occurring 13 places after it.
            -----Dear user in this program You can:
            - encoding the text You provide
            or
            - decoding the text You provided
            <><><><><><><><><><><><><><><><><><><>
            <><><><><><><><><><><><><><><><><><><>
            <><><><><><><><><><><><><><><><><><><>
            So now let's check how working program :)  
            """)

    def show_menu(self) -> None:
        print(self.describe_rot13())

        user_menu_choice: str = input("1.Encode\n2.Decode\n3.Exit\n")
        user_provided_text: str = input("Provide text: ")

        available_options = {
            "1": self.execute_rot13_algo,
            "2": self.execute_rot13_algo,
            "3": sys.exit}  # TODO IN ceaser try list solution

        print(available_options.get(user_menu_choice, wrong_choice)(user_provided_text))

    def execute_rot13_algo(self, user_input: str) -> None:
        """Function that decodes/encodes text entered by user.

        :param user_input: Text entered by user to decode.
        :return: decoded text entered by user
        """
        # TODO Provide for uppercase also, use modulo % 26
        for letter in user_input.lower():
            letter_position: int = ord(letter)
            if letter_position <= 109:
                self.output_msg += chr(letter_position + 13)
            else:
                self.output_msg += chr(letter_position - 13)
        print(self.output_msg)

    def save_results(self) -> None:
        with open("ROT13.txt", "a") as file:
            file.write(self.output_msg)
            file.write('\n')

    def return_output(self):
        return f"Your decoded text is - {self.output_msg}"

