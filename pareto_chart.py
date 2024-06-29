import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import sqlite3

conn = sqlite3.connect('mySQLLite.db')
# c = conn.cursor()
# c.execute("SELECT * FROM pareto_data")

# # Fetch all the rows
# rows = c.fetchall()

myDf = pd.read_sql_query("SELECT * FROM pareto_data", conn)
myDf.head()
myField = myDf['prod_name']

def pareto(data, x, y):
    data = data.sort_values(y, ascending=False)
    data["cumpercentage"] = data[y].cumsum()/data[y].sum()*100

    fig, ax = plt.subplots()
    ax.bar(data[x], data[y], color="C0") 
    ax2 = ax.twinx()
    ax2.plot(data[x], data["cumpercentage"], color="C1", marker="o", ms=7)
    ax2.yaxis.set_major_formatter(PercentFormatter())

    ax.tick_params(axis="y", colors="C0")
    ax2.tick_params(axis="y", colors="C1")

# Add labels to the axes
    ax.set_xlabel('Product Name')
    ax.set_ylabel('Frequency')
    ax2.set_ylabel('Cummulative Percentage')
    plt.show()

pareto(myDf, 'prod_name', 'frequency')