import asyncio
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
import string
import re
from pyrogram import Client

#Надо получить от телеги
api_id =
api_hash = ""

app = Client("my_account", api_id=api_id, api_hash=api_hash)

#Выводит список диалогов с название и id
# async def main():
#     async with app:
#         async for dialog in app.get_dialogs(limit=21):
#             print(dialog.chat.title or dialog.chat.first_name)
#             print(dialog.chat.id)
#             print("\n")
#
# app.run(main())



#Берем последние 3к сообщений из диалога
messages_text = []

async def main():
    async with app:
        async for message in app.get_chat_history(X, limit=3000):
            if message.text is not None:
                messages_text.append(message.text)

app.run(main())

#Убираем спец символы и цифры
big_str = " ".join(messages_text).lower()
spec_chars = string.punctuation + '«»\t—…’'
big_str = "".join([ch for ch in big_str if ch not in spec_chars and ch not in string.digits])
big_str = re.sub('\n', ' ', big_str)

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('corpus')
#Считаем частотность слов
text_tokens = word_tokenize(big_str)
russian_stopwords = stopwords.words("russian")
russian_stopwords.extend(['это', 'чтò','всё','сказал', 'сказала','говорил','говорила'])
text_tokens = [token.strip() for token in text_tokens if token not in russian_stopwords]
text = nltk.Text(text_tokens)
fdist_sw = FreqDist(text)
most_common_words = [most_common_pairs[0] for most_common_pairs in fdist_sw.most_common(100)]

#Рисуем
text_raw = " ".join(most_common_words)
wordcloud = WordCloud(width=800, height=400).generate(text_raw)
plt.figure(figsize=(10, 5), facecolor='k')
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
