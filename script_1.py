
# Create comprehensive data for the portfolio website
import json

# Tech stack recommendations
tech_stack_data = {
    "Frontend Framework": ["React with Vite", "Next.js 14+"],
    "3D Graphics": ["Three.js", "React Three Fiber", "@react-three/drei"],
    "Animation Libraries": ["GSAP 3.x with ScrollTrigger", "Framer Motion"],
    "Styling": ["Tailwind CSS", "Styled Components (optional)"],
    "Additional Packages": [
        "react-parallax-mouse",
        "lenis (smooth scroll)",
        "locomotive-scroll (alternative)"
    ]
}

# Color scheme
color_palette = {
    "Neon Colors": {
        "Pink": "#ff006e",
        "Purple": "#8338ec", 
        "Blue": "#3a86ff",
        "Green": "#06ffa5",
        "Yellow": "#ffbe0b",
        "Orange": "#fb5607"
    },
    "Base Colors": {
        "Black": "#000000",
        "Dark Grey": "#1a1a1a",
        "Medium Grey": "#2d2d2d",
        "Light Grey": "#404040"
    }
}

# Section breakdown with implementation details
sections_implementation = {
    "Hero Section": {
        "Components": [
            "3D animated background (Three.js cityscape)",
            "Parallax layers",
            "Floating navigation cards",
            "Name/logo with glitch effect"
        ],
        "Animations": [
            "Camera zoom on load",
            "Text fade-in with stagger",
            "Neon glow pulsing",
            "Particle effects"
        ],
        "Code_Libraries": ["Three.js", "GSAP Timeline", "Framer Motion"]
    },
    "Resume Section": {
        "Components": [
            "Accordion/drawer system",
            "PDF viewer modal",
            "Video embeds (YouTube API)",
            "Timeline visualization"
        ],
        "Animations": [
            "Unfold animation (GSAP)",
            "Scroll-triggered reveals",
            "Smooth transitions"
        ],
        "Integration": ["YouTube Player API", "PDF.js or iframe embed"]
    },
    "Work Showcase": {
        "Video Editing": {
            "Layout": "Masonry grid of thumbnails",
            "Interaction": "Click to open video in lightbox modal",
            "APIs": "YouTube IFrame API"
        },
        "Choreography": {
            "Layout": "Carousel of Instagram reels",
            "Interaction": "Auto-play on scroll into view",
            "APIs": "Instagram oEmbed API"
        },
        "Technical Support": {
            "Layout": "Animated circuit board background",
            "Interaction": "Hover to reveal certificate modals",
            "Visual": "Network diagram with D3.js or SVG animations"
        }
    },
    "Projects Section": {
        "Movies on Mood": {
            "Display": "Hero card with demo embed",
            "Features": ["Live demo iframe", "GitHub link", "Tech stack badges"],
            "Animation": "3D card hover effect"
        }
    },
    "Contact Form": {
        "Style": "Holographic glass morphism",
        "Features": ["FormSpree or EmailJS integration", "Social media icon links"],
        "Animation": "Floating animation with mouse parallax"
    }
}

# Hosting comparison
hosting_comparison = {
    "Vercel": {
        "Build Minutes (Free)": "6000/month",
        "Bandwidth": "100GB",
        "Best For": "Next.js projects",
        "Deployment": "Git push auto-deploy",
        "Custom Domain": "Yes (free SSL)",
        "Rating": "⭐⭐⭐⭐⭐"
    },
    "Netlify": {
        "Build Minutes (Free)": "300/month",
        "Bandwidth": "100GB", 
        "Best For": "Static sites + forms",
        "Deployment": "Git push auto-deploy",
        "Custom Domain": "Yes (free SSL)",
        "Rating": "⭐⭐⭐⭐"
    },
    "GitHub Pages": {
        "Build Minutes (Free)": "10 builds/hour",
        "Bandwidth": "100GB soft limit",
        "Best For": "Simple static portfolios",
        "Deployment": "GitHub Actions",
        "Custom Domain": "Yes (free SSL)",
        "Rating": "⭐⭐⭐"
    }
}

# Key features implementation guide
implementation_guide = {
    "3D Background": {
        "Approach": "React Three Fiber scene with cityscape models",
        "Performance": "Use LOD (Level of Detail) for mobile",
        "Resources": "Free 3D models from Sketchfab or Poly Pizza"
    },
    "Scroll Animations": {
        "Library": "GSAP ScrollTrigger",
        "Pattern": "Pin sections, scrub animations to scroll position",
        "Example": "GTA VI website uses pinned video with scroll sync"
    },
    "Video Lightbox": {
        "Approach": "Modal component with YouTube iframe",
        "Libraries": "React Modal or Headless UI",
        "Features": ["Autoplay on open", "Pause on close", "Keyboard navigation"]
    },
    "Instagram Feed": {
        "Method": "Embed Instagram widget or use Taggbox/Juicer",
        "Free Option": "Instagram oEmbed API (single posts) or ElfSight widget",
        "Auto-Update": "Widget services auto-refresh feeds"
    },
    "Interactive Cursor": {
        "Implementation": "Custom cursor div that follows mouse",
        "Effect": "Radial gradient glow, blend mode: screen",
        "Performance": "Use CSS transform for 60fps smooth movement"
    },
    "Parallax Mouse Effect": {
        "Library": "react-parallax-mouse or vanilla JS",
        "Calculation": "Offset based on mouse distance from center",
        "Layers": "Different speeds for depth illusion"
    },
    "Loading Screen": {
        "Design": "Animated progress bar or 3D spinner",
        "Text": "'Loading My Universe...' or custom tagline",
        "Implementation": "Suspense boundary with loading state"
    }
}

# Create summary
print("=" * 70)
print("GTA VI-INSPIRED PORTFOLIO WEBSITE - TECHNICAL SPECIFICATIONS")
print("=" * 70)

print("\n📦 RECOMMENDED TECH STACK")
print("-" * 70)
for category, items in tech_stack_data.items():
    print(f"\n{category}:")
    for item in items:
        print(f"  • {item}")

print("\n\n🎨 COLOR PALETTE")
print("-" * 70)
for category, colors in color_palette.items():
    print(f"\n{category}:")
    for name, hex_code in colors.items():
        print(f"  {name}: {hex_code}")

print("\n\n🏗️ SECTION IMPLEMENTATION DETAILS")
print("-" * 70)
for section, details in sections_implementation.items():
    print(f"\n{section}:")
    if isinstance(details, dict):
        for key, value in details.items():
            if isinstance(value, list):
                print(f"  {key}: {', '.join(value[:2])}")
            elif isinstance(value, dict):
                print(f"  {key}:")
                for k, v in value.items():
                    print(f"    - {k}: {v}")

print("\n\n🌐 HOSTING COMPARISON")
print("-" * 70)
for host, specs in hosting_comparison.items():
    print(f"\n{host}:")
    for spec, value in specs.items():
        print(f"  {spec}: {value}")

print("\n\n✅ RECOMMENDATION: Use Vercel")
print("  Reasons: Best Next.js support, most build minutes, excellent performance")

print("\n\n💡 KEY IMPLEMENTATION TIPS")
print("-" * 70)
for feature, guide in implementation_guide.items():
    print(f"\n{feature}:")
    for key, value in guide.items():
        print(f"  {key}: {value}")

print("\n" + "=" * 70)
print("Ready to build! All technical specifications compiled.")
print("=" * 70)
