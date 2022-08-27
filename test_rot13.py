# unittest | pytest
import unittest
from os import path # do sprawdzenia czy sie zapisuje do pliku /PATH/

from rot13_decoder import Rot13


class TestRot13(unittest.TestCase):

    def setUp(self) -> None:
        self.rot13 = Rot13()

    def test_execute_rot13_algo_encoding(self):
        self.rot13.execute_rot13_algo(user_input="test")
        self.assertEqual("grfg", self.rot13.output_msg,
                         msg="Testing execute_rot13_algo() encoding on inputted text 'test'")

        self.rot13.output_msg: str = ""  # Clear last generated results
        self.rot13.execute_rot13_algo(user_input="unitest")
        self.assertEqual("havgrfg", self.rot13.output_msg,
                         msg="Testing execute_rot13_algo() encoding on inputted text 'unitest'")

    def test_is_rot13_txt_exist_after_encoding_user_input(self):
        # Simulate working of rot13 encoder with saving
        self.rot13.save_results()

        self.assertTrue(path.exists("rot13.txt"), msg="Should return True if rot13.txt file exits.")
