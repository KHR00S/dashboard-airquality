# Data Analysis Project: Air Pollution Analysis in Wanshouxigong

**Project Owner:**
- **Name:** Fakhrus Syakir
- **Email:** fakhroosyakir@gmail.com

## Business Questions

1. How has air pollution trended in Wanshouxigong over the last 5 years?
2. What is the correlation between air pollution and other variables?
3. What is the correlation between temperature and dew point (DEWP) in Wanshouxigong?
4. Have there been instances when PM2.5 and PM10 levels became hazardous in Wanshouxigong?

## Repository Structure

- **Notebooks:**
  - **Data_Collection_and_Wrangling.ipynb:** Contains code for importing data, assessing and cleaning it.
  - **Exploratory_Data_Analysis.ipynb:** Focuses on exploring the data, creating visualizations, and answering business questions.
  
- **Dashboard:**
  - **dashboard.py:** Python script for the dashboard application that visualizes the analyzed data.

- **Data:**
  - **all_data.csv:** Cleaned and processed dataset used for analysis.

- **README.md:**
  - Detailed documentation of the project, explaining the purpose, data analysis steps, and findings.

## Tools and Libraries

- Python
- Jupyter Notebooks
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Geopandas

## How to Use

1. Clone the repository to your local machine.
2. Open and run the Jupyter Notebooks in the `kualitas udara gong.ipynb` to understand the data analysis process.
3. Execute the `dashboard.py` script in the `Dashboard` folder to launch the dashboard application.
4. Explore the visualizations and findings in the dashboard.

## Dashboard Application

The `dashboard.py` script in the `Dashboard` folder contains the application to interactively explore the analyzed data. Run the script and navigate to the provided URL to access the dashboard.

## Setup environment
```
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit
```

## Run steamlit app
```
streamlit run dashboard.py
```


or you can open this link: https://khroos.streamlit.app

Feel free to reach out if you have any questions or suggestions!

---

*Note: Update the repository structure and instructions based on your actual project content and requirements.*
