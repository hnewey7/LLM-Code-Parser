'''
Script for displaying example conversation.

Created on 11-07-2025
@author: Harry New

'''

from LLM_code_parser import ConversationResponse, ResponseDisplayer

# - - - - - - - - - - - - - - - - - - -

test_file = "examples/LLM_response_conversation.txt"

# - - - - - - - - - - - - - - - - - - -

if __name__ == "__main__":
    f = open(test_file, "r", encoding="utf-8")

    conversation = ConversationResponse(f)
    display = ResponseDisplayer(conversation)
    display.display_conversation()