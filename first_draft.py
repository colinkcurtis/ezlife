import pandas
import argparse


class Importer:
    def __init__(self):
        pass

    @staticmethod
    def import_excel(input_file_name):
        new_file = pandas.read_excel(input_file_name)
        return new_file


if __name__ == "__main__":
    ImporterObject = Importer()

    parser = argparse.ArgumentParser(description=" henlo2")

    parser.add_argument(
        "-f", "--file", help="input file", default="./data/test_input.xlsx",
    )

    args = parser.parse_args()

    if args.file.endswith(".xlsx"):
        test1 = ImporterObject.import_excel(args.file)
        print(type(test1))
