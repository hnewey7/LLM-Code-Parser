'''
Script for displaying example conversation.

Created on 11-07-2025
@author: Harry New

'''

from LLM_code_parser import ConversationResponse, ResponseDisplayer

# - - - - - - - - - - - - - - - - - - -

if __name__ == "__main__":
    f = open("output/test.txt", "r", encoding="utf-8")

    conversation = ConversationResponse(f)
    display = ResponseDisplayer(conversation)
    display.display_conversation()