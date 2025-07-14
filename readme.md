# Code Parser for LLM Responses

As part of Mercor projects, code reviewers receive a large body of text containing a conversation between a human and a LLM. The conversation contains code and updates throughout the whole conversation, which the reviewers must read to stay up-to-date on the latest version to then finally run.

This code parser will be used for inputting the entire text body, and outputting each stage in a digestible format.

## How to use

1. Import the `ConversationResponse` and `ResponseDisplayer` objects from package.
2. Open valid file, see `/examples` for an example LLM conversation.
3. Enter file as argument for `ConversationResponse`.
4. Enter conversation as argument for `ResponseDisplayer`.
5. Run `.display_conversation()` method to view conversation in digestible format.

## Example - example_conversation.py
```python

from LLM_code_parser import ConversationResponse, ResponseDisplayer

# - - - - - - - - - - - - - - - - - - -

test_file = "examples/LLM_response_conversation.txt"

# - - - - - - - - - - - - - - - - - - -

if __name__ == "__main__":
    f = open(test_file, "r", encoding="utf-8")

    conversation = ConversationResponse(f)
    display = ResponseDisplayer(conversation)
    display.display_conversation()

```