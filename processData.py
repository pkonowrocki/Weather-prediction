import pandas as pd
import os
import dictionaries as d

globalPath = 'projekt_3_dane/'
byCityPath = f'byCity/'

def readFile(filename, separator = ','):
    data = pd.read_csv(f'{globalPath}{filename}', sep=separator)
    return data

def groupByCityAndSave(data, filepath):
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    data["month"] = pd.DatetimeIndex(data["Local time"]).month
    data["hour"] = pd.DatetimeIndex(data["Local time"]).hour
    groups = list(data.groupby('City'))
    for group in groups:
        temp = group[1].drop(columns='City')
        temp.to_csv(f'{filepath}{group[0]}', header=False, index=False)
    return [group[0] for group in groups]

def changeWithDictionaryAndSave(file, cloudsDictionary, windDictionary, filepath, filename):
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    with open(file, 'r', encoding="UTF-8") as data:
        text = data.read()
        for k in cloudsDictionary.keys():
            text = text.replace(k, cloudsDictionary[k])

        for k in windDictionary.keys():
            text = text.replace(k, windDictionary[k])

        with open(f'{filepath}{filename}', 'w', encoding="UTF-8") as temp:
            temp.write(text.replace('"',''))

def main(filenames, folder):
    for filename in filenames:
        data = readFile(filename, separator=';')
        filesGroupedByCity = groupByCityAndSave(data, f'{globalPath}{folder}{byCityPath}')

        for groupedByCity in filesGroupedByCity:
            changeWithDictionaryAndSave(f'{globalPath}{folder}{byCityPath}{groupedByCity}', d.cloudsOktaCode, d.grayCode, f'{globalPath}{folder}CloudsOktaWindGray/', groupedByCity)
            changeWithDictionaryAndSave(f'{globalPath}{folder}{byCityPath}{groupedByCity}', d.cloudsOktaStupidCode, d.grayCode, f'{globalPath}{folder}CloudsOneHotWindGray/', groupedByCity)
            changeWithDictionaryAndSave(f'{globalPath}{folder}{byCityPath}{groupedByCity}', d.cloudsOktaCode, d.naturalCode, f'{globalPath}{folder}CloudsOktaWindNatural/', groupedByCity)
            changeWithDictionaryAndSave(f'{globalPath}{folder}{byCityPath}{groupedByCity}', d.cloudsOktaStupidCode, d.naturalCode, f'{globalPath}{folder}CloudsOneHotWindNatural/', groupedByCity)

if __name__ == "__main__":
    main(filenames = ['train_1', 'train_2'], folder='train/')
    main(filenames = ['test_1', 'test_2'], folder='test/')