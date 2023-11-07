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

# ランダムな表データ作成（ダミー）
data = np.random.rand(50,2)

# データフレーム作成
df = pd.DataFrame(data, columns=["サンプル1","サンプル2"])
df2 = get_data()

# ==================================================================================
# アプリ画面デザイン
# ==================================================================================

# H1見出し
st.markdown("# グラフアプリ")

# H3見出し
st.markdown("### 表データst")

# 表データをアプリ上に表示
st.dataframe(df2)