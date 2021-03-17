# Combine HHD &CDD

import pandas as pd 
import numpy as np
from pandas import DataFrame
import datetime

import pandas

import statsmodels.api as sm
import matplotlib.pyplot as plt

starttime = datetime.datetime.now()

# Albania
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Albania CDD.csv')
AlbaniaCDD = table.iloc[6:, 0:2]
AlbaniaCDD.columns = ['date','value']
AlbaniaCDD.insert(AlbaniaCDD.shape[1], 'area', 'Albania')
AlbaniaCDD.insert(AlbaniaCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
AlbaniaCDD = AlbaniaCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Albania HDD.csv')
AlbaniaHDD = table.iloc[6:, 0:2]
AlbaniaHDD.columns = ['date','value']
AlbaniaHDD.insert(AlbaniaHDD.shape[1], 'area', 'Albania')
AlbaniaHDD.insert(AlbaniaHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
AlbaniaHDD = AlbaniaHDD[order]

# Algeria
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Algeria CDD.csv')
AlgeriaCDD = table.iloc[6:, 0:2]
AlgeriaCDD.columns = ['date','value']
AlgeriaCDD.insert(AlgeriaCDD.shape[1], 'area', 'Algeria')
AlgeriaCDD.insert(AlgeriaCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
AlgeriaCDD = AlgeriaCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Algeria HDD.csv')
AlgeriaHDD = table.iloc[6:, 0:2]
AlgeriaHDD.columns = ['date','value']
AlgeriaHDD.insert(AlgeriaHDD.shape[1], 'area', 'Algeria')
AlgeriaHDD.insert(AlgeriaHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
AlgeriaHDD = AlgeriaHDD[order]

# Bahrain
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Bahrain CDD.csv')
BahrainCDD = table.iloc[6:, 0:2]
BahrainCDD.columns = ['date','value']
BahrainCDD.insert(BahrainCDD.shape[1], 'area', 'Bahrain')
BahrainCDD.insert(BahrainCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
BahrainCDD = BahrainCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Bahrain HDD.csv')
BahrainHDD = table.iloc[6:, 0:2]
BahrainHDD.columns = ['date','value']
BahrainHDD.insert(BahrainHDD.shape[1], 'area', 'Bahrain')
BahrainHDD.insert(BahrainHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
BahrainHDD = BahrainHDD[order]


# Belgium
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Belgium CDD.csv')
BelgiumCDD = table.iloc[6:, 0:2]
BelgiumCDD.columns = ['date','value']
BelgiumCDD.insert(BelgiumCDD.shape[1], 'area', 'Belgium')
BelgiumCDD.insert(BelgiumCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
BelgiumCDD = BelgiumCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Belgium HDD.csv')
BelgiumHDD = table.iloc[6:, 0:2]
BelgiumHDD.columns = ['date','value']
BelgiumHDD.insert(BelgiumHDD.shape[1], 'area', 'Belgium')
BelgiumHDD.insert(BelgiumHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
BelgiumHDD = BelgiumHDD[order]

# Bolivia
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Bolivia CDD.csv')
BoliviaCDD = table.iloc[6:, 0:2]
BoliviaCDD.columns = ['date','value']
BoliviaCDD.insert(BoliviaCDD.shape[1], 'area', 'Bolivia')
BoliviaCDD.insert(BoliviaCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
BoliviaCDD = BoliviaCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Bolivia HDD.csv')
BoliviaHDD = table.iloc[6:, 0:2]
BoliviaHDD.columns = ['date','value']
BoliviaHDD.insert(BoliviaHDD.shape[1], 'area', 'Bolivia')
BoliviaHDD.insert(BoliviaHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
BoliviaHDD = BoliviaHDD[order]

# Brunei Darussalam
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Brunei Darussalam CDD.csv')
BruneiDarussalamCDD = table.iloc[6:, 0:2]
BruneiDarussalamCDD.columns = ['date','value']
BruneiDarussalamCDD.insert(BruneiDarussalamCDD.shape[1], 'area', 'Brunei Darussalam')
BruneiDarussalamCDD.insert(BruneiDarussalamCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
BruneiDarussalamCDD = BruneiDarussalamCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Brunei Darussalam HDD.csv')
BruneiDarussalamHDD = table.iloc[6:, 0:2]
BruneiDarussalamHDD.columns = ['date','value']
BruneiDarussalamHDD.insert(BruneiDarussalamHDD.shape[1], 'area', 'Brunei Darussalam')
BruneiDarussalamHDD.insert(BruneiDarussalamHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
BruneiDarussalamHDD = BruneiDarussalamHDD[order]

# Bulgaria
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Bulgaria CDD.csv')
BulgariaCDD = table.iloc[6:, 0:2]
BulgariaCDD.columns = ['date','value']
BulgariaCDD.insert(BulgariaCDD.shape[1], 'area', 'Bulgaria')
BulgariaCDD.insert(BulgariaCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
BulgariaCDD = BulgariaCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Bulgaria HDD.csv')
BulgariaHDD = table.iloc[6:, 0:2]
BulgariaHDD.columns = ['date','value']
BulgariaHDD.insert(BulgariaHDD.shape[1], 'area', 'Bulgaria')
BulgariaHDD.insert(BulgariaHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
BulgariaHDD = BulgariaHDD[order]


# Chile
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Chile CDD.csv')
ChileCDD = table.iloc[6:, 0:2]
ChileCDD.columns = ['date','value']
ChileCDD.insert(ChileCDD.shape[1], 'area', 'Chile')
ChileCDD.insert(ChileCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
ChileCDD = ChileCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Chile HDD.csv')
ChileHDD = table.iloc[6:, 0:2]
ChileHDD.columns = ['date','value']
ChileHDD.insert(ChileHDD.shape[1], 'area', 'Chile')
ChileHDD.insert(ChileHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
ChileHDD = ChileHDD[order]


# Croatia
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Croatia CDD.csv')
CroatiaCDD = table.iloc[6:, 0:2]
CroatiaCDD.columns = ['date','value']
CroatiaCDD.insert(CroatiaCDD.shape[1], 'area', 'Croatia')
CroatiaCDD.insert(CroatiaCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
CroatiaCDD = CroatiaCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Croatia HDD.csv')
CroatiaHDD = table.iloc[6:, 0:2]
CroatiaHDD.columns = ['date','value']
CroatiaHDD.insert(CroatiaHDD.shape[1], 'area', 'Croatia')
CroatiaHDD.insert(CroatiaHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
CroatiaHDD = CroatiaHDD[order]


# Czech Republic
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Czech Republic CDD.csv')
CzechRepublicCDD = table.iloc[6:, 0:2]
CzechRepublicCDD.columns = ['date','value']
CzechRepublicCDD.insert(CzechRepublicCDD.shape[1], 'area', 'Czech Republic')
CzechRepublicCDD.insert(CzechRepublicCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
CzechRepublicCDD = CzechRepublicCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Czech Republic HDD.csv')
CzechRepublicHDD = table.iloc[6:, 0:2]
CzechRepublicHDD.columns = ['date','value']
CzechRepublicHDD.insert(CzechRepublicHDD.shape[1], 'area', 'Czech Republic')
CzechRepublicHDD.insert(CzechRepublicHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
CzechRepublicHDD = CzechRepublicHDD[order]

# Denmark
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Denmark CDD.csv')
DenmarkCDD = table.iloc[6:, 0:2]
DenmarkCDD.columns = ['date','value']
DenmarkCDD.insert(DenmarkCDD.shape[1], 'area', 'Denmark')
DenmarkCDD.insert(DenmarkCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
DenmarkCDD = DenmarkCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Denmark HDD.csv')
DenmarkHDD = table.iloc[6:, 0:2]
DenmarkHDD.columns = ['date','value']
DenmarkHDD.insert(DenmarkHDD.shape[1], 'area', 'Denmark')
DenmarkHDD.insert(DenmarkHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
DenmarkHDD = DenmarkHDD[order]


# Egypt
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Egypt CDD.csv')
EgyptCDD = table.iloc[6:, 0:2]
EgyptCDD.columns = ['date','value']
EgyptCDD.insert(EgyptCDD.shape[1], 'area', 'Egypt (Arab Rep.)')
EgyptCDD.insert(EgyptCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
EgyptCDD = EgyptCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Egypt HDD.csv')
EgyptHDD = table.iloc[6:, 0:2]
EgyptHDD.columns = ['date','value']
EgyptHDD.insert(EgyptHDD.shape[1], 'area', 'Egypt (Arab Rep.)')
EgyptHDD.insert(EgyptHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
EgyptHDD = EgyptHDD[order]


# Equatorial Guinea
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Equatorial Guinea CDD.csv')
EquatorialGuineaCDD = table.iloc[6:, 0:2]
EquatorialGuineaCDD.columns = ['date','value']
EquatorialGuineaCDD.insert(EquatorialGuineaCDD.shape[1], 'area', 'Equatorial Guinea')
EquatorialGuineaCDD.insert(EquatorialGuineaCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
EquatorialGuineaCDD = EquatorialGuineaCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Equatorial Guinea HDD.csv')
EquatorialGuineaHDD = table.iloc[6:, 0:2]
EquatorialGuineaHDD.columns = ['date','value']
EquatorialGuineaHDD.insert(EquatorialGuineaHDD.shape[1], 'area', 'Equatorial Guinea')
EquatorialGuineaHDD.insert(EquatorialGuineaHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
EquatorialGuineaHDD = EquatorialGuineaHDD[order]


# Estonia
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Estonia CDD.csv')
EstoniaCDD = table.iloc[6:, 0:2]
EstoniaCDD.columns = ['date','value']
EstoniaCDD.insert(EstoniaCDD.shape[1], 'area', 'Estonia')
EstoniaCDD.insert(EstoniaCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
EstoniaCDD = EstoniaCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Estonia HDD.csv')
EstoniaHDD = table.iloc[6:, 0:2]
EstoniaHDD.columns = ['date','value']
EstoniaHDD.insert(EstoniaHDD.shape[1], 'area', 'Estonia')
EstoniaHDD.insert(EstoniaHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
EstoniaHDD = EstoniaHDD[order]

# Finland
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Finland CDD.csv')
FinlandCDD = table.iloc[6:, 0:2]
FinlandCDD.columns = ['date','value']
FinlandCDD.insert(FinlandCDD.shape[1], 'area', 'Finland')
FinlandCDD.insert(FinlandCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
FinlandCDD = FinlandCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Finland HDD.csv')
FinlandHDD = table.iloc[6:, 0:2]
FinlandHDD.columns = ['date','value']
FinlandHDD.insert(FinlandHDD.shape[1], 'area', 'Finland')
FinlandHDD.insert(FinlandHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
FinlandHDD = FinlandHDD[order]


# France
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\France CDD.csv')
FranceCDD = table.iloc[6:, 0:2]
FranceCDD.columns = ['date','value']
FranceCDD.insert(FranceCDD.shape[1], 'area', 'France')
FranceCDD.insert(FranceCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
FranceCDD = FranceCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\France HDD.csv')
FranceHDD = table.iloc[6:, 0:2]
FranceHDD.columns = ['date','value']
FranceHDD.insert(FranceHDD.shape[1], 'area', 'France')
FranceHDD.insert(FranceHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
FranceHDD = FranceHDD[order]


# Georgia
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Georgia CDD.csv')
GeorgiaCDD = table.iloc[6:, 0:2]
GeorgiaCDD.columns = ['date','value']
GeorgiaCDD.insert(GeorgiaCDD.shape[1], 'area', 'Georgia')
GeorgiaCDD.insert(GeorgiaCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
GeorgiaCDD = GeorgiaCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Georgia HDD.csv')
GeorgiaHDD = table.iloc[6:, 0:2]
GeorgiaHDD.columns = ['date','value']
GeorgiaHDD.insert(GeorgiaHDD.shape[1], 'area', 'Georgia')
GeorgiaHDD.insert(GeorgiaHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
GeorgiaHDD = GeorgiaHDD[order]


# Germany
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Germany CDD.csv')
GermanyCDD = table.iloc[6:, 0:2]
GermanyCDD.columns = ['date','value']
GermanyCDD.insert(GermanyCDD.shape[1], 'area', 'Germany')
GermanyCDD.insert(GermanyCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
GermanyCDD = GermanyCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Germany HDD.csv')
GermanyHDD = table.iloc[6:, 0:2]
GermanyHDD.columns = ['date','value']
GermanyHDD.insert(GermanyHDD.shape[1], 'area', 'Germany')
GermanyHDD.insert(GermanyHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
GermanyHDD = GermanyHDD[order]



# Greece
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Greece CDD.csv')
GreeceCDD = table.iloc[6:, 0:2]
GreeceCDD.columns = ['date','value']
GreeceCDD.insert(GreeceCDD.shape[1], 'area', 'Greece')
GreeceCDD.insert(GreeceCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
GreeceCDD = GreeceCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Greece HDD.csv')
GreeceHDD = table.iloc[6:, 0:2]
GreeceHDD.columns = ['date','value']
GreeceHDD.insert(GreeceHDD.shape[1], 'area', 'Greece')
GreeceHDD.insert(GreeceHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
GreeceHDD = GreeceHDD[order]

# Hungary
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Hungary CDD.csv')
HungaryCDD = table.iloc[6:, 0:2]
HungaryCDD.columns = ['date','value']
HungaryCDD.insert(HungaryCDD.shape[1], 'area', 'Hungary')
HungaryCDD.insert(HungaryCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
HungaryCDD = HungaryCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Hungary HDD.csv')
HungaryHDD = table.iloc[6:, 0:2]
HungaryHDD.columns = ['date','value']
HungaryHDD.insert(HungaryHDD.shape[1], 'area', 'Hungary')
HungaryHDD.insert(HungaryHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
HungaryHDD = HungaryHDD[order]


# Ireland
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Ireland CDD.csv')
IrelandCDD = table.iloc[6:, 0:2]
IrelandCDD.columns = ['date','value']
IrelandCDD.insert(IrelandCDD.shape[1], 'area', 'Ireland')
IrelandCDD.insert(IrelandCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
IrelandCDD = IrelandCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Ireland HDD.csv')
IrelandHDD = table.iloc[6:, 0:2]
IrelandHDD.columns = ['date','value']
IrelandHDD.insert(IrelandHDD.shape[1], 'area', 'Ireland')
IrelandHDD.insert(IrelandHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
IrelandHDD = IrelandHDD[order]


# Israel
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Israel CDD.csv')
IsraelCDD = table.iloc[6:, 0:2]
IsraelCDD.columns = ['date','value']
IsraelCDD.insert(IsraelCDD.shape[1], 'area', 'Israel')
IsraelCDD.insert(IsraelCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
IsraelCDD = IsraelCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Israel HDD.csv')
IsraelHDD = table.iloc[6:, 0:2]
IsraelHDD.columns = ['date','value']
IsraelHDD.insert(IsraelHDD.shape[1], 'area', 'Israel')
IsraelHDD.insert(IsraelHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
IsraelHDD = IsraelHDD[order]


# Italy
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Italy CDD.csv')
ItalyCDD = table.iloc[6:, 0:2]
ItalyCDD.columns = ['date','value']
ItalyCDD.insert(ItalyCDD.shape[1], 'area', 'Italy')
ItalyCDD.insert(ItalyCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
ItalyCDD = ItalyCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Italy HDD.csv')
ItalyHDD = table.iloc[6:, 0:2]
ItalyHDD.columns = ['date','value']
ItalyHDD.insert(ItalyHDD.shape[1], 'area', 'Italy')
ItalyHDD.insert(ItalyHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
ItalyHDD = ItalyHDD[order]


# Kuwait
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Kuwait CDD.csv')
KuwaitCDD = table.iloc[6:, 0:2]
KuwaitCDD.columns = ['date','value']
KuwaitCDD.insert(KuwaitCDD.shape[1], 'area', 'Kuwait')
KuwaitCDD.insert(KuwaitCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
KuwaitCDD = KuwaitCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Kuwait HDD.csv')
KuwaitHDD = table.iloc[6:, 0:2]
KuwaitHDD.columns = ['date','value']
KuwaitHDD.insert(KuwaitHDD.shape[1], 'area', 'Kuwait')
KuwaitHDD.insert(KuwaitHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
KuwaitHDD = KuwaitHDD[order]


# Latvia
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Latvia CDD.csv')
LatviaCDD = table.iloc[6:, 0:2]
LatviaCDD.columns = ['date','value']
LatviaCDD.insert(LatviaCDD.shape[1], 'area', 'Latvia')
LatviaCDD.insert(LatviaCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
LatviaCDD = LatviaCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Latvia HDD.csv')
LatviaHDD = table.iloc[6:, 0:2]
LatviaHDD.columns = ['date','value']
LatviaHDD.insert(LatviaHDD.shape[1], 'area', 'Latvia')
LatviaHDD.insert(LatviaHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
LatviaHDD = LatviaHDD[order]


# Lithuania
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Lithuania CDD.csv')
LithuaniaCDD = table.iloc[6:, 0:2]
LithuaniaCDD.columns = ['date','value']
LithuaniaCDD.insert(LithuaniaCDD.shape[1], 'area', 'Lithuania')
LithuaniaCDD.insert(LithuaniaCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
LithuaniaCDD = LithuaniaCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Lithuania HDD.csv')
LithuaniaHDD = table.iloc[6:, 0:2]
LithuaniaHDD.columns = ['date','value']
LithuaniaHDD.insert(LithuaniaHDD.shape[1], 'area', 'Lithuania')
LithuaniaHDD.insert(LithuaniaHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
LithuaniaHDD = LithuaniaHDD[order]



# Luxembourg
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Luxembourg CDD.csv')
LuxembourgCDD = table.iloc[6:, 0:2]
LuxembourgCDD.columns = ['date','value']
LuxembourgCDD.insert(LuxembourgCDD.shape[1], 'area', 'Luxembourg')
LuxembourgCDD.insert(LuxembourgCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
LuxembourgCDD = LuxembourgCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Luxembourg HDD.csv')
LuxembourgHDD = table.iloc[6:, 0:2]
LuxembourgHDD.columns = ['date','value']
LuxembourgHDD.insert(LuxembourgHDD.shape[1], 'area', 'Luxembourg')
LuxembourgHDD.insert(LuxembourgHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
LuxembourgHDD = LuxembourgHDD[order]



# Moldova
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Moldova CDD.csv')
MoldovaCDD = table.iloc[6:, 0:2]
MoldovaCDD.columns = ['date','value']
MoldovaCDD.insert(MoldovaCDD.shape[1], 'area', 'Moldova')
MoldovaCDD.insert(MoldovaCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
MoldovaCDD = MoldovaCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Moldova HDD.csv')
MoldovaHDD = table.iloc[6:, 0:2]
MoldovaHDD.columns = ['date','value']
MoldovaHDD.insert(MoldovaHDD.shape[1], 'area', 'Moldova')
MoldovaHDD.insert(MoldovaHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
MoldovaHDD = MoldovaHDD[order]


# Morocco
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Morocco CDD.csv')
MoroccoCDD = table.iloc[6:, 0:2]
MoroccoCDD.columns = ['date','value']
MoroccoCDD.insert(MoroccoCDD.shape[1], 'area', 'Morocco')
MoroccoCDD.insert(MoroccoCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
MoroccoCDD = MoroccoCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Morocco HDD.csv')
MoroccoHDD = table.iloc[6:, 0:2]
MoroccoHDD.columns = ['date','value']
MoroccoHDD.insert(MoroccoHDD.shape[1], 'area', 'Morocco')
MoroccoHDD.insert(MoroccoHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
MoroccoHDD = MoroccoHDD[order]




# Netherlands
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Netherlands CDD.csv')
NetherlandsCDD = table.iloc[6:, 0:2]
NetherlandsCDD.columns = ['date','value']
NetherlandsCDD.insert(NetherlandsCDD.shape[1], 'area', 'Netherlands')
NetherlandsCDD.insert(NetherlandsCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
NetherlandsCDD = NetherlandsCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Netherlands HDD.csv')
NetherlandsHDD = table.iloc[6:, 0:2]
NetherlandsHDD.columns = ['date','value']
NetherlandsHDD.insert(NetherlandsHDD.shape[1], 'area', 'Netherlands')
NetherlandsHDD.insert(NetherlandsHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
NetherlandsHDD = NetherlandsHDD[order]


# New Zealands
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\New Zealands CDD.csv')
NewZealandsCDD = table.iloc[6:, 0:2]
NewZealandsCDD.columns = ['date','value']
NewZealandsCDD.insert(NewZealandsCDD.shape[1], 'area', 'New Zealand')
NewZealandsCDD.insert(NewZealandsCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
NewZealandsCDD = NewZealandsCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\New Zealands HDD.csv')
NewZealandsHDD = table.iloc[6:, 0:2]
NewZealandsHDD.columns = ['date','value']
NewZealandsHDD.insert(NewZealandsHDD.shape[1], 'area', 'New Zealand')
NewZealandsHDD.insert(NewZealandsHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
NewZealandsHDD = NewZealandsHDD[order]


# Nigeria
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Nigeria CDD.csv')
NigeriaCDD = table.iloc[6:, 0:2]
NigeriaCDD.columns = ['date','value']
NigeriaCDD.insert(NigeriaCDD.shape[1], 'area', 'Nigeria')
NigeriaCDD.insert(NigeriaCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
NigeriaCDD = NigeriaCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Nigeria HDD.csv')
NigeriaHDD = table.iloc[6:, 0:2]
NigeriaHDD.columns = ['date','value']
NigeriaHDD.insert(NigeriaHDD.shape[1], 'area', 'Nigeria')
NigeriaHDD.insert(NigeriaHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
NigeriaHDD = NigeriaHDD[order]


# Norway
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Norway CDD.csv')
NorwayCDD = table.iloc[6:, 0:2]
NorwayCDD.columns = ['date','value']
NorwayCDD.insert(NorwayCDD.shape[1], 'area', 'Norway')
NorwayCDD.insert(NorwayCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
NorwayCDD = NorwayCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Norway HDD.csv')
NorwayHDD = table.iloc[6:, 0:2]
NorwayHDD.columns = ['date','value']
NorwayHDD.insert(NorwayHDD.shape[1], 'area', 'Norway')
NorwayHDD.insert(NorwayHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
NorwayHDD = NorwayHDD[order]


# Philippines
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Philippines CDD.csv')
PhilippinesCDD = table.iloc[6:, 0:2]
PhilippinesCDD.columns = ['date','value']
PhilippinesCDD.insert(PhilippinesCDD.shape[1], 'area', 'Philippines')
PhilippinesCDD.insert(PhilippinesCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
PhilippinesCDD = PhilippinesCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Philippines HDD.csv')
PhilippinesHDD = table.iloc[6:, 0:2]
PhilippinesHDD.columns = ['date','value']
PhilippinesHDD.insert(PhilippinesHDD.shape[1], 'area', 'Philippines')
PhilippinesHDD.insert(PhilippinesHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
PhilippinesHDD = PhilippinesHDD[order]


# Poland
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Poland CDD.csv')
PolandCDD = table.iloc[6:, 0:2]
PolandCDD.columns = ['date','value']
PolandCDD.insert(PolandCDD.shape[1], 'area', 'Poland')
PolandCDD.insert(PolandCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
PolandCDD = PolandCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Poland HDD.csv')
PolandHDD = table.iloc[6:, 0:2]
PolandHDD.columns = ['date','value']
PolandHDD.insert(PolandHDD.shape[1], 'area', 'Poland')
PolandHDD.insert(PolandHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
PolandHDD = PolandHDD[order]


# Portugal
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Portugal CDD.csv')
PortugalCDD = table.iloc[6:, 0:2]
PortugalCDD.columns = ['date','value']
PortugalCDD.insert(PortugalCDD.shape[1], 'area', 'Portugal')
PortugalCDD.insert(PortugalCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
PortugalCDD = PortugalCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Portugal HDD.csv')
PortugalHDD = table.iloc[6:, 0:2]
PortugalHDD.columns = ['date','value']
PortugalHDD.insert(PortugalHDD.shape[1], 'area', 'Portugal')
PortugalHDD.insert(PortugalHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
PortugalHDD = PortugalHDD[order]


# Qatar
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Qatar CDD.csv')
QatarCDD = table.iloc[6:, 0:2]
QatarCDD.columns = ['date','value']
QatarCDD.insert(QatarCDD.shape[1], 'area', 'Qatar')
QatarCDD.insert(QatarCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
QatarCDD = QatarCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Qatar HDD.csv')
QatarHDD = table.iloc[6:, 0:2]
QatarHDD.columns = ['date','value']
QatarHDD.insert(QatarHDD.shape[1], 'area', 'Qatar')
QatarHDD.insert(QatarHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
QatarHDD = QatarHDD[order]


# Romania
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Romania CDD.csv')
RomaniaCDD = table.iloc[6:, 0:2]
RomaniaCDD.columns = ['date','value']
RomaniaCDD.insert(RomaniaCDD.shape[1], 'area', 'Romania')
RomaniaCDD.insert(RomaniaCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
RomaniaCDD = RomaniaCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Romania HDD.csv')
RomaniaHDD = table.iloc[6:, 0:2]
RomaniaHDD.columns = ['date','value']
RomaniaHDD.insert(RomaniaHDD.shape[1], 'area', 'Romania')
RomaniaHDD.insert(RomaniaHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
RomaniaHDD = RomaniaHDD[order]



# Slovak Republic
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Slovak Republic CDD.csv')
SlovakRepublicCDD = table.iloc[6:, 0:2]
SlovakRepublicCDD.columns = ['date','value']
SlovakRepublicCDD.insert(SlovakRepublicCDD.shape[1], 'area', 'Slovak Republic')
SlovakRepublicCDD.insert(SlovakRepublicCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
SlovakRepublicCDD = SlovakRepublicCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Slovak Republic HDD.csv')
SlovakRepublicHDD = table.iloc[6:, 0:2]
SlovakRepublicHDD.columns = ['date','value']
SlovakRepublicHDD.insert(SlovakRepublicHDD.shape[1], 'area', 'Slovak Republic')
SlovakRepublicHDD.insert(SlovakRepublicHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
SlovakRepublicHDD = SlovakRepublicHDD[order]


# Slovenia
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Slovenia CDD.csv')
SloveniaCDD = table.iloc[6:, 0:2]
SloveniaCDD.columns = ['date','value']
SloveniaCDD.insert(SloveniaCDD.shape[1], 'area', 'Slovenia')
SloveniaCDD.insert(SloveniaCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
SloveniaCDD = SloveniaCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Slovenia HDD.csv')
SloveniaHDD = table.iloc[6:, 0:2]
SloveniaHDD.columns = ['date','value']
SloveniaHDD.insert(SloveniaHDD.shape[1], 'area', 'Slovenia')
SloveniaHDD.insert(SloveniaHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
SloveniaHDD = SloveniaHDD[order]


# Spain
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Spain CDD.csv')
SpainCDD = table.iloc[6:, 0:2]
SpainCDD.columns = ['date','value']
SpainCDD.insert(SpainCDD.shape[1], 'area', 'Spain')
SpainCDD.insert(SpainCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
SpainCDD = SpainCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Spain HDD.csv')
SpainHDD = table.iloc[6:, 0:2]
SpainHDD.columns = ['date','value']
SpainHDD.insert(SpainHDD.shape[1], 'area', 'Spain')
SpainHDD.insert(SpainHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
SpainHDD = SpainHDD[order]


# Sweden
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Sweden CDD.csv')
SwedenCDD = table.iloc[6:, 0:2]
SwedenCDD.columns = ['date','value']
SwedenCDD.insert(SwedenCDD.shape[1], 'area', 'Sweden')
SwedenCDD.insert(SwedenCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
SwedenCDD = SwedenCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Sweden HDD.csv')
SwedenHDD = table.iloc[6:, 0:2]
SwedenHDD.columns = ['date','value']
SwedenHDD.insert(SwedenHDD.shape[1], 'area', 'Sweden')
SwedenHDD.insert(SwedenHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
SwedenHDD = SwedenHDD[order]



# Switzerland
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Switzerland CDD.csv')
SwitzerlandCDD = table.iloc[6:, 0:2]
SwitzerlandCDD.columns = ['date','value']
SwitzerlandCDD.insert(SwitzerlandCDD.shape[1], 'area', 'Switzerland')
SwitzerlandCDD.insert(SwitzerlandCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
SwitzerlandCDD = SwitzerlandCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Switzerland HDD.csv')
SwitzerlandHDD = table.iloc[6:, 0:2]
SwitzerlandHDD.columns = ['date','value']
SwitzerlandHDD.insert(SwitzerlandHDD.shape[1], 'area', 'Switzerland')
SwitzerlandHDD.insert(SwitzerlandHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
SwitzerlandHDD = SwitzerlandHDD[order]




# Trinidad
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Trinidad CDD.csv')
TrinidadCDD = table.iloc[6:, 0:2]
TrinidadCDD.columns = ['date','value']
TrinidadCDD.insert(TrinidadCDD.shape[1], 'area', 'Trinidad/Tobago')
TrinidadCDD.insert(TrinidadCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
TrinidadCDD = TrinidadCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Trinidad HDD.csv')
TrinidadHDD = table.iloc[6:, 0:2]
TrinidadHDD.columns = ['date','value']
TrinidadHDD.insert(TrinidadHDD.shape[1], 'area', 'Trinidad/Tobago')
TrinidadHDD.insert(TrinidadHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
TrinidadHDD = TrinidadHDD[order]


# Tunisia
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Tunisia CDD.csv')
TunisiaCDD = table.iloc[6:, 0:2]
TunisiaCDD.columns = ['date','value']
TunisiaCDD.insert(TunisiaCDD.shape[1], 'area', 'Tunisia')
TunisiaCDD.insert(TunisiaCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
TunisiaCDD = TunisiaCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Tunisia HDD.csv')
TunisiaHDD = table.iloc[6:, 0:2]
TunisiaHDD.columns = ['date','value']
TunisiaHDD.insert(TunisiaHDD.shape[1], 'area', 'Tunisia')
TunisiaHDD.insert(TunisiaHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
TunisiaHDD = TunisiaHDD[order]


# Turkey
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Turkey CDD.csv')
TurkeyCDD = table.iloc[6:, 0:2]
TurkeyCDD.columns = ['date','value']
TurkeyCDD.insert(TurkeyCDD.shape[1], 'area', 'Turkey')
TurkeyCDD.insert(TurkeyCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
TurkeyCDD = TurkeyCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Turkey HDD.csv')
TurkeyHDD = table.iloc[6:, 0:2]
TurkeyHDD.columns = ['date','value']
TurkeyHDD.insert(TurkeyHDD.shape[1], 'area', 'Turkey')
TurkeyHDD.insert(TurkeyHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
TurkeyHDD = TurkeyHDD[order]

# UK
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\UK CDD.csv')
UKCDD = table.iloc[6:, 0:2]
UKCDD.columns = ['date','value']
UKCDD.insert(UKCDD.shape[1], 'area', 'United Kingdom')
UKCDD.insert(UKCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
UKCDD = UKCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\UK HDD.csv')
UKHDD = table.iloc[6:, 0:2]
UKHDD.columns = ['date','value']
UKHDD.insert(UKHDD.shape[1], 'area', 'United Kingdom')
UKHDD.insert(UKHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
UKHDD = UKHDD[order]


# Ukraine
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Ukraine CDD.csv')
UkraineCDD = table.iloc[6:, 0:2]
UkraineCDD.columns = ['date','value']
UkraineCDD.insert(UkraineCDD.shape[1], 'area', 'Ukraine')
UkraineCDD.insert(UkraineCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
UkraineCDD = UkraineCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Ukraine HDD.csv')
UkraineHDD = table.iloc[6:, 0:2]
UkraineHDD.columns = ['date','value']
UkraineHDD.insert(UkraineHDD.shape[1], 'area', 'Ukraine')
UkraineHDD.insert(UkraineHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
UkraineHDD = UkraineHDD[order]


# Venezuela
table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Venezuela CDD.csv')
VenezuelaCDD = table.iloc[6:, 0:2]
VenezuelaCDD.columns = ['date','value']
VenezuelaCDD.insert(VenezuelaCDD.shape[1], 'area', 'Venezuela')
VenezuelaCDD.insert(VenezuelaCDD.shape[1], 'degree', 'CDD')
order = ['area', 'degree', 'date', 'value']
VenezuelaCDD = VenezuelaCDD[order]

table = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\桌面\RBAC 2021\Weather Seasonality - Global\Degree Days\Venezuela HDD.csv')
VenezuelaHDD = table.iloc[6:, 0:2]
VenezuelaHDD.columns = ['date','value']
VenezuelaHDD.insert(VenezuelaHDD.shape[1], 'area', 'Venezuela')
VenezuelaHDD.insert(VenezuelaHDD.shape[1], 'degree', 'HDD')
order = ['area', 'degree', 'date', 'value']
VenezuelaHDD = VenezuelaHDD[order]





Output1 = [AlbaniaCDD, AlbaniaHDD, AlgeriaCDD, AlgeriaHDD, BahrainCDD, BahrainHDD, \
           BelgiumCDD, BelgiumHDD, BoliviaCDD, BoliviaHDD, BruneiDarussalamCDD, BruneiDarussalamHDD, \
           BulgariaCDD, BulgariaHDD, ChileCDD, ChileHDD, CroatiaCDD, CroatiaHDD, \
           CzechRepublicCDD, CzechRepublicHDD, DenmarkCDD, DenmarkHDD, EgyptCDD, EgyptHDD,
           EquatorialGuineaCDD, EquatorialGuineaHDD, EstoniaCDD, EstoniaHDD, FinlandCDD, FinlandHDD, FranceCDD, FranceHDD, \
           GeorgiaCDD, GeorgiaHDD, GermanyCDD, GermanyHDD, GreeceCDD, GreeceHDD, \
           HungaryCDD, HungaryHDD, IrelandCDD, IrelandHDD, IsraelCDD, IsraelHDD, ItalyCDD, ItalyHDD, \
           KuwaitCDD, KuwaitHDD, LatviaCDD, LatviaHDD, LithuaniaCDD, LithuaniaHDD, \
           LuxembourgCDD, LuxembourgHDD, MoldovaCDD, MoldovaHDD, MoroccoCDD, MoroccoHDD, NetherlandsCDD, NetherlandsHDD, \
           NewZealandsCDD, NewZealandsHDD, NigeriaCDD, NigeriaHDD, NorwayCDD, NorwayHDD, \
           PhilippinesCDD, PhilippinesHDD, PolandCDD, PolandHDD, PortugalCDD, PortugalHDD, \
           QatarCDD, QatarHDD, RomaniaCDD, RomaniaHDD, SlovakRepublicCDD, SlovakRepublicHDD, \
           SloveniaCDD, SloveniaHDD, SpainCDD, SpainHDD, SwedenCDD, SwedenHDD, SwitzerlandCDD, SwitzerlandHDD, \
           TrinidadCDD, TrinidadHDD, TunisiaCDD, TunisiaHDD, TurkeyCDD, TurkeyHDD, \
           UKCDD, UKHDD, UkraineCDD, UkraineHDD, VenezuelaCDD, VenezuelaHDD]
           
Output2 = pd.concat(Output1)

Output2.to_csv('C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC 2021\\Weather Seasonality - Global\Degree Days\\Global Degree Days.csv',index=None)
endtime = datetime.datetime.now()
print("Congradulations! Finished") 
print("duraion", endtime - starttime)



