#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# Imports
import pandas as pd
import numpy as np
import time
import sys

# For dates
import datetime as dt
from dateutil.relativedelta import relativedelta

# For financial data
import yahoo_fin
import yahoo_fin.stock_info as si
# import yahoo_fin.options as ops


# In[ ]:


# Read the file
subs = pd.read_csv("./Data/{}".format(sys.argv[1]))


# In[ ]:

"""
Description: Calculate the 2 month difference start date from the posted date
Parameters: Input date as string
Output: Output date as string
"""

def start_Date(date):
    
    return (dt.datetime.strptime(date, "%m/%d/%Y") + relativedelta(months=-2)).strftime("%m/%d/%Y")



"""
Description: Calculate the 2 month difference end date from the posted date
Parameters: Input date as string
Output: Output date as string
"""

def end_Date(date):
    
    return (dt.datetime.strptime(date, "%m/%d/%Y") + relativedelta(months=+2)).strftime("%m/%d/%Y")


"""
Description: Reverse the values in a data frame row
Parameters: row
Output: Reversed row
Source: https://stackoverflow.com/questions/57633212/reverse-row-values-in-pandas-dataframe
"""
def reverse(s):
    # Strip the NaN on both ends, but not in the middle
    idx1 = s.first_valid_index()
    idx2 = s.last_valid_index()
    idx = s.loc[idx1:idx2].index

    return pd.Series(s.loc[idx[::-1]].values, index=idx)

# In[ ]:


# Lists to store the stock information dataframes
stockInfoX = []
stockInfoY = []

for i in range(len(subs.index)):
    
    # Both data sets must exist
    try:
        # Get the X stock information
        stockX = si.get_data(subs.ticker[i], 
                            start_date=start_Date(subs.date[i]), 
                            end_date=subs.date[i],
                            index_as_date = False, 
                            interval = "1d"
                           )
        
        # Get the Y stock information
        stockY = si.get_data(subs.ticker[i], 
                            start_date=subs.date[i], 
                            end_date=end_Date(subs.date[i]),
                            index_as_date = False, 
                            interval = "1d"
                           )
    
    # Otherwise, fetching failed
    except:
        print("Error happened")
        stockInfoX.append(pd.DataFrame(-1, index=[0],
                                       columns=['volume_20_X', 'adjclose_20_X', 'close_20_X', 'low_20_X', 'high_20_X', 
                                                'open_20_X', 'volume_19_X', 'adjclose_19_X', 'close_19_X', 'low_19_X', 
                                                'high_19_X', 'open_19_X', 'volume_18_X', 'adjclose_18_X', 'close_18_X', 
                                                'low_18_X', 'high_18_X', 'open_18_X', 'volume_17_X', 'adjclose_17_X', 
                                                'close_17_X', 'low_17_X', 'high_17_X', 'open_17_X', 'volume_16_X', 
                                                'adjclose_16_X', 'close_16_X', 'low_16_X', 'high_16_X', 'open_16_X', 
                                                'volume_15_X', 'adjclose_15_X', 'close_15_X', 'low_15_X', 'high_15_X', 
                                                'open_15_X', 'volume_14_X', 'adjclose_14_X', 'close_14_X', 'low_14_X', 
                                                'high_14_X', 'open_14_X', 'volume_13_X', 'adjclose_13_X', 'close_13_X', 
                                                'low_13_X', 'high_13_X', 'open_13_X', 'volume_12_X', 'adjclose_12_X', 
                                                'close_12_X', 'low_12_X', 'high_12_X', 'open_12_X', 'volume_11_X', 
                                                'adjclose_11_X', 'close_11_X', 'low_11_X', 'high_11_X', 'open_11_X', 
                                                'volume_10_X', 'adjclose_10_X', 'close_10_X', 'low_10_X', 'high_10_X', 
                                                'open_10_X', 'volume_9_X', 'adjclose_9_X', 'close_9_X', 'low_9_X', 
                                                'high_9_X', 'open_9_X', 'volume_8_X', 'adjclose_8_X', 'close_8_X', 
                                                'low_8_X', 'high_8_X', 'open_8_X', 'volume_7_X', 'adjclose_7_X', 
                                                'close_7_X', 'low_7_X', 'high_7_X', 'open_7_X', 'volume_6_X', 
                                                'adjclose_6_X', 'close_6_X', 'low_6_X', 'high_6_X', 'open_6_X', 
                                                'volume_5_X', 'adjclose_5_X', 'close_5_X', 'low_5_X', 'high_5_X', 
                                                'open_5_X', 'volume_4_X', 'adjclose_4_X', 'close_4_X', 'low_4_X', 
                                                'high_4_X', 'open_4_X', 'volume_3_X', 'adjclose_3_X', 'close_3_X', 
                                                'low_3_X', 'high_3_X', 'open_3_X', 'volume_2_X', 'adjclose_2_X', 
                                                'close_2_X', 'low_2_X', 'high_2_X', 'open_2_X', 'volume_1_X', 
                                                'adjclose_1_X', 'close_1_X', 'low_1_X', 'high_1_X', 'open_1_X']))
        
        stockInfoY.append(pd.DataFrame(-1, index=[0],
                                       columns=['open_2_Y', 'high_2_Y', 'low_2_Y', 'close_2_Y', 'adjclose_2_Y', 
                                                'volume_2_Y', 'open_3_Y', 'high_3_Y', 'low_3_Y', 'close_3_Y', 
                                                'adjclose_3_Y', 'volume_3_Y', 'open_4_Y', 'high_4_Y', 'low_4_Y', 
                                                'close_4_Y', 'adjclose_4_Y', 'volume_4_Y', 'open_5_Y', 
                                                'high_5_Y', 'low_5_Y', 'close_5_Y', 'adjclose_5_Y', 'volume_5_Y', 
                                                'open_6_Y', 'high_6_Y', 'low_6_Y', 'close_6_Y', 'adjclose_6_Y', 
                                                'volume_6_Y', 'open_7_Y', 'high_7_Y', 'low_7_Y', 'close_7_Y', 
                                                'adjclose_7_Y', 'volume_7_Y', 'open_8_Y', 'high_8_Y', 'low_8_Y', 
                                                'close_8_Y', 'adjclose_8_Y', 'volume_8_Y', 'open_9_Y', 'high_9_Y', 
                                                'low_9_Y', 'close_9_Y', 'adjclose_9_Y', 'volume_9_Y', 'open_10_Y', 
                                                'high_10_Y', 'low_10_Y', 'close_10_Y', 'adjclose_10_Y', 
                                                'volume_10_Y', 'open_11_Y', 'high_11_Y', 'low_11_Y', 'close_11_Y', 
                                                'adjclose_11_Y', 'volume_11_Y', 'open_12_Y', 'high_12_Y', 
                                                'low_12_Y', 'close_12_Y', 'adjclose_12_Y', 'volume_12_Y', 
                                                'open_13_Y', 'high_13_Y', 'low_13_Y', 'close_13_Y', 'adjclose_13_Y', 
                                                'volume_13_Y', 'open_14_Y', 'high_14_Y', 'low_14_Y', 'close_14_Y', 
                                                'adjclose_14_Y', 'volume_14_Y', 'open_15_Y', 'high_15_Y', 'low_15_Y', 
                                                'close_15_Y', 'adjclose_15_Y', 'volume_15_Y', 'open_16_Y', 
                                                'high_16_Y', 'low_16_Y', 'close_16_Y', 'adjclose_16_Y', 'volume_16_Y', 
                                                'open_17_Y', 'high_17_Y', 'low_17_Y', 'close_17_Y', 'adjclose_17_Y', 
                                                'volume_17_Y', 'open_18_Y', 'high_18_Y', 'low_18_Y', 'close_18_Y', 
                                                'adjclose_18_Y', 'volume_18_Y', 'open_19_Y', 'high_19_Y', 'low_19_Y', 
                                                'close_19_Y', 'adjclose_19_Y', 'volume_19_Y', 'open_20_Y', 
                                                'high_20_Y', 'low_20_Y', 'close_20_Y', 'adjclose_20_Y', 
                                                'volume_20_Y', 'open_21_Y', 'high_21_Y', 'low_21_Y', 
                                                'close_21_Y', 'adjclose_21_Y', 'volume_21_Y']))
        continue
    
    # Drop the date and ticker column
    stockX.drop(columns=["date", "ticker"], inplace=True)
    stockY.drop(columns=["date", "ticker"], inplace=True)
    
    # Increment the index by 1
    stockX.index = stockX.index + 1
    stockY.index = stockY.index + 1
    
    # Stack the data frame
    stockX_out = stockX.stack()
    stockY_out = stockY.stack()
    
    # Rename the columns
    stockX_out.index = stockX_out.index[::-1].map('{0[1]}_{0[0]}_X'.format) # Reverse the order for X to make it easily concatenated
    stockY_out.index = stockY_out.index.map('{0[1]}_{0[0]}_Y'.format)
    
    # Add the 1-row data frame into stockInfo
    stockInfoX.append(stockX_out.to_frame().T.apply(reverse, axis=1)) # Reverse the values to match with the index
    stockInfoY.append(stockY_out.to_frame().T)
    
    # Pause every 5th request to avoid overloading the API call
    if (i % 5 == 0):
        time.sleep(5)

# In[ ]:


# Concatenate all the stock data frames into 1 data frame (row-wise stacking)
stockDataX = pd.concat(stockInfoX, ignore_index = True, sort=False)
stockDataY = pd.concat(stockInfoY, ignore_index = True, sort=False)

# display(stockDataX)
# display(stockDataY)

# Select 20 sets of days for X data
stockDataX = stockDataX[['volume_20_X', 'adjclose_20_X', 'close_20_X', 'low_20_X', 'high_20_X', 'open_20_X', 
                         'volume_19_X', 'adjclose_19_X', 'close_19_X', 'low_19_X', 'high_19_X', 'open_19_X', 
                         'volume_18_X', 'adjclose_18_X', 'close_18_X', 'low_18_X', 'high_18_X', 'open_18_X', 
                         'volume_17_X', 'adjclose_17_X', 'close_17_X', 'low_17_X', 'high_17_X', 'open_17_X', 
                         'volume_16_X', 'adjclose_16_X', 'close_16_X', 'low_16_X', 'high_16_X', 'open_16_X', 
                         'volume_15_X', 'adjclose_15_X', 'close_15_X', 'low_15_X', 'high_15_X', 'open_15_X', 
                         'volume_14_X', 'adjclose_14_X', 'close_14_X', 'low_14_X', 'high_14_X', 'open_14_X', 
                         'volume_13_X', 'adjclose_13_X', 'close_13_X', 'low_13_X', 'high_13_X', 'open_13_X', 
                         'volume_12_X', 'adjclose_12_X', 'close_12_X', 'low_12_X', 'high_12_X', 'open_12_X', 
                         'volume_11_X', 'adjclose_11_X', 'close_11_X', 'low_11_X', 'high_11_X', 'open_11_X', 
                         'volume_10_X', 'adjclose_10_X', 'close_10_X', 'low_10_X', 'high_10_X', 'open_10_X', 
                         'volume_9_X', 'adjclose_9_X', 'close_9_X', 'low_9_X', 'high_9_X', 'open_9_X', 
                         'volume_8_X', 'adjclose_8_X', 'close_8_X', 'low_8_X', 'high_8_X', 'open_8_X', 
                         'volume_7_X', 'adjclose_7_X', 'close_7_X', 'low_7_X', 'high_7_X', 'open_7_X', 
                         'volume_6_X', 'adjclose_6_X', 'close_6_X', 'low_6_X', 'high_6_X', 'open_6_X', 
                         'volume_5_X', 'adjclose_5_X', 'close_5_X', 'low_5_X', 'high_5_X', 'open_5_X', 
                         'volume_4_X', 'adjclose_4_X', 'close_4_X', 'low_4_X', 'high_4_X', 'open_4_X', 
                         'volume_3_X', 'adjclose_3_X', 'close_3_X', 'low_3_X', 'high_3_X', 'open_3_X', 
                         'volume_2_X', 'adjclose_2_X', 'close_2_X', 'low_2_X', 'high_2_X', 'open_2_X', 
                         'volume_1_X', 'adjclose_1_X', 'close_1_X', 'low_1_X', 'high_1_X', 'open_1_X']]

# Select 20 sets of days for Y data (Skip 1 set, since start date is used in X data, use next 20 sets) 
stockDataY = stockDataY[['open_2_Y', 'high_2_Y', 'low_2_Y', 'close_2_Y', 'adjclose_2_Y','volume_2_Y', 
                         'open_3_Y', 'high_3_Y', 'low_3_Y', 'close_3_Y', 'adjclose_3_Y', 'volume_3_Y', 
                         'open_4_Y', 'high_4_Y', 'low_4_Y', 'close_4_Y', 'adjclose_4_Y', 'volume_4_Y', 
                         'open_5_Y', 'high_5_Y', 'low_5_Y', 'close_5_Y', 'adjclose_5_Y', 'volume_5_Y', 
                         'open_6_Y', 'high_6_Y', 'low_6_Y', 'close_6_Y', 'adjclose_6_Y', 'volume_6_Y', 
                         'open_7_Y', 'high_7_Y', 'low_7_Y', 'close_7_Y', 'adjclose_7_Y', 'volume_7_Y', 
                         'open_8_Y', 'high_8_Y', 'low_8_Y', 'close_8_Y', 'adjclose_8_Y', 'volume_8_Y', 
                         'open_9_Y', 'high_9_Y', 'low_9_Y', 'close_9_Y', 'adjclose_9_Y', 'volume_9_Y', 
                         'open_10_Y', 'high_10_Y', 'low_10_Y', 'close_10_Y', 'adjclose_10_Y', 'volume_10_Y', 
                         'open_11_Y', 'high_11_Y', 'low_11_Y', 'close_11_Y', 'adjclose_11_Y', 'volume_11_Y', 
                         'open_12_Y', 'high_12_Y', 'low_12_Y', 'close_12_Y', 'adjclose_12_Y', 'volume_12_Y', 
                         'open_13_Y', 'high_13_Y', 'low_13_Y', 'close_13_Y', 'adjclose_13_Y', 'volume_13_Y', 
                         'open_14_Y', 'high_14_Y', 'low_14_Y', 'close_14_Y', 'adjclose_14_Y', 'volume_14_Y', 
                         'open_15_Y', 'high_15_Y', 'low_15_Y', 'close_15_Y', 'adjclose_15_Y', 'volume_15_Y', 
                         'open_16_Y', 'high_16_Y', 'low_16_Y', 'close_16_Y', 'adjclose_16_Y', 'volume_16_Y', 
                         'open_17_Y', 'high_17_Y', 'low_17_Y', 'close_17_Y', 'adjclose_17_Y', 'volume_17_Y', 
                         'open_18_Y', 'high_18_Y', 'low_18_Y', 'close_18_Y', 'adjclose_18_Y', 'volume_18_Y', 
                         'open_19_Y', 'high_19_Y', 'low_19_Y', 'close_19_Y', 'adjclose_19_Y', 'volume_19_Y', 
                         'open_20_Y', 'high_20_Y', 'low_20_Y', 'close_20_Y', 'adjclose_20_Y', 'volume_20_Y', 
                         'open_21_Y', 'high_21_Y', 'low_21_Y', 'close_21_Y', 'adjclose_21_Y', 'volume_21_Y']]

# display(stockDataX)
# display(stockDataY)

# In[ ]:

# Concatenate (column-wise) the stock data frames
# stocks = pd.concat([stockDataX, stockDataY], axis=1, sort=False)

# display(stocks)

# Concatenate (column-wise) the stock data frame with the submission information data frame
subs = pd.concat([subs, stockDataX, stockDataY], axis=1, sort=False)

# Keep all the rows without an error (Remember error means there's a -1)
# Volume can never be negative
subs = subs[subs['volume_20_X'] != -1]

# In[ ]:

#display(subs)

# Overwrite the original file
subs.to_csv("./Data/{}".format(sys.argv[2]), index=False)
