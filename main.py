import numpy as np
import pandas as pd


# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    data = pd.read_csv(filepath_or_buffer=".\\resources\\analcatdata_bankruptcy.csv")

    print(len(data))
    print(data.size)
    print(data.values)
    print(data.columns)

    print(data)
