# Description: Write csv files within a time range
import pandas as pd
import datetime as dt

# Read the file
data = pd.read_csv("filename.csv")

# Convert date column from string to date
data["date"] = pd.to_datetime(data["date"])

dates = data["date"].unique()

# For each unique date
for i in range(len(dates)):
    
    # start date
    sd = dates[i]
    
    # end date
    # Change the value for days to make different groupings
    ed = sd - pd.Timedelta(2, unit='d')
    
    # If the end date is in the date column 
    # Skips records with no end date, i.e. for 5 days windows, Jan 1-4 will be ignored
    if (pd.Timestamp(ed) in set(data.date)):
        
        # Create the mask
        mask = (data['date'] >= ed) & (data['date'] <= sd)
        
        # Create the subset to the window size
        subset = data.loc[mask]
        
        # Write the subset into a csv
        subset.to_csv("filepath/subset_windowsize_3_{}.csv".format(i+1), index = False)