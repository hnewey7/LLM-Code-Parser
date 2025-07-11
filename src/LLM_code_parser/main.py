'''
Module for handling main functions of package.

Created on 11-07-2025
@author: Harry New

'''
from typing import TextIO
from io import StringIO
import string
from termcolor import colored

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
# GET CODE BLOCKS.

def split_human_LLM_response(file: StringIO) -> list[StringIO]:
    """
    Splitting file into human and LLM responses.

    Args:
        file (StringIO): Original file.

    Returns:
        list[StringIO]: List of responses.
    """
    keywords = ["Human:","Assistant:"]
    response = StringIO()
    response_type = keywords[0]
    responses = []
    
    # Filter responses.
    for line in file:
        for keyword in keywords:
            if keyword in line:
                response_type = keyword
                # Add response to responses.
                response.seek(0)
                responses.append(response)
                # Create new StringIO.
                response = StringIO()

        # Colouring response.
        colour = "yellow" if response_type == keywords[1] else "blue"
        colour_line = colored(line,colour)
        response.write(colour_line)

    responses.append(response)
    return responses
    

def get_whitespace_per_line(file: StringIO):
    for line in file:
        whitespace = [i for i in line if i in string.whitespace]
        print(whitespace.count(" "))

# - - - - - - - - - - - - - - - - - - -
# DISPLAY

def display_response(buffer: StringIO):
    """
    Displaying response.

    Args:
        buffer (StringIO): Buffer containing response.
    """
    for line in buffer:
        print(line,end="")


def display_conversation(responses: list[StringIO]):
    """
    Displaying full conversation.

    Args:
        responses (list[StringIO]): List of responses.
    """
    for response in responses:
        display_response(response)
        input(colored("Press any key to continue to next response...",attrs=["bold","blink"]))


# - - - - - - - - - - - - - - - - - - -

if __name__ == "__main__":
    # Open file.
    f = open("examples/ticket.txt", "r", encoding="utf-8")
    
    # Remove extra lines.
    new_file = remove_extra_lines(f)

    # Get whitespace.
    responses = split_human_LLM_response(new_file)

    # Display conversation.
    display_conversation(responses)

    # with open("output/test.txt","w", encoding="utf-8") as fd:
    #     new_file.seek(0)
    #     shutil.copyfileobj(new_file, fd)