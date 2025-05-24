import plotly.graph_objects as go
import numpy as np
import plotly.io as pio
pio.renderers.default = "browser"

# --- Your vector data ---
x = np.array([0, 1, 2, 3])
y = np.array([0, 1, 2, 3])
u = np.array([1, 2, 3, 4])
v = np.array([2, 3, 4, 5])

# --- Animation parameters ---
n_frames = 30
duration_per_frame = 100  # milliseconds

# Precompute all frames
frames = []
for k in range(n_frames + 1):
    frac = k / n_frames
    traces = []
    for i in range(len(x)):
        # tip moves from tail → head
        traces.append(go.Scatter(
            x=[x[i], x[i] + u[i] * frac],
            y=[y[i], y[i] + v[i] * frac],
            mode='lines+markers',
            line=dict(color='blue', width=3),
            marker=dict(size=6),
            showlegend=False
        ))
    frames.append(go.Frame(data=traces, name=str(k)))

# Build figure with initial (frame 0) data + controls
fig = go.Figure(
    data=frames[0].data,
    layout=go.Layout(
        title="Animated Vector Growth",
        xaxis=dict(range=[-1, np.max(x+u)+1], zeroline=True, title="X"),
        yaxis=dict(range=[-1, np.max(y+v)+1], zeroline=True, title="Y"),
        width=700, height=700,
        updatemenus=[{
            'type': 'buttons',
            'showactive': False,
            'y': 1.05,
            'x': 1.15,
            'xanchor': 'right',
            'buttons': [{
                'label': '► Play',
                'method': 'animate',
                'args': [None, {
                    'frame': {'duration': duration_per_frame, 'redraw': True},
                    'fromcurrent': True,
                    'transition': {'duration': 0}
                }]
            }]
        }]
    ),
    frames=frames
)

# Slider (optional, Plotly often auto-generates it if you omit this)
fig.update_layout(
    sliders=[{
        'steps': [{
            'args': [[f.name], {'frame': {'duration': duration_per_frame, 'redraw': True},
                                 'mode': 'immediate'}],
            'label': f.name,
            'method': 'animate'
        } for f in frames],
        'transition': {'duration': 0},
        'x': 0.1, 'y': -0.1,
        'currentvalue': {'prefix': 'Frame: '}
    }]
)

fig.show()
