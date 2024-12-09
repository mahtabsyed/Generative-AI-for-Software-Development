import pandas as pd
import json
import sys

def parse_json_schedule_and_save(file_path):
    # Load json
    with open(file_path, 'r') as f:
        df_json = json.load(f)   
        
    # Convert json into dataframe
    df = pd.io.json.json_normalize(df_json)
    
    # Cast variables to correct types
    df['income_day'] = df['income_day'].astype(int)
    df['time_in'] = pd.to_datetime(df['time_in'])
    df['time_out'] = pd.to_datetime(df['time_out'])
    
    # Create a new column, working_time
    new_data = [('working_time', df['time_out'] - df['time_in'])]
    
    # Create a new dataframe from it
    # new_df = pd.DataFrame.from_items(new_data) 
    # Deprecated since version 0.23.0: from_items is deprecated and will be removed in a future version. Use 
    # DataFrame.from_dict(dict(items)) instead. DataFrame.from_dict(OrderedDict(items)) may be used to preserve the key order.
    
    # new_df = pd.DataFrame.from_dict(OrderedDict(new_data)) 
    new_df = pd.DataFrame.from_dict(dict(new_data))
    
    # Add this new_df as new columns to the original df
    df['working_time'] = new_df['working_time']
    
    df.to_csv("data.csv", index = False)
    
    return df

    
