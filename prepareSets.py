import pandas as pd
import numpy as  np
import glob
import datetime as dt

measurements = ['wind', 'temperature']
imputations = ['imputation', 'noImputation']
setType = ['train', 'test']
codes = ['CloudsOktaWindGray', 'CloudsOktaWindNatural', 'CloudsOneHotWindGray', 'CloudsOneHotWindNatural']

for measure in measurements:
    for imputation in imputations:
        for train in setType:
            for code in codes:
                directory = f'projekt_3_dane\\{measure}\\{imputation}\\{train}\\{code}\\*'
                files = glob.glob(directory)
                
                X = []
                Y = []
                
                for file in files:
                    if 'csv' in file:
                        break
                    df = pd.read_csv(file, header=None).values

                    for idx in range(df.shape[0]):
                        if idx < df.shape[0]-7:
                            date = dt.datetime.strptime(df[idx, 0], '%Y-%m-%d')
                            isOk = True
                            for offset in range(1, 7):
                                if not offset == 6:
                                    if not date + dt.timedelta(days=offset) == dt.datetime.strptime(df[idx+offset, 0], '%Y-%m-%d'):
                                        isOk = False
        
                            if isOk:
                                input = np.array([])
                                for offset in range(0, 5):
                                    input = np.concatenate((input, df[idx+offset, 1:df.shape[1]-1]))
                                output = np.array(df[idx+6, df.shape[1]-1])
                                X.append(input)
                                Y.append(output)

                X = np.array(X)
                Y = np.array(Y)
                print(f'SAVE: {measure}\t{imputation}\t{train}\t{code}')
                np.savetxt(f'projekt_3_dane\\{measure}\\{imputation}\\{code}-{train}-input.csv', X, delimiter=",")
                np.savetxt(f'projekt_3_dane\\{measure}\\{imputation}\\{code}-{train}-output.csv', Y, delimiter=",")




