import pandas as pd
import plotly.express as px
import requests

import streamlit as st


class Model:
    header = "Random numbers served from an API"
    description = """
    These numbers are all fed to you by an external API. The API is built with FastAPI.
    """
    slider_caption = "Select number of random points"

    def __init__(self):
        self.min = 1
        self.max = 100
        self.step = 1

    def chart(self, nums):
        return px.scatter(
            pd.DataFrame(
                requests.get(f"http://fastapi:5000/random?n={nums}").json()
            ),
            x="x",
            y="y",
        )


def view(model):
    st.header(model.header)

    st.write(model.description)

    nums = st.slider(
        label=model.slider_caption,
        min_value=model.min,
        max_value=model.max,
        value=model.min,
        step=model.step,
    )

    st.plotly_chart(model.chart(nums), use_container_width=True)


m = Model()
view(m)
