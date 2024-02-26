import unittest


def write_lat_eng_dict(output_name, input_dict):
    with open(f"{output_name}", "w") as output:
        for key, values in input_dict.items():
            pretty_values = ", ".join(values)
            output.write(f"{key} - {pretty_values}\n")


def generate_lat_eng_dict(input_dict, key, values):
    for value in values.split(", "):
        if value not in input_dict:
            input_dict[value] = [key]
        else:
            input_dict[value].append(key)


def translate_dict(filename, output_name):
    lat_eng_dict = {}
    try:
        with open(filename, mode="r") as file:
            for line in file.readlines():
                key, values = line.strip().split(" - ")
                generate_lat_eng_dict(lat_eng_dict, key, values)
    except FileNotFoundError:
        raise Exception(f"File with filename {filename} doesn't' exist")

    sorted_dict = dict(sorted(lat_eng_dict.items(), key=lambda items: items[0]))
    write_lat_eng_dict(output_name, sorted_dict)


class TestLatinEnglishDict(unittest.TestCase):
    def test_example(self):
        translate_dict(
            "test/latin-english-dict.txt",
            "test/latin-english-dict-test.out")
        self.assertListEqual(
            list(open("test/latin-english-dict-test.out")),
            list(open("test/latin-english-dict.out")))

    def test_empty_file(self):
        translate_dict(
            "test/empty-dict.txt",
            "test/empty-dict-test.out")
        self.assertListEqual(
            list(open("test/empty-dict-test.out")),
            list(open("test/empty-dict.out")))


if __name__ == "__main__":
    unittest.main()
