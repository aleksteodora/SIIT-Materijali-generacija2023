import pandas as pd
from sklearn.model_selection import train_test_split
from utils_nans1 import *
import matplotlib.pyplot as plt


matplotlib.rcParams['figure.figsize'] = (8, 3)
sb.set(font_scale=1.)

#zadatak 1

df = pd.read_csv('./data/train.csv')
df = df.dropna()

x = df.drop(columns = ['test_score'])
y = df['test_score']

#print(df)

model = get_fitted_model(x, y)

df_test = pd.read_csv('./data/test.csv')
df_test = df_test.dropna()

x_test = df_test.drop(columns = ['test_score'])
y_test = df_test['test_score']

rmse = get_rmse(model, x_test, y_test)
print(rmse)


#razlika
# get_pred_interval pravis novi model!!!!!!
x = df['study_hours']
y = df['test_score']

model = get_fitted_model(x,y)
min, maks = get_pred_interval(model,1, p_value_trash=0.05)


#zadatak 2
min_study, max_study = get_conf_interval(model, 'study_hours', alpha = 0.05)
print('min')
print(min_study)
print('max')
print(max_study)

autocorr = independence_of_errors_assumption(model, sm.add_constant(x), y, plot = None)
if autocorr is None:
    print('validna')
else:
    print('nije validna')
    


#zadatak 3
df = pd.read_csv('./data/train.csv')

#resavas null vrednosti, interpolacija(spline, linear), srednja vrednost
print(check_for_missing_values(df))

df['previous_test_scores'] = df['previous_test_scores'].interpolate(method = 'linear', limit_direction = 'both')
df['statistics_course'] = df['statistics_course'].interpolate(method ='spline', order = 3,  limit_direction = 'both')

#korelacija
print(perfect_collinearity_assumption(df))

df = df.drop(columns = ['anxiety_level', 'mathematics_course'])

x = df.drop(columns=['test_score'])
y = df['test_score']
x_train, x_val, y_train, y_val = train_test_split(x, y, train_size=0.8, shuffle=True, random_state=50)

model = get_fitted_model(x_train, y_train)
print(model.summary())

print(are_assumptions_satisfied(model, x_train, y_train))

val_rmse = get_rmse(model, x_val, y_val)
print(val_rmse)

df_test = pd.read_csv('./data/test.csv')
x_test = df_test.drop(columns = ['test_score', 'anxiety_level', 'mathematics_course', 'statistics_course', 'stress_level', 'secondary_school'])
y_test = df_test['test_score']

rmse3 = get_rmse(model, x_test, y_test)
print(rmse3)