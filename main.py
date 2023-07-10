import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('insurance.csv')
print("Witaj! Wczytane dane dotyczą Szwedzkich ubezbieczeń. Aby zobaczyć: ")
print("1) Podstawowy wykres rozrzutu punktów")
print("2) Wykres rozrzutu punktów z regresją liniową")
print("3) Wykres rozrzutu punktów jako sześciokątów")
print("4) Wykres oszacowania gęstości jądra")

x = int(input())
if x==1:
    plt.figure(figsize=(15,6))
    plt.plot("X", "Y", data=df, linestyle='none', marker='o')
    plt.xlabel('number of claims', fontsize='12',
           horizontalalignment='center')
    plt.ylabel('total payment for all the claims in thousands of Swedish Kronor', fontsize='12',
           horizontalalignment='center')
    plt.title('Auto Insurance in Sweeden')
    plt.show();
elif x==2:
    fig = sns.lmplot(x="X", y="Y", data=df, fit_reg=True,
                 truncate=True, height=5, aspect=2.5)
    fig.set_axis_labels("avarage number of claims", "avarage total payment for all the claims in thousands of Swedish Kronor")
    fig.set(title='avarage number of claims vs avarage total payment for all the claims in thousands of Swedish Kronor');
    plt.show();
# To wyżej to to samo co to:
    #sns.jointplot(x=df["X"], y=df["Y"], kind='reg');
elif x==3:
    sns.jointplot(x=df["X"], y=df["Y"], kind='hex');
    plt.show();
elif x==4:
    sns.jointplot(x=df["X"], y=df["Y"], kind='kde');
    plt.show();

print("Czy chcesz zobaczyć kolejny wykres?")
czy = input()
if czy=="tak":
    x = int(input())
elif czy=="nie":
    exit();
# w przypadku zmiennej testowej
# palette1 = ['blue','orange']
# fig1 = sns.lmplot(x="X", y="Y", data=df, fit_reg=False,
#                   legend=True, height=3, aspect=0.9, hue='Y',
#                   palette=palette1, col='continent')
# fig1.set_axis_labels("avarage age in country", "avarage GDP in country");




