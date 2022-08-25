import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer


class ModelT5:
    model_name = "cointegrated/rut5-base-absum"
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    tokenizer = T5Tokenizer.from_pretrained(model_name)


def summarize(
    text, n_words=None, compression=None,
    max_length=50, num_beams=3, do_sample=False, repetition_penalty=10.0,
    **kwargs
):
    """
    Create title for text

    The following parameters are mutually exclusive:
    - n_words (int) is an approximate number of words to generate.
    - compression (float) is an approximate length ratio of summary and original text.
    """

    ModelT5.model.cuda()
    ModelT5.model.eval()
    if n_words:
        text = '[{}] '.format(n_words) + text
    elif compression:
        text = '[{0:.1g}] '.format(compression) + text
    x = ModelT5.tokenizer(text, return_tensors='pt',
                          padding=True).to(ModelT5.model.device)
    with torch.inference_mode():
        out = ModelT5.model.generate(
            **x,
            max_length=max_length, num_beams=num_beams,
            do_sample=do_sample, repetition_penalty=repetition_penalty,
            **kwargs
        )
    return ModelT5.tokenizer.decode(out[0], skip_special_tokens=True)
