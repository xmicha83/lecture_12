import csv
import os
import random

cwd_path = os.getcwd()

def read_row(file_name):
    """
    Reads one row for a CSV file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (list, int),
    """
    with open(file_name, "r", encoding="utf-8") as file:
        soubor = csv.reader(file, delimiter="\t")
        values = []
        for line in soubor:
            row = [int(number) for number in line]

    return row




def read_rows(file_name, row_number):
    """
    Reads selected row for a CSV file and returns selected numeric data.
    :param file_name: (str), name of CSV file
    :param row_number: (int), number of selected row
    :return: (list, int),
    """
    with open(file_name, "r", encoding="utf-8") as file:
        soubor = csv.reader(file)
        # rows = []
        for idx, line in enumerate(soubor):
            row = [int(number) for number in line]
    #         rows.append(row)
    #
    # return rows[row_number-1]


def selection_sort(number_array, direction="ascending"):
    """
        Sorts and returns selected numeric data with Selection Sort.
        :param number_array: (list,int), list with numeric array
        :return: (list, int), sorted numeric array
    """

    for i in range(len(number_array)):
        minimum = i
        for j in range(i+1, len(number_array)):
            if direction == "ascending":
                if number_array[j] < number_array[minimum]:
                    minimum = j
            if direction == "descending":
                if number_array[j] > number_array[minimum]:
                    minimum = j
        number_array[i], number_array[minimum] = number_array[minimum], number_array[i]

    return number_array


def bubble_sort(number_array):
    """
       Sorts and returns selected numeric data with Bubble Sort.
       :param number_array: (list,int), list with numeric array
       :return: (list, int), sorted numeric array
    """
    for i in range(len(number_array)-1):
        for j in range(len(number_array)-i-1):
            if number_array[j] > number_array[j+1]:
                number_array[j], number_array[j+1] = number_array[j+1], number_array[j]


def main():

    data = read_row('numbers_one.csv')
    print(data)

    data2 = read_rows('numbers_two.csv', 2)
    print(data2)

    # Ukol: Selection Sort
    sel_sort = selection_sort(data, 'ascending')
    print(sel_sort)

    bubble = bubble_sort(data2)
    print(bubble)

    # Ukol: Selection Sort - se smerem razeni
    

    # Ukol: Bubble Sort


    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()

