#!/usr/bin/env python3
from textshuffler import RandomizedWordsRearranger, SortedWordsRearranger

import unittest

class RearrangerTests(unittest.TestCase):
    def test_random_basic(self):
        rearranger = RandomizedWordsRearranger(100500)
        self.assertEqual(rearranger.rearrange_text('I love the smell of napalm in the morning'), 'I lvoe the smlel of nlaapm in the morning')


    def test_random_with_repetion(self):
        src = 'hellooooooooooooooooooooo it is a sentence with a word with manymanymanymanymany characters'
        res_list = [
            'hoooeoooooooloooooloooooo it is a snetnece with a word wtih maynyynmmnaaanmynamy chcaaertrs',
            'hoooooooooooooooleooloooo it is a scneente wtih a wrod with mmmaanyanmyaynmnyany chaaerrtcs',
            'hoooooooooooooolooooeoloo it is a snncteee wtih a wrod with mynmnnnamaamynamayyy ccarerahts',
            'hooooooooooooloooleoooooo it is a setnncee wtih a word with manaanaymmnnmynamyyy crtacahres',
            'hoooloeoooooooolooooooooo it is a secnetne wtih a word wtih mmymmanynayynmaaanny cechtraras',
            'hooooooollooooooeoooooooo it is a scnnetee with a word with mmnymaynnannmaymyaay ceahtrcars',
            'hoooooooooooloooooolooeoo it is a stceenne wtih a word wtih mmannnynmnyyayaammay chaaretcrs',
            'heooolooooooooooolooooooo it is a snenecte with a wrod wtih mamanyymyaaynmnmnany crrhatcaes',
            'hooloooooeooooooooooloooo it is a scenetne with a word with mymmnanayaynmnmnaayy carhcaerts',
            'hoooooooooooooelooloooooo it is a scentene with a wrod with mnnmnmyanynaaaammyyy cctrhaeras',
            'hooooooooooeolooooooolooo it is a sncneete with a wrod wtih myaamyynmamnnnnamyay crcretahas',
            'hooooloooooooooooloooooeo it is a snetcene wtih a word with myyaaaamnymnmnamnyny crtcraehas'
        ]

        for _ in range(4):
            rearranger = RandomizedWordsRearranger(100500)
            for res in res_list:
                self.assertEqual(rearranger.rearrange_text(src), res)


    def test_sorted_basic(self):
        rearranger = SortedWordsRearranger()

        self.assertEqual(rearranger.rearrange_text('I love the smell of napalm in the morning'), 'I love the selml of naalpm in the minnorg')


    def test_sorted_with_repetion(self):
        src = 'hellooooooooooooooooooooo it is a sentence with a word with manymanymanymanymany characters'
        res = 'hellooooooooooooooooooooo it is a sceennte with a word with maaaaammmmnnnnnyyyyy caacehrrts'

        for _ in range(4):
            rearranger = SortedWordsRearranger()

            for _ in range(20):
                self.assertEqual(rearranger.rearrange_text(src), res)


if __name__ == '__main__':
    unittest.main()