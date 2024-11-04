# Written By Adam Kaci
# Date: 11/04/2024

# Importing the necessary libraries
import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Loading in campus map as background
img = plt.imread("CSUF-Smart-Campus-Navigation-System/campus_map.png")
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, 7084, 0, 9167])

# Define nodes with example coordinates (x, y) and add them to graph
nodes = {
    # Buildings
    "AD": (3550, 2366),
    "AF": (3277, 6895),
    "ASC": (355, 3906),
    "B": (2250, 4254),
    "CC": (1356, 6762),
    "CJ": (3823, 2648),
    "CP": (3881, 1522),
    "CPAC": (2308, 3385),
    "CS": (4411, 4486),
    "CY": (1042, 5835),
    "DBH": (2640, 2515),
    "E": (4163, 4502),
    "EC": (3567, 3923),
    "ENPS": (4925, 3691),
    "ESPS": (4900, 3186),
    "GAH": (951, 4527),
    "GAS": (4751, 5049),
    "GC": (2168, 2822),
    "GF": (3004, 7508),
    "GH": (3650, 2888),
    "H": (3650, 3352),
    "HRE": (4966, 5355),
    "KHS": (2623, 4734),
    "LH": (3368, 2499),
    "MC": (2863, 2209),
    "MH": (2946, 2888),
    "MS": (3666, 5719),
    "NPS": (1381, 2490),
    "P": (934, 6075),
    "PL": (3037, 4006),
    "RG": (4130, 5272),
    "RH": (4726, 5396),
    "SCPS": (1365, 5016),
    "SGMH": (3848, 2217),
    "SHCC": (3625, 4900),
    "SRC": (1803, 5024),
    "T": (3674, 5446),
    "TG": (2764, 4999),
    "TH": (562, 3658),
    "TS": (2275, 7292),
    "TSC": (2863, 6696),
    "TSF": (3451, 6365),
    "TSU": (1348, 4213),
    "TTC": (2217, 5678),
    "TTF": (2606, 6348),
    "UP": (967, 4966),
    "VA": (1108, 3542),
    # Waypoints/Intersections, this is to buffer the nodes to make the graph more realistic
    "W1": (2598, 7866),
    "W2": (1850, 6419),
    "W3": (1947, 5340),
    "W4": (3146, 6360),
    "W5": (2930, 6012),
    "W6": (2922, 5337),
    "W7": (3413, 5326)
}

# Define stock edges with only distances
# Edges Define as (node1, node2, distance in feet, time in minutes, and accessibility)
edges = [
    ("AD", "AF", 500),
    ("AD", "ASC", 200),
    ("AD", "CJ", 300),
    ("AF", "GF", 250),
    ("AF", "TSC", 400),
    ("ASC", "TH", 150),
    ("ASC", "TSU", 350),
    ("B", "KHS", 100),
    ("B", "PL", 300),
    ("CC", "CY", 150),
    ("CC", "TSU", 250),
    ("CJ", "GH", 200),
    ("CJ", "LH", 300),
    ("CP", "SGMH", 250),
    ("CP", "MC", 400),
    ("CPAC", "GC", 150),
    ("CS", "E", 300),
    ("CS", "EC", 400),
    ("CY", "SCPS", 200),
    ("CY", "SRC", 350),
    ("DBH", "LH", 200),
    ("DBH", "MH", 300),
    ("E", "RG", 150),
    ("E", "GAS", 250),
    ("EC", "GH", 200),
    ("ENPS", "ESPS", 250),
    ("ENPS", "GAH", 300),
    ("GF", "TS", 200),
    ("GF", "TSC", 350),
    ("GH", "H", 150),
    ("H", "KHS", 200),
    ("HRE", "RH", 250),
    ("HRE", "SHCC", 300),
    ("KHS", "TG", 150),
    ("LH", "MC", 200),
    ("MC", "MH", 250),
    ("MS", "T", 200),
    ("MS", "SHCC", 350),
    ("NPS", "VA", 150),
    ("NPS", "GC", 200),
    ("P", "CY", 250),
    ("PL", "TG", 150),
    ("PL", "T", 300),
    ("RG", "RH", 200),
    ("RG", "SHCC", 350),
    ("SCPS", "SRC", 250),
    ("SGMH", "MC", 200),
    ("SGMH", "CP", 300),
    ("SHCC", "T", 200),
    ("SHCC", "TG", 350),
    ("SRC", "UP", 250),
    ("T", "TG", 150),
    ("TG", "TSC", 300),
    ("TH", "VA", 200),
    ("TS", "TSC", 150),
    ("TSF", "TSC", 250),
    ("TTC", "TTF", 300),
    ("TTF", "TSF", 200),
    ("UP", "P", 150),
    ("VA", "TH", 250),
]

# Plot nodes
for node, (x, y) in nodes.items():
    ax.scatter(x, y, s=5, label=node)  # Scatter plot each node

# Plot edges with distances
for node1, node2, distance in edges:
    x_values = [nodes[node1][0], nodes[node2][0]]
    y_values = [nodes[node1][1], nodes[node2][1]]
    ax.plot(x_values, y_values, 'k-', lw=1)
    mid_x, mid_y = (x_values[0] + x_values[1]) / 2, (y_values[0] + y_values[1]) / 2
    ax.text(mid_x, mid_y, str(distance),fontsize = 6, color="blue")  # Annotate with distance

# Show legend outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Show plot
plt.show()
