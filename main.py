from app.T5_summary import summarize


def get_title(text: str) -> str:
    """Get article text from text

    Args:
        text (str): _description_

    Returns:
        str: _description_
    """

    summary = summarize(text)

    return summary
