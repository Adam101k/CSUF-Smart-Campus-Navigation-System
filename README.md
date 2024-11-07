# Campus Navigation System README
Made by Adam Kaci as a part of the Fall 2024 CPSC 335 CSUF Course.

## Overview
The Campus Navigation System is a GUI-based application designed to facilitate navigation across a university campus. The system allows users to choose start and end points on a campus map and compare three traversal algorithms—Breadth-First Search (BFS), Depth-First Search (DFS), and Dijkstra's Algorithm. Each algorithm is evaluated based on the user-selected criteria of distance, time, and accessibility.

### Features
- **Campus Map Visualization**: Displays a background map of the campus, with nodes representing buildings and waypoints.
- **Algorithm Comparison**: BFS, DFS, and Dijkstra's Algorithm can be executed simultaneously to find paths between selected points.
- **Performance Metrics**: Displays memory usage and execution time for each algorithm.
- **Customizable Pathfinding**: Users can filter paths by distance, travel time, and accessibility.

## Getting Started

### Prerequisites
- Python 3.x
- Required packages: `tkinter`, `matplotlib`, `threading`, `tracemalloc`, `time`

### Installation
1. Clone the repository.
2. Ensure `campus_map.png` is placed in the `CSUF-Smart-Campus-Navigation-System` directory.
3. Install required packages:
   ```bash
   pip install matplotlib
   ```

### Usage
1. Run the program:
   ```bash
   python csn.py
   ```
2. In the GUI:
   - Enter start and end node labels.
   - Choose path criteria (distance, time, accessibility).
   - Click "Compare Traversal" to start the algorithms.
3. Observe each algorithm's progress and the performance summary.

### Code Structure
- **Nodes and Edges**: Each node represents a point of interest or intersection, connected by edges with calculated distances.
- **Graph Rendering**: Utilizes `matplotlib` for map visualization and path updates.
- **Algorithms**:
  - **BFS**: Explores all neighbors level-by-level.
  - **DFS**: Recursively explores each path to its end.
  - **Dijkstra**: Finds the shortest path based on edge weights.
  
### GUI Components
- **Inputs**: Entry fields for start and end points.
- **Check Buttons**: Toggle between distance, time, and accessibility criteria.
- **Path Visualization**: Three side-by-side displays show each algorithm's traversal and final path.

## Future Improvements
- Implement user-defined waypoint creation.
- Integrate real-time campus traffic data for path optimization.
- Expand on Accessibility pathing to better represent real life data.
