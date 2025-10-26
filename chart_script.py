import plotly.graph_objects as go
import pandas as pd

# Create the data
data = [
    {"Platform": "Vercel", "Build Minutes": 6000, "Bandwidth GB": 100, "Rating": 5},
    {"Platform": "Netlify", "Build Minutes": 300, "Bandwidth GB": 100, "Rating": 4},
    {"Platform": "GitHub Pages", "Build Minutes": 600, "Bandwidth GB": 100, "Rating": 3.5}
]

df = pd.DataFrame(data)

# Normalize the data to make comparison possible (scale to 0-100)
# Build Minutes: normalize to percentage of max
max_build = df['Build Minutes'].max()
df['Build_Norm'] = (df['Build Minutes'] / max_build) * 100

# Bandwidth: already at 100 for all, so just use as is
df['Bandwidth_Norm'] = df['Bandwidth GB']

# Rating: scale from 0-5 to 0-100
df['Rating_Norm'] = (df['Rating'] / 5) * 100

# Create the grouped bar chart
fig = go.Figure()

# Theme colors in order (following prior instructions)
colors = ['#1FB8CD', '#DB4545', '#2E8B57']

# Add bars for each platform with hover info showing original values
for i, platform in enumerate(df['Platform']):
    fig.add_trace(go.Bar(
        name=platform,
        x=['Build Min/Mo', 'Bandwidth GB', 'Rating (/5)'],
        y=[df.iloc[i]['Build_Norm'], df.iloc[i]['Bandwidth_Norm'], df.iloc[i]['Rating_Norm']],
        marker_color=colors[i],
        cliponaxis=False,
        customdata=[df.iloc[i]['Build Minutes'], df.iloc[i]['Bandwidth GB'], df.iloc[i]['Rating']],
        hovertemplate='<b>%{fullData.name}</b><br>' +
                     'Build Min: %{customdata[0]}<br>' +
                     'Bandwidth: %{customdata[1]} GB<br>' +
                     'Rating: %{customdata[2]}/5<extra></extra>'
    ))

# Update layout
fig.update_layout(
    title='Hosting Platform Comparison',
    xaxis_title='Metrics',
    yaxis_title='Normalized Score',
    barmode='group',
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# Update traces for better display
fig.update_traces(cliponaxis=False)

# Save as both PNG and SVG
fig.write_image('hosting_comparison.png')
fig.write_image('hosting_comparison.svg', format='svg')

fig.show()