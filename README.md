# Модуль для генерации новостных заголовков

Функция для генерации заголовка <b>get_title</b> в файле <b>main.py</b>

        def get_title(text: str) -> str:
        '''
        Get article text from text
        Args:
            text (str): article text
        Returns:
            str: title
        '''

Для генерации заголовка используется модель [MBart](https://huggingface.co/IlyaGusev/mbart_ru_sum_gazeta)

При первом запуске может долго загружать веса модели. Можно загрузить веса заранее и в <b>app/m_bart.py</b> заменить <i>model_name</i> на путь до директории с моделью