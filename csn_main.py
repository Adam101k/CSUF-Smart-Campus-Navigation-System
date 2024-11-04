# Written By Adam Kaci
# Date: 11/04/2024

# Importing the necessary libraries
import math
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
    # Buildings/Points of Interest
    "A": (1216, 7566),
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
    "G": (2532, 8269),
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
    "W7": (3413, 5326),
    "W8": (2862, 8642),
    "W9": (1837, 8443),
    "W10": (2938, 7905),
    "W11": (744, 6978),
    "W12": (752, 5951),
    "W13": (769, 5330),
    "W14": (752, 4055),
    "W15": (760, 2838),
    "W16": (777, 1679),
    "W17": (1522, 1754),
    "W18": (2358, 1894),
    "W19": (4287, 1894),
    "W20": (628, 8062),
    "W21": (2350, 6613),
    "W22": (3567, 1870),
    "W23": (1671, 7011),
    "W24": (1911, 5951),
    "W25": (2689, 7317),
    "W26": (3368, 7706),
    "W27": (3666, 6721),
    "W28": (3757, 5728),
    "W29": (4560, 4908),
    "W30": (4552, 4353),
    "W31": (4569, 3997),
    "W32": (4552, 3832),
    "W33": (4105, 3823),
    "W34": (3666, 3749),
    "W35": (3327, 2863),
    "W36": (3318, 3343),
    "W37": (2226, 5338),
    "W38": (3029, 3633),
    "W39": (2830, 3352),
    "W40": (3004, 3004),
    "W41": (2615, 3078),
    "W42": (1919, 3095),
    "W43": (1762, 3327),
    "W44": (1861, 3790),
    "W45": (1249, 2871),
    "W46": (1555, 2871),
    "W47": (2408, 3956),
    "W48": (2847, 3625),
    "W49": (3277, 3616),
    "W50": (3310, 3020),
    "W51": (2441, 4428),
    "W52": (2789, 4544),
    "W53": (3227, 4660),
    "W54": (3501, 4726),
    "W55": (3939, 4759),
    "W56": (4039, 4941),
    "W57": (4627, 2871),
    "W58": (4486, 2706),
    "W59": (3989, 3012),
    "W60": (3948, 3492),
    "W61": (4320, 2226),
    "W62": (2557, 5338),
    "W63": (2913, 5711),
    "W64": (3029, 1878),
    "W65": (2159, 2507),
    "W66": (1787, 7657),
    "W67": (2764, 7052),
    "W68": (3517, 7276),
    "W69": (3749, 6208),
    "W70": (2830, 3029),
    "W71": (3023, 2681),
    "W72": (2780, 2656),
    "W73": (2457, 2664),
    "W74": (4271, 4941),
    "W75": (2813, 4246),
    "W76": (3277, 4270),
    "W77": (2052, 4850),
    "W78": (2027, 4585),
    "W79": (1588, 4593),
    "W80": (1563, 4428),
    "W81": (1082, 4444),
    "W82": (1058, 4072),
    "W83": (744, 4726),
    "W84": (4569, 3426)
}

# Define stock edges with only distances
# Edges Define as (node1, node2, distance in feet, time in minutes, and accessibility)


# Function to calculate Euclidean distance between two points
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Generate edges based on the three closest nodes for each node
edges = []
for node1 in nodes:
    distances = []
    for node2 in nodes:
        if node1 != node2:
            distance = calculate_distance(nodes[node1], nodes[node2])
            distances.append((node2, distance))
    # Sort distances and select the three closest nodes
    distances.sort(key=lambda x: x[1])
    closest_nodes = distances[:3]  # Adjust this number to add more or fewer connections
    for node2, distance in closest_nodes:
        edges.append((node1, node2, int(distance)))  # Add edge with integer distance

# Plot edges first (so they appear under the nodes)
for node1, node2, distance in edges:
    x_values = [nodes[node1][0], nodes[node2][0]]
    y_values = [nodes[node1][1], nodes[node2][1]]
    ax.plot(x_values, y_values, lw=1, color="black", zorder=1)  # Plot edges in black with low zorder

# Plot nodes with color distinction and higher zorder
for node, (x, y) in nodes.items():
    color = "green" if node.startswith("W") else "red"  # Waypoints in green, other nodes in red
    ax.scatter(x, y, s=15, color=color, label=node, zorder=2)  # Scatter plot each node with specified color and high zorder

# Show plot
plt.show()
