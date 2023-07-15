# Imports
import pandas as pd
import numpy as np
import datetime as dt
import re

# Read the comments data
ci = pd.read_csv("./Data/comment_aa_info.csv", 
                 usecols = ["body", "date", "comment_id", "score", "submission_id", "number_of_replies", "total_awards"],
                 low_memory = False)

# Read the comment author info data
cai = pd.read_csv("./Data/comment_author_aa_info.csv", 
                  usecols = ["author_commentkarma", "author_id", "author_name", "comment_id", "submission_id"],
                  low_memory = False)

# Merge ci and cai
coms = ci.merge(cai, how="outer", on="comment_id")

# Filter out removed and deleted comments comments
coms = coms[coms['body'] != "[removed]"]
coms = coms[coms['body'] != "[deleted]"]

# Filter out comments that have NaN
coms = coms[~coms['body'].isna()]
coms = coms[~coms['date'].isna()] # Will only affect the 2nd partition
coms = coms[~coms['total_awards'].isna()] # Will only affect the 2nd partition

# Convert date to month-day-Year format as string
coms["date"] = coms["date"].map(dt.datetime.utcfromtimestamp)

# Reset the indices
coms.reset_index(inplace = True)

# Convert the date column into string and reorder it as month, day, year
for i in range(len(coms["date"])):
    coms["date"][i] = coms["date"][i].strftime("%m/%d/%Y")

for j in range(len(com["date"])):
    coms["date"][i] = (coms["date"][i] + "/")[5:] + (coms["date"][i][:4])
    
# Remove all rows with 2021
coms = coms[~(coms.date.str.contains("2021"))]

# Save the file
coms.to_csv("./Data/comment_all_1.csv", index=False)
