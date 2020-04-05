import pandas
import argparse
import matplotlib.pyplot as pyplot


class ezlife:
    def __init__(self):
        pass


    @staticmethod
    def import_csv(input_file_name):
        """
        read input files from excel, at least for this demonstration
        """
        new_file = pandas.read_csv(input_file_name, index_col=0)
        print(new_file)

        return new_file



if __name__ == "__main__":
    ezlife = ezlife()

    parser = argparse.ArgumentParser(description=" hello")

    parser.add_argument(
        "-f", "--file", help="input file", default="./data/test_input.csv",
    )

    args = parser.parse_args()

    new_file = ezlife.import_csv(args.file)
