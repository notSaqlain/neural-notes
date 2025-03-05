
# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numba.core.cgutils import true_bit
from sklearn.linear_model import LinearRegression

def main():
    # download and prepare the data
    data_root = "github.com/ageron/data/raw/main/"
    lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")

    x = lifesat[["GDP per capita (USD)"]].values
    y = lifesat[["Life satisfacation"]].values

    # Visualize the data
    lifesat.plot(kind="scatter", grid=True, x = "GDP per capita (USD)", y = "Life satisfacation")
    plt.axis([23_500, 62_500, 4, 9])
    plt.show()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


