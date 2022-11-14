import pandas as pd

def null_validator(dataframe):
    '''
    this function shows the null data of a dataframe and the percentage with respect to the number of rows
    '''
    null_values = []
    percentage = []
    for i in dataframe.columns:
        null_values.append(dataframe[i].isnull().sum())
        percentage.append(f'{round(dataframe[i].isnull().sum() * 100 /dataframe.shape[0], 2)} %')

    df_aux = pd.DataFrame()
    df_aux['column_name'] = dataframe.columns.tolist()
    df_aux['null_values'] = null_values
    df_aux['percentage'] = percentage
    
    return df_aux