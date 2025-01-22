# Two-Level Graph Visualization: Articulation Points and Biconnected Components

This project provides an interactive visualization of a graph's articulation points and biconnected components (BCCs) using a two-level representation. It leverages NetworkX for graph analysis, Dash for the web interface, and Plotly for creating responsive, interactive visualizations.

---

## Objective

- Identify and visualize **articulation points** and **biconnected components** in a graph.
- Represent the graph as a two-level hierarchical structure, with articulation points connecting different BCCs.
- Provide an interactive, web-based visualization for better insight into the graph's structure.

---

## Features

1. **Graph Analysis**:
   - Reads the graph's edge list and node labels from CSV files.
   - Identifies articulation points and biconnected components using NetworkX.

2. **Two-Level Graph Construction**:
   - Constructs a graph where:
     - Articulation points are represented as separate nodes.
     - BCCs are represented as nodes connected to their articulation points.

3. **Interactive Visualization**:
   - Displays the two-level graph using Plotly for an intuitive and interactive experience.
   - Nodes are color-coded:
     - **Red**: Articulation points.
     - **Blue**: BCC nodes.
   - Labels and tooltips provide additional context for each node.

4. **Web-Based Interface**:
   - Uses Dash to host the visualization on a local server.
   - Fully responsive and adjustable layout for seamless interaction.

---

## Libraries Used

1. **NetworkX**:
   - Used for graph creation and analysis.
   - Functions like `articulation_points()` and `biconnected_components()` enable efficient computation.

2. **Pandas**:
   - Handles reading edge lists and node labels from CSV files.

3. **Plotly**:
   - Provides interactive graph visualization.
   - Enables dynamic rendering with custom layouts, colors, and hover text.

4. **Dash**:
   - Serves as the framework for the web application.
   - Provides a responsive user interface for hosting the visualization.

---

## File Descriptions

### 1. **`p7.py`**
- **Objective**:
  - Reads the edge list and node labels from CSV files.
  - Analyzes the graph to identify articulation points and BCCs.
  - Constructs a two-level graph representation.
  - Visualizes the graph in an interactive Dash app.
- **Output**:
  - A web-based visualization with:
    - Nodes labeled and color-coded based on their type (articulation or BCC).
    - Interactive elements such as tooltips and zooming capabilities.

---

## How to Run

1. **Prerequisites**:
   - Install the required libraries:
     ```bash
     pip install pandas networkx dash plotly
     ```

2. **Prepare Input Files**:
   - **Edge List** (`ogbn-arxiv-FP7.csv`):
     - Format: Two columns representing source and target nodes of the edges.
   - **Node Labels** (`ogbn-arxiv_label.csv`):
     - Format: Two columns with node IDs and their corresponding labels.

3. **Run the Script**:
   - Execute the script:
     ```bash
     python p7.py
     ```
   - Open the browser at `http://127.0.0.1:8050/` to view the visualization.

---

## Example Visualization

The graph visualization includes:
- **Articulation Points**: Highlighted in red.
- **BCC Nodes**: Highlighted in blue.
- Interactive layout with zooming, panning, and tooltips for node labels.

---

## Use Cases

- **Educational**:
  - Learn about graph theory concepts like articulation points and biconnected components.
- **Graph Analysis**:
  - Explore the structure of complex graphs in network analysis.
- **Visualization**:
  - Gain insights into hierarchical relationships in graphs.


