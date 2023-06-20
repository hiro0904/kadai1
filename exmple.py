import streamlit as st
import numpy as np
import pandas as pd
from janome.tokenizer import Tokenizer
import collections

st.title("課題1")


tokenizer = Tokenizer()

string = "Pythonは1991年にグイド・ヴァン・ロッサムにより開発されたプログラミング言語である。最初にリリースされたPythonの設計哲学は、ホワイトスペース(オフサイドルール)の顕著な使用によってコードの可読性を重視している。その言語構成とオブジェクト指向のアプローチは、プログラマが小規模なプロジェクトから大規模なプロジェクトまで、明確で論理的なコードを書くのを支援することを目的としている。"

st.write("DataFrame")

# string 引数を形態素解析 t.で指定
# 文字と頻度をくっつけた

"""
# 進捗
## こんなダサいコードはやめろ！
```
for i in range(len(sorted_by_desc_list)):
    print(
        "{}\t{} {}".format(
            sorted_by_desc_list[i][0],
            sorted_by_desc_list[i][1],
            tokenizer.tokenize(sorted_by_desc_list[i][0]).__next__().part_of_speech,
        )
    )
```
"""
