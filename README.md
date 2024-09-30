# Fake News Detector

## Overview
This project is a machine learning-based fake news detector. It uses a combination of natural language processing (NLP) techniques and machine learning algorithms to classify news articles as real or fake.

## Features
- **Data Preprocessing**: Cleans and prepares the text data for analysis.
- **TF-IDF Vectorization**: Converts text data into numerical features using Term Frequency-Inverse Document Frequency (TF-IDF).
- **Model Training**: Uses the Passive Aggressive Classifier to train the model.
- **Evaluation**: Evaluates the model using accuracy score and confusion matrix.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/Ahmad8426/Fake-News-Detector.git
    cd Fake-News-Detector
    ```
2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Collect data by running the data collection script:
    ```sh
    python data_collection.py
    ```
2. Prepare your dataset and place it in the `data` directory.
3. Run the Jupyter Notebook:
    ```sh
    jupyter notebook Fake_news_2.ipynb
    ```
4. Follow the steps in the notebook to preprocess the data, train the model, and evaluate its performance.

## Dependencies
- numpy
- pandas
- scikit-learn
- jupyter
- requests
- beautifulsoup4

## Project Structure
- [`Fake_news_2.ipynb`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22vscode-notebook-cell%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FAHMAD%2FDownloads%2FFake_News_Detection_Machine_learning_project%2FFake_news_2.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22W0sZmlsZQ%3D%3D%22%7D%5D "c:\Users\AHMAD\Downloads\Fake_News_Detection_Machine_learning_project\Fake_news_2.ipynb"): Main Jupyter Notebook containing the code for data preprocessing, model training, and evaluation.
- `data/`: Directory to store the dataset.
- `requirements.txt`: List of dependencies required to run the project.

## License
This project is licensed under the MIT License.

## Acknowledgements
- [Scikit-learn](https://scikit-learn.org/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)

## Contact
For any questions or suggestions, please contact ahmy40404@gmail.com
