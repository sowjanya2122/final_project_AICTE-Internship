from tkinter import *
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

main = Tk()
main.title("Supply Chain GHG Emissions Visualization")
main.geometry("1000x700")

dataset = None

# Function to load dataset
def loadDataset():
    global dataset
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    text.delete('1.0', END)
    if os.path.exists(file_path):
        dataset = pd.read_csv(file_path)
        # Display only the file name without the full path.
        file_name = os.path.basename(file_path)
        text.insert(END, f"✅ Dataset Loaded: {file_name}\n\n")
        text.insert(END, str(dataset.head()))
    else:
        text.insert(END, "⚠️ File not found!")

# Function to visualize dataset with column check
def visualizeData():
    global dataset
    required_columns = ['Sector', 'Year', 'Emissions_CO2e']

    if dataset is None:
        text.delete('1.0', END)
        text.insert(END, "⚠️ Please upload a dataset first!")
        return

    # Check if all required columns exist
    missing = [col for col in required_columns if col not in dataset.columns]
    if missing:
        text.delete('1.0', END)
        text.insert(END, f"⚠️ Missing required columns: {', '.join(missing)}\n")
        return

    # Visualization 1: Total Emissions by Sector
    plt.figure(figsize=(10, 6))
    sector_emissions = dataset.groupby('Sector')['Emissions_CO2e'].sum().reset_index()
    sns.barplot(data=sector_emissions, x='Sector', y='Emissions_CO2e')
    plt.xticks(rotation=45)
    plt.title("Total GHG Emissions by Sector")
    plt.xlabel("Sector")
    plt.ylabel("Total Emissions (CO2-equivalent)")
    plt.tight_layout()
    plt.show()

    # Visualization 2: Emissions Trend Over Years by Sector
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=dataset, x='Year', y='Emissions_CO2e', hue='Sector')
    plt.title("GHG Emissions Trends Over Years by Sector")
    plt.xlabel("Year")
    plt.ylabel("Emissions (CO2-equivalent)")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

# Function to close the application
def close():
    main.destroy()

# GUI Elements
font = ('times', 16, 'bold')
title = Label(main, text='Supply Chain GHG Emissions Visualization', justify=LEFT)
title.config(bg='lavender blush', fg='DarkOrchid1', font=font, height=3, width=120)
title.pack()

font1 = ('times', 13, 'bold')
uploadButton = Button(main, text="Upload Dataset", command=loadDataset)
uploadButton.place(x=10, y=100)
uploadButton.config(font=font1)

visualizeButton = Button(main, text="Visualize Data", command=visualizeData)
visualizeButton.place(x=250, y=100)
visualizeButton.config(font=font1)

exitButton = Button(main, text="Exit", command=close)
exitButton.place(x=450, y=100)
exitButton.config(font=font1)

font2 = ('times', 12, 'bold')
text = Text(main, height=25, width=140)
text.place(x=10, y=200)
text.config(font=font2)

main.config(bg='light coral')
main.mainloop()
