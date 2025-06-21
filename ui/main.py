import streamlit as st
import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.perceptron import Perceptron

st.title("🧠 Perceptron AND Gate UI")

# AND gate training data
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([0, 0, 0, 1])

# Train perceptron
p = Perceptron(input_size=2)
p.train(X, y)

# User Inputs
a = st.selectbox("Input A", [0, 1])
b = st.selectbox("Input B", [0, 1])

# Prediction
input_data = np.array([a, b])
pred = p.predict(input_data)

# Output
st.markdown(f"### ✅ Output: {pred}")
st.markdown(f"**Weights:** {p.weights}")
