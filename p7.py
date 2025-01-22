import pandas as pd
import networkx as nx
import plotly.graph_objects as go
from dash import Dash, dcc, html

edges_df = pd.read_csv('ogbn-arxiv-FP7.csv', sep=',', header=None, names=['Source', 'Target'])


labels_df = pd.read_csv('ogbn-arxiv_label.csv', sep='\t', header=None, names=['ID', 'Label'])

label_dict = labels_df.set_index('ID')['Label'].to_dict()


G = nx.Graph()

for _, row in edges_df.iterrows():
    G.add_edge(row['Source'], row['Target'])


nx.set_node_attributes(G, label_dict, 'label')


articulation_points = list(nx.articulation_points(G))
biconnected_components = list(nx.biconnected_components(G))


two_level_graph = nx.Graph()


for i, bcc in enumerate(biconnected_components):
    two_level_graph.add_node(f'BCC_{i}', label=f'BCC {i}')

for i, bcc in enumerate(biconnected_components):
    for node in bcc:
        if node in articulation_points:
            two_level_graph.add_node(f'Art_{node}', label=label_dict.get(node, f'Art {node}'))
            two_level_graph.add_edge(f'Art_{node}', f'BCC_{i}')

pos = nx.spring_layout(two_level_graph)

node_x = []
node_y = []
node_text = []
node_color = []

for node in two_level_graph.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    label = two_level_graph.nodes[node].get('label', str(node))
    node_text.append(f"{label}")
   
    if 'Art' in node:
        node_color.append('red')
    else:
        node_color.append('blue')


edge_x = []
edge_y = []
for edge in two_level_graph.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=1.0, color='#888'),
    hoverinfo='none',
    mode='lines'
)


node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    hoverinfo='text',
    text=node_text,
    marker=dict(
        showscale=True,
        colorscale='YlGnBu',
        size=20,
        color=node_color,  
        colorbar=dict(
            thickness=15,
            title='Node Color (Red=Articulation, Blue=BCC)',
            xanchor='left',
            titleside='right'
        )
    )
)


app = Dash(__name__)


app.layout = html.Div(
    style={'height': '100vh', 'width': '100vw', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'},
    children=[
        dcc.Graph(
            id='two-level-graph',
            config={'responsive': True},
            figure={
                'data': [edge_trace, node_trace],
                'layout': go.Layout(
                    title='<br>Two-Level Representation of Biconnected Component Tree',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=0, l=0, r=0, t=0),
                    xaxis=dict(showgrid=False, zeroline=False),
                    yaxis=dict(showgrid=False, zeroline=False),
                    height=None,
                    autosize=True
                )
            },
            style={'height': '100%', 'width': '100%'}
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
