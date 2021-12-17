import pandas as pd
import numpy as np
from pandas.core.reshape.concat import concat
import os

def data_preprocess():
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)


    # New Cases
    file_path1 = "D:/GLA Lessons/MSc Project/Data/data/CONVENIENT_global_confirmed_cases.csv"

    df1 = pd.read_csv(file_path1).T
    df1 = df1.rename_axis('Country/Region').reset_index()
    df1 = df1.drop(df1.index[0:1, ]).reset_index(drop=True)
    df1.iloc[:, [-1]] = df1.iloc[:, [-1]].astype(np.float64)
    df1.iloc[:, [-1]] = df1.iloc[:, [-1]].astype(np.int64)

    df1_1 = df1.iloc[0:8, [0, -1]]

    temp = df1.iloc[8:16, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'Australia'
    temp = pd.concat([df1_1, temp]).reset_index(drop=True)
    df1_2 = temp.drop(temp.index[8:16, ]).reset_index(drop=True)

    df1_3 = df1.iloc[16:39, [0, -1]]

    temp = df1.iloc[39:55, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'Canada'
    temp = pd.concat([df1_2, df1_3, temp]).reset_index(drop=True)
    df1_4 = temp.drop(temp.index[32:48, ]).reset_index(drop=True)

    df1_5 = df1.iloc[55:58, [0, -1]]

    temp = df1.iloc[58:92, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'China'
    temp = pd.concat([df1_4, df1_5, temp]).reset_index(drop=True)
    df1_6 = temp.drop(temp.index[36:70, ]).reset_index(drop=True)

    df1_7 = df1.iloc[92:102, [0, -1]]

    temp = df1.iloc[102:105, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'Denmark'
    temp = pd.concat([df1_6, df1_7, temp]).reset_index(drop=True)
    df1_8 = temp.drop(temp.index[47:50, ]).reset_index(drop=True)

    df1_9 = df1.iloc[105:119, [0, -1]]

    temp = df1.iloc[119:131, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'France'
    temp = pd.concat([df1_8, df1_9, temp]).reset_index(drop=True)
    df1_10 = temp.drop(temp.index[62:74, ]).reset_index(drop=True)

    df1_11 = df1.iloc[131:193, [0, -1]]

    temp = df1.iloc[193:198, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'Netherlands'
    temp = pd.concat([df1_10, df1_11, temp]).reset_index(drop=True)
    df1_12 = temp.drop(temp.index[125:130, ]).reset_index(drop=True)

    temp = df1.iloc[198:200, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'New Zealand'
    temp = pd.concat([df1_12, temp]).reset_index(drop=True)
    df1_13 = temp.drop(temp.index[126:128, ]).reset_index(drop=True)

    df1_14 = df1.iloc[200:259, [0, -1]]

    temp = df1.iloc[259:271, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'United Kingdom'
    temp = pd.concat([df1_13, df1_14, temp]).reset_index(drop=True)
    df1_15 = temp.drop(temp.index[186:198, ]).reset_index(drop=True)

    df1_16 = df1.iloc[271:280, [0, -1]]

    df1_processed = pd.concat([df1_15, df1_16]).reset_index(drop=True)
    df1_processed.columns = ['Country/Region', 'New Cases']
    df1_processed['New Cases'] = df1_processed['New Cases'].astype(np.int64)

    # print(df1_processed)




    # Total Cases
    file_path2 = "D:/GLA Lessons/MSc Project/Data/data/RAW_global_confirmed_cases.csv"

    df2 = pd.read_csv(file_path2)

    df2_1 = df2.iloc[0:8, [0, -1]]

    temp = df2.iloc[8:16, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'Australia'
    temp = pd.concat([df2_1, temp]).reset_index(drop=True)
    df2_2 = temp.drop(temp.index[8:16, ]).reset_index(drop=True)

    df2_3 = df2.iloc[16:39, [0, -1]]

    temp = df2.iloc[39:55, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'Canada'
    temp = pd.concat([df2_2, df2_3, temp]).reset_index(drop=True)
    df2_4 = temp.drop(temp.index[32:48, ]).reset_index(drop=True)

    df2_5 = df2.iloc[55:58, [0, -1]]

    temp = df2.iloc[58:92, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'China'
    temp = pd.concat([df2_4, df2_5, temp]).reset_index(drop=True)
    df2_6 = temp.drop(temp.index[36:70, ]).reset_index(drop=True)

    df2_7 = df2.iloc[92:102, [0, -1]]

    temp = df2.iloc[102:105, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'Denmark'
    temp = pd.concat([df2_6, df2_7, temp]).reset_index(drop=True)
    df2_8 = temp.drop(temp.index[47:50, ]).reset_index(drop=True)

    df2_9 = df2.iloc[105:119, [0, -1]]

    temp = df2.iloc[119:131, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'France'
    temp = pd.concat([df2_8, df2_9, temp]).reset_index(drop=True)
    df2_10 = temp.drop(temp.index[62:74, ]).reset_index(drop=True)

    df2_11 = df2.iloc[131:193, [0, -1]]

    temp = df2.iloc[193:198, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'Netherlands'
    temp = pd.concat([df2_10, df2_11, temp]).reset_index(drop=True)
    df2_12 = temp.drop(temp.index[125:130, ]).reset_index(drop=True)

    temp = df2.iloc[198:200, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'New Zealand'
    temp = pd.concat([df2_12, temp]).reset_index(drop=True)
    df2_13 = temp.drop(temp.index[126:128, ]).reset_index(drop=True)

    df2_14 = df2.iloc[200:259, [0, -1]]

    temp = df2.iloc[259:271, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'United Kingdom'
    temp = pd.concat([df2_13, df2_14, temp]).reset_index(drop=True)
    df2_15 = temp.drop(temp.index[186:198, ]).reset_index(drop=True)

    df2_16 = df2.iloc[271:280, [0, -1]]

    df2_processed = pd.concat([df2_15, df2_16]).reset_index(drop=True)
    df2_processed.columns = ['Country/Region', 'Total Cases']
    df2_processed['Total Cases'] = df2_processed['Total Cases'].astype(np.int64)

    # print(df2_processed)




    # New Deaths
    file_path3 = "D:/GLA Lessons/MSc Project/Data/data/CONVENIENT_global_deaths.csv"

    df3 = pd.read_csv(file_path3).T
    df3 = df3.rename_axis('Country/Region').reset_index()
    df3 = df3.drop(df3.index[0:1, ]).reset_index(drop=True)
    df3.iloc[:, [-1]] = df3.iloc[:, [-1]].astype(np.float64)
    df3.iloc[:, [-1]] = df3.iloc[:, [-1]].astype(np.int64)

    df3_1 = df3.iloc[0:8, [0, -1]]

    temp = df3.iloc[8:16, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'Australia'
    temp = pd.concat([df3_1, temp]).reset_index(drop=True)
    df3_2 = temp.drop(temp.index[8:16, ]).reset_index(drop=True)

    df3_3 = df3.iloc[16:39, [0, -1]]

    temp = df3.iloc[39:55, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'Canada'
    temp = pd.concat([df3_2, df3_3, temp]).reset_index(drop=True)
    df3_4 = temp.drop(temp.index[32:48, ]).reset_index(drop=True)

    df3_5 = df3.iloc[55:58, [0, -1]]

    temp = df3.iloc[58:92, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'China'
    temp = pd.concat([df3_4, df3_5, temp]).reset_index(drop=True)
    df3_6 = temp.drop(temp.index[36:70, ]).reset_index(drop=True)

    df3_7 = df3.iloc[92:102, [0, -1]]

    temp = df3.iloc[102:105, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'Denmark'
    temp = pd.concat([df3_6, df3_7, temp]).reset_index(drop=True)
    df3_8 = temp.drop(temp.index[47:50, ]).reset_index(drop=True)

    df3_9 = df3.iloc[105:119, [0, -1]]

    temp = df3.iloc[119:131, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'France'
    temp = pd.concat([df3_8, df3_9, temp]).reset_index(drop=True)
    df3_10 = temp.drop(temp.index[62:74, ]).reset_index(drop=True)

    df3_11 = df3.iloc[131:193, [0, -1]]

    temp = df3.iloc[193:198, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'Netherlands'
    temp = pd.concat([df3_10, df3_11, temp]).reset_index(drop=True)
    df3_12 = temp.drop(temp.index[125:130, ]).reset_index(drop=True)

    temp = df3.iloc[198:200, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'New Zealand'
    temp = pd.concat([df3_12, temp]).reset_index(drop=True)
    df3_13 = temp.drop(temp.index[126:128, ]).reset_index(drop=True)

    df3_14 = df3.iloc[200:259, [0, -1]]

    temp = df3.iloc[259:271, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'United Kingdom'
    temp = pd.concat([df3_13, df3_14, temp]).reset_index(drop=True)
    df3_15 = temp.drop(temp.index[186:198, ]).reset_index(drop=True)

    df3_16 = df3.iloc[271:280, [0, -1]]

    df3_processed = pd.concat([df3_15, df3_16]).reset_index(drop=True)
    df3_processed.columns = ['Country/Region', 'New Deaths']
    df3_processed['New Deaths'] = df3_processed['New Deaths'].astype(np.int64)

    # print(df3_processed)




    #  Total Deaths
    file_path4 = "D:/GLA Lessons/MSc Project/Data/data/RAW_global_deaths.csv"

    df4 = pd.read_csv(file_path4)

    df4_1 = df4.iloc[0:8, [0, -1]]

    temp = df4.iloc[8:16, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'Australia'
    temp = pd.concat([df4_1, temp]).reset_index(drop=True)
    df4_2 = temp.drop(temp.index[8:16, ]).reset_index(drop=True)

    df4_3 = df4.iloc[16:39, [0, -1]]

    temp = df4.iloc[39:55, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'Canada'
    temp = pd.concat([df4_2, df4_3, temp]).reset_index(drop=True)
    df4_4 = temp.drop(temp.index[32:48, ]).reset_index(drop=True)

    df4_5 = df4.iloc[55:58, [0, -1]]

    temp = df4.iloc[58:92, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'China'
    temp = pd.concat([df4_4, df4_5, temp]).reset_index(drop=True)
    df4_6 = temp.drop(temp.index[36:70, ]).reset_index(drop=True)

    df4_7 = df4.iloc[92:102, [0, -1]]

    temp = df4.iloc[102:105, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'Denmark'
    temp = pd.concat([df4_6, df4_7, temp]).reset_index(drop=True)
    df4_8 = temp.drop(temp.index[47:50, ]).reset_index(drop=True)

    df4_9 = df4.iloc[105:119, [0, -1]]

    temp = df4.iloc[119:131, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'France'
    temp = pd.concat([df4_8, df4_9, temp]).reset_index(drop=True)
    df4_10 = temp.drop(temp.index[62:74, ]).reset_index(drop=True)

    df4_11 = df4.iloc[131:193, [0, -1]]

    temp = df4.iloc[193:198, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'Netherlands'
    temp = pd.concat([df4_10, df4_11, temp]).reset_index(drop=True)
    df4_12 = temp.drop(temp.index[125:130, ]).reset_index(drop=True)

    temp = df4.iloc[198:200, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'New Zealand'
    temp = pd.concat([df4_12, temp]).reset_index(drop=True)
    df4_13 = temp.drop(temp.index[126:128, ]).reset_index(drop=True)

    df4_14 = df4.iloc[200:259, [0, -1]]

    temp = df4.iloc[259:271, [0, -1]]
    sum = temp.iloc[:, [1]].sum(axis=0)
    temp.loc[temp.index.max()+1] = sum
    temp.loc[temp.index.max(),'Country/Region'] = 'United Kingdom'
    temp = pd.concat([df4_13, df4_14, temp]).reset_index(drop=True)
    df4_15 = temp.drop(temp.index[186:198, ]).reset_index(drop=True)

    df4_16 = df4.iloc[271:280, [0, -1]]

    df4_processed = pd.concat([df4_15, df4_16]).reset_index(drop=True)
    df4_processed.columns = ['Country/Region', 'Total Deaths']
    df4_processed['Total Deaths'] = df4_processed['Total Deaths'].astype(np.int64)

    # print(df4_processed)


    # Concatenation
    df_processed = pd.concat([df1_processed, df2_processed['Total Cases'], df3_processed['New Deaths'], df4_processed['Total Deaths']], axis=1)

    print(df_processed)    

    new_cases = df_processed['New Cases'].sum()
    total_cases = df_processed['Total Cases'].sum()
    new_deaths = df_processed['New Deaths'].sum()
    total_deaths = df_processed['Total Deaths'].sum()

    os.getcwd()
    df_processed.to_csv('PROCESSED_DATA.csv')

if __name__ == '__main__':
    data_preprocess()
