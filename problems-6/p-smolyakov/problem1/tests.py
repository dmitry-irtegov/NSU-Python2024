#!/usr/bin/env python3
from textshuffler import RandomizedWordsRearranger, SortedWordsRearranger

import unittest

class RearrangerTests(unittest.TestCase):
    def test_random_basic(self):
        rearranger = RandomizedWordsRearranger(100500)
        self.assertEqual(rearranger.rearrange_text('I love the smell of napalm in the morning.'), 'I lvoe the smlel of nlaapm in the morning.')


    def test_random_with_repetion(self):
        src = 'Mmyy kkeeyybbooaarrdd ttyyppeess eevveerryytthhinngg ttwwiiccee!!!!!! hheellpp,, pplleeassee!!!!!!'
        res_list = [
            'Mymy kkeyoaaebrydbord tpeyetypss eyvthieevnnhygrtreg tccwiiewte!!!!!! hlhleepp,, plpeeeslase!!!!!!',
            'Mmyy kbeedyboararkoyd tpyeyestps eentiryyhgerhevnvtg tcteciwiwe!!!!!! hllpeehp,, ppsleelseae!!!!!!',
            'Mmyy kyreybbeaaokdrod tyyeepptss ervyvgrhttyneeihneg ttcewiwice!!!!!! hleelhpp,, peespllsaee!!!!!!',
            'Mmyy kbbkoodeerayaryd tspytpeeys eveyrgrheeiynthntvg twcwiitece!!!!!! hllhpeep,, ppsseelleae!!!!!!',
            'Mmyy kardeaybkboryeod teeytpsyps eenhiyhygvrrttneveg twwicteice!!!!!! helphelp,, peeelspslae!!!!!!',
            'Mymy kdyokabearboeyrd tteseppyys evivhenternhegyrytg tciceiwtwe!!!!!! hphellep,, pleepslasee!!!!!!',
            'Mmyy kroybbreakoydead teepyytsps egeirenhtrventyyhvg ticcwwtiee!!!!!! hhllpeep,, peaepseslle!!!!!!',
            'Mymy kokeboabeyraydrd typtsypees engvnvhthereyteryig twetwciice!!!!!! hllheepp,, pespelasele!!!!!!',
            'Mymy kbokydreeyraobad typpteesys evetyhvyhnigterrneg tietiwcwce!!!!!! hehleplp,, peelespalse!!!!!!',
            'Mymy kaybakryoroeedbd tetpyyepss enhgivynhyterrevteg tiwtewcice!!!!!! helhplep,, pepsleeslae!!!!!!',
            'Mymy kaoerekbyryabodd tpyeeystps evyyneirvgterhntheg tiiwtccwee!!!!!! helehlpp,, paeleslsepe!!!!!!',
            'Mymy kayodaeyerrkobbd tteppyeyss eternhvyteirhnygevg twictewcie!!!!!! hhellepp,, pseeeasplle!!!!!!',
            'Mmyy krbodbaeakryyoed typytspees ennhvriyeytrehgetvg twewtciice!!!!!! hehllepp,, psseeeaplle!!!!!!',
            'Mymy kyakoabrrbdoeyed typyepstes evgryrvytinehenethg tiictewcwe!!!!!! hlelhepp,, papselselee!!!!!!',
            'Mymy kboerroykdbyaead teepystpys evnygntrhiteevyehrg ticcwtiwee!!!!!! heelhlpp,, peelsspleae!!!!!!',
            'Mymy kbaoerdrabeykyod tyeeystpps egyyehtnetrhivnrveg ttiwcecwie!!!!!! hpehlelp,, pesslpeaele!!!!!!',
            'Mymy kkdberoaboerayyd typetspyes enetiyrterhvynvhegg tiecciwwte!!!!!! heelhplp,, pllsaeespee!!!!!!',
            'Mmyy kkrreyeobboadyad typteeysps ernntrghheyyitevveg tiwteiccwe!!!!!! hlehpelp,, pesleseaple!!!!!!',
            'Mymy kbooaekrryyebadd tpetsyyeps etehvvrtnhinyryeegg tewctwicie!!!!!! hpelelhp,, pelasspleee!!!!!!',
            'Mmyy kbyedaeyorobrkad tyetpseyps eryiyvhnvetehngertg ttwciecwie!!!!!! hllheepp,, pasleseplee!!!!!!'
        ]

        for _ in range(4):
            rearranger = RandomizedWordsRearranger(100500)
            for res in res_list:
                self.assertEqual(rearranger.rearrange_text(src), res)


    def test_sorted_basic(self):
        rearranger = SortedWordsRearranger()

        self.assertEqual(rearranger.rearrange_text('I love the smell of napalm in the morning.'), 'I love the selml of naalpm in the minnorg.')


    def test_sorted_with_repetion(self):
        src = 'Mmyy kkeeyybbooaarrdd ttyyppeess eevveerryytthhinngg ttwwiiccee!!!!!! hheellpp,, pplleeassee!!!!!!'
        res = 'Mmyy kaabbdeekoorryyd teeppstyys eeeeghhinnrrttvvyyg tcceiitwwe!!!!!! heehllpp,, paeeellpsse!!!!!!'

        for _ in range(4):
            rearranger = SortedWordsRearranger()

            for _ in range(5):
                self.assertEqual(rearranger.rearrange_text(src), res)


if __name__ == '__main__':
    unittest.main()
