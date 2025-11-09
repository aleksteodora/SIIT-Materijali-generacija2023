
import pandas as pd
from sklearn.model_selection import train_test_split
from utils_nans1 import *


#zad1

df = pd.read_csv('./data/train.csv', sep = ',')
df = df.dropna()
#print(check_for_missing_values(df))
print(df.head())

x = df.drop(columns=['Test Score'])
y = df['Test Score']

model = get_fitted_model(x, y)

df_test = pd.read_csv('./data/test.csv', sep = ',')
x_test = df_test.drop(columns=['Test Score'])
y_test = df_test['Test Score']
test_adj_r2 = get_rsquared_adj(model, x_test, y_test)
print(f'Mera prilagodjeni r2: {test_adj_r2:.2f}')



#zad2

x = df['Sleep Hours']
y = df['Test Score']
model = get_fitted_model(x, y)
# s obzirom da trazimo izmedju kojih vrednosti se nalazi y ako imamo datu konkretnu vrednost x(8 sati spavanja), koristimo interval predikcije
low, high = get_pred_interval(model, 8, p_value_trash=0.05)
print(f'Minimalni rezultat na testu: {low:.2f}')

#zad3

df = pd.read_csv('./data/train.csv', sep=',')
#print(df.head())
df['Previous Scores'] = df['Previous Scores'].interpolate(method='linear', limit_direction='both')
df['Sleep Hours'] = df['Sleep Hours'].interpolate(method='spline', order = 2, limit_direction='both')

#zbog savrsene kolinearnosti u matrici korelacije
df = df.drop(columns=['Questions Practiced', 'Questions Skipped'])
#print(perfect_collinearity_assumption(df))

x = df.drop(columns=['Test Score'])
y = df['Test Score']

x_train, x_val, y_train, y_val = train_test_split(x, y, train_size=0.7, shuffle=True, random_state=123)

model = get_fitted_model(x_train, y_train)
if are_assumptions_satisfied(model, x_train, y_train, p_value_thresh=0.05):
    print('Pretpostavke su ispunjene')
else:
    print('Pretpostavke nisu ispunjene')
    
    
val_adj_r2 = get_rsquared_adj(model, x_val, y_val)
print(f'Validacioni skup: {val_adj_r2:.2f}')

df_test = pd.read_csv('./data/test.csv', sep=',')
x_test = df_test.drop(columns=['Test Score', 'Questions Practiced', 'Questions Skipped'])
y_test = df_test['Test Score']
test_adj_r2 = get_rsquared_adj(model, x_test, y_test)
print(f'Test prilagodjeni r2: {test_adj_r2:.2f}')


#zad4
#Reziduali predstavljaju razliku izmedju stvarne vrednosti modela i prediktovane vrednosti modela, tj. reziduali su procenjene vrednosti gresaka modela


#zad5
#Regresija pomocu polinoma treceg stepena je takodje linearna jer je linearna po parametrima, a ne po nezavisnim promenljivima