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


# Function to calculate Euclidean distance between two points
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Wheelchair Regions
accessible_x_min, accessible_x_max = 1000, 4000
accessible_y_min, accessible_y_max = 3000, 7000

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


# Generate edges based on the three closest nodes for each node
edges = []
for node1 in nodes:
    distances = []
    for node2 in nodes:
        if node1 != node2:
            distance = calculate_distance(nodes[node1], nodes[node2])
            distances.append((node2, distance))
    distances.sort(key=lambda x: x[1])
    closest_nodes = distances[:3]
    for i, (node2, distance) in enumerate(closest_nodes):
        time = i + 1
        accessibility = (
            "Accessible" if (accessible_x_min <= nodes[node1][0] <= accessible_x_max and
                             accessible_y_min <= nodes[node1][1] <= accessible_y_max)
            else "Not Accessible"
        )
        edges.append((node1, node2, int(distance), time, accessibility))

# BFS function with criteria filters
def bfs(start, end, use_distance, use_time, use_accessibility):
    queue = [(start, [start])]
    visited = set()

    while queue:
        current, path = queue.pop(0)
        if current == end:
            return path
        
        visited.add(current)
        for node1, node2, distance, time, accessibility in edges:
            if node1 == current and node2 not in visited:
                if ((use_distance and distance <= 1000) or not use_distance) and \
                   ((use_time and time <= 2) or not use_time) and \
                   ((use_accessibility and accessibility == "Accessible") or not use_accessibility):
                    queue.append((node2, path + [node2]))
    
    return None

# DFS function with criteria filters
def dfs(start, end, use_distance, use_time, use_accessibility, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()

    visited.add(start)
    if start == end:
        return path

    for node1, node2, distance, time, accessibility in edges:
        if node1 == start and node2 not in visited:
            if ((use_distance and distance <= 1000) or not use_distance) and \
               ((use_time and time <= 2) or not use_time) and \
               ((use_accessibility and accessibility == "Accessible") or not use_accessibility):
                result = dfs(node2, end, use_distance, use_time, use_accessibility, path + [node2], visited)
                if result:
                    return result

    visited.remove(start)
    return None

# GUI setup
class GraphTraversalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Traversal with BFS and DFS")

        # Input for start and end nodes
        tk.Label(root, text="Start Node:").grid(row=0, column=0)
        self.start_entry = tk.Entry(root)
        self.start_entry.grid(row=0, column=1)

        tk.Label(root, text="End Node:").grid(row=0, column=2)
        self.end_entry = tk.Entry(root)
        self.end_entry.grid(row=0, column=3)

        # Checkboxes for toggles
        self.use_distance = tk.BooleanVar()
        tk.Checkbutton(root, text="Use Distance", variable=self.use_distance).grid(row=1, column=0)

        self.use_time = tk.BooleanVar()
        tk.Checkbutton(root, text="Use Time", variable=self.use_time).grid(row=1, column=1)

        self.use_accessibility = tk.BooleanVar()
        tk.Checkbutton(root, text="Use Accessibility", variable=self.use_accessibility).grid(row=1, column=2)

        # Buttons to start BFS and DFS
        tk.Button(root, text="Find Path (BFS)", command=self.find_path_bfs).grid(row=2, column=0)
        tk.Button(root, text="Find Path (DFS)", command=self.find_path_dfs).grid(row=2, column=1)

        # Canvas for matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().grid(row=3, column=0, columnspan=4)
        
        # Display the initial graph
        self.update_graph()

    # Function to highlight the path on the graph
    def highlight_path(self, path):
        self.ax.clear()
        self.update_graph(base_only=True)
        for i in range(len(path) - 1):
            node1, node2 = path[i], path[i+1]
            x_values = [nodes[node1][0], nodes[node2][0]]
            y_values = [nodes[node1][1], nodes[node2][1]]
            self.ax.plot(x_values, y_values, color="blue", lw=2, zorder=3)
        self.canvas.draw()

    # Function to update the graph visualization
    def update_graph(self, base_only=False):
        self.ax.imshow(img, extent=[0, 7084, 0, 9167])
        
        # Draw all edges in the graph
        if not base_only:
            for node1, node2, distance, time, accessibility in edges:
                x_values = [nodes[node1][0], nodes[node2][0]]
                y_values = [nodes[node1][1], nodes[node2][1]]
                self.ax.plot(x_values, y_values, color="black", lw=1, zorder=1)

        # Draw nodes with accessibility distinction
        for node, (x, y) in nodes.items():
            color = "green" if node.startswith("W") else "red"
            self.ax.scatter(x, y, s=15, color=color, label=node, zorder=2)
        
        self.canvas.draw()

    # Function to find path using BFS
    def find_path_bfs(self):
        start = self.start_entry.get()
        end = self.end_entry.get()
        if start and end and start in nodes and end in nodes:
            path = bfs(start, end, self.use_distance.get(), self.use_time.get(), self.use_accessibility.get())
            if path:
                self.highlight_path(path)
                messagebox.showinfo("BFS Path", f"Path found: {' -> '.join(path)}")
            else:
                messagebox.showinfo("BFS Path", "No path found.")
        else:
            messagebox.showerror("Error", "Please enter valid start and end nodes.")

    # Function to find path using DFS
    def find_path_dfs(self):
        start = self.start_entry.get()
        end = self.end_entry.get()
        if start and end and start in nodes and end in nodes:
            path = dfs(start, end, self.use_distance.get(), self.use_time.get(), self.use_accessibility.get())
            if path:
                self.highlight_path(path)
                messagebox.showinfo("DFS Path", f"Path found: {' -> '.join(path)}")
            else:
                messagebox.showinfo("DFS Path", "No path found.")
        else:
            messagebox.showerror("Error", "Please enter valid start and end nodes.")

# Load campus map as background
img = plt.imread("CSUF-Smart-Campus-Navigation-System/campus_map.png")

# Initialize the GUI application
root = tk.Tk()
app = GraphTraversalApp(root)
root.mainloop()