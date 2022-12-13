# define the number of rows in the pyramid
rows = 10

# use a for loop to print each row of the pyramid
for i in range(rows):
    # calculate the number of asterisks in this row
    # the first row has one asterisk, the second row has three, and so on
  num_asterisks = 2 * i + 1

  # print the row of asterisks, using the format() function to center it
  print("{:^21}".format("*" * num_asterisks))
