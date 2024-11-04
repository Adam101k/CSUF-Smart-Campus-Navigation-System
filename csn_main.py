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
    "AD": (3550, 2366),
    "AF": (3277, 6895),
    "ASC": (355, 3906),
    "B": (2250, 4254)
}

# Define edges with distances or weights
edges = [
    ("AD", "AF", 456),
    ("AD", "ASC", 123),
    ("AD", "B", 789),
    ("AF", "ASC", 321),
    ("AF", "B", 654),
    ("ASC", "B", 987)
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
    ax.text(mid_x, mid_y, str(distance), color="blue")  # Annotate with distance

# Show legend outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Show plot
plt.show()
