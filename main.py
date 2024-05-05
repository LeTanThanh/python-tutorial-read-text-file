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

  # Reading text methods

  """
  The file object provides you with three methods for reading text from a text file:

  - read(size): read some contents of a file base on the optional size and return the contents as a string.
  If you omit the size, the read() method reads from where it left off till the end of the file.
  If the end of a file has been reached, the read() method returns an empty string.

  - readline(): read a single line from a text file and return the line as a string.
  If the end of a file has been reached, the readline() returns an empty string.

  - readlines(): read all lines of the text file into a list of strings.
  This method is useful if you have a small file and you want to manipulate the whole text of that file.
  """

  # close() method

  """
  The file that you open will remain open until it close it using the close() method.

  It's important to close the file that is no longer in use for the following reasons:

  - First, when you open a file in your script, the file system usually locks it down so no other programs or scripts can use it until you close it.

  - Second, your file system has a limited number of file descriptors that you can create before it runs out them.
  Although this number might be high, it's possible to open a lot of files and deplete your system resources.

  - Third, leaving many files open may lead to race conditions which occur when multiple process attempt to modify one file at the same time and can cause all kinds of unpected behaviors.

  The following shows how to call the close() method to close the file:

  f.close()

  To close the file automatically without calling the close() method, you use the with statement like this:

  with open(path_to_file) as f:
    contents = f.readlines()

  In practice, you'll use the with statement to close the file automatically.
  """
