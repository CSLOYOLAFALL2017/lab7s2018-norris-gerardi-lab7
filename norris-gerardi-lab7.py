import os

def file_read():
    """
    The purpose of this function is to open an existing file to read, given the filename by the user.
    :return: filename, for use in 'highest_profit'.
    """
    filename = input("Please enter a valid filename:\n")
    while not os.path.exists(filename):
      filename = input("Please enter a valid filename:\n")
    return filename

def file_to_write():
    """
    The purpose of this function is to create/override a file for writing, given a filename by the user.
    :return: new_file, for use in 'highest_profit'.
    """
    global new_file
    global new_files_name
    new_files_name = input("Please enter a new filename:\n")
    new_file = open(new_files_name + ".csv", "w")
    return new_file


def highest_profit(filename):
    """
    The purpose of this function is to process the existing file, and calculate the profit of each movie found.
    After iterating through all movies, the highest profit is returned, and the new file created will contain
    the profits of each movie, along with title and release date.
    :param filename: from 'file_read'.
    :return: max_profit, and the creation of a new file.
    """
    max_profit = 0
    global max_profit_title
    file_open = open(filename, "r")
    file_to_write()
    for line in file_open:
        releaseDate, movieTitle, budget, boxOfficeGross = line.split(',')
        profit = float(boxOfficeGross) - float(budget)
        print(releaseDate, movieTitle, profit, '\n', file= new_file)
        if profit > max_profit:
            max_profit = profit
            max_profit_title = movieTitle
    max_profit = '{0:,.2f}'.format(max_profit)
    file_open.close()
    new_file.close()

    return max_profit

def main():
    """
    As always, this is the beginning of flow for our program.
    :return: functions' outputs, formatted for display to the user.
    """
    print('{:15}{}'.format("Highest profit: $", highest_profit(file_read())),
        '\n', '{:16}{}'.format("Movie title: ", max_profit_title),
        '\n', "File: ", new_files_name, ".csv, has been created in the local directory.",
        sep='')

main()
