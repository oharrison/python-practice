import csv, math

def csv_median(file_path, column_index = 0):
    """
    Args:
        file_path (str): The path to a file.
        column_index (Optional[int]): The index of a column in the file. Defaults to 0.

    Returns:
        float/long/int: The median value of the column processed in the file.

    Raises:
        Exception: If error occurs while processing a line in the file.

    Examples:
        >>> print(csv_median('/home/username/filename.ext', column_index = 0))
        >>> print(csv_median('./filename.ext', column_index = 3))
        >>> print(csv_median('./filename.ext'))
    """
    assert type(column_index) == int 
    assert type(file_path) == str
  
    median = 0
    numbers_list = []
    with open(file_path, 'r') as file:
        data_lines = csv.reader(file)
        for line_num, line in enumerate(data_lines):
            try:
                value = int(line[column_index])
                numbers_list.append(value)
            except Exception:
                raise Exception("Error processing line " + str(line_num + 1))
    
    numbers_list.sort()
    numbers_list_length = len(numbers_list)

    if numbers_list_length % 2 == 0:
        midpoint = int(math.floor(numbers_list_length / 2) - 1)
        midpoint_pair = (midpoint, midpoint + 1)
        median = (numbers_list[midpoint_pair[0]] + numbers_list[midpoint_pair[1]]) / 2.0
    else:
        midpoint = int(math.floor(numbers_list_length / 2))
        median = numbers_list[midpoint]

    assert type(median) == float or type(median) == int or type(median) == long
    return median


if __name__ == '__main__':

    file_path = 'numbers.txt'
    median = csv_median(file_path)
    print(median)
