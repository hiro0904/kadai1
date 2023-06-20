import streamlit as st
import numpy as np
import pandas as pd
from janome.tokenizer import Tokenizer
import collections

st.title("課題1 形態素解析")
st.header("ここに入力してね")
tokenizer = Tokenizer()
string = "Pythonは1991年にグイド・ヴァン・ロッサムにより開発されたプログラミング言語である。最初にリリースされたPythonの設計哲学は、ホワイトスペース(オフサイドルール)の顕著な使用によってコードの可読性を重視している。その言語構成とオブジェクト指向のアプローチは、プログラマが小規模なプロジェクトから大規模なプロジェクトまで、明確で論理的なコードを書くのを支援することを目的としている。"
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

