import pandas as pd
import os
import dictionaries as d
from io import StringIO 
from fancyimpute import KNN
import copy

globalPath = 'projekt_3_dane/'
byCityPath = f'byCity/'

def readFile(filename, separator = ','):
    data = pd.read_csv(f'{globalPath}{filename}', sep=separator)
    return data

def groupByCityAndSave(data, filepath, isTemperature = False):
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    data["month"] = pd.DatetimeIndex(data["Local time"]).month
    data["hour"] = pd.DatetimeIndex(data["Local time"]).hour
    data["helper"] = data["T" if isTemperature else "VV"]
    data = data.drop(columns="T" if isTemperature else "VV")

    groups = list(data.groupby('City'))
    for group in groups:
        temp = group[1].drop(columns='City')
        temp.to_csv(f'{filepath}{group[0]}', header=False, index=False)
    return [group[0] for group in groups]

def changeWithDictionaryAndSave(file, cloudsDictionary, windDictionary, filepath, filename, isTemperature, imputation = False):
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    with open(file, 'r', encoding="UTF-8") as data:
        text = data.read()
        for k in cloudsDictionary.keys():
            text = text.replace(k, cloudsDictionary[k])

        for k in windDictionary.keys():
            text = text.replace(k, windDictionary[k])

        text = text.replace('less than 0.1', '0.05')
        text = text.replace('less than 0.05', '0.025')

        df = pd.read_csv(StringIO(text.replace('"','')), header = None)
        if imputation:
            df = prepareImputation(df)
        df = prepareDayMean(df)
        if not isTemperature:
            df = prepareForClassification(df)
        df.to_csv(f'{filepath}/{filename}', header = False, index = True)

def separateByCityAndCodes(filenames, folder, isTemperature = False, imputation = True):
    for filename in filenames:
        data = readFile(filename, separator=';')
        filesGroupedByCity = groupByCityAndSave(data, f'{globalPath}{folder}{byCityPath}', isTemperature)

        for groupedByCity in filesGroupedByCity:
            changeWithDictionaryAndSave(f'{globalPath}{folder}{byCityPath}{groupedByCity}', d.cloudsOktaCode, d.grayCode, f'{globalPath}{folder}CloudsOktaWindGray/', groupedByCity, isTemperature, imputation)
            changeWithDictionaryAndSave(f'{globalPath}{folder}{byCityPath}{groupedByCity}', d.cloudsOktaStupidCode, d.grayCode, f'{globalPath}{folder}CloudsOneHotWindGray/', groupedByCity, isTemperature, imputation)
            changeWithDictionaryAndSave(f'{globalPath}{folder}{byCityPath}{groupedByCity}', d.cloudsOktaCode, d.naturalCode, f'{globalPath}{folder}CloudsOktaWindNatural/', groupedByCity, isTemperature, imputation)
            changeWithDictionaryAndSave(f'{globalPath}{folder}{byCityPath}{groupedByCity}', d.cloudsOktaStupidCode, d.naturalCode, f'{globalPath}{folder}CloudsOneHotWindNatural/', groupedByCity, isTemperature, imputation)

def prepareForTemperatureRegression():
    separateByCityAndCodes(filenames = ['train_1', 'train_2'], folder='temperature/imputation/train/', isTemperature=True, imputation=True)
    separateByCityAndCodes(filenames = ['test_1', 'test_2'], folder='temperature/imputation/test/', isTemperature=True, imputation=True)
    separateByCityAndCodes(filenames = ['train_1', 'train_2'], folder='temperature/noImputation/train/', isTemperature=True, imputation=False)
    separateByCityAndCodes(filenames = ['test_1', 'test_2'], folder='temperature/noImputation/test/', isTemperature=True, imputation=False)

def prepareForWindClassification():
    separateByCityAndCodes(filenames = ['train_1', 'train_2'], folder='wind/imputation/train/', isTemperature=False, imputation=True)
    separateByCityAndCodes(filenames = ['test_1', 'test_2'], folder='wind/imputation/test/', isTemperature=False, imputation=True)
    separateByCityAndCodes(filenames = ['train_1', 'train_2'], folder='wind/noImputation/train/', isTemperature=False, imputation=False)
    separateByCityAndCodes(filenames = ['test_1', 'test_2'], folder='wind/noImputation/test/', isTemperature=False, imputation=False)

def prepareImputation(df):
    afterImputation = pd.DataFrame(KNN(k = 3).fit_transform(df.loc[:, df.columns != 0]))
    for c in afterImputation.columns:
        df[c+1] = afterImputation[c].values
    return df

def prepareDayMean(df):
    df[0] = pd.to_datetime(df[0])
    groups = df.groupby(df[0].dt.floor('d'))
    i = 0
    for group in groups:
        if not (group[1].shape[0] == 8 and not group[1].isnull().values.any()):
            df = df[df[0].dt.floor('d') != group[0]]
            i += 1
    print(f'deleted {i} days')
    return pd.DataFrame(df.groupby(df[0].dt.floor('d')).mean())


def prepareForClassification(df):
    df[df.columns[-1]] = 1 if df[df.columns[-1]]>=15 else 0
    return df


if __name__ == "__main__":
    prepareForTemperatureRegression()
    prepareForWindClassification()