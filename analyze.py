import pandas as pd

# Define the file path
file_path = "E:\Projects\Time Pass\Blood Donation\data.csv"

# Read the CSV file into a pandas dataframe
data = pd.read_csv(file_path)

# Extract the phone numbers and names from the dataframe
phone_numbers = data["Mobile Number"].tolist()
names = data["full_name"].tolist()
bloodGroup = data["Blood_Group"].tolist()

bloodGroupCount = {
    'B positive':0, 'A positive':0, 'A negative':0, 'O negative':0, 'B negative':0, 'Not Known':0, 'O positive':0, 'AB positive':0
}
for i in range(len(phone_numbers)):
    currentGroup =bloodGroup[i]
    bloodGroupCount[currentGroup]=bloodGroupCount[currentGroup]+1

print(bloodGroupCount)
