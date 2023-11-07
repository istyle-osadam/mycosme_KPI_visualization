import streamlit as st
import pandas as pd
import numpy as np
import sys
from pathlib import Path
print(sys.path)
sys.path.append(str(Path(__file__).parent.parent))

from services.data_load import get_data

# ==================================================================================
# データ準備
# ==================================================================================

#表示するインデックスのリスト
df_index_by_checkbox = []
#表示する日付(カラム)
df_columns_in_date = []
df_columns_in_date.append("test")
df_columns_in_date.append("2月1日(水)")

# ==================================================================================
# アプリ画面デザイン
# ==================================================================================

# H1見出し
st.markdown("# ページ軸_全体_集計(経由購入)")

# H3見出し
checks = st.columns(4)
action_list = ["a","b","c","d"]
action_click_values = [action + "check" for action in action_list]
col4, col5, col6 = st.columns([3,2,1])
col6.write('アクション別')
for i in range(len(action_list)):
    action_click_values[i] = col6.checkbox(action_list[i])

for action_click_index in range(len(action_click_values)):
    if action_click_values[action_click_index]:
        #st.write(action_list[action_click_index])
        df_index_by_checkbox.append(action_list[action_click_index])
#option_1 = st.checkbox("(すべて)")
#option_2 = st.checkbox('final velocity (v)')
#option_3 = st.checkbox('acceleration (a)')
#option_4 = st.checkbox('ti˙

# 表データをアプリ上に表示
data = np.random.rand(len(df_index_by_checkbox),len(df_columns_in_date))
df = pd.DataFrame(data, index =df_index_by_checkbox,columns=df_columns_in_date)
col4.dataframe(df)
#col4.dataframe(df.groupby("test"))