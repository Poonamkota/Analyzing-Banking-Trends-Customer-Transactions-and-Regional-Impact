Project Description
In the ever-evolving world of banking and finance, understanding customer behavior and the regional impact of transactions plays a crucial role in decision-making and strategic planning. This project, titled "Analyzing Banking Trends: Customer Transactions and Regional Impact," aims to explore and analyze the vast troves of transaction data to gain valuable insights into customer behavior patterns and their implications on different world regions.

Objective: The primary objective of this project is to delve into customer transactions and identify trends that may impact regional economies and financial systems. By combining data cleaning techniques in Python and utilizing SQL queries on a set of interconnected tables, we aim to gain a comprehensive understanding of how customer transactions vary across different regions and the possible implications on the banking sector.

Data Sources: The project leverages three key tables that provide valuable information for analysis:

world_regions table: This table contains data on various world regions and their corresponding codes and names. It serves as a reference to categorize customers based on their regional affiliation.

user_nodes table: The user_nodes table holds crucial details about consumers' banking nodes, including their unique consumer IDs, associated region IDs, node IDs, start dates, and end dates. This data enables us to identify the specific banking nodes to which customers are connected and their duration of association.

user_transaction table: This table is a comprehensive repository of customer transactions, containing data such as consumer IDs, transaction dates, types of transactions, and transaction amounts. Analyzing this data allows us to uncover patterns in customer spending and financial behaviors


Module 1



import pandas as pd
import warnings
warnings.filterwarnings("ignore")

Read CSV file user_nodes.csv

# Function to read the CSV file into a DataFrame
def read_csv():
    # read the user_nodes.csv file using pandas library and return it
    df = pd.read_csv('user_nodes.csv')
    return df

Task 1: Check the null values
The function check_null_values() reads a DataFrame from read_csv  function which returns data in the user_nodes csv file and the it needs to  calculates the sum of null (missing) values for each column in the DataFrame.

# Function to check for null (missing) values in the DataFrame
def check_null_values():
    # do not edit the predefined function name
    df = read_csv()
    # Check for null values using the isnull() method and sum them for each column
    null_values = df.isnull().sum()
    
    return null_values

Task 2: Find the Duplicate Values
Here, We need to check for duplicate values in a dataset  for each column.

# Function to check for duplicate rows in the DataFrame
def check_duplicates():
    # do not edit the predefined function name
    df = read_csv()
    # Calculate the number of duplicate rows using the duplicated() method and sum them
    duplicates = df.duplicated().sum()
    
    return duplicates

Task 3: Remove the Duplicate Values
The function drop_duplicates() reads a DataFrame from a CSV file, removes any duplicate rows in the DataFrame, and returns the cleaned DataFrame without duplicates.

# Function to drop duplicate rows from the DataFrame
def drop_duplicates():
    # do not edit the predefined function name
    df = read_csv()
    # Drop duplicate rows using the drop_duplicates() method with inplace=True
    df.drop_duplicates(inplace=True)
    return df

Task 4: Data Cleaning:
The provided function, data_cleaning(), aims to enhance the quality and structure of a given DataFrame. It starts by removing duplicate rows to ensure data consistency. Subsequently, the function eliminates the columns "has_loan" and "is_act" from the DataFrame, streamlining it for analysis. To improve clarity, column names are adjusted: 'id_' becomes 'consumer_id', 'area_id_' is transformed to 'region_id', 'node_id_' is changed to 'node_id', 'act_date' is renamed to 'start_date', and 'deact_date' is converted to 'end_date'. The final step involves exporting the cleaned DataFrame to a CSV file named 'user_nodes_cleaned.csv', without including the index column. Upon completion, the function returns the cleaned DataFrame, now prepared for further analysis.

def data_cleaning():

    df = drop_duplicates()

    # Step 3: Drop specified columns from the DataFrame("has_loan", "is_act")
    df = df.drop(columns=['has_loan','is_act'])
    #Rename columns names id_,area_id_,node_id_,act_date',deact_date to  consumer_id,region_id,node_id,start_date,end_date
    df.rename(columns = {'id_':'consumer_id','area_id_':'region_id', 'node_id_':'node_id', 'act_date':'start_date','deact_date':'end_date'}, inplace = True)

    #df.to_csv('user_nodes_cleaned.csv', index=False)
    df.to_csv('user_nodes_cleaned.csv', index=False)
    return df

Read CSV file user_transactions.csv

import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# Function to read the CSV file into a DataFrame
def read_csv():
    # read the user_transactions.csv file using pandas library and return it
    df = pd.read_csv('user_transactions.csv')
    return df
	
Rask 5: Check the null values
The function check_null_values() reads a DataFrame from read_csv  function which returns data in the user_transactions csv file and the it needs to  calculates the sum of null (missing) values for each column in the DataFrame.

Check the null values
The function check_null_values() reads a DataFrame from read_csv  function which returns data in the user_transactions csv file and the it needs to  calculates the sum of null (missing) values for each column in the DataFrame.

# Function to check for null (missing) values in the DataFrame
def check_null_values():
    # do not edit the predefined function name
    df = read_csv()
    # Check for null values using the isnull() method and sum them for each column
    null_values = df.isnull().sum()
    
    return null_values

# Function to check for duplicate rows in the DataFrame
def check_duplicates():
    # do not edit the predefined function name
    df = read_csv()
    # Calculate the number of duplicate rows using the duplicated() method and sum them
    duplicates = df.duplicated().sum()
    
    return duplicates


Task 6: Find the Duplicate Values
We need to check for duplicate values in a dataset  for each column. Finally, the counts of duplicated values are returned as a integer. This information can be useful in identifying duplicate data and deciding on appropriate strategies to deal with them, such as imputation or deletion.


Task 7: Remove the Duplicate Values. The function drop_duplicates() reads a DataFrame from a CSV file, removes any duplicate rows in the DataFrame, and returns the cleaned DataFrame without duplicates.


# Function to drop duplicate rows from the DataFrame
def drop_duplicates():
    # do not edit the predefined function name
    df = read_csv()
    # Drop duplicate rows using the drop_duplicates() method with inplace=True
    df.drop_duplicates(inplace=True)
    return df

Task 8: Data Cleaning:
The function data_cleaning() is designed to enhance a DataFrame's quality by removing specific columns and renaming others, preparing the data for analysis. Initially, duplicate rows are removed and any rows with null values are dropped. Then, the columns "has_credit_card" and "account_type" are selected for removal to streamline the dataset for analysis. The DataFrame's columns are updated by renaming 'id_' to 'consumer_id', 't_date' to 'transaction_date', 't_type' to 'transaction_type', and 't_amt' to 'transaction_amount' for improved clarity and interpretation. Once these steps are completed, the cleaned DataFrame is saved as 'user_transaction_cleaned.csv' without the index column and returned for further analysis.
def data_cleaning():
    """
    Data Cleaning Function:
    Cleans the DataFrame by dropping specified columns and renaming others.

    Returns:
    DataFrame: The cleaned DataFrame after dropping and renaming columns.
    """
    # Step 1: Get the DataFrame with duplicate rows removed and rows with null values dropped
    df = drop_duplicates()
 
    # Step 2: Columns to remove from the DataFrame
    #columns needs to be removed "has_credit_card" and  "account_type"
    # Drop specified columns from the DataFrame
    df = df.drop(columns=['has_credit_card','account_type'])

    #Rename columns id_,t_date,t_type,t_amt to consumer_id,transaction_date,transaction_type,transaction_amount
    df.rename(columns = {'id_':'consumer_id','t_date':'transaction_date', 't_type':'transaction_type', 't_amt':'transaction_amount'}, inplace = True)

    # Step 5: Rename columns using the new column names

    #df.to_csv('user_transaction_cleaned.csv', index=False)
    df.to_csv('user_transaction_cleaned.csv', index=False)
    return df

Task 9: Generate tables using the cleaned dataset:
Download the cleaned dataset by clicking on the file name from File explorer.

You must download the world_regions csv file as well as the user nodes and user transactions cleaned csv files in order to proceed. To continue with this project, you must add all three CSV files to the database.

Utilize the MySQL database information provided in ""Database Details"" to manually create the following tables for the cleaned dataset

user_nodes
user_transaction
world_regions

