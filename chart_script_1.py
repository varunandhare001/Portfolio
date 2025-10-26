import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# Create a hierarchical tree structure with better spacing
fig = go.Figure()

# Define neon colors for better contrast on dark background
neon_colors = {
    0: "#00FFFF",  # Bright cyan for root
    1: "#FF1493",  # Hot pink for main sections  
    2: "#00FF00",  # Bright green for sub-items
    3: "#FFFF00"   # Bright yellow for sub-sub-items
}

# Define node positions in a clear tree structure
nodes = [
    # Root
    {"id": "root", "text": "GTA VI Portfolio", "x": 0, "y": 10, "level": 0, "size": 40},
    
    # Main sections - level 1 (spread horizontally)
    {"id": "hero", "text": "Hero/Landing", "x": -8, "y": 8, "level": 1, "size": 25},
    {"id": "about", "text": "About Me", "x": -6, "y": 8, "level": 1, "size": 25},
    {"id": "resume", "text": "Interactive Resume", "x": -4, "y": 8, "level": 1, "size": 25},
    {"id": "work", "text": "Work Showcase", "x": -2, "y": 8, "level": 1, "size": 25},
    {"id": "projects", "text": "Projects", "x": 0, "y": 8, "level": 1, "size": 25},
    {"id": "proof", "text": "Proof Documents", "x": 2, "y": 8, "level": 1, "size": 25},
    {"id": "insta", "text": "Instagram Feed", "x": 4, "y": 8, "level": 1, "size": 25},
    {"id": "contact", "text": "Contact", "x": 6, "y": 8, "level": 1, "size": 25},
    {"id": "interactive", "text": "Interactive Features", "x": 8, "y": 8, "level": 1, "size": 25},
    
    # Hero/Landing sub-items
    {"id": "hero1", "text": "3D Background", "x": -9, "y": 6, "level": 2, "size": 18},
    {"id": "hero2", "text": "Name Animation", "x": -8, "y": 6, "level": 2, "size": 18},
    {"id": "hero3", "text": "Navigation Cards", "x": -7, "y": 6, "level": 2, "size": 18},
    
    # About Me sub-items
    {"id": "about1", "text": "Bio Text", "x": -7, "y": 6, "level": 2, "size": 18},
    {"id": "about2", "text": "3D Avatar", "x": -6, "y": 6, "level": 2, "size": 18},
    {"id": "about3", "text": "Scroll Animations", "x": -5, "y": 6, "level": 2, "size": 18},
    
    # Interactive Resume sub-items
    {"id": "resume1", "text": "Experience", "x": -5, "y": 6, "level": 2, "size": 18},
    {"id": "resume2", "text": "Education", "x": -4, "y": 6, "level": 2, "size": 18},
    {"id": "resume3", "text": "Skills", "x": -3, "y": 6, "level": 2, "size": 18},
    {"id": "resume4", "text": "Certifications", "x": -4.5, "y": 5, "level": 2, "size": 18},
    {"id": "resume5", "text": "PDF Download", "x": -3.5, "y": 5, "level": 2, "size": 18},
    
    # Work Showcase main categories
    {"id": "video", "text": "Video Editing", "x": -3, "y": 6, "level": 2, "size": 18},
    {"id": "choreo", "text": "Choreography", "x": -2, "y": 6, "level": 2, "size": 18},
    {"id": "script", "text": "Scripting", "x": -1, "y": 6, "level": 2, "size": 18},
    {"id": "thumb", "text": "Thumbnails", "x": -2.5, "y": 5, "level": 2, "size": 18},
    {"id": "tech", "text": "Technical Support", "x": -1.5, "y": 5, "level": 2, "size": 18},
    
    # Video Editing sub-items
    {"id": "video1", "text": "Thumbnail Grid", "x": -3.5, "y": 4, "level": 3, "size": 15},
    {"id": "video2", "text": "Lightbox Modal", "x": -2.5, "y": 4, "level": 3, "size": 15},
    
    # Choreography sub-items
    {"id": "choreo1", "text": "Carousel", "x": -2.5, "y": 4, "level": 3, "size": 15},
    {"id": "choreo2", "text": "Instagram Reels", "x": -1.5, "y": 4, "level": 3, "size": 15},
    
    # Scripting sub-items
    {"id": "script1", "text": "Code Display", "x": -1.5, "y": 4, "level": 3, "size": 15},
    {"id": "script2", "text": "Downloads", "x": -0.5, "y": 4, "level": 3, "size": 15},
    
    # Thumbnails sub-items
    {"id": "thumb1", "text": "Before/After Slider", "x": -2.5, "y": 3.5, "level": 3, "size": 15},
    
    # Technical Support sub-items
    {"id": "tech1", "text": "Network Diagram", "x": -2, "y": 3.5, "level": 3, "size": 15},
    {"id": "tech2", "text": "Certificates", "x": -1, "y": 3.5, "level": 3, "size": 15},
    
    # Projects sub-items
    {"id": "proj1", "text": "Movies on Mood", "x": -0.5, "y": 6, "level": 2, "size": 18},
    {"id": "proj2", "text": "Demo Embed", "x": 0, "y": 6, "level": 2, "size": 18},
    {"id": "proj3", "text": "GitHub Link", "x": 0.5, "y": 6, "level": 2, "size": 18},
    
    # Proof Documents sub-items
    {"id": "proof1", "text": "Certificate Gallery", "x": 1.5, "y": 6, "level": 2, "size": 18},
    {"id": "proof2", "text": "Modal Viewer", "x": 2.5, "y": 6, "level": 2, "size": 18},
    
    # Instagram Feed sub-items
    {"id": "insta1", "text": "Live Feed Widget", "x": 3.5, "y": 6, "level": 2, "size": 18},
    {"id": "insta2", "text": "Follow Button", "x": 4.5, "y": 6, "level": 2, "size": 18},
    
    # Contact sub-items
    {"id": "contact1", "text": "Form", "x": 5.5, "y": 6, "level": 2, "size": 18},
    {"id": "contact2", "text": "Social Links", "x": 6.5, "y": 6, "level": 2, "size": 18},
    
    # Interactive Features sub-items
    {"id": "int1", "text": "Custom Cursor", "x": 7.5, "y": 6, "level": 2, "size": 18},
    {"id": "int2", "text": "Scroll Animations", "x": 8.5, "y": 6, "level": 2, "size": 18},
    {"id": "int3", "text": "Parallax", "x": 7.5, "y": 5, "level": 2, "size": 18},
    {"id": "int4", "text": "Loading Screen", "x": 8.5, "y": 5, "level": 2, "size": 18},
]

# Define connections (parent-child relationships)
connections = [
    # Root to main sections
    ("root", "hero"), ("root", "about"), ("root", "resume"), ("root", "work"), ("root", "projects"),
    ("root", "proof"), ("root", "insta"), ("root", "contact"), ("root", "interactive"),
    
    # Hero/Landing connections
    ("hero", "hero1"), ("hero", "hero2"), ("hero", "hero3"),
    
    # About Me connections
    ("about", "about1"), ("about", "about2"), ("about", "about3"),
    
    # Interactive Resume connections
    ("resume", "resume1"), ("resume", "resume2"), ("resume", "resume3"), ("resume", "resume4"), ("resume", "resume5"),
    
    # Work Showcase connections
    ("work", "video"), ("work", "choreo"), ("work", "script"), ("work", "thumb"), ("work", "tech"),
    
    # Video Editing connections
    ("video", "video1"), ("video", "video2"),
    
    # Choreography connections
    ("choreo", "choreo1"), ("choreo", "choreo2"),
    
    # Scripting connections
    ("script", "script1"), ("script", "script2"),
    
    # Thumbnails connections
    ("thumb", "thumb1"),
    
    # Technical Support connections
    ("tech", "tech1"), ("tech", "tech2"),
    
    # Projects connections
    ("projects", "proj1"), ("projects", "proj2"), ("projects", "proj3"),
    
    # Proof Documents connections
    ("proof", "proof1"), ("proof", "proof2"),
    
    # Instagram Feed connections
    ("insta", "insta1"), ("insta", "insta2"),
    
    # Contact connections
    ("contact", "contact1"), ("contact", "contact2"),
    
    # Interactive Features connections
    ("interactive", "int1"), ("interactive", "int2"), ("interactive", "int3"), ("interactive", "int4"),
]

# Create node lookup dictionary
node_dict = {node["id"]: node for node in nodes}

# Add connection lines with bright neon colors
for parent_id, child_id in connections:
    parent = node_dict[parent_id]
    child = node_dict[child_id]
    
    fig.add_trace(go.Scatter(
        x=[parent["x"], child["x"]],
        y=[parent["y"], child["y"]],
        mode='lines',
        line=dict(color='#00FFFF', width=3),
        showlegend=False,
        hoverinfo='skip'
    ))

# Add nodes with bright neon colors
for node in nodes:
    fig.add_trace(go.Scatter(
        x=[node["x"]],
        y=[node["y"]],
        mode='markers+text',
        marker=dict(
            size=node["size"],
            color=neon_colors[node["level"]],
            line=dict(width=3, color='#FFFFFF')
        ),
        text=node["text"],
        textposition="middle center",
        textfont=dict(size=10, color='#000000', family="Arial Black"),
        showlegend=False,
        hovertemplate=f'<b>{node["text"]}</b><extra></extra>'
    ))

# Update layout for dark theme with neon aesthetic
fig.update_layout(
    title=dict(
        text="GTA VI Portfolio Structure",
        font=dict(size=20, color='#00FFFF', family="Arial Black"),
        x=0.5
    ),
    showlegend=False,
    xaxis=dict(
        showgrid=False, 
        zeroline=False, 
        showticklabels=False,
        range=[-10, 10]
    ),
    yaxis=dict(
        showgrid=False, 
        zeroline=False, 
        showticklabels=False,
        range=[3, 11]
    ),
    plot_bgcolor='#000000',
    paper_bgcolor='#000000'
)

# Save the chart
fig.write_image("portfolio_structure.png")
fig.write_image("portfolio_structure.svg", format="svg")

print("Updated GTA VI portfolio structure flowchart created successfully!")