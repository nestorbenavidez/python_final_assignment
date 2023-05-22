"""
Python Programming: Coursework
------------------------------

The instructions are listed in the attached Word document. Please do not change the
structure of this file. Add your solutions within the functions where it says "Your
code follows below: replace `None` with your code". Do not remove any of the code.

"""

import os
import pickle
import pandas as pd


# Add your import statements here...


# Change working directory: add the correct path
os.chdir('/Users/nestorbenavidez/Documents/python_final_assignment')
print('Current working dir:', os.getcwd())

# Replace your student ID
student_id = '355422032'


"""
Example:
You have to add your answer within the functions. This is slightly different to what 
we did in class and similar to the Jupyter Notebook exercises we had at the start. You
can see an example below:

    Q0: Compute the sum of two integers.

The template for this question looks like that:

    def q0(num_1, num_2):
        # Your code follows below: replace `None` with your code
        sum_of_the_two = None
        
        # Do not change the code below
        return sum_of_the_two 

The code below shows my attempt in solving the question:
"""

def q0(num_1, num_2):
    # Your code follows below: replace `None` with your code
    sum_of_the_two = num_1 + num_2

    # Do not change the code below
    return sum_of_the_two

"""
Task 1: Python fundamentals
"""

def q1():
    # Example of using a list: storing a series of measurements
    example_list = [1.2, 1.5, 1.3, 1.4, 1.6]

    # Example of using a tuple: representing a point in 3D space
    example_tuple = (1.0, 2.0, 3.0)

    # Example of using a dictionary: storing information about proteins
    example_dict = {'p53': 'tumor suppressor', 'insulin': 'hormone'}

    # Return the examples
    return example_list, example_tuple, example_dict


#we use the exponentiation operator ** with the value of 0.5 to calculate the square root of each number
# in the range. The resulting list of square roots is then returned.

def q2(lower_limit=11, upper_limit=23):
    # Your code follows below: replace `None` with your code
    # NOTE: The range() function in Python includes the lower limit but excludes the upper limit.
    # This means that range(lower_limit, upper_limit) generates a sequence that starts at lower_limit
    # and goes up to, but does not include, upper_limit.
    square_roots = [(n ** 0.5) for n in range(lower_limit, upper_limit+1)]

    # Do not change the code below
    return square_roots



def q3(num_rows=15, num_cols=100):
    # Your code follows below: add your code and assign the created DataFrame to `df`
    df = [[None] * num_cols for _ in range(num_rows)]

    # Save the DataFrame as a pickle file
    with open('./data-task1/q3_df.pkl', 'wb') as f:
        pickle.dump(df, f)

    # Return the DataFrame
    return df



def q4(companies=('Apple', 'Amazon', 'Alphabet', 'Microsoft', 'Visa')):
    # List comprehension that checks for the presence of 'p' in each company name and appends
    # the uppercase or lowercase version of the name to `companies_new` accordingly.
    companies_new = [company.upper() if 'p' in company else company.lower() for company in companies]

    # Return the new list of company names.
    return companies_new

def q5(companies=('Microsoft', 'Berkshire Hathaway', 'Apple')):
    # Create the subdirectory if it doesn't exist
    if not os.path.exists('data-task1'):
        os.makedirs('data-task1')

    # Create empty text files for each company
    for company in companies:
        filename = os.path.join('data-task1', f'{company}.txt')
        with open(filename, 'w') as f:
            pass

    return True


def q6(input_dir='data-task1/q6/'):
    # Your code follows below: add your code (find all .txt files in `input_dir` and
    # assign the corresponding list to `extracted_contents`
    extracted_contents = []
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    extracted_contents.append(content)

    # Do not change the code below
    return extracted_contents


"""
Task 2: pandas
"""

def q10():
    # Load the two CSV files: company-info.csv and compensation-data.csv
    comp_info = pd.read_csv('./data-task2/company-info.csv')
    comp_data = pd.read_csv('./data-task2/compensation-data.csv')

    # Return the loaded data frames
    return comp_info, comp_data
print("q10")
print(q10())

def q11():
    # Load the data set
    _, df_data = q10()

    # Check if the 'GENDER' column exists in the DataFrame
    if 'gender' not in df_data.columns:
        print("Error: 'GENDER' column is missing in the DataFrame.")
        return None

    # Create a new column 'female' with a value of 1 if the executive is female, 0 otherwise
    df_data['female'] = df_data['gender'].apply(lambda x: 1 if x == 'F' else 0)

    # Return the modified data frame
    return df_data

print("q11")
print(q11())

def q12():
    # Run this code to load the data set (necessary for next steps)
    df_info, _ = q10()
    df_data = q11()

    # Step 1: Filter `df_data` and keep only observations of 2017
    filtered_df = df_data[df_data['year'] == 2017]

    # Step 2: Use the filtered DataFrame and compute/count the overall number of executives
    # and the number of female executives per company
    exec_counts = filtered_df.groupby('gvkey').agg(
        num_total_execs=('exec_fullname', 'size'),
        num_female_execs=('female', 'sum')
    ).reset_index()

    # Step 3: Use `exec_counts` and compute the share/percentage of female executives per company
    exec_counts['share_female'] = exec_counts['num_female_execs'] / exec_counts['num_total_execs']

    # Step 4: Merge `exec_counts` with `df_info` to retrieve company names
    merged_df = pd.merge(exec_counts, df_info[['gvkey', 'coname']], on='gvkey', how='inner')

    # Step 5: Find the maximum share_female value
    max_share_female = merged_df['share_female'].max()

    # Step 6: Get the company names with the maximum share_female value
    company_names = merged_df[merged_df['share_female'] == max_share_female]['coname'].tolist()

    # Return the list of company names
    return company_names



print("q12")
print(q12())

def q13():
    # Load the data set
    _, df_data = q10()

    # Filter the data for the year 2016 and calculate the average age per company
    average_age_per_company = df_data[df_data['year'] == 2016].groupby('gvkey')['age'].mean()

    # Return the average age per company
    return average_age_per_company
print("q13")
print(q13())

def q14():
    # Load the data sets
    df_info, df_data = q10()

    # Merge `df_data` and `df_info`
    merged_df = pd.merge(df_data, df_info, on='gvkey')

    # Format the date columns 'becameceo' and 'leftofc' as a date
    merged_df['becameceo'] = pd.to_datetime(merged_df['becameceo'])
    merged_df['leftofc'] = pd.to_datetime(merged_df['leftofc'])

    # If the CEO was appointed in the past but there is no end date, set the end date to '2020-12-31'
    merged_df.loc[merged_df['leftofc'].isnull() & (merged_df['becameceo'] < '2021-01-01'), 'leftofc'] = '2020-12-31'

    # Create a new column 'duration_tenure' with the tenure, i.e., difference of end and start date
    merged_df['duration_tenure'] = (merged_df['leftofc'] - merged_df['becameceo']).dt.days

    # Remove rows with invalid 'duration_tenure', remove duplicates, and keep only the desired columns
    cols_to_export = ['gvkey', 'coname', 'exec_fullname', 'gender', 'becameceo', 'leftofc', 'duration_tenure']
    filtered_ceo_tenure = merged_df.drop_duplicates(subset=cols_to_export).loc[merged_df['duration_tenure'] >= 0, cols_to_export]

    # Export the DataFrame as a pickled file
    filtered_ceo_tenure.to_pickle('./data-task2/ceo_data.pkl')

    # Return the filtered DataFrame
    return filtered_ceo_tenure

print("q14")
print(q14())

"""
Task 3: Matplotlib
"""

def q21():
    # Your code follows below: replace `None` with your code
    df = None

    # Do not change the code below
    return df


def q22():
    # Run this code to load the data set
    returns_data = q21()

    # Your code follows below: add your code and assign the new DataFrame to `monthly_data`.
    monthly_data = None

    # Do not change the code below
    return monthly_data


def q23():
    global student_id

    # Run this code to load the data set
    monthly_data = q22()

    # Your code follows below: add your code and assign the plot to a variable `plot`
    plot = None

    # Run this to show your plot
    plot.figure.show()

    # Do not change the code below
    plot.figure.savefig(str(student_id) + '.png')
    return plot
