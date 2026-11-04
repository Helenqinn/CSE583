import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the CSV file into a pandas dataframe
df = pd.read_csv("/Users/ruihanqin/CSE583/hw1/src/hw1_data_analysis/bicycle_data.csv")
print(df.dtypes)

# 2. Describe the columns in the dataframe and what data types they should be
# Date: The timestamp of each hour, and the data type should be a datetime but currently is a string.
# Fremont Bridge Sidewalks, south of N 34th St Total: The total count of bicycles crossing the Fremont Bridge. The data type should be numeric 
#                                                     and currently is float, which is number with decimal part. Float is an appropriate type. 
#                                                     But to be more precise, integer would be the best fit as count should not have decimal part.
# Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk: The count of bicycles on the west sidewalk. The data type should be numeric 
#                                                     and currently is float, which is number with decimal part. Float is an appropriate type. 
#                                                     But to be more precise, integer would be the best fit as count should not have decimal part.
# Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk: The count of bicycles on the east sidewalk. The data type should be numeric 
#                                                     and currently is float, which is number with decimal part. Float is an appropriate type. 
#                                                     But to be more precise, integer would be the best fit as count should not have decimal part.

# Convert Date to be datetime
df["Date"] = pd.to_datetime(df["Date"], format="mixed")

# 3. Add columns to the dataframe
df["Total"] = df[["Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk", "Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"]].sum(axis=1)
df["Hour"] = df["Date"].dt.hour
df["Year"] = df["Date"].dt.year

# 4. Create a new dataframe with the subset of data from the year 2016
df_2016 = df[df["Year"] == 2016].copy()

# 5. Missing data
missing = df_2016[["Fremont Bridge Sidewalks, south of N 34th St Total", "Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk", "Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"]].isna().any(axis=1)
int(missing.sum())

# There is 1 point in the new dataframe with missing data.
# I decided to drop this missing data.
df_2016 = df_2016[~missing]

# 6. Plot the counts by hour
hourly_mean = df_2016.groupby("Hour")["Total"].mean()
 
fig, ax = plt.subplots(figsize=(8, 5))
hourly_mean.plot(kind="bar", ax=ax, color="steelblue")
ax.set_title("Fremont Bridge bicycle counts by hour of day, 2016")
ax.set_xlabel("Hour of day")
ax.set_ylabel("Average total count (East + West)")
fig.tight_layout()
fig.savefig("/Users/ruihanqin/CSE583/hw1/src/hw1_data_analysis/counts_by_hour.png", dpi=150)

# 7. Busiest hour of the day
busiest_hour = int(hourly_mean.idxmax())
print(busiest_hour)

# The busiest hour of the day is 17:00.