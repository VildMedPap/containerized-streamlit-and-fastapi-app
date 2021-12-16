"""Endpoints for the model."""

from numpy.random import random

from fastapi import FastAPI

app = FastAPI(
    title="Random numbers",
    description="The only purpose of this API is to provide an endpoint which deliver random numbers given request parameter from the user",
)


@app.get("/random")
async def random_numbers(n: int = 1) -> str:
    """Generate random numbers for a scatter plot."""
    return {"x": random(n).tolist(), "y": random(n).tolist()}
