import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "/content/SupplyChainEmissionFactorsforUSIndustriesCommodities(2015_Summary_Industry).csv"
dataset = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("✅ Dataset Loaded successfully!\n")
display(dataset.head())

# Function to visualize dataset with column check
def visualizeData(dataset):
    # Use 'Industry Name' as the Sector and 'Supply Chain Emission Factors with Margins' for emissions
    plt.figure(figsize=(12, 8))
    #The 'Supply Chain Emission Factors with Margins' is object type, convert to numeric.
    dataset['Supply Chain Emission Factors with Margins'] = pd.to_numeric(dataset['Supply Chain Emission Factors with Margins'], errors='coerce')
    sector_emissions = dataset.groupby('Industry Name')['Supply Chain Emission Factors with Margins'].sum().reset_index()
    sns.barplot(data=sector_emissions, x='Industry Name', y='Supply Chain Emission Factors with Margins')
    plt.xticks(rotation=90)
    plt.title("Total GHG Emissions by Industry")
    plt.xlabel("Industry")
    plt.ylabel("Total Emissions (CO2-equivalent)")
    plt.tight_layout()
    plt.show()


# Visualize the data
visualizeData(dataset)
