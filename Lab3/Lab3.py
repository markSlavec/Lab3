import json
import pandas as pd

#1.1


# �������� ����� contributors_sample.json.
with open('contributors_sample.json') as f:
    contributors = json.load(f)

# ����������� ���������� � ������ ���� �������������
print("(1.1):")
for i in range(3):
    user = contributors[i]
    print(f"User {i+1}:")
    print(f"Username: {user['username']}")
    print(f"Name: {user['name']}")
    print(f"Sex: {user['sex']}")
    print(f"Address: {user['address']}")
    print(f"Mail: {user['mail']}")
    print(f"Jobs: {user['jobs']}")
    print(f"ID: {user['id']}")
    print()



#1.2


# ���������� ���������� ������� ����������� �����
domains = set()
for user in contributors:
    domain = user['mail'].split('@')[1]
    domains.add(domain)

# Print unique email domains
print("(1.2):")
print("Unique email domains:")
for domain in domains:
    print(domain)
print()





#1.3


def search_by_username(username):
    # ����� ������������ � �������� ������ ������������
    for user in contributors:
        if user['username'] == username:
            # ����������� ���������� � ������������ 
            print(f"Username: {user['username']}")
            print(f"Name: {user['name']}")
            print(f"Sex: {user['sex']}")
            print(f"Address: {user['address']}")
            print(f"Mail: {user['mail']}")
            print(f"Jobs: {user['jobs']}")
            print(f"ID: {user['id']}")
            return

    # ���� ������������ �� ��� ������, ���������� ���������� ValueError.
    raise ValueError(f"No user with username {username} found")





#1.4



# ������� ������ � ������ 
men_count = 0
women_count = 0
for user in contributors:
    if user['sex'] == 'M':
        men_count += 1
    elif user['sex'] == 'F':
        women_count += 1

# ����������� �����������
print("(1.4):")
print(f"Men: {men_count}")
print(f"Women: {women_count}")
print()





#1.5


# ������ ��������, ���������� ������ �������
contributors_list = []
for user in contributors:
    contributor_dict = {'id': user['id'], 'username': user['username'], 'sex': user['sex']}
    contributors_list.append(contributor_dict)

# DataFrame �� ������ ��������
contributors_df = pd.DataFrame(contributors_list)

# Print DataFrame
print("(1.5):")
print(contributors_df)
print()





#1.6


# Load data from CSV file into a pandas DataFrame
recipes_df = pd.read_csv('recipes_sample.csv')

# Load data from JSON file into a pandas DataFrame
with open('contributors_sample.json') as f:
    contributors_data = json.load(f)
contributors_df = pd.DataFrame(contributors_data)

# Merge the recipes and contributors DataFrames on the 'contributor_id' column
merged_df = pd.merge(recipes_df, contributors_df, on='id', how='left')

# Count the number of rows in the merged DataFrame where the person information is missing
missing_info_count = merged_df[merged_df['username'].isnull()].shape[0]

print(f'{missing_info_count} people are missing information.')