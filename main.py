from pyarabic.araby import tokenize, is_arabicrange, strip_tashkeel
import pyarabic.araby as araby
import csv
import re


def clean_non_arabic_words(text):
    new = tokenize(text, conditions=is_arabicrange, morphs=strip_tashkeel)
    return new


def clean_arabic(text):
    after_filter = araby.strip_diacritics(text)
    return after_filter


def remove_emojis(data):
    emoji = re.compile("["
                      u"\U0001F600-\U0001F64F"  # emoticons
                      u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                      u"\U0001F680-\U0001F6FF"  # transport & map symbols
                      u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                      u"\U00002500-\U00002BEF"  # chinese char
                      u"\U00002702-\U000027B0"
                      u"\U00002702-\U000027B0"
                      u"\U000024C2-\U0001F251"
                      u"\U0001f926-\U0001f937"
                      u"\U00010000-\U0010ffff"
                      u"\u2640-\u2642"
                      u"\u2600-\u2B55"
                      u"\u200d"
                      u"\u23cf"
                      u"\u23e9"
                      u"\u231a"
                      u"\ufe0f"  # dingbats
                      u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoji, '', data)


def make_word(arr_word):
    words = ""
    count = 0
    if len(arr_word) == 0:
        return ""

    for word in arr_word:
        words += word + " "
        count += 1

    return words


def validate_corpus():
    corpus_arr = []
    count = 0
    with open('test.csv', "rb") as csvfile:
        reader = csv.reader(csvfile, encoding="utf-8")
        text_edit = ""
        for line in reader:
            text_edit = clean_non_arabic_words(line)
            print(text_edit)
            world_new = make_word(text_edit)
            text_edit = world_new.replace("أ", "ا")
            new_text = text_edit
            new_text = world_new.replace("ة", "ه")
            last_text = new_text
            last_text = clean_arabic(new_text)
            last_text = remove_emojis(last_text)
            print(last_text)
            corpus_arr.append(last_text)
            count += 1
    print(corpus_arr)


if __name__ == '_main__':
    validate_corpus()