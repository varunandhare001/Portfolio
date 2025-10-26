
import csv

# Create a comprehensive technical specification CSV
tech_specs = [
    ["Category", "Technology/Tool", "Purpose", "Free?", "Link/Resource"],
    
    # Frontend Framework
    ["Framework", "React 18+", "Component-based UI development", "Yes", "react.dev"],
    ["Framework", "Next.js 14+", "React framework with SSR", "Yes", "nextjs.org"],
    ["Build Tool", "Vite", "Fast build tool and dev server", "Yes", "vitejs.dev"],
    
    # 3D & Animation
    ["3D Graphics", "Three.js", "WebGL 3D library", "Yes", "threejs.org"],
    ["3D Graphics", "React Three Fiber", "React renderer for Three.js", "Yes", "docs.pmnd.rs/react-three-fiber"],
    ["3D Graphics", "@react-three/drei", "Useful helpers for R3F", "Yes", "github.com/pmndrs/drei"],
    ["Animation", "GSAP 3.x", "Professional-grade animation library", "Yes (free version)", "greensock.com"],
    ["Animation", "ScrollTrigger", "GSAP plugin for scroll animations", "Yes", "greensock.com/scrolltrigger"],
    ["Animation", "Framer Motion", "React animation library", "Yes", "framer.com/motion"],
    
    # Styling
    ["CSS Framework", "Tailwind CSS", "Utility-first CSS framework", "Yes", "tailwindcss.com"],
    ["CSS Effects", "Custom CSS", "Neon glows, glass morphism, gradients", "N/A", "N/A"],
    
    # Interactive Features
    ["Mouse Effects", "react-parallax-mouse", "Parallax mouse interactions", "Yes", "npmjs.com/package/react-parallax-mouse"],
    ["Smooth Scroll", "Lenis", "Smooth scroll library", "Yes", "github.com/studio-freight/lenis"],
    ["Smooth Scroll", "Locomotive Scroll", "Alternative smooth scroll", "Yes", "locomotivemtl.github.io/locomotive-scroll"],
    
    # Media Integration
    ["Video Embed", "YouTube IFrame API", "Embed YouTube videos", "Yes", "developers.google.com/youtube/iframe_api_reference"],
    ["Instagram Feed", "ElfSight Widget", "Free Instagram feed widget", "Yes (free tier)", "elfsight.com/instagram-feed-instashow"],
    ["Instagram Feed", "Taggbox", "Social media aggregator", "Yes (free tier)", "taggbox.com"],
    ["Instagram Feed", "Juicer", "Instagram feed embedding", "Yes (free tier)", "juicer.io"],
    
    # Form & Contact
    ["Contact Form", "FormSpree", "Form backend service", "Yes (50 submissions/mo)", "formspree.io"],
    ["Contact Form", "EmailJS", "Email sending from JS", "Yes (200 emails/mo)", "emailjs.com"],
    ["Contact Form", "Web3Forms", "Form to email service", "Yes (250 submissions/mo)", "web3forms.com"],
    
    # Analytics
    ["Analytics", "Google Analytics 4", "Website analytics", "Yes", "analytics.google.com"],
    ["Analytics", "Vercel Analytics", "Built-in Vercel analytics", "Yes (basic)", "vercel.com/analytics"],
    ["Performance", "PageSpeed Insights", "Performance testing", "Yes", "pagespeed.web.dev"],
    
    # Hosting Platforms
    ["Hosting", "Vercel", "Recommended - Best for Next.js", "Yes (6000 build min/mo)", "vercel.com"],
    ["Hosting", "Netlify", "Great for static sites", "Yes (300 build min/mo)", "netlify.com"],
    ["Hosting", "GitHub Pages", "Simple static hosting", "Yes", "pages.github.com"],
    ["Hosting", "Cloudflare Pages", "Alternative with good features", "Yes", "pages.cloudflare.com"],
    
    # Image/Asset Optimization
    ["Image Optimization", "TinyPNG", "Image compression", "Yes", "tinypng.com"],
    ["Image Optimization", "Squoosh", "Advanced image compression", "Yes", "squoosh.app"],
    ["Image Optimization", "Cloudinary", "Image CDN and optimization", "Yes (25GB/mo)", "cloudinary.com"],
    
    # Design Resources
    ["Icons", "Font Awesome", "Icon library", "Yes", "fontawesome.com"],
    ["Icons", "Heroicons", "Beautiful hand-crafted SVG icons", "Yes", "heroicons.com"],
    ["Fonts", "Google Fonts", "Free web fonts", "Yes", "fonts.google.com"],
    ["Colors", "Coolors", "Color palette generator", "Yes", "coolors.co"],
    ["Stock Images", "Unsplash", "Free high-quality images", "Yes", "unsplash.com"],
    ["Stock Images", "Pexels", "Free stock photos/videos", "Yes", "pexels.com"],
    ["3D Models", "Sketchfab", "Free 3D models", "Yes (some free)", "sketchfab.com"],
    ["3D Models", "Poly Pizza", "Low-poly 3D models", "Yes", "poly.pizza"],
    
    # Audio
    ["Audio", "Web Audio API", "Browser audio control", "Native", "developer.mozilla.org/docs/Web/API/Web_Audio_API"],
    ["Music", "Incompetech", "Royalty-free music", "Yes (attribution)", "incompetech.com"],
    ["Sound FX", "Freesound", "Free sound effects", "Yes", "freesound.org"],
    
    # Development Tools
    ["Code Editor", "VS Code", "Recommended code editor", "Yes", "code.visualstudio.com"],
    ["Version Control", "Git", "Version control system", "Yes", "git-scm.com"],
    ["Repository", "GitHub", "Code hosting platform", "Yes", "github.com"],
    ["Package Manager", "npm", "Node package manager", "Yes", "npmjs.com"],
    ["Package Manager", "pnpm", "Fast, disk space efficient package manager", "Yes", "pnpm.io"],
    
    # Testing & Debugging
    ["Browser DevTools", "Chrome DevTools", "Browser debugging", "Native", "N/A"],
    ["Responsiveness", "Responsive Design Mode", "Test mobile layouts", "Native", "N/A"],
    ["Accessibility", "Lighthouse", "Performance & accessibility audits", "Native (Chrome)", "N/A"],
    ["Accessibility", "WAVE", "Accessibility evaluation tool", "Yes", "wave.webaim.org"],
    
    # SEO
    ["SEO", "Google Search Console", "Monitor search presence", "Yes", "search.google.com/search-console"],
    ["SEO", "Meta Tags Generator", "Generate social media meta tags", "Yes", "metatags.io"],
    ["SEO", "Schema Markup Generator", "Structured data for SEO", "Yes", "technicalseo.com/tools/schema-markup-generator"],
]

# Write to CSV
filename = 'portfolio-tech-stack-resources.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(tech_specs)

print(f"✅ Created {filename} with {len(tech_specs)-1} resources")
print("\n" + "="*80)
print("COMPREHENSIVE TECH STACK & RESOURCES")
print("="*80)

# Display by category
current_category = ""
for row in tech_specs[1:]:  # Skip header
    if row[0] != current_category:
        current_category = row[0]
        print(f"\n📁 {current_category}")
        print("-"*80)
    
    free_status = "✅ FREE" if row[3] == "Yes" else ("💰 FREE TIER" if "free" in row[3].lower() else "❌ PAID")
    print(f"  • {row[1]:<25} | {free_status:<15} | {row[2]}")

print("\n" + "="*80)
print(f"Total Resources: {len(tech_specs)-1}")
print("All resources compiled and saved to CSV!")
print("="*80)
