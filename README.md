# Indian Military News Analysis: A ML Experiment

This repository contains code and resources for a machine learning experiment focused on Indian defense news articles from the website IDRW.org. The goal of this project is to perform exploratory data analysis, preprocess the text data, extract features, train machine learning models, and interpret the results to gain insights into the trends and topics covered in the articles.

The main Jupyter Notebook file, `Mil_Def.ipynb`, contains the core code for the project. The notebook is used to perform data analysis, visualization, and modeling.

The `Data Scraping` directory includes scripts for scraping and cleaning article data from the website. The script `better_article_scraping.py` improves the efficiency of article scraping, while `cleaning_article_data.py` provides data cleaning functionality. Additionally, `title_scraping.py` focuses on scraping article titles.

The resulting cleaned data is saved in `cleaned.csv`, and the data without article text is stored in `idrw_webdata.csv`.

## Files

The following files are included in this repository:

- `.ipynb_checkpoints`: Checkpoint folder for Jupyter Notebook.
- `Mil_Def-checkpoint.ipynb`: Jupyter Notebook checkpoint.
- `Data Scraping`: Directory containing data scraping scripts.
  - `better_article_scraping.py`: Python script for improved article scraping.
  - `cleaning_article_data.py`: Python script for cleaning article data.
  - `title_scraping.py`: Python script for scraping article titles.
- `Mil_Def.ipynb`: Main Jupyter Notebook file for the project.
- `cleaned.csv`: Cleaned data in CSV format.
- `idrw_webdata.csv`: Data without article text in CSV format.

## Methodology

The project follows the following steps:

1. **Exploratory Data Analysis (EDA):** Perform EDA on the dataset to gain insights and understand the distribution of the articles. This involves analyzing various aspects such as the frequency of articles over time, the most common keywords or topics, and any other patterns that might be relevant to the research question.

2. **Text Preprocessing:** Prepare the article text for modeling by performing text preprocessing techniques such as tokenization, lowercasing, removing stopwords, and stemming or lemmatization. These steps help improve the quality of the text data and make it suitable for further analysis.

3. **Feature Extraction:** Use techniques like TF-IDF (Term Frequency-Inverse Document Frequency) and word embeddings (Word2Ve) to convert the text into numerical features that can be used for machine learning. TF-IDF assigns weights to words based on their frequency, while word embeddings represent words in a continuous vector space capturing semantic relationships.

4. **Model Training:** Select a suitable machine learning algorithm based on the specific objectives. Since the goal is to identify trends and topics, topic modeling techniques like Latent Dirichlet Allocation (LDA) and Non-negative Matrix Factorization (NMF) can be considered. These methods help discover latent topics within the articles or group similar articles together.

5. **Interpretation of Results:** Analyze the outputs of the trained model and extract meaningful insights from the discovered trends or clusters. This involves identifying the most prevalent topics, tracking their frequency over time, or finding relationships between different topics.

6. **Visualization and Reporting:** Creating visualizations such as bar plots, line charts, or word clouds to present the findings. Libraries like Matplotlib, Seaborn, or Plotly are used for generating informative and visually appealing plots.

## Usage

To use the code in this repository, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have the necessary dependencies installed (if any).
3. Run the desired scripts or open the Jupyter Notebook file (`Mil_Def.ipynb`) to explore the project.
4. Refer to this README file and comments within the notebooks for further guidance.

## Contributing

Contributions to this repo are welcome. If you find any issues or want to propose improvements, please create a new issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
