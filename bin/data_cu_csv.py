import pandas as pd

# https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment

# URL to open venv^

# 1. Open the .csv file using Pandas into a DF


def to_list(s):
    items = s.replace("[", "").replace("]", "").split(",")
    ret = []
    for i in items:
        ret.append(i.lstrip())
    return ret

# .csv needs to be changed to the file that contains the data 

df = pd.read_csv("../data/addresses.csv", converters={'Assignee': to_list})

#   2. Create a dataset that includes addresses from SD

df2 = df.explode('Assignee')[["Assignee", "Task Name"]]

#   3. Write the dataset to a datafile

people = df2["Assignee"].unique()

# 2. Create a dataset that includes only the columns "Task Name" and "Assignee"


# 3. Create a dataset that only includes tasks that "Smith" was assigned

# 3. Write the dataset to a datafile
for person in people:
    print("------------------------")
    print(df2[df2["Assignee"] == person])






