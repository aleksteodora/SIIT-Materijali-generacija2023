import pandas as pd
from sklearn.model_selection import train_test_split
from utils_nans1 import *
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sb
import statsmodels.api as sm


matplotlib.rcParams['figure.figsize'] = (8, 3)
sb.set(font_scale=1.)

TRAIN_PATH = "data/train.csv"
TEST_PATH = "data/test.csv"
Y_COL = "AirPollution"

# zadatak 1
# zadatak 2
# zadatak 3

def zad12():
    df = pd.read_csv(TRAIN_PATH)
    df = df.dropna()
    
    x = df.drop(columns=[Y_COL])
    y = df[Y_COL]   
    model = get_fitted_model(x, y)

    df_test = pd.read_csv(TEST_PATH)
    x_test = df_test.drop(columns=[Y_COL])
    y_test = df_test[Y_COL]

    r2 = get_rsquared(model, x_test, y_test)
    print(f"R**2 ad = {r2}")

    min_v, max_v = get_conf_interval(model, "TrafficDensity")
    print(f"min: {min_v}, max: {max_v}")
    
    # Add constant term for independence check since model was fitted with constant
    ind, v = independence_of_errors_assumption(model, sm.add_constant(x), y)
    if ind is None:
        print(f"Validno, value {v}")
    else:
        print(f"Nije validno, value {v}")



def zad3():
    cols_to_drop = []
    df = pd.read_csv(TRAIN_PATH)
    # print(check_for_missing_values(df)) TrafficDensity GreenSpace
    # df = df.drop(columns=cols_to_drop) 

    df["TrafficDensity"] = df["TrafficDensity"].interpolate(method="linear", limit_direction="both")
    df["GreenSpace"] = df["GreenSpace"].interpolate(method="linear", limit_direction="both")
    
    
    x = df.drop(columns=[Y_COL])
    y = df[Y_COL]   
    x_tr, x_vl, y_tr, y_vl = train_test_split(x, y, test_size=0.9, shuffle=True, random_state=42)
    model = get_fitted_model(x_tr, y_tr)

    df_test = pd.read_csv(TEST_PATH)
    # df_test = df_test.drop(columns=cols_to_drop)

    x_test = df_test.drop(columns=[Y_COL])
    y_test = df_test[Y_COL]

    r2_adj_val = get_rsquared_adj(model, x_vl, y_vl)
    print(r2_adj_val)
    r2_adj_test = get_rsquared_adj(model, x_test, y_test)
    print(r2_adj_test)
    print(f"{r2_adj_test} >= 0.50 is {r2_adj_test >= 0.50}")
    print(f"LINE is {are_assumptions_satisfied(model, x_vl, y_vl)}")

if __name__ == "__main__":
    # zad12()
    zad3()