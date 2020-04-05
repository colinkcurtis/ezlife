import pandas
import argparse
import matplotlib.pyplot as plt


class Importer:
    def __init__(self):
        pass

    @staticmethod
    def import_excel(input_file_name):
        """
        read input files from excel, at least for this demonstration
        """
        new_file = pandas.read_excel(input_file_name, index_col=0)
        # sorted_by_percentage = new_file.sort_values(["%"], ascending=False)
        return new_file

    @staticmethod
    def import_csv(input_file_name):
        """
        read input files from excel, at least for this demonstration
        """
        new_file = pandas.read_csv(input_file_name, index_col=0)
        # sorted_by_percentage = new_file.sort_values(["%"], ascending=False)
        return new_file

    @staticmethod
    def export_json(export_file_name):
        """
        export to json format, probably a decent method for the foreseeable future
        """

        return


if __name__ == "__main__":
    ImporterObject = Importer()

    parser = argparse.ArgumentParser(description=" hello")

    parser.add_argument(
        "-f", "--file", help="input file", default="./data/test_file_csv.csv",
    )

    args = parser.parse_args()

    if args.file.endswith(".xlsx"):
        new_file = ImporterObject.import_excel(args.file)
        # new_file.to_csv("./test_file_csv.csv")
        new_file.head(10).plot(kind="barh")
        plt.show()
        print()
        print(new_file.shape)
        print()
        print(new_file.head())

    elif args.file.endswith(".csv"):
        new_file = ImporterObject.import_csv(args.file)
        # new_file.to_csv("./test_file_csv.csv")
        new_file.head(10).plot(kind="barh")
        plt.show()
        print()
        print(new_file.shape)
        print()
        print(new_file.head())
