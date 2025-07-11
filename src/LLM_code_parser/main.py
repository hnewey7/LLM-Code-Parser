'''
Module for handling main functions of package.

Created on 11-07-2025
@author: Harry New

'''
from typing import TextIO
from io import StringIO
import shutil

# - - - - - - - - - - - - - - - - - - -
# MODIFYING FILE.

def remove_extra_lines(file: TextIO) -> StringIO:
    """
    Removing extra lines from file.

    Args:
        file (TextIO): Original file.

    Returns:
        TextIO: New file.
    """
    output = StringIO()
    for i, line in enumerate(file):
        if i % 2 == 0:
            output.write(line)
    output.seek(0)
    return output

# - - - - - - - - - - - - - - - - - - -

if __name__ == "__main__":
    # Open file.
    f = open("examples/ticket.txt", "r", encoding="utf-8")
    
    # Remove extra lines.
    new_file = remove_extra_lines(f)

    with open("output/test.txt","w", encoding="utf-8") as fd:
        new_file.seek(0)
        shutil.copyfileobj(new_file, fd)