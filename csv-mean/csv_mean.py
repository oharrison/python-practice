import csv

def csv_mean(file_path, column_index = 0):
    """
    Args:
        file_path (str): The path to a file.
        column_index (Optional[int]): The index of a column in the file. Defaults to 0.

    Returns:
        float: The mean of the column processed in the file.

    Raises:
        IndexError: If column_index is greater than or equal to the length of a line.
        Exception: If error occurs while processing a line in the file.

    Examples:
        >>> print(csv_mean('/home/username/filename.ext', column_index = 0))
        >>> print(csv_mean('./filename.ext', column_index = 3))
        >>> print(csv_mean('./filename.ext'))
    """
    assert type(column_index) == int 
    assert type(file_path) == str
  
    mean = 0
    numbers_list = []
    with open(file_path, 'r') as file:
        data_lines = csv.reader(file)
        
        for line_num, line in enumerate(data_lines):

            line_length = len(line)
            current_line = line_num + 1
            
            try:
                if column_index >= line_length:
                    raise IndexError("column_index out of range for line %d" % current_line)

                value = float(line[column_index])
                numbers_list.append(value)
            except Exception:
                raise Exception("Error processing line %d" % current_line)
    
    numbers_list_length = len(numbers_list)
    mean = float(sum(numbers_list) / numbers_list_length) 
     
    assert type(mean) == float
    return mean


if __name__ == '__main__':

    file_path = 'numbers.txt'
    mean = csv_mean(file_path)
    print(mean)
