import pandas as pd
import plotly.express as px
import streamlit as st
from numpy.random import random


class Model:
    def __init__(self):
        self.min = 1
        self.max = 10
        self.step = 1

    def chart(self, nums):
        return px.scatter(
            pd.DataFrame({"x": random(nums), "y": random(nums)}), x="x", y="y"
        )

    header = "Random numbers served from an API"
    description = """
    These numbers are all fed to you by an external API. The API is built with FastAPI.
    """
    sliderCaption = "Select number of random points"


def view(model):
    # Header
    st.header(model.header)

    st.write(model.description)

    nums = st.slider(
        model.sliderCaption,
        model.min,
        model.max,
        model.min,
        model.step,
    )

    st.plotly_chart(model.chart(nums), use_container_width=True)


m = Model()
view(m)
