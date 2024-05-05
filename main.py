if __name__ == "__main__":
  # Steps for reading a text file in Python

  """
  To read a text file in Python, you follow these steps:

  - First, open a text file for reading by using the open() function.

  - Second, read text from the text file using the read(), readline() or readlines() method of the file object.

  - Third, close the file using the file close() method.
  """

  # open() function

  """
  The open() function has many parameters but you'll be focusing on the first two:

  open(path_to_file, mode)

  The path_to_file parameter specifies the path to the text file.

  If the program and file are in the same folder, you need to specify only the filename of the file.
  Otherwise, you need to include the path to the file as well as the filename.

  To specify the path to the file, you use the forward-slash ('/') even if you're working on Windows.

  For example, if the file readme.txt is stored in the sample folder as the program, you need to specify the path to the file as C:/sample/readme.txt.

  The mode is an optional parameter.
  It's a string that specifies the mode in which you want to open the file.
  The following table shows available modes for opening a text file:

  - r: Open for text file for reading text
  - w: Open a text file for writing text
  - a: Open a text file for appending text

  For example, to open a file whose name is the-zen-of-python.txt stored in the same folder as the program, you use the following code:

  f = open("the-zen-of-python.txt", "r")

  The open() function returns a file object which you will use to read text from a text file.
  """
