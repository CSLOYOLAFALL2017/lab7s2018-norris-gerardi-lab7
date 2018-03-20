import os

def file_read():
    filename = input("Please enter a valid filename:\n")
    while not os.path.exists(filename):
      filename = input("Please enter a valid filename:\n")
    return filename

def file_to_write():
    global new_file
    global new_files_name
    new_files_name = input("Please enter a new filename:\n")
    new_file = open(new_files_name + ".csv", "w")
    return new_file


def highest_profit(filename):
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


print("Highest profit of these movies: $", highest_profit(file_read()),
      '\n', "Movie title: ", max_profit_title,
      '\n', "File: ", new_files_name, " has been created in the local directory.",
      sep='')

