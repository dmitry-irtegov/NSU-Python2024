import unittest


def translate_dict(filename):
    lat_eng_dict = {}

    def write_lat_eng_dict(dict):
        output_name = filename.split('.')[0]
        with open(f"{output_name}.out", "w") as output:
            for key, values in dict.items():
                pretty_values = ", ".join(values)
                output.write(f"{key} - {pretty_values}\n")

    def generate_lat_eng_dict(key, values):
        for value in values.split(", "):
            if value not in lat_eng_dict:
                lat_eng_dict[value] = [key]
            else:
                lat_eng_dict[value].append(key)

    try:
        with open(filename, mode="r") as input:
            for line in input.readlines():
                key, values = line.strip().split(" - ")
                generate_lat_eng_dict(key, values)
    except FileNotFoundError:
        raise Exception(f"File with filename {filename} doesn't' exist")

    sorted_dict = dict(sorted(lat_eng_dict.items(), key=lambda items: items[0]))
    write_lat_eng_dict(sorted_dict)


if __name__ == "__main__":
    translate_dict("latin-english-dict.txt")
