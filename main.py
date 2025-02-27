import csv
import numpy as np

# GLOBAL VARIABLES

data_file_lines = []

# USER-DEFINED FUNCTIONS
def import_data():
    # Need declare as global to share across all functions that
    # need to access data_file_lines
    global data_file_lines

    # Get file name from user
    my_file_path_name = input('Enter file path and name:')

    # Create IO Wrapper object
    data_file = open(str(my_file_path_name))
    # Check its structure
    print(data_file)
    # Convert IO Wrapper object to list of strings
    data_file_lines = data_file.readlines()
    # Check its structure
    print(data_file_lines)
    # Close the IO stream
    data_file.close()

    # Does not work due to hetero datatype mix
    # file_data = np.loadtxt("Heart.csv", delimiter=',')
    # print(file_data)
    pass


def gather_sex():
    global data_file_lines

    #sex_col = []
    # Stub assignment. Replace with above after loop is written.
    sex_col = [1, 2, 3, 4, 5]

    # Write the loop to get sex data column into sex_col list

    return sex_col


# Store age column into a list
def gather_age():
    global data_file_lines

    #age_col = []
    # Stub assignment. Replace with above after loop is written.
    age_col = [1, 2, 3, 4, 5]

    # Write the loop to get age data column into sex_col list

    return age_col


# Store cholesterol in a list
def gather_cholesterol():
    global data_file_lines

    #cholesterol_col = []
    # Stub assignment. Replace with above after loop is written.
    cholesterol_col = [1,2,3,4,5]

    # Write the loop to get cholesterol data column into sex_col list

    return cholesterol_col

# Store all numerical data into numpy array
def gather_num_data():
    '''
    Conversion of list to numpy array
    For multiple lists, all lists must have the same number of elements
    my_list1 = [1, 2, 3, 4, 5]
    my_list2 = [6, 7, 8, 9, 10]
    my_array = np.array([my_list1,my_list2])
    '''

    # Each function call returns a list that becomes a member row of the numpy array
    num_data_np_array = np.array([ gather_sex(), gather_age() , gather_cholesterol() ])

    # Check values and structure
    # print(num_data_np_array)

    return num_data_np_array

def calc_avg(iterable):

    iterable_count = len(iterable)

    iterable_sum = sum(iterable)

    return iterable_sum/iterable_count


def main():

    import_data()

    # gather_sex()

    # print(gather_age())

    # print(gather_cholesterol())

    gather_num_data()

    # Use calc_avg(). Replace dummy list with function that returns column data, eg. gather_age()
    res = calc_avg(gather_num_data()[2])

    print(res)

    pass


main()

