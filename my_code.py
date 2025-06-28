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
df["Gender"] = ["Male", "Male", "Male"]
# df["GF1"] = ["Shrouti", "Riya", "Piya"]

# Step 4: Save to CSV file in specified directory
file_path = r"E:\Code_practice\datasets\people.csv"
df.to_csv(file_path, index=False)

print(f"CSV file saved successfully at '{file_path}'")
