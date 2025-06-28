import pandas as pd

# Step 1: Create a list of dictionaries (data)
data = [
    {"Name": "Rahul", "Age": 24, "City": "Kolkata"},
    {"Name": "Rohit", "Age": 29, "City": "Salt-lake"},
    {"Name": "Ramij", "Age": 23, "City": "Dimond Harbour"}
]

# Step 2: Convert to DataFrame
df = pd.DataFrame(data)

# Step 3: Add a new column with values
#df["Gender"] = ["Male", "Male","Male"]
#df["GF1"] = ["Shrouti","Riya", "Piya"]

# Step 4: Save to CSV file
df.to_csv("people.csv", index=False)

print("CSV file 'people.csv' created successfully with 'Gender' column.")
