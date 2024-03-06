# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import geopandas as gpd

# Set seaborn style
sns.set_style("whitegrid")

# Load data
all_df = pd.read_csv("all_data.csv")
all_df.sort_values(by="year", inplace=True)
all_df['year'] = pd.to_datetime(all_df['year'], format='%Y')

# Define air_polution_df function
def air_polution_df(df):
    air_polution_df = df.groupby(by=['year']).agg({
        "PM2.5": "mean",
        "PM10": "mean",
        "SO2": "mean",
        "NO2": "mean",
        "CO": "mean",
        "O3": "mean"
    }).sort_values(by=['year'], ascending=True)
    air_polution_df = air_polution_df.reset_index()
    air_polution_df['time'] = air_polution_df["year"].astype(str)
    return air_polution_df

# Define airpolution_display function
def airpolution_display(df):
    pm25 = round(df['PM2.5'].mean(), 1)
    pm10 = round(df['PM10'].mean(), 0)
    SO2 = round(df['SO2'].mean(), 2)
    NO2 = round(df['NO2'].mean(), 2)
    CO = round(df['CO'].mean(), 2)
    O3 = round(df['O3'].mean(), 2)

    with st.container():
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            if (pm25 <= 15.5):
                st.metric("PM25: " + str(pm25), value="BAIK")
            elif ((pm25 >= 15.6) & (pm25 <= 55.4)):
                st.metric("PM25: " + str(pm25), value="SEDANG")
            elif ((pm25 >= 55.5) & (pm25 <= 150.4)):
                st.metric("PM25: " + str(pm25), value="TIDAK SEHAT")
            elif ((pm25 >= 150.5) & (pm25 <= 250.4)):
                st.metric("PM25: " + str(pm25), value="SANGAT TIDAK SEHAT")
            else:
                st.metric("PM25: " + str(pm25), value="BERBAHAYA")
        with col2:
            st.metric("SO2:", value=SO2)
        with col3:
            st.metric("NO2:", value=NO2)

    with st.container():
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            if (pm10 <= 50):
                st.metric("PM10: " + str(pm10), value="BAIK")
            elif ((pm10 >= 51) & (pm10 <= 150)):
                st.metric("PM10: " + str(pm10), value="SEDANG")
            elif ((pm10 >= 151) & (pm10 <= 350)):
                st.metric("PM10: " + str(pm10), value="TIDAK SEHAT")
            elif ((pm10 >= 351) & (pm10 <= 420)):
                st.metric("PM10: " + str(pm10), value="SANGAT TIDAK SEHAT")
            else:
                st.metric("PM10: " + str(pm10), value="BERBAHAYA")
        with col2:
            st.metric("CO:", value=CO)
        with col3:
            st.metric("O3:", value=O3)

# Define air_polution_graph function
def air_polution_graph(df):
    df = df.sort_values(by='year')  # Ensure DataFrame is sorted by 'year'

    with st.expander("PM2.5"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['year'].to_numpy(), df['PM2.5'].to_numpy(), marker='o', linewidth=2, color="#39064B")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation=45)
        ax.set_ylabel("PM2.5", fontsize=25)
        ax.set_title("PM2.5", loc="center", fontsize=35)
        st.pyplot(fig)


    with st.expander("PM10"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['year'].to_numpy(), df['PM10'].to_numpy(), marker='o', linewidth=2, color="#39064B")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation=45)
        ax.set_ylabel("PM10", fontsize=25)
        ax.set_title("PM10", loc="center", fontsize=35)
        st.pyplot(fig)

    with st.expander("SO2"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['year'].to_numpy(), df['SO2'].to_numpy(), marker='o', linewidth=2, color="#39064B")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation=45)
        ax.set_ylabel("SO2", fontsize=25)
        ax.set_title("SO2", loc="center", fontsize=35)
        st.pyplot(fig)

    with st.expander("NO2"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['year'].to_numpy(), df['NO2'].to_numpy(), marker='o', linewidth=2, color="#39064B")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation=45)
        ax.set_ylabel("NO2", fontsize=25)
        ax.set_title("NO2", loc="center", fontsize=35)
        st.pyplot(fig)

    with st.expander("CO"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['year'].to_numpy(), df['CO'].to_numpy(), marker='o', linewidth=2, color="#39064B")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation=45)
        ax.set_ylabel("CO", fontsize=25)
        ax.set_title("CO", loc="center", fontsize=35)
        st.pyplot(fig)

    with st.expander("O3"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['year'].to_numpy(), df['O3'].to_numpy(), marker='o', linewidth=2, color="#39064B")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation=45)
        ax.set_ylabel("O3", fontsize=25)
        ax.set_title("O3", loc="center", fontsize=35)
        st.pyplot(fig)

# Sidebar with author information
st.sidebar.header("Author Information")
st.sidebar.text("Name: FAKHRUS SYAKIR")
st.sidebar.text("BANGKIT ID: M322D4KY1790")
st.sidebar.text("GitHub: KHR00S")

# Title and data display
st.title("Air Quality in Wanshouxigong")

#Display air pollution graphs
polusi_pertahun = air_polution_df(all_df)
with st.container():
        st.header("1. Bagaimana trend polusi udara di Wanshouxigong")
        air_polution_graph(polusi_pertahun)
st.write("Dari Trend Polusi selama 5 tahun terakhir dapat ditarik kesimpulan bahwa pada setiap indikator (PM2.5, PM10, SO2, NO2,dan Co) mengalami fluktuasi")

# Display correlation heatmap
st.header("2. Bagaimana korelasi polusi udara terhadap variabel lainnya")
numeric_columns = all_df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = all_df[numeric_columns].corr()

fig, ax = plt.subplots(figsize=(15, 10))
sns.heatmap(correlation_matrix, vmax=1, vmin=-1, center=0, cmap="plasma")
ax.tick_params(labelsize=10)
ax.set_title("Korelasi heatmap", loc="center", fontsize=35)
st.pyplot(fig)
st.write("Dari korelasi Heatmap didapatkan bahwa polusi udara berkorelasi rendah terhadap variabel lainnya(O3, TEMP, PRES, DEWP, RAIN,dan WSPM)")

# Regression plot between DEWP and TEMP
st.header("3. Bagaimana korelasi antara temperatur dan Dew Point (DEWP) di Wanshouxigong")
fig, ax = plt.subplots(figsize=(10, 6))
sns.regplot(x='DEWP', y='TEMP', data=all_df, scatter_kws={'s': 10}, line_kws={'color': 'red'})
plt.title('Regplot antara DEWP dan TEMP')
plt.xlabel('DEWP')
plt.ylabel('TEMP')
st.pyplot(fig)

st.write("Dari Regplot yang dihasilkan didapatkan korelasi antara suhu udara (temperature) dan titik embun (dew point) erat kaitannya, karena titik embun adalah suhu di mana udara menjadi jenuh dan uap air mulai mengembun menjadi tetesan air.")

# Bar plot for Air Pollution Level (PM2.5)
st.header("4. Apakah pernah terjadi keadaan berbahaya ketika PM2.5 menjadi berbahaya di Wanshouxigong")
pm25_counts = all_df['Air Pollution Level (PM2.5)'].value_counts()
fig, ax = plt.subplots()
ax.bar(pm25_counts.index, pm25_counts.values, color='skyblue')
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('Frequency')
ax.set_title('Proportion of Air Pollution Levels From PM2.5')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Bar plot for Air Pollution Level (PM10)
pm10_counts = all_df['Air Pollution Level (PM10)'].value_counts()
fig, ax = plt.subplots()
ax.bar(pm10_counts.index, pm10_counts.values, color='skyblue')
ax.set_xlabel('Air Pollution Level')
ax.set_ylabel('Frequency')
ax.set_title('Proportion of Air Pollution Levels From PM10')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

st.write("Dari proporsi polusi udara yang ditampilkan dapat disimpulkan bahwa di Wanshouxigong terdapat lebih dari 2000 kali keadaan polusi udara menjadi berbahaya, melebihi dari keadaan tidak berbahaya")

# Create a synthetic DataFrame with latitude and longitude columns
synthetic_data = {
    'time': ['2018', '2019', '2020'],
    'latitude': [30.0, 31.0, 32.0],
    'longitude': [120.0, 121.0, 122.0],
    'PM2.5': [25, 30, 20],
    'PM10': [40, 35, 45],
}

# Create a synthetic DataFrame with latitude and longitude columns
synthetic_data = {
    'time': ['2018', '2019', '2020'],
    'latitude': [30.0, 31.0, 32.0],
    'longitude': [120.0, 121.0, 122.0],
    'PM2.5': [25, 30, 20],
    'PM10': [40, 35, 45],
}

# Create a synthetic DataFrame with latitude and longitude columns
synthetic_data = {
    'time': ['2018', '2019', '2020'],
    'latitude': [30.0, 31.0, 32.0],
    'longitude': [120.0, 121.0, 122.0],
    'PM2.5': [25, 30, 20],
    'PM10': [40, 35, 45],
}

# Create a synthetic DataFrame with latitude and longitude columns
synthetic_data = {
    'time': ['2018', '2019', '2020'],
    'latitude': [30.0, 31.0, 32.0],
    'longitude': [120.0, 121.0, 122.0],
    'PM2.5': [25, 30, 20],
    'PM10': [40, 35, 45],
}

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(synthetic_data, geometry=gpd.points_from_xy(synthetic_data['longitude'], synthetic_data['latitude']))

# World map for background
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Select specific countries (Change this to 'China')
selected_countries = ['China']

# Filter the world GeoDataFrame
filtered_world = world[world['name'].isin(selected_countries)]

# Streamlit app
st.title("5. Bagaimana GeoDataFrame Visualization di Streamlit")

# Display the filtered world map for China
st.write("Country Map - China:")
fig, ax = plt.subplots(figsize=(15, 10))
filtered_world.plot(ax=ax, color='lightgrey', edgecolor='black')
st.pyplot(fig)

# Display the GeoDataFrame plot for China
st.write("GeoDataFrame Plot - China:")
fig, ax = plt.subplots(figsize=(15, 10))
filtered_world.plot(ax=ax, color='lightgrey', edgecolor='black')
gdf.plot(ax=ax, color='red', markersize=100)
st.pyplot(fig)

st.write("Pada plot GeoDataFrame di contoh sebelumnya, tanda merah menunjukkan lokasi yang diwakili oleh data dalam DataFrame Anda. Dalam contoh synthetic data yang diberikan, tanda merah mewakili titik-titik dengan koordinat latitude dan longitude yang telah ditentukan. Lokasi ini kemudian digambarkan pada peta negara yang diambil dari GeoDataFrame dunia.")

st.caption("Made By @Fakhrus Syakir")