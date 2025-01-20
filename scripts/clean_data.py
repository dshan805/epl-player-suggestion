import pandas as pd
import numpy as np
import os
from scripts.config import missing_position_dict


# set up cleaning data function 
def clean_data(main_df, fifa_df):
    """Clean the data."""

    # remove players who never played or played less than 10 matches 
    main_df = main_df[main_df['Appearances'] >= 10]

    # only need name and position from fifa table 
    fifa_df = fifa_df[['name', 'position']]

    # joining main df and fifa df
    main_df_fifa = pd.merge(
        main_df, fifa_df, how='left', left_on='Name', right_on='name'
    )

    # remove duplicates, can safely remove
    main_df_fifa=main_df_fifa.drop_duplicates(subset='Name')

    # Goalkeepers are missing specialized categories, fill with GK
    main_df_fifa['position'] = np.where(
        main_df_fifa['Position'] == 'Goalkeeper', 'GK', main_df_fifa['position']
    )
    
    # fill df_fifa using dictionary mapping
    for index, row in main_df_fifa.iterrows():
        if pd.isna(row['position']):
            if row['Name'] in missing_position_dict:
                main_df_fifa.at[index, 'position'] = missing_position_dict[row['Name']]

    # remove column "Position", Wins/Losses are also not necessary as it does not tell us anything about player characteristics. 
    main_df_fifa.drop(columns=["Position","Wins", "Losses", "Jersey Number", "Goals per match", 'Tackle success %' , 'Cross accuracy %', 'Passes per match'], inplace=True)

    # Get columns that do not contain '%'
    columns_without_percentage = [col for col in main_df_fifa.columns if '%' not in col]
    main_df_fifa[columns_without_percentage] = main_df_fifa[columns_without_percentage].fillna(0)

    # create column shooting accuracy 
    main_df_fifa['Shooting accuracy %'] = main_df_fifa['Shots on target']/main_df_fifa['Shots']
    main_df_fifa['Shooting accuracy %'] = main_df_fifa['Shooting accuracy %'].fillna(0)

    # convert data to per match data 
    # Create a copy of df_fifa to avoid modifying the original DataFrame
    df_per_match = main_df_fifa.copy()

    # Iterate through the columns of df_fifa
    for col in main_df_fifa.columns:
        # Check if the column is numeric (integer or float) and not 'Appearances' or 'Age'
        if main_df_fifa[col].dtype in ['int64', 'float64'] and col not in ['Appearances', 'Age']:
            # Divide each value by the 'Appearances' column
            df_per_match[col] = main_df_fifa[col] / main_df_fifa['Appearances']

    # Display the resulting DataFrame
    return df_per_match
