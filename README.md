# Stock Price Prediction Leveraging Reddit

This project investigates whether Reddit discussions can inform stock-price prediction, including whether an author’s historical prediction accuracy helps identify useful signals. The experiments compare financial and Reddit-derived features, trust filters, and sliding windows across several machine-learning models. The repository accompanies [Stock Price Prediction Leveraging Reddit: The Role of Trust Filter and Sliding Window](https://ieeexplore.ieee.org/document/9671412), published at IEEE Big Data 2021. It contains research notebooks, saved plots, and experiment results.

## Repository Guide

- [Webscrape_351.ipynb](Webscrape_351.ipynb): Reddit data collection using PRAW and Pushshift APIs in the original research workflow.
- [Preprocessing/](Preprocessing/): Submission and comment filtering, text cleaning, ticker extraction, financial data collection, sentiment scoring, and trustworthiness calculations.
- [Code/](Code/): Model experiments comparing financial and Reddit-derived features, trust filters, and different sliding windows.
- [Graphs/](Graphs/): Saved result visualizations and the R Markdown script used to generate comparison plots.
- [results.xlsx](results.xlsx): Experiment results workbook used by the graph-generation script.

## Experimental Approach

The experiments examine how the age of information and an author's historical prediction accuracy affect its usefulness for stock-price prediction. The model notebooks include random forests, LightGBM, neural networks, and LSTMs.

The saved plots compare selected experiments using mean absolute error (MAE) and root mean squared error (RMSE). See [Graphs/result_graphs.Rmd](Graphs/result_graphs.Rmd) for the plotting workflow and the [paper](https://ieeexplore.ieee.org/document/9671412) for the research context.

## Reproduction Requirements

The experiments are organized as notebooks. Reproduction currently requires the following preparation.

- Several model notebooks read intermediate data files, including `all_merged_sw.csv`, that are not included in the public repository.
- A dependency manifest and end-to-end setup guide are not included. Dependencies must be identified from the relevant notebooks and scripts before reproducing an experiment.
- Some notebooks contain Google Colab or local working-directory paths that need to be adapted to the chosen environment.
- The collection notebooks use historical API integrations. Confirm current access requirements and compatibility before attempting to collect new data.
- Saved notebook outputs, plots, and workbook results record the existing experiments. They do not establish that the notebooks run unchanged in a current environment.

## Publication and Authors

Dennis Huynh, Garrett Audet, Nikolay Alabi, and Yuan Tian. **Stock Price Prediction Leveraging Reddit: The Role of Trust Filter and Sliding Window.** IEEE International Conference on Big Data, 2021.

[Read the publication on IEEE Xplore](https://ieeexplore.ieee.org/document/9671412).
