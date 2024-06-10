import os
import unittest

from cipher.table.cipher import TableCipher
from cipher.table.decrypter import FrequencyDecrypter
from cipher.table.entity.key import TableKey
from cipher.table.entity.text import TableText


class DecrypterTest(unittest.TestCase):

    def test_vote_decrypter(self):
        os.chdir("..")
        decoder = FrequencyDecrypter()
        key = TableKey("wvmpqydznkhgfcabjiruxelsot")
        text = """"
        Joanna walked all the way to the capital city. 
        She pushed a wooden cart full of stone fruit. She carried with her a beautiful wooden market stall. 
        The stall had belonged to her mother, and before that to Joanna's grandmother. On this stall, 
        she would sell her fruit. When she finally arrived at the city, she was very tired after months 
        on the road. But the stone fruit were almost ripe. So far, her plan was working.
        Of course, there was a tax to enter the city gates. And there were market fees to pay. Plus, 
        it wasn't easy to sell strange, new foods like hers at the market. The fruit had to be tested 
        to prove it was safe to eat. The tests were not cheap and they took days to do.
        """
        encrypted_text = TableCipher.encrypt(TableText(text), key=key)
        decrypted_text = decoder.decode(encrypted_text)
        print(decrypted_text)
