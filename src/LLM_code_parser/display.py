'''
Module for handling display of responses.

Created on 11-07-2025
@author: Harry New

'''
from .response import ConversationResponse, IndividualResponse
from termcolor import colored
import keyboard
import time
import os
import sys

# - - - - - - - - - - - - - - - - - - -

class ResponseDisplayer():
    def __init__(self, conversation_response: ConversationResponse):
        self.conversation: ConversationResponse = conversation_response

    
    def display_conversation(self):
        """
        Display entire conversation.
        """
        response_index = 0
        scroll_pos = 0
        terminal_offset = 5 # Size of options.
        code_height = os.get_terminal_size().lines - terminal_offset

        while True:
            # Display response.
            displayed_response = self.conversation.internal_responses[response_index]
            scroll_limit = len(displayed_response.buffer.getvalue().splitlines()) - code_height
            print("")
            self.display_response(displayed_response,scroll_pos,code_height,terminal_offset)
            selected = self.display_options(response_index, scroll_pos, scroll_limit)
            
            if selected == "left" and response_index > 0:
                time.sleep(0.2)
                response_index -= 1
                scroll_pos = 0
            elif selected == "right" and response_index < len(self.conversation.internal_responses) -1:
                time.sleep(0.2)
                response_index += 1
                scroll_pos = 0
            elif selected == "up":
                scroll_pos -= 1
            elif selected == "down":
                scroll_pos += 1
            else:
                break
    
    
    def display_response(self, response: IndividualResponse, scroll_pos: int, code_height: int, terminal_offset: int):
        """
        Displaying individual response.

        Args:
            response (IndividualResponse): Response to display.
            scroll_pos (int): Scroll position.
            code_height (int): Code height.
            terminal_offset (int): Offset to subtract from terminal height.
        """
        response.buffer.seek(0)
        lines = response.buffer.getvalue().splitlines()

        os.system('cls' if os.name == 'nt' else 'clear')

        visible_lines = lines[scroll_pos:scroll_pos + code_height]
        for line in visible_lines:
            print(colored(line,color=response.colour,attrs=response.display_attrs))


    def display_options(self, response_index: int, scroll_pos: int, scroll_limit: int):
        """
        Display options for navigating display.

        Args:
            response_index (int): Index of response in responses.
            scroll_pos (int): Current scroll position.
            scroll_limit (int): Scroll limit.
        """
        print(colored(f"\n=== Response {response_index+1}/{len(self.conversation.internal_responses)} ===",attrs=["bold"]))
        print(colored("[\u2190] Previous Response \t [\u2191] Move Up \t [Q] Quit",attrs=["bold"]))
        print(colored("[\u2192] Next Response \t [\u2193] Move Down",attrs=["bold"]))

        while True:
            if keyboard.is_pressed("left"):
                return "left"
            elif keyboard.is_pressed("right"):
                return "right"
            elif keyboard.is_pressed("q"):
                return "q"
            elif keyboard.is_pressed("up") and scroll_pos > 0:
                return "up"
            elif keyboard.is_pressed("down") and scroll_pos < scroll_limit:
                return "down"