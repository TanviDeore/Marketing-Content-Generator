# Product Marketing Content Generator

## Overview

The Product Marketing Content Generator is a powerful web application built with Streamlit and Ollama that helps marketing professionals quickly create compelling product descriptions and engaging ad copy. By simply providing key details about a product, users can generate high-quality marketing content tailored to their target audience and desired tone.

This tool streamlines the content creation process, ensuring consistency, persuasiveness, and adherence to specific marketing goals, leveraging the power of local large language models (LLMs) via Ollama.

## Features

* **Product Description Generation:** Creates detailed and persuasive product descriptions based on product name, category, features, benefits, target audience, and desired tone.
* **Ad Copy Generation:** Generates 3 distinct, catchy headlines and a concise body text for advertisements, adhering to the specified tone and target audience.
* **Ollama Integration:** Utilizes the `gemma` model for text generation, allowing for local, privacy-focused LLM inference.
* **Streamlit User Interface:** Provides an intuitive and easy-to-use web interface for inputting product details and viewing generated content.
* **Progress Indicators:** Includes a progress bar and status messages to enhance the user experience during content generation.
* **Input Validation:** Ensures all required product details are provided before attempting content generation.

## Technologies Used

* **Python:** The core programming language.
* **Streamlit:** For building the interactive web application.
* **Ollama:** For running large language models locally and performing text generation.
* **`pyngrok`:** Used when running the application on platforms like Google Colab to expose the local Streamlit server to a public URL.

## Setup and Installation

This application requires Python and relies on Ollama for its language model capabilities. It can be run locally or within a cloud environment like Google Colab.

### Prerequisites

* Python 3.8+
* `ollama` installed and running on your system (or within your Colab environment).
* The `gemma` model (or your preferred compatible LLM) pulled in Ollama.

### Step-by-Step Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/TanviDeore/Marketing-Content-Generator.git
    cd marketing-content-generator 
    ```
    If you're just using the provided Python file, save the code as `app.py` (or any `.py` file name you prefer).


2.  **Install Python Dependencies:**
    ```bash
    pip install streamlit ollama pyngrok
    ```

3.  **Install and Run Ollama:**
    * **Download Ollama:** Visit [ollama.com/download](https://ollama.com/download) and follow the instructions for your operating system.
    * **Start Ollama Server:** Ensure the Ollama server is running in the background.
        * **macOS/Windows:** The Ollama application typically starts automatically and runs in the background/system tray.
        * **Linux/CLI:** Run `ollama serve` in your terminal. You might want to use `nohup ollama serve &` to run it in the background.
    * **Pull the `gemma` Model:**
        ```bash
        ollama pull gemma
        ```
        (If you intend to use a different model, pull that one instead and update `model='gemma'` in `app.py` accordingly).

## Usage

### Running Locally

1.  Ensure you have followed all "Setup and Installation" steps.
2.  Open your terminal, navigate to the directory containing your `app.py` file.
3.  Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```
4.  Your default web browser will open to `http://localhost:8501` (or a similar port), displaying the application.

### Running on Google Colab

To run this application on Google Colab, you need to use `pyngrok` to create a public tunnel to your Streamlit app running within the Colab environment.

1.  **Open a New Google Colab Notebook.**
2.  **Set GPU Runtime:** Go to `Runtime > Change runtime type` and select `GPU` as the hardware accelerator.
3.  **Run the following cells sequentially:**

    **Cell 1: Install Dependencies**
    ```python
    !pip install streamlit pyngrok ollama
    ```

    **Cell 2: Authenticate ngrok**
    ```python
    from pyngrok import ngrok

    # Get your ngrok authtoken from [https://dashboard.ngrok.com/get-started/your-authtoken](https://dashboard.ngrok.com/get-started/your-authtoken)
    ngrok.set_auth_token("YOUR_NGROK_AUTH_TOKEN")
    ```
    * **Important:** Replace `"YOUR_NGROK_AUTH_TOKEN"` with your actual token obtained from the ngrok dashboard.

    **Cell 3: Create the Streamlit App File (`app.py`)**
    ```python
    %%writefile app.py

    #copy paste app.py contents here
    ```

    **Cell 4: Start Ollama Server and Pull Model**
    ```python
    # Install Ollama (if not already installed in previous Colab session)
    !curl -fsSL https://ollama.com/install.sh | sh

    # Start Ollama server in the background
    !nohup ollama serve > ollama.log 2>&1 &
    import time
    time.sleep(10) 

    # Pull the gemma model (required by the app)
    !ollama pull gemma
    print("gemma model pulled!")
    ```
    * **Important:** This cell ensures Ollama is running and the `gemma` model is available. Without it, your Streamlit app will fail to connect.

    **Cell 5: Run Streamlit and Create ngrok Tunnel**
    ```python
    # Start Streamlit in the background
    !nohup streamlit run app.py &

    # Give Streamlit a moment to start up
    import time
    time.sleep(5)

    # Create a public URL for your Streamlit app
    public_url = ngrok.connect(addr="8501", proto="http")
    print(f"Your Streamlit app is live at: {public_url}")
    ```
4.  **Access the App:** After running all cells, click the `public_url` printed in the output of Cell 5. This will open your Streamlit app in a new tab.

5.  Example
   
![example-1](https://github.com/user-attachments/assets/4fe187e2-b277-4203-ab30-96b6c1c09a63)
![image](https://github.com/user-attachments/assets/ab0bbcad-db80-461f-a0fc-a2d45647486a)
![image](https://github.com/user-attachments/assets/173b154b-0590-4304-962c-87870f5e20fa)


