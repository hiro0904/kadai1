import streamlit as st
import numpy as np
import pandas as pd
from janome.tokenizer import Tokenizer
import collections

st.title("課題1 形態素解析 InputTextVer")
tokenizer = Tokenizer()
string = st.text_input(
    "形態素解析したい文章を入力してね", "Pythonは1991年にオランダ人のグイド・ヴァン・ロッサム氏によって開発されたプログラミング言語です。"
)
st.header("入力文")
st.subheader(string)
st.header("分かち書き")
# string 引数を形態素解析 t.で指定
surface_list = []
speech_list = []
divided_string = ""
times_list = []
read_list = []
for t in tokenizer.tokenize(string):
    # t.surfaceが分けられた文字、t.part_of_speechは品詞
    divided_string += t.surface + " | "
    surface_list.append(t.surface)
    # 文字のリストを作る
st.subheader(divided_string)
count = collections.Counter(surface_list)
surface_list = []
sorted_by_desc_list = count.most_common()
# 文字と頻度をくっつけた

for i in range(len(sorted_by_desc_list)):
    # print(sorted_by_desc_list[i][0])
    surface_list.append(sorted_by_desc_list[i][0])

    speech_list.append(
        tokenizer.tokenize(sorted_by_desc_list[i][0])
        .__next__()
        .part_of_speech.split(",")[0]
    )
    times_list.append(sorted_by_desc_list[i][1])
    read_list.append(tokenizer.tokenize(sorted_by_desc_list[i][0]).__next__().reading)

st.header("形態素解析:名詞")
df = pd.DataFrame(
    {"回数": times_list, "単語名": surface_list, "読み方": read_list, "品詞": speech_list}
)
# st.table(df)
st.table(df[df["品詞"] == "名詞"])

