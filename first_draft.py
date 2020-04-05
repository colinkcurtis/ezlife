import pandas
import argparse


class Importer:
    def __init__(self):
        pass

    @staticmethod
    def import_excel(input_file_name):
        """
        read input files from excel, at least for this demonstration
        """
        new_file = pandas.read_excel(input_file_name)
        return new_file

    @staticmethod
    def export_json(export_file_name):
        """
        export to json format, probably a decent method for the foreseeable future
        """

        test = 5
        return


if __name__ == "__main__":
    ImporterObject = Importer()

    parser = argparse.ArgumentParser(description=" henlo2")

    parser.add_argument(
        "-f", "--file", help="input file", default="./data/new_test_input.xlsx",
    )

    args = parser.parse_args()

    if args.file.endswith(".xlsx"):
        new_file = ImporterObject.import_excel(args.file)
        print(new_file.head())
