import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(20, 3), # standard normal
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)