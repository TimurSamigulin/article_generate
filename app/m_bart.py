from transformers import MBartTokenizer, MBartForConditionalGeneration

class MBart:
    model_name = "IlyaGusev/mbart_ru_sum_gazeta"
    tokenizer = MBartTokenizer.from_pretrained(model_name)
    model = MBartForConditionalGeneration.from_pretrained(model_name)


def mbart(article_text: str):
    input_ids = MBart.tokenizer(
        [article_text],
        max_length=600,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )["input_ids"]

    output_ids = MBart.model.generate(       
        input_ids=input_ids,
        num_beams=5,
        length_penalty=1.0,
        max_length=30,
        min_length=5,
        no_repeat_ngram_size=0,
        early_stopping=True
    )[0]
    
    summary = MBart.tokenizer.decode(output_ids, skip_special_tokens=True)
    
    return summary