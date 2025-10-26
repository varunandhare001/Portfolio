
# Let me create a comprehensive data structure for the portfolio website

portfolio_structure = {
    "site_name": "Personal Portfolio - GTA VI Inspired",
    "theme": {
        "colors": {
            "primary": ["#ff006e", "#8338ec", "#3a86ff"],  # Pink, Purple, Blue neons
            "base": ["#000000", "#1a1a1a", "#2d2d2d"],  # Black and grey tones
            "accents": ["#06ffa5", "#ffbe0b", "#fb5607"]  # Additional neon accents
        },
        "fonts": {
            "primary": "Montserrat",
            "fallback": "sans-serif"
        },
        "effects": [
            "3D parallax scrolling",
            "Neon glow effects",
            "Smooth camera movements",
            "Floating panels",
            "Dynamic transitions",
            "Mouse parallax",
            "Interactive cursor glow"
        ]
    },
    "sections": {
        "1_landing_hero": {
            "title": "Landing Page / Hero Section",
            "features": [
                "Cinematic intro animation",
                "3D name/logo reveal",
                "Moving skyline background",
                "Neon reflections",
                "Animated 3D environment",
                "Floating navigation buttons",
                "Tagline: 'Creator | Editor | Choreographer | Engineer | Innovator'"
            ],
            "navigation_buttons": [
                "Video Editing",
                "Choreography",
                "Scripting",
                "Thumbnails",
                "Technical Support",
                "Projects",
                "Resume",
                "Instagram"
            ]
        },
        "2_about_me": {
            "title": "About Me",
            "features": [
                "Animated text reveal",
                "3D rotating avatar/silhouette",
                "Dynamic scrolling layers",
                "Background story",
                "Journey highlights"
            ]
        },
        "3_interactive_resume": {
            "title": "Unfold My Resume",
            "features": [
                "Unfolding/layered animation",
                "Sections: Experience, Education, Skills, Certifications",
                "Futuristic dossier style",
                "PDF download link",
                "Embedded YouTube/Instagram clips",
                "Auto-play videos beside relevant entries"
            ]
        },
        "4_work_experience": {
            "subsections": {
                "video_editing": {
                    "features": [
                        "Grid of YouTube thumbnails",
                        "Expandable floating lightbox",
                        "Software badges (Premiere Pro, After Effects, DaVinci Resolve)"
                    ]
                },
                "choreography": {
                    "features": [
                        "Embedded Instagram reels",
                        "YouTube dance clips",
                        "3D dance silhouettes",
                        "Floating video panels"
                    ]
                },
                "scripting": {
                    "features": [
                        "Code snippets display",
                        "Screenplay-style text layout",
                        "Download/view scripts",
                        "Cinematic scrolling interface"
                    ]
                },
                "thumbnails": {
                    "features": [
                        "Carousel of thumbnail designs",
                        "Hover animations (before/after)"
                    ]
                },
                "technical_support": {
                    "features": [
                        "Company/project list",
                        "Animated network diagram",
                        "Circuit diagram background",
                        "Interactive certificate files",
                        "Modal window for documents"
                    ]
                }
            }
        },
        "5_projects": {
            "title": "Movies on Mood",
            "features": [
                "Dedicated section showcase",
                "Hero graphic",
                "Concept explanation",
                "Live demo embed",
                "GitHub repository link"
            ]
        },
        "6_proof_documents": {
            "title": "Proof Documents",
            "features": [
                "Secure gallery",
                "Embedded file viewer",
                "Certificates display",
                "Client feedback screenshots",
                "Achievements",
                "Hover-to-reveal mechanism",
                "Optional password protection"
            ]
        },
        "7_instagram_integration": {
            "title": "Instagram Feed",
            "features": [
                "Real-time embedded feed",
                "Scrollable carousel",
                "Latest posts display",
                "Follow button with neon hover",
                "Auto-updating content"
            ]
        },
        "8_contact": {
            "title": "Contact Section",
            "features": [
                "Floating holographic contact form",
                "Email, LinkedIn, GitHub, YouTube, Instagram links",
                "Optional chatbot/voice assistant theme",
                "Ask Me Anything feature"
            ]
        }
    },
    "tech_stack": {
        "frontend": {
            "framework": "React or Next.js",
            "3d_library": "Three.js / React Three Fiber",
            "animation": ["GSAP", "Framer Motion"],
            "styling": "Tailwind CSS"
        },
        "hosting": {
            "free_options": [
                {
                    "name": "Vercel",
                    "pros": ["6000 build minutes/month", "Excellent Next.js support", "Automatic HTTPS", "Global CDN"],
                    "cons": ["Limited to 100 sites on free tier"]
                },
                {
                    "name": "Netlify",
                    "pros": ["300 build minutes/month", "Form handling", "Split testing", "Easy deployment"],
                    "cons": ["Fewer build minutes than Vercel"]
                },
                {
                    "name": "GitHub Pages",
                    "pros": ["Completely free", "Easy GitHub integration", "10 builds/hour"],
                    "cons": ["Limited features", "Static only", "No server-side functions"]
                }
            ],
            "recommendation": "Vercel (best for Next.js + React Three Fiber)"
        }
    },
    "optimization": {
        "performance": [
            "Lazy load embedded videos",
            "Mobile-first responsiveness",
            "Compress media files",
            "Code splitting",
            "Asset optimization"
        ]
    },
    "bonus_features": [
        "Smooth section transitions (no hard cuts)",
        "Parallax mouse movement for depth",
        "Interactive neon glow cursor",
        "Animated loading screen ('Loading My Universe...')",
        "Theme toggle (Dark/Neon vs Light/Minimal)",
        "Optional ambient sound/music toggle",
        "Scroll-based animations",
        "3D model interactions"
    ]
}

# Save to CSV for reference
import csv
import json

# Convert to a more readable format
print("Portfolio Website Structure - GTA VI Inspired")
print("=" * 60)
print(f"\nSite Name: {portfolio_structure['site_name']}")
print(f"\nTheme Colors:")
print(f"  Primary: {', '.join(portfolio_structure['theme']['colors']['primary'])}")
print(f"  Base: {', '.join(portfolio_structure['theme']['colors']['base'])}")
print(f"  Accents: {', '.join(portfolio_structure['theme']['colors']['accents'])}")

print(f"\n\nRecommended Tech Stack:")
print(f"  Framework: {portfolio_structure['tech_stack']['frontend']['framework']}")
print(f"  3D Library: {portfolio_structure['tech_stack']['frontend']['3d_library']}")
print(f"  Animation: {', '.join(portfolio_structure['tech_stack']['frontend']['animation'])}")
print(f"  Styling: {portfolio_structure['tech_stack']['frontend']['styling']}")

print(f"\n\nRecommended Hosting: Vercel")
print("  - 6000 build minutes/month")
print("  - Best Next.js support")
print("  - Free SSL & CDN")

print("\n\nWebsite Sections:")
for key, section in portfolio_structure['sections'].items():
    print(f"\n{section['title']}:")
    if 'features' in section:
        for feature in section['features'][:3]:  # Show first 3 features
            print(f"  • {feature}")

print("\n\nData structure created successfully!")
