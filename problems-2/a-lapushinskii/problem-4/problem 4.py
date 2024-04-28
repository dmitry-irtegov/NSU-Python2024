import unittest

def find_sequences(filename, sequence, chunk_size = 4096):
    overlap = len(sequence) - 1
    positions = []
    overall_index = 0
    try:
        with open(filename, 'r') as file:
            chunk = file.read(chunk_size).replace("\n", "")
            previous_tail = ''
        
            while chunk:
                working_chunk = previous_tail + chunk
               
                index = working_chunk.find(sequence)
                while index != -1:
                    positions.append(overall_index + index)
                    index = working_chunk.find(sequence, index + 1)

                overall_index += max(len(working_chunk)-overlap, 0)
                previous_tail = working_chunk[-overlap:]
                chunk = file.read(chunk_size).replace("\n", "")
    except Exception :
        print(f"problem with reading {filename}.")   
    return positions


def find_sequences_in_pi():
    sequence = input()
    positions = find_sequences("pi.txt", sequence)
    print(f"Found {len(positions)} results.")
    if positions:
        print(f"Positions: {' '.join(map(str, positions[:5]))} ...")

###
class TestPiSequence(unittest.TestCase):
    def test_base(self):
        positions = find_sequences("pi.txt", "15")
        self.assertEqual(4, positions[0])
    def test_probably_unique(self):
        sequence = "021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989380952572010654858632788659361533818279682303019520353018529689957736225994138912497217752834791315155748572424541506959508295331168617278558890750983817546374649393192550604009277016711390098488240128583616035637076601047101819429555961989467678374494482553797747268471040475346462080466842590694912933136770289891521047521620569660240580381501935112533824300355876402474964732639141992726042699227967823547816360093417216412199245863150"
        positions = find_sequences("pi.txt", sequence)
        self.assertEqual(78 * 7, positions[0])
        self.assertEqual(1, len(positions))
    def test_not_enough_chunk(self):
        sequence = "1415926535897"
        positions = find_sequences("pi.txt", sequence)
        positions_small_chunk = find_sequences("pi.txt", sequence, 5)
        self.assertEqual(positions, positions_small_chunk)
        self.assertEqual(positions, positions_small_chunk)
        self.assertEqual(2, positions_small_chunk[0])
    def test_too_much_chunk(self):
        sequence = "1415926535897"
        positions = find_sequences("pi.txt", sequence)
        positions_big_chunk = find_sequences("pi.txt", sequence, 8000000)
        self.assertEqual(positions, positions_big_chunk)
        self.assertEqual(positions, positions_big_chunk)
        self.assertEqual(2, positions_big_chunk[0])
        
if __name__ == '__main__':
     unittest.main()
    
