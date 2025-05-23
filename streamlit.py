# -*- coding: utf-8 -*-
"""Streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_v6bWcN8c0krUpKyl7T1ruiUWl0JPQmc
"""

!pip install streamlit

!pip install langchain-cli

import streamlit as st
import pandas as pd
from langchain.chains.llm import LLMChain
from langchain.chains.summarize import load_summarize_chain

if "query_history" not in st.session_state:
    st.session_state.query_history = []

query = st.text_input("Enter your query")

if st.button("Get News"):
    if query:
      summaries = load_summarize_chain(query)
      response =LLMChain.run({"query": query,"summaries": summaries})

      # Save Query & Response
      st.session_state.query_history.append({"Query": query, "Summary": response})

      st.subheader(" Summary:")
      st.write(response)

        # Download as CSV
      df = pd.DataFrame(st.session_state.query_history)
      csv = df.to_csv(index=False).encode("utf-8")

      st.download_button(" Download History", csv, "summary_history.csv", "text/csv")

