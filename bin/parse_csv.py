import pandas as pd

# 1. Open the .csv file using Pandas into a DF
# dataframe = pd.read_csv('../data/addresses.csv')
dataframe = pd.read_csv('../data/addresses.csv')
print(dataframe)
# 2. Create a dataset that includes addresses from SD
# rslt_df = dataframe[dataframe['state'] == 'SD'] 
# rslt_df = dataframe[dataframe["state"].str.contains("SD",case=False)]
# 3. Write the dataset to a datafile
# print(rslt_df)
# rslt_df.to_csv('../output.csv', header=False, index=False)


# 2. Create a dataset that includes only the columns "Task Name" and "Assignee"
# rslt_df = dataframe[dataframe['state'] == 'SD'] 
rslt_df = dataframe[['Task Name', 'Assignee']]
# print(rslt_df)
# rslt_df = dataframe[dataframe["state"].str.contains("SD",case=False)]

# 3. Create a dataset that only includes tasks that "Smith" was assigned
rslt_df = dataframe[dataframe["Assignee"].str.contains("Smith",case=False)]
print(rslt_df)

# 3. Write the dataset to a datafile
# print(rslt_df)
# rslt_df.to_csv('../output.csv', header=False, index=False)