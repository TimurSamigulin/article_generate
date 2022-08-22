from app.m_bart import mbart


def get_title(text: str) -> str:
    """Get article text from text

    Args:
        text (str): _description_

    Returns:
        str: _description_
    """   

    summary = mbart(text)

    return summary.split('.')[0]
