# Ques 2. Create a DataFrame directly from the url provided. Set Month as index and rename the column "1960" to "1961" .

# Url = https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv

import pandas as pd

Q2_df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv")
Q2_column = Q2_df.columns
print(Q2_column)

Q2_df.set_index("Month", inplace=True)
Q2_df.rename(columns={' "1960"' : ' "1961"'}, inplace=True)

print(Q2_df.head())