

#THis is for OSA_score calculation

import pandas as pd

def OSA_Score(pandas_df = None,
              excel_file_name = None,
              max_value = 100):


    print("Value of max_value is",max_value)

    #Validating the inputs
    if(excel_file_name is None and pandas_df is None):
        print("Please specify the inptus either pandas_df or excel_file_name")
    
    elif(excel_file_name is not None):
        dataframe = pd.read_csv(excel_file_name)
    else:
        dataframe = pandas_df
        assert isinstance(pandas_df,pd.DataFrame),"Please input a pandas dataframe as input"
        print("Using pandas dataframe passed to the function as input")


    
    # Code for OSA score 



    return osa_score

OSA_Score(pandas_df = None,
         excel_file_name = None,
         max_value = 333 )
