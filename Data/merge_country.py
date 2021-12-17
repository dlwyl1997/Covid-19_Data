import pandas as pd
import numpy as np
from pandas.core.reshape.concat import concat
import os

def merge_country():
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    
    # New Cases
    # file_path1 = "D:/GLA Lessons/MSc Project/Data/data/CONVENIENT_global_confirmed_cases.csv"

    # df1 = pd.read_csv(file_path1).T
    # df1 = df1.rename_axis('Country/Region').reset_index()
    # df1 = df1.drop(df1.index[0:1, ]).reset_index(drop=True)
    # df1.iloc[:, [-1]] = df1.iloc[:, [-1]].astype(np.float64)
    # df1.iloc[:, [-1]] = df1.iloc[:, [-1]].astype(np.int64)

    # df1_1 = df1.iloc[0:8, :]

    # df1_merged = df1.iloc[8:16, :]
    # sum = df1_merged.iloc[:, 1:].sum(axis=0)
    # df1_merged.loc[df1_merged.index.max()+1] = sum
    # df1_merged.loc[df1_merged.index.max(),'Country/Region'] = 'Australia'
    # df1_merged = pd.concat([df1_1, df1_merged]).reset_index(drop=True)
    # df1_2 = df1_merged.drop(df1_merged.index[8:16, ]).reset_index(drop=True)

    # df1_3 = df1.iloc[16:39, :]

    # df1_merged = df1.iloc[39:55, :]
    # sum = df1_merged.iloc[:, 1:].sum(axis=0)
    # df1_merged.loc[df1_merged.index.max()+1] = sum
    # df1_merged.loc[df1_merged.index.max(),'Country/Region'] = 'Canada'
    # df1_merged = pd.concat([df1_2, df1_3, df1_merged]).reset_index(drop=True)
    # df1_4 = df1_merged.drop(df1_merged.index[32:48, ]).reset_index(drop=True)

    # df1_5 = df1.iloc[55:58, :]

    # df1_merged = df1.iloc[58:92, :]
    # sum = df1_merged.iloc[:, 1:].sum(axis=0)
    # df1_merged.loc[df1_merged.index.max()+1] = sum
    # df1_merged.loc[df1_merged.index.max(),'Country/Region'] = 'China'
    # df1_merged = pd.concat([df1_4, df1_5, df1_merged]).reset_index(drop=True)
    # df1_6 = df1_merged.drop(df1_merged.index[36:70, ]).reset_index(drop=True)

    # df1_7 = df1.iloc[92:102, :]

    # df1_merged = df1.iloc[102:105, :]
    # sum = df1_merged.iloc[:, 1:].sum(axis=0)
    # df1_merged.loc[df1_merged.index.max()+1] = sum
    # df1_merged.loc[df1_merged.index.max(),'Country/Region'] = 'Denmark'
    # df1_merged = pd.concat([df1_6, df1_7, df1_merged]).reset_index(drop=True)
    # df1_8 = df1_merged.drop(df1_merged.index[47:50, ]).reset_index(drop=True)

    # df1_9 = df1.iloc[105:119, :]

    # df1_merged = df1.iloc[119:131, :]
    # sum = df1_merged.iloc[:, 1:].sum(axis=0)
    # df1_merged.loc[df1_merged.index.max()+1] = sum
    # df1_merged.loc[df1_merged.index.max(),'Country/Region'] = 'France'
    # df1_merged = pd.concat([df1_8, df1_9, df1_merged]).reset_index(drop=True)
    # df1_10 = df1_merged.drop(df1_merged.index[62:74, ]).reset_index(drop=True)

    # df1_11 = df1.iloc[131:193, :]

    # df1_merged = df1.iloc[193:198, :]
    # sum = df1_merged.iloc[:, 1:].sum(axis=0)
    # df1_merged.loc[df1_merged.index.max()+1] = sum
    # df1_merged.loc[df1_merged.index.max(),'Country/Region'] = 'Netherlands'
    # df1_merged = pd.concat([df1_10, df1_11, df1_merged]).reset_index(drop=True)
    # df1_12 = df1_merged.drop(df1_merged.index[125:130, ]).reset_index(drop=True)

    # df1_merged = df1.iloc[198:200, :]
    # sum = df1_merged.iloc[:, 1:].sum(axis=0)
    # df1_merged.loc[df1_merged.index.max()+1] = sum
    # df1_merged.loc[df1_merged.index.max(),'Country/Region'] = 'New Zealand'
    # df1_merged = pd.concat([df1_12, df1_merged]).reset_index(drop=True)
    # df1_13 = df1_merged.drop(df1_merged.index[126:128, ]).reset_index(drop=True)

    # df1_14 = df1.iloc[200:259, :]

    # df1_merged = df1.iloc[259:271, :]
    # sum = df1_merged.iloc[:, 1:].sum(axis=0)
    # df1_merged.loc[df1_merged.index.max()+1] = sum
    # df1_merged.loc[df1_merged.index.max(),'Country/Region'] = 'United Kingdom'
    # df1_merged = pd.concat([df1_13, df1_14, df1_merged]).reset_index(drop=True)
    # df1_15 = df1_merged.drop(df1_merged.index[186:198, ]).reset_index(drop=True)

    # df1_16 = df1.iloc[271:280, :]

    # df1_merged = pd.concat([df1_15, df1_16]).reset_index(drop=True)

    # # calculate world data
    # sum = df1_merged.iloc[:, 1:].sum(axis=0)
    # df1_merged.loc[df1_merged.index.max()+1] = sum
    # df1_merged.loc[df1_merged.index.max(),'Country/Region'] = 'World'

    # df1_merged.iloc[:, 1:] = df1_merged.iloc[:, 1:].astype(np.int64)

    # df1_us = df1_merged.iloc[[182], :]
    # df1_india = df1_merged.iloc[[79], :]
    # df1_uk = df1_merged.iloc[[186], :]
    # df1_brazil = df1_merged.iloc[[23], :]
    # df1_russia = df1_merged.iloc[[144], :]

    # os.getcwd()
    # df1_us.to_csv('US_total_cases.csv')
    # df1_india.to_csv('INDIA_total_cases.csv')
    # df1_uk.to_csv('UK_total_cases.csv')
    # df1_brazil.to_csv('BRAZIL_total_cases.csv')
    # df1_russia.to_csv('RUSSIA_total_cases.csv')

    # print(df1_merged)





    # Total Cases
    file_path2 = "D:/GLA Lessons/MSc Project/Data/data/RAW_global_confirmed_cases.csv"

    df2 = pd.read_csv(file_path2)

    df2 = df2.drop(df2.columns[1:4], axis=1)

    df2_1 = df2.iloc[0:8, :]

    df2_merged = df2.iloc[8:16, :]
    sum = df2_merged.iloc[:, 1:].sum(axis=0)
    df2_merged.loc[df2_merged.index.max()+1] = sum
    df2_merged.loc[df2_merged.index.max(),'Country/Region'] = 'Australia'
    df2_merged = pd.concat([df2_1, df2_merged]).reset_index(drop=True)
    df2_2 = df2_merged.drop(df2_merged.index[8:16, ]).reset_index(drop=True)

    df2_3 = df2.iloc[16:39, :]

    df2_merged = df2.iloc[39:55, :]
    sum = df2_merged.iloc[:, 1:].sum(axis=0)
    df2_merged.loc[df2_merged.index.max()+1] = sum
    df2_merged.loc[df2_merged.index.max(),'Country/Region'] = 'Canada'
    df2_merged = pd.concat([df2_2, df2_3, df2_merged]).reset_index(drop=True)
    df2_4 = df2_merged.drop(df2_merged.index[32:48, ]).reset_index(drop=True)

    df2_5 = df2.iloc[55:58, :]

    df2_merged = df2.iloc[58:92, :]
    sum = df2_merged.iloc[:, 1:].sum(axis=0)
    df2_merged.loc[df2_merged.index.max()+1] = sum
    df2_merged.loc[df2_merged.index.max(),'Country/Region'] = 'China'
    df2_merged = pd.concat([df2_4, df2_5, df2_merged]).reset_index(drop=True)
    df2_6 = df2_merged.drop(df2_merged.index[36:70, ]).reset_index(drop=True)

    df2_7 = df2.iloc[92:102, :]

    df2_merged = df2.iloc[102:105, :]
    sum = df2_merged.iloc[:, 1:].sum(axis=0)
    df2_merged.loc[df2_merged.index.max()+1] = sum
    df2_merged.loc[df2_merged.index.max(),'Country/Region'] = 'Denmark'
    df2_merged = pd.concat([df2_6, df2_7, df2_merged]).reset_index(drop=True)
    df2_8 = df2_merged.drop(df2_merged.index[47:50, ]).reset_index(drop=True)

    df2_9 = df2.iloc[105:119, :]

    df2_merged = df2.iloc[119:131, :]
    sum = df2_merged.iloc[:, 1:].sum(axis=0)
    df2_merged.loc[df2_merged.index.max()+1] = sum
    df2_merged.loc[df2_merged.index.max(),'Country/Region'] = 'France'
    df2_merged = pd.concat([df2_8, df2_9, df2_merged]).reset_index(drop=True)
    df2_10 = df2_merged.drop(df2_merged.index[62:74, ]).reset_index(drop=True)

    df2_11 = df2.iloc[131:193, :]

    df2_merged = df2.iloc[193:198, :]
    sum = df2_merged.iloc[:, 1:].sum(axis=0)
    df2_merged.loc[df2_merged.index.max()+1] = sum
    df2_merged.loc[df2_merged.index.max(),'Country/Region'] = 'Netherlands'
    df2_merged = pd.concat([df2_10, df2_11, df2_merged]).reset_index(drop=True)
    df2_12 = df2_merged.drop(df2_merged.index[125:130, ]).reset_index(drop=True)

    df2_merged = df2.iloc[198:200, :]
    sum = df2_merged.iloc[:, 1:].sum(axis=0)
    df2_merged.loc[df2_merged.index.max()+1] = sum
    df2_merged.loc[df2_merged.index.max(),'Country/Region'] = 'New Zealand'
    df2_merged = pd.concat([df2_12, df2_merged]).reset_index(drop=True)
    df2_13 = df2_merged.drop(df2_merged.index[126:128, ]).reset_index(drop=True)

    df2_14 = df2.iloc[200:259, :]

    df2_merged = df2.iloc[259:271, :]
    sum = df2_merged.iloc[:, 1:].sum(axis=0)
    df2_merged.loc[df2_merged.index.max()+1] = sum
    df2_merged.loc[df2_merged.index.max(),'Country/Region'] = 'United Kingdom'
    df2_merged = pd.concat([df2_13, df2_14, df2_merged]).reset_index(drop=True)
    df2_15 = df2_merged.drop(df2_merged.index[186:198, ]).reset_index(drop=True)

    df2_16 = df2.iloc[271:280, :]

    df2_merged = pd.concat([df2_15, df2_16]).reset_index(drop=True)

    # calculate world data
    sum = df2_merged.iloc[:, 1:].sum(axis=0)
    df2_merged.loc[df2_merged.index.max()+1] = sum
    df2_merged.loc[df2_merged.index.max(),'Country/Region'] = 'World'

    df2_merged.iloc[:, 1:] = df2_merged.iloc[:, 1:].astype(np.int64)

    df2_us = df2_merged.iloc[[182], :]
    df2_india = df2_merged.iloc[[79], :]
    df2_uk = df2_merged.iloc[[186], :]
    df2_brazil = df2_merged.iloc[[23], :]
    df2_russia = df2_merged.iloc[[144], :]
    df2_world = df2_merged.iloc[[-1], :]

    df2_selected = pd.concat([df2_us, df2_india, df2_uk, df2_brazil, df2_russia, df2_world]).reset_index(drop=True)

    os.getcwd()
    df2_selected.to_csv('SELECTED_total_cases.csv')
    df2_merged.to_csv('WORLD_total_cases.csv')


    # print(df2_merged)



    # Total Deaths
    file_path4 = "D:/GLA Lessons/MSc Project/Data/data/RAW_global_deaths.csv"

    df4 = pd.read_csv(file_path4)

    df4 = df4.drop(df4.columns[1:4], axis=1)

    df4_1 = df4.iloc[0:8, :]

    df4_merged = df4.iloc[8:16, :]
    sum = df4_merged.iloc[:, 1:].sum(axis=0)
    df4_merged.loc[df4_merged.index.max()+1] = sum
    df4_merged.loc[df4_merged.index.max(),'Country/Region'] = 'Australia'
    df4_merged = pd.concat([df4_1, df4_merged]).reset_index(drop=True)
    df4_2 = df4_merged.drop(df4_merged.index[8:16, ]).reset_index(drop=True)

    df4_3 = df4.iloc[16:39, :]

    df4_merged = df4.iloc[39:55, :]
    sum = df4_merged.iloc[:, 1:].sum(axis=0)
    df4_merged.loc[df4_merged.index.max()+1] = sum
    df4_merged.loc[df4_merged.index.max(),'Country/Region'] = 'Canada'
    df4_merged = pd.concat([df4_2, df4_3, df4_merged]).reset_index(drop=True)
    df4_4 = df4_merged.drop(df4_merged.index[32:48, ]).reset_index(drop=True)

    df4_5 = df4.iloc[55:58, :]

    df4_merged = df4.iloc[58:92, :]
    sum = df4_merged.iloc[:, 1:].sum(axis=0)
    df4_merged.loc[df4_merged.index.max()+1] = sum
    df4_merged.loc[df4_merged.index.max(),'Country/Region'] = 'China'
    df4_merged = pd.concat([df4_4, df4_5, df4_merged]).reset_index(drop=True)
    df4_6 = df4_merged.drop(df4_merged.index[36:70, ]).reset_index(drop=True)

    df4_7 = df4.iloc[92:102, :]

    df4_merged = df4.iloc[102:105, :]
    sum = df4_merged.iloc[:, 1:].sum(axis=0)
    df4_merged.loc[df4_merged.index.max()+1] = sum
    df4_merged.loc[df4_merged.index.max(),'Country/Region'] = 'Denmark'
    df4_merged = pd.concat([df4_6, df4_7, df4_merged]).reset_index(drop=True)
    df4_8 = df4_merged.drop(df4_merged.index[47:50, ]).reset_index(drop=True)

    df4_9 = df4.iloc[105:119, :]

    df4_merged = df4.iloc[119:131, :]
    sum = df4_merged.iloc[:, 1:].sum(axis=0)
    df4_merged.loc[df4_merged.index.max()+1] = sum
    df4_merged.loc[df4_merged.index.max(),'Country/Region'] = 'France'
    df4_merged = pd.concat([df4_8, df4_9, df4_merged]).reset_index(drop=True)
    df4_10 = df4_merged.drop(df4_merged.index[62:74, ]).reset_index(drop=True)

    df4_11 = df4.iloc[131:193, :]

    df4_merged = df4.iloc[193:198, :]
    sum = df4_merged.iloc[:, 1:].sum(axis=0)
    df4_merged.loc[df4_merged.index.max()+1] = sum
    df4_merged.loc[df4_merged.index.max(),'Country/Region'] = 'Netherlands'
    df4_merged = pd.concat([df4_10, df4_11, df4_merged]).reset_index(drop=True)
    df4_12 = df4_merged.drop(df4_merged.index[125:130, ]).reset_index(drop=True)

    df4_merged = df4.iloc[198:200, :]
    sum = df4_merged.iloc[:, 1:].sum(axis=0)
    df4_merged.loc[df4_merged.index.max()+1] = sum
    df4_merged.loc[df4_merged.index.max(),'Country/Region'] = 'New Zealand'
    df4_merged = pd.concat([df4_12, df4_merged]).reset_index(drop=True)
    df4_13 = df4_merged.drop(df4_merged.index[126:128, ]).reset_index(drop=True)

    df4_14 = df4.iloc[200:259, :]

    df4_merged = df4.iloc[259:271, :]
    sum = df4_merged.iloc[:, 1:].sum(axis=0)
    df4_merged.loc[df4_merged.index.max()+1] = sum
    df4_merged.loc[df4_merged.index.max(),'Country/Region'] = 'United Kingdom'
    df4_merged = pd.concat([df4_13, df4_14, df4_merged]).reset_index(drop=True)
    df4_15 = df4_merged.drop(df4_merged.index[186:198, ]).reset_index(drop=True)

    df4_16 = df4.iloc[271:280, :]

    df4_merged = pd.concat([df4_15, df4_16]).reset_index(drop=True)

    # calculate world data
    sum = df4_merged.iloc[:, 1:].sum(axis=0)
    df4_merged.loc[df4_merged.index.max()+1] = sum
    df4_merged.loc[df4_merged.index.max(),'Country/Region'] = 'World'

    df4_merged.iloc[:, 1:] = df4_merged.iloc[:, 1:].astype(np.int64)

    df4_us = df4_merged.iloc[[182], :]
    df4_india = df4_merged.iloc[[79], :]
    df4_uk = df4_merged.iloc[[186], :]
    df4_brazil = df4_merged.iloc[[23], :]
    df4_russia = df4_merged.iloc[[144], :]
    df4_world = df4_merged.iloc[[-1], :]

    df4_selected = pd.concat([df4_us, df4_india, df4_uk, df4_brazil, df4_russia, df4_world]).reset_index(drop=True)
    
    os.getcwd()
    df4_selected.to_csv('SELECTED_total_deaths.csv')
    df4_merged.to_csv('WORLD_total_deaths.csv')

    # print(df4_merged)


if __name__ == '__main__':
    merge_country()

