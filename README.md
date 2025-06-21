<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="font-family: Arial, sans-serif; padding: 20px; max-width: 900px; margin: auto; background-color: #f9f9f9; color: #333;">

  <h1>🧠 Perceptron AND Gate UI</h1>
  <p>This project demonstrates a simple Perceptron model trained to simulate the logical <strong>AND</strong> gate using a web-based user interface built with <code>Streamlit</code>.</p>

  <h2>📁 Folder Structure</h2>
  <pre><code>perceptron-final/
├── app/
│   └── perceptron.py       # Perceptron model logic
├── ui/
│   └── main.py             # Streamlit UI to interact with the model
├── environment.yml         # Conda environment file
└── README.html             # Project documentation in HTML
</code></pre>

  <h2>🧠 Perceptron Overview</h2>
  <p>The <code>Perceptron</code> is one of the earliest neural network models that performs binary classification using a linear decision boundary.</p>

  <h3>How it Works</h3>
  <ul>
    <li>Each input is multiplied by its corresponding weight</li>
    <li>A bias is added to the result</li>
    <li>The sum is passed through a step activation function</li>
  </ul>

  <h3>Mathematical Expression</h3>
  <pre><code>z = (w1 * x1) + (w2 * x2) + bias
output = activation(z)  # Step function: 1 if z >= 0 else 0
</code></pre>

  <h3>Weight Update Rule</h3>
  <p>During training, weights are updated using the following formula:</p>
  <pre><code>wi = wi + (lr * error * xi)
bias = bias + (lr * error)</code></pre>
  <p>This continues for a number of epochs or until convergence.</p>

  <h2>✅ AND Gate Truth Table</h2>
  <table border="1" cellpadding="8" cellspacing="0">
    <tr>
      <th>Input A</th>
      <th>Input B</th>
      <th>Output (A AND B)</th>
    </tr>
    <tr><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>0</td><td>1</td><td>0</td></tr>
    <tr><td>1</td><td>0</td><td>0</td></tr>
    <tr><td>1</td><td>1</td><td>1</td></tr>
  </table>

  <h2>📦 Setup Instructions</h2>
  <ol>
    <li><strong>Open CMD</strong> in your target folder:<br>
        File Explorer → Address bar → Type <code>cmd</code> → Press <strong>Enter</strong>
    </li>
    <li><strong>Create folders and files:</strong></li>
  </ol>

  <pre><code>
<b>Step 1:</b>
<b>D:\MachineLearning\projects> mkdir perceptron-final</b>

<b>Step 2:</b>
<b>D:\MachineLearning\projects> cd perceptron-final</b>

<b>Step 3:</b>
<b>D:\MachineLearning\projects\perceptron-final> mkdir app ui</b>

<b>Step 4:</b>
<b>D:\MachineLearning\projects\perceptron-final> cd app</b>

<b>Step 5:</b>
<b>D:\MachineLearning\projects\perceptron-final\app> type nul > perceptron.py</b>

<b>Step 6:</b>
<b>D:\MachineLearning\projects\perceptron-final\app> cd ../ui</b>

<b>Step 7:</b>
<b>D:\MachineLearning\projects\perceptron-final\ui> type nul > main.py</b>
</code></pre>

  <ol start="3">
    <li><strong>Create Conda Environment (recommended):</strong></li>
  </ol>

  <pre><code>
conda create --name perceptron-ui python=3.10 -y
conda activate perceptron-ui
conda install streamlit numpy
</code></pre>

  <ol start="4">
    <li><strong>Export environment for others</strong></li>
  </ol>

  <pre><code>conda env export --from-history > environment.yml</code></pre>

  <h2>🚀 How to Run the App</h2>
  <pre><code>cd ui
streamlit run main.py
</code></pre>
  <p>This will launch the app in your default web browser.</p>

  <h2>🎯 Features</h2>
  <ul>
    <li>Interactive Streamlit interface</li>
    <li>Binary inputs A and B as dropdowns</li>
    <li>Instant output prediction using trained perceptron</li>
    <li>Displays learned weights after training</li>
  </ul>

  <h2>📌 Example Use</h2>
  <ul>
    <li><code>Input A = 1</code></li>
    <li><code>Input B = 1</code></li>
    <li><strong>Output:</strong> ✅ 1</li>
    <li><strong>Learned Weights:</strong> shown below output</li>
  </ul>

  <h2>💡 Tips</h2>
  <ul>
    <li>Bias is the first weight stored at <code>self.weights[0]</code></li>
    <li>Weights are initialized to zero and updated during training</li>
    <li>Training is repeated over all samples for multiple epochs</li>
  </ul>

  <h2>👨‍💻 Author</h2>
  <p>Created by <strong>Sai Bhargav Ram Koduru</strong></p>

</body>
</html>
