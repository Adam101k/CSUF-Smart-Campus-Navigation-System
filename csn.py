# Written By Adam Kaci
# Date: 11/06/2024

from collections import deque
import tkinter as tk
import math
import threading
from tkinter import messagebox
import tracemalloc  # For tracking memory usage
import time as timer  # For tracking time taken by algorithms
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Loading in campus map as background
img = plt.imread("CSUF-Smart-Campus-Navigation-System/campus_map.png")
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, 7084, 0, 9167])

# Function to calculate Euclidean distance between two points
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

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
edges = {}  # Dictionary to store the edges as we fill them in
# Calculate the distance between each pair of nodes and store the 3 closest nodes for each node
for node1 in nodes:
    distances = []
    for node2 in nodes:
        if node1 != node2:
            distances.append((node2, calculate_distance(nodes[node1], nodes[node2])))
    distances.sort(key=lambda x: x[1])
    closest_nodes = distances[:3]  # Get the 3 closest nodes
    for i, (node2, distance) in enumerate(closest_nodes):
        time = i + 1  # Time to travel between nodes
        edges.setdefault(node1, []).append((node2, int(distance), time))


class CampusNavigationSystemGUI:
    def __init__(self, root):
        self.root = root  # The main window of the GUI
        self.root.title("Campus Navigation System")  # Setting the title of the window
        
        self.graph = {}  # Dictionary to store the graph as an adjacency list
        self.edges = []  # List to store the edges for easy access
        self.visited = set()  # Set to keep track of visited nodes
        self.mst = []  # List to store edges in the MST
        self.edge_list = []  # Priority queue for candidate edges
        
        self.performance_data = {}  # Dictionary to store performance data for each algorithm
        self.step = 0  # Variable to track the current step in the MST construction

        self.bfs_complete = False  # Flag to indicate if BFS has completed
        self.dfs_complete = False  # Flag to indicate if DFS has completed
        self.dijkstra_complete = False  # Flag to indicate if Dijkstra's algorithm has completed
        
        # Call the function to set up the GUI layout
        self.setup_gui()
    
    def setup_gui(self):
        # Frame to hold input fields and buttons
        frame = tk.Frame(self.root)
        frame.pack(pady=10)  # Add padding for better appearance

        # Input field for start node
        tk.Label(frame, text="Start Node:").grid(row=0, column=0)
        self.start_node_entry = tk.Entry(frame, width=5)  # Entry box for start node
        self.start_node_entry.grid(row=0, column=1)

        # Input field for end node
        tk.Label(frame, text="End Node:").grid(row=0, column=2)
        self.end_node_entry = tk.Entry(frame, width=5)  # Entry box for end node
        self.end_node_entry.grid(row=0, column=3)

        # Toggle checkboxes for distance, time, and accessibility
        self.use_distance = tk.BooleanVar()
        tk.Checkbutton(frame, text="Use Distance", variable=self.use_distance).grid(row=1, column=0)

        self.use_time = tk.BooleanVar()
        tk.Checkbutton(frame, text="Use Time", variable=self.use_time).grid(row=1, column=1)

        self.use_accessibility = tk.BooleanVar()
        tk.Checkbutton(frame, text="Use Accessibility", variable=self.use_accessibility).grid(row=1, column=2)

        # Button to start running the program
        self.run_button = tk.Button(frame, text="Compare Traversal", command=self.start_traversal)
        self.run_button.grid(row=2, column=0, columnspan=4, pady=10)



        # Create a canvas to display the graph using matplotlib
        self.fig_bfs, self.ax_bfs = plt.subplots(figsize=(5, 5))  # Create a figure and axis for plotting
        self.canvas_bfs = FigureCanvasTkAgg(self.fig_bfs, master=self.root)  # Integrate matplotlib with Tkinter
        self.canvas_bfs.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)  # Add the canvas to the window
        self.ax_bfs.set_title("BFS Traversal")  # Set the title of the plot

        self.fig_dfs, self.ax_dfs = plt.subplots(figsize=(5, 5))  # Create a figure and axis for plotting
        self.canvas_dfs = FigureCanvasTkAgg(self.fig_dfs, master=self.root)  # Integrate matplotlib with Tkinter
        self.canvas_dfs.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)  # Add the canvas to the window
        self.ax_dfs.set_title("DFS Traversal")  # Set the title of the plot

        self.fig_dijkstra, self.ax_dijkstra = plt.subplots(figsize=(5, 5))  # Create a figure and axis for plotting
        self.canvas_dijkstra = FigureCanvasTkAgg(self.fig_dijkstra, master=self.root)  # Integrate matplotlib with Tkinter
        self.canvas_dijkstra.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)  # Add the canvas to the window
        self.ax_dijkstra.set_title("Dijkstra's Algorithm")

        self.update_graph(self.ax_bfs)  # Update the graph with the initial state
        self.update_graph(self.ax_dfs)  # Update the graph with the initial state
        self.update_graph(self.ax_dijkstra)  # Update the graph with the initial state

    def start_traversal(self):

        # Reset completion flags
        self.reset_state()

        start = self.start_node_entry.get()
        end = self.end_node_entry.get()

        if start in nodes and end in nodes:
            self.clear_paths() # Clear the previous paths from the graph

            # Run BFS, DFS, and Dijkstra's algorithms in seperate threads
            bfs_thread = threading.Thread(target=self.bfs, args=(start, end, self.use_distance.get(), self.use_time.get(), self.use_accessibility.get(), self.ax_bfs))
            dfs_thread = threading.Thread(target=self.dfs, args=(start, end, self.use_distance.get(), self.use_time.get(), self.use_accessibility.get(), self.ax_dfs))
            dijkstra_thread = threading.Thread(target=self.dijkstra, args=(start, end, self.use_distance.get(), self.use_time.get(), self.use_accessibility.get(), self.ax_dijkstra))

            # Start all threads
            bfs_thread.start()
            dfs_thread.start()
            dijkstra_thread.start()

        else:
            messagebox.showerror("Error", "Invalid start or end node entered")
        
    
    def bfs(self, start, end, use_distance, use_time, use_accessibility, ax):
        print("Running BFS")
        
        queue = deque([(start, [start])])  # Initialize the queue with the start node and path
        visited = set()

        # Start timing and memory tracking for BFS
        start_time = timer.perf_counter()
        tracemalloc.start()  # Start memory tracking

        def bfs_step():
            if self.bfs_complete or not queue:
                return
            current, path = queue.popleft()  # Use popleft() to dequeue from the front
            if current == end:
                # End timing and memory tracking
                end_time = timer.perf_counter()
                current_memory, peak_memory = tracemalloc.get_traced_memory()
                tracemalloc.stop()  # Stop memory tracking
                
                # Update path on GUI
                self.bfs_complete = True
                self.root.after(0, lambda: self.handle_algorithm_completion("BFS", (end_time - start_time) * 1000, current_memory, peak_memory))
                app.highlight_path(path, app.ax_bfs)
                return
            
            visited.add(current)
            for edge in edges.get(current, []):
                node2, distance, time = edge[:3]
                accessibility = edge[3] if len(edge) > 3 else "Unknown"  # Using "Unknown" if accessibility is missing
                if node2 not in visited and not self.bfs_complete:
                    if ((use_distance and distance <= 1000) or not use_distance) and \
                    ((use_time and time <= 2) or not use_time) and \
                    ((use_accessibility and accessibility == "Accessible") or not use_accessibility):
                        queue.append((node2, path + [node2]))
                        app.update_edge_color(current, node2, "blue", app.ax_bfs)
                        app.update_node_color(node2, "blue", app.ax_bfs)
            
            app.canvas_bfs.draw_idle()
            app.root.after(10, bfs_step)


        bfs_step()


    def dfs(self, start, end, use_distance, use_time, use_accessibility, ax):
        
        print("Running DFS")

        # Start timing and memory tracking for dfs
        start_time = timer.perf_counter()
        tracemalloc.start()

        visited = set()

        def dfs_step(current, path):
            if self.dfs_complete:
                return
            if current == end:
                # End timing and memory tracking
                end_time = timer.perf_counter()
                current_memory, peak_memory = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                # Update path on GUI
                self.dfs_complete = True
                self.root.after(0, lambda: self.handle_algorithm_completion("DFS", (end_time - start_time) * 1000, current_memory, peak_memory))
                app.highlight_path(path, app.ax_dfs)
                return
            visited.add(current)

            # Recursively visit all the neighbors of the current node
            for edge in edges.get(current, []):
                node2, distance, time = edge[:3]
                accessibility = edge[3] if len(edge) > 3 else "Unknown"
                if node2 not in visited and not self.dfs_complete:
                    if ((use_distance and distance <= 1000) or not use_distance) and \
                    ((use_time and time <= 2) or not use_time) and \
                    ((use_accessibility and accessibility == "Accessible") or not use_accessibility):
                        app.update_edge_color(current, node2, "blue", app.ax_dfs)
                        app.update_node_color(node2, "blue", app.ax_dfs)
                        dfs_step(node2, path + [node2])
            app.canvas_dfs.draw_idle()
            app.root.after(10, dfs_step, current, path)

        dfs_step(start, [start])

    def dijkstra(self, start, end, use_distance, use_time, use_accessibility, ax):
    
        print("Running Dijkstra")
        # Start timing and memory tracking for dijkstra
        start_time = timer.perf_counter()
        tracemalloc.start()

        # Initialize distances and tracking structures
        distances = {node: float('inf') for node in nodes}
        distances[start] = 0
        previous = {node: None for node in nodes}
        visited = set()

        while not self.dijkstra_complete:
            # Select the unvisited node with the smallest known distance
            current = min((node for node in nodes if node not in visited), key=distances.get, default=None)
            
            # If there are no reachable nodes left, exit the loop
            if current is None or distances[current] == float('inf'):
                break
            
            visited.add(current)
            
            # Stop if we've reached the destination node
            if current == end:
                end_time = timer.perf_counter()
                current_memory, peak_memory = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                # Reconstruct the path from start to end
                path = []
                step = end
                while step:
                    path.insert(0, step)
                    step = previous[step]

                # Update path on GUI
                self.dijkstra_complete = True
                self.root.after(0, lambda: self.handle_algorithm_completion("Dijkstra", (end_time - start_time) * 1000, current_memory, peak_memory))
                app.highlight_path(path, app.ax_dijkstra)
                return

            # Explore neighbors
            for edge in edges.get(current, []):
                node2, distance, time = edge[:3]
                accessibility = edge[3] if len(edge) > 3 else "Unknown"

                if ((use_distance and distance <= 1000) or not use_distance) and \
                ((use_time and time <= 2) or not use_time) and \
                ((use_accessibility and accessibility == "Accessible") or not use_accessibility):
                    
                    new_distance = distances[current] + distance
                    if new_distance < distances[node2]:
                        distances[node2] = new_distance
                        previous[node2] = current
                        # Update the GUI to show the path traversal
                        app.update_edge_color(current, node2, "blue", app.ax_dijkstra)
                        app.update_node_color(node2, "blue", app.ax_dijkstra)

            # Refresh the GUI canvas
            app.canvas_dijkstra.draw_idle()     

    
    def clear_paths(self):
        self.ax_bfs.clear()  # Clear the previous plot
        self.ax_bfs.set_title("BFS Traversal")  # Set the title of the plot

        self.ax_dfs.clear()  # Clear the previous plot
        self.ax_dfs.set_title("DFS Traversal")

        self.ax_dijkstra.clear()  # Clear the previous plot
        self.ax_dijkstra.set_title("Dijkstra's Algorithm")
        
        self.update_graph(self.ax_bfs, background_only=True)
        self.update_graph(self.ax_dfs, background_only=True)
        self.update_graph(self.ax_dijkstra, background_only=True)
        # Would put idle code here

    def highlight_path(self, path, ax):
        # Highlights the nodes and edges in the given path on the specified axis.
        for i in range(len(path) - 1):
            node1, node2 = path[i], path[i + 1]
            self.update_edge_color(node1, node2, "red", ax)  # Highlight edges in yellow
            self.update_node_color(node1, "red", ax)  # Highlight nodes in yellow

        # Highlight the final node in the path
        self.update_node_color(path[-1], "yellow", ax)
        ax.figure.canvas.draw_idle()  # Redraw the canvas to show updates


    def update_edge_color(self, node1, node2, color, ax):
        x_values = [nodes[node1][0], nodes[node2][0]]
        y_values = [nodes[node1][1], nodes[node2][1]]
        ax.plot(x_values, y_values, color=color, linewidth=2, zorder=3)  # Draw the edge between the nodes

    def update_node_color(self, node, color, ax):
        x, y = nodes[node]
        ax.scatter(x, y, s=50, color=color, zorder=4)
    def update_graph(self, ax, background_only=False):
        ax.imshow(img, extent=[0, 7084, 0, 9167])  # Display the campus map as the background

        if not background_only:
            for node1, node2 in [(n1, n2) for n1 in edges for n2 in edges[n1]]:
                x_values = [nodes[node1][0], nodes[node2[0]][0]]
                y_values = [nodes[node1][1], nodes[node2[0]][1]]
                ax.plot(x_values, y_values, color='black', linewidth=1, zorder=1) # Draw the edge between the nodes
        
        for node, (x, y) in nodes.items():
            color = "green" if node.startswith("W") else "red"
            ax.scatter(x, y, color=color, s=15, label=node, zorder=2)

    def handle_algorithm_completion(self, algorithm_name, duration, current_memory, peak_memory):
        # Store performance data for each algorithm
        self.performance_data[algorithm_name] = {
            "duration": duration,
            "current_memory": current_memory / 1024,  # Convert to KB
            "peak_memory": peak_memory / 1024  # Convert to KB
        }

        # Check if all algorithms have completed
        if len(self.performance_data) == 3:
            # Generate and show summary
            summary_text = "\n\n".join(
                f"{algo}:\n"
                f" - Duration: {data['duration']:.2f} ms\n"
                f" - Current Memory Usage: {data['current_memory']:.2f} KB\n"
                f" - Peak Memory Usage: {data['peak_memory']:.2f} KB"
                for algo, data in self.performance_data.items()
            )
            self.root.after(0, lambda: messagebox.showinfo("Algorithm Performance Summary", summary_text))
            self.performance_data.clear()
    
    def reset_state(self):
        self.bfs_complete = False
        self.dfs_complete = False
        self.dijkstra_complete = False
        self.performance_data.clear()
        self.clear_paths()  # Clear any highlighted paths from previous runs


# Create the main window for the GUI
root = tk.Tk()
app = CampusNavigationSystemGUI(root)  # Create an instance of the CampusNavigationSystemGUI class
root.mainloop()  # Start the main event loop of the GUI
