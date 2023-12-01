# WhatsApp Chat Analyzer

Welcome to the WhatsApp Chat Analyzer repository! This project allows you to analyze your WhatsApp chat data using a Streamlit web application. The application provides insights into various aspects of your chat, making it an informative and fun tool.

## Installation

Before you can run the WhatsApp Chat Analyzer, you'll need to follow these installation steps:

1. Clone the repository to your local machine. Open your terminal and run:

    ```bash
    git clone https://github.com/Obsidianage/whatsappAnalyzer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd whatsappAnalyzer
    ```

3. Install the required dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Open main.py in PyCharm

To work on the project in PyCharm, open the `main.py` file in the PyCharm IDE.

### Running the Web Application

Before running the web application, ensure that Streamlit is installed. If not, install it using:

```bash
pip install streamlit
```

Now, run the web application using the following command:

```bash
streamlit run main.py
```

This will launch the application in your default web browser.

## Project Structure

The repository contains the following files:

- **.idea**: IDE configuration files.
- **Procfile**: Specifies the command that should be executed by the app on startup.
- **helper.py**: Contains helper functions for the main application.
- **hinglish.txt**: English + Hindi stop words file named 'hinglish.txt'.
- **main.py**: Main application file.
- **preprocessor.py**: The editing of data frame which contains the chat information.
- **requirements.txt**: Lists the Python dependencies and their versions.
- **setup.sh**: Shell script for setup. ( In case you are deploying it on web instead of runing it on local host)

Feel free to explore and contribute to the WhatsApp Chat Analyzer project! If you have any questions or issues, please open an [issue](https://github.com/Obsidianage/whatsappAnalyzer/issues). Happy analyzing!
