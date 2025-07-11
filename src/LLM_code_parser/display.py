'''
Module for handling display of responses.

Created on 11-07-2025
@author: Harry New

'''
from .response import ConversationResponse
from termcolor import colored
import keyboard
import time
import os

# - - - - - - - - - - - - - - - - - - -

class ResponseDisplayer():
    def __init__(self, conversation_response: ConversationResponse):
        self.conversation: ConversationResponse = conversation_response

    
    def display_conversation(self):
        """
        Display entire conversation.
        """
        response_index = 0

        while True:
            # Add small wait.
            time.sleep(0.2)

            # Display response.
            displayed_response = self.conversation.internal_responses[response_index]
            print("")
            displayed_response.display()
            selected = self.display_options(response_index)
            
            if selected == "up" and response_index > 0:
                response_index -= 1
            elif selected == "down" and response_index < len(self.conversation.internal_responses) -1:
                response_index += 1
            else:
                break
            

    def display_options(self, response_index: int):
        """
        Display options for navigating display.
        """
        print(colored(f"=== Response {response_index+1}/{len(self.conversation.internal_responses)} ===",attrs=["bold"]))
        print(colored("[\u2191] Previous Response",attrs=["bold"]))
        print(colored("[\u2193] Next Response",attrs=["bold"]))
        print(colored("[Q] Quit",attrs=["bold"]))

        while True:
            if keyboard.is_pressed("up"):
                return "up"
            elif keyboard.is_pressed("down"):
                return "down"
            elif keyboard.is_pressed("q"):
                return "q"