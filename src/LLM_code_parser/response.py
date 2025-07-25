'''
Module for defining Response classes.

Created on 11-07-2025
@author: Harry New

'''
from io import StringIO
from termcolor import colored
import os

# - - - - - - - - - - - - - - - - - - -

class Response():
    def __init__(self):
        self.type: str = "text"
        self.user: str = None
        self.buffer: StringIO = None
        self.internal_responses: list = []
        self.colour: str = None
        self.display_attrs: list[str] = []

# - - - - - - - - - - - - - - - - - - -

class ConversationResponse(Response):
    def __init__(self, buffer):
        super().__init__()
        self.buffer = buffer
        self.internal_responses = self.split_individual_responses()

    
    def split_individual_responses(self) -> list["IndividualResponse"]:
        """
        Split buffer into individual responses.

        Returns:
            list[IndividualResponse]: List of individual responses.
        """
        keywords = {
            "human":"Human:",
            "assistant":"Assistant:",
            "last":"Last Human Response",
            "response_a":"Model Response A",
            "response_b":"Model Response B"
        }
        response = StringIO()
        user = "human"
        responses = []
        
        # Filter responses.
        for line in self.buffer:
            for keyword in keywords.values():
                if keyword in line:
                    # Add response to responses.
                    response.seek(0)
                    responses.append(IndividualResponse(response,user))
                    # Determining user of next response.
                    user = next((k for k, v in keywords.items() if v == keyword), None)
                    # Create new StringIO.
                    response = StringIO()
            response.write(line)
        responses.append(IndividualResponse(response,user))
        return responses

# - - - - - - - - - - - - - - - - - - -

class IndividualResponse(Response):
    def __init__(self, buffer, user):
        super().__init__()
        self.user = user
        self.buffer = buffer
        self.colour = self.set_colour()


    def set_colour(self) -> str:
        """
        Set colour of response.

        Returns:
            str: Colour string.
        """
        if self.user == "human" or self.user == "last":
            return "blue"
        else:
            return "yellow"      

# - - - - - - - - - - - - - - - - - - -

if __name__ == "__main__":
    f = open("output/test.txt", "r", encoding="utf-8")

    conversation = ConversationResponse(f)
    conversation.display_internal()
