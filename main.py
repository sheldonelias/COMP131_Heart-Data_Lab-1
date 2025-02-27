import csv
import numpy as np

# GLOBAL VARIABLES

data_file_lines = []

# USER-DEFINED FUNCTIONS
def import_data():
    global data_file_lines

    my_file_path_name = input('Enter file path and name:')

    data_file = open(str(my_file_path_name))

    print(data_file)

    data_file_lines = data_file.readlines()

    print(data_file_lines)

    data_file.close()

    # Does not work due to hetero datatype mix
    # file_data = np.loadtxt("Heart.csv", delimiter=',')
    # print(file_data)
    pass


def gather_sex():
    global data_file_lines

    sex_col = []

    for row in data_file_lines:

        # print(row.split(',')[2])

        sex_col.append(row.split(',')[2])

    return sex_col




# Store age column into a list
def gather_age():
    global data_file_lines

    age_col = []

    for row in data_file_lines:

        #print(row.split(',')[1])

        age_col.append(row.split(',')[1])

    return age_col

# Store cholesterol in a list
def gather_cholesterol():
    global data_file_lines

    cholesterol_col = []

    for row in data_file_lines:

        #print(row.split(',')[5])

        cholesterol_col.append(row.split(',')[5])

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

    num_data_np_array = np.array([ gather_sex(), gather_age() , gather_cholesterol() ])

    print(num_data_np_array)


    pass

def calc_avg(iterable):

    count = len(iterable)


    pass

def main():

    import_data()

    # gather_sex()

    # print(gather_age())

    # print(gather_cholesterol())

    #calc_avg(gather_age())

    gather_num_data()

    pass


main()

