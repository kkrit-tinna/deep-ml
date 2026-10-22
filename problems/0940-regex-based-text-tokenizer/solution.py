import re

def tokenize_text(text: str) -> list:
    """
    Split raw text into tokens using regex-based splitting on whitespace
    and punctuation. Returns a list of non-empty stripped tokens.
    """
    tokens = re.split(r'(--|[,.:;?_!"()\']|\s)', text)
    # -- Matches a double dash exactly (first thing to try)
    # | "OR": try the option on the left, then the next one
    # [,.:;?_!"()\'] potential delimiter
    # \'  escapes the single quote so it doesn't end the Python string
    # \s Matches any one whitespace character: space, tab or newline

    res = []
    for token in tokens:
        token = token.strip()
        if token:
            res.append(token)

    return res