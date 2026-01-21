
import os

OUTPUT_DIR = r"d:\Projects - Community\docs\images\azure"
os.makedirs(OUTPUT_DIR, exist_ok=True)

COLORS = {
    "blue": "#0078D4",
    "light_blue": "#E0F2FF",
    "white": "#FFFFFF",
    "gray": "#505050",
    "light_gray": "#F3F2F1",
    "border": "#CCCCCC",
    "text": "#333333",
    "red": "#FF4444",
    "green": "#4CAF50"
}

def create_svg(filename, title, content_svg):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400">
    <!-- Background -->
    <rect width="800" height="400" fill="{COLORS['white']}" />
    <rect width="800" height="400" fill="none" stroke="{COLORS['blue']}" stroke-width="4"/>
    
    <!-- Header -->
    <rect width="800" height="60" fill="{COLORS['blue']}" />
    <text x="400" y="40" font-family="Segoe UI, sans-serif" font-size="24" font-weight="bold" fill="white" text-anchor="middle">{title}</text>
    
    <!-- Content -->
    {content_svg}
    </svg>"""
    
    with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {filename}")

def create_hero_svg(filename, title, subtitle, content_svg):
    svg = f"""<svg width="1080" height="1080" viewBox="0 0 1080 1080" fill="none" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="1080" height="1080" fill="#FAFAFA"/>
      
      <!-- Header -->
      <text x="60" y="80" font-family="system-ui, sans-serif" font-size="14" font-weight="600" letter-spacing="3">
        <tspan fill="{COLORS['blue']}">AZURE</tspan><tspan fill="#232F3E"> CLOUD ENGINEERING</tspan>
      </text>
      
      <!-- Topic Tag -->
      <rect x="60" y="110" width="200" height="36" rx="18" fill="{COLORS['blue']}"/>
      <text x="160" y="134" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#FFFFFF" text-anchor="middle" letter-spacing="2">NETWORKING</text>
      
      <!-- Title -->
      <text x="60" y="220" font-family="system-ui, sans-serif" font-size="48" font-weight="800" fill="#232F3E">{title.split(' ')[0]}</text>
      <text x="60" y="280" font-family="system-ui, sans-serif" font-size="48" font-weight="800" fill="{COLORS['blue']}">{title.split(' ', 1)[1]}</text>
      
      <!-- Subtitle -->
      <text x="60" y="330" font-family="system-ui, sans-serif" font-size="18" fill="#6B7280">{subtitle}</text>
      
      <!-- Main Diagram Area -->
      <rect x="60" y="360" width="960" height="400" rx="16" fill="#EFF6FF"/>
      
      <!-- Content Injection (Scaled/Translated to fit 960x400 box starting at 60,360) -->
      <g transform="translate(60, 360)">
        {content_svg}
      </g>
      
      <!-- Footer -->
      <text x="540" y="1040" font-family="system-ui, sans-serif" font-size="14" fill="#9CA3AF" text-anchor="middle">@devweekends</text>
    </svg>"""
    
    with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated Hero {filename}")

# 1. Header 3a: 03a-networking-fundamentals.svg
create_hero_svg("03a-networking-fundamentals.svg", "Networking Fundamentals", "Subnets, CIDR, Peering, and Security", f"""
    <g transform="translate(180, 50)">
        <rect x="0" y="0" width="200" height="200" rx="10" fill="{COLORS['light_blue']}" stroke="{COLORS['blue']}" stroke-width="2"/>
        <text x="100" y="30" font-family="Segoe UI" font-size="16" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">VNet A</text>
        <text x="100" y="100" font-family="Segoe UI" font-size="14" fill="{COLORS['text']}" text-anchor="middle">10.0.0.0/16</text>
        
        <rect x="400" y="0" width="200" height="200" rx="10" fill="{COLORS['light_blue']}" stroke="{COLORS['blue']}" stroke-width="2"/>
        <text x="500" y="30" font-family="Segoe UI" font-size="16" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">VNet B</text>
        <text x="500" y="100" font-family="Segoe UI" font-size="14" fill="{COLORS['text']}" text-anchor="middle">10.1.0.0/16</text>
        
        <!-- Peering -->
        <line x1="200" y1="100" x2="400" y2="100" stroke="{COLORS['green']}" stroke-width="4" stroke-dasharray="10 5"/>
        <text x="300" y="90" font-family="Segoe UI" font-size="12" fill="{COLORS['green']}" text-anchor="middle">VNet Peering</text>
        
        <rect x="40" y="140" width="120" height="40" rx="5" fill="white" stroke="{COLORS['gray']}"/>
        <text x="100" y="165" font-family="Segoe UI" font-size="12" fill="{COLORS['text']}" text-anchor="middle">Subnet A (Web)</text>
        
        <rect x="440" y="140" width="120" height="40" rx="5" fill="white" stroke="{COLORS['gray']}"/>
        <text x="500" y="165" font-family="Segoe UI" font-size="12" fill="{COLORS['text']}" text-anchor="middle">Subnet B (DB)</text>
    </g>
""")

# 2. Content 3a: 03a-nsg-vs-asg.svg
create_svg("03a-nsg-vs-asg.svg", "NSG vs ASG: Simplifying Security", f"""
    <g transform="translate(50, 80)">
        <!-- Traditional NSG -->
        <text x="150" y="30" font-family="Segoe UI" font-size="16" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">Traditional NSG</text>
        <rect x="50" y="50" width="200" height="200" rx="5" fill="{COLORS['light_gray']}" stroke="{COLORS['border']}"/>
        <text x="150" y="100" font-family="Segoe UI" font-size="12" fill="{COLORS['text']}" text-anchor="middle">Rules:</text>
        <text x="150" y="130" font-family="Segoe UI" font-size="11" fill="{COLORS['text']}" text-anchor="middle">Allow 10.0.0.4:80</text>
        <text x="150" y="150" font-family="Segoe UI" font-size="11" fill="{COLORS['text']}" text-anchor="middle">Allow 10.0.0.5:80</text>
        <text x="150" y="170" font-family="Segoe UI" font-size="11" fill="{COLORS['text']}" text-anchor="middle">Allow 10.0.0.6:80</text>

        <!-- With ASG -->
        <text x="550" y="30" font-family="Segoe UI" font-size="16" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">With ASG</text>
        <rect x="450" y="50" width="200" height="200" rx="5" fill="{COLORS['light_blue']}" stroke="{COLORS['blue']}"/>
        
        <rect x="470" y="140" width="160" height="90" rx="5" fill="white" stroke="{COLORS['blue']}" stroke-dasharray="4"/>
        <text x="550" y="130" font-family="Segoe UI" font-size="12" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">ASG: "WebServers"</text>
        
        <circle cx="500" cy="180" r="15" fill="{COLORS['gray']}" />
        <circle cx="550" cy="180" r="15" fill="{COLORS['gray']}" />
        <circle cx="600" cy="180" r="15" fill="{COLORS['gray']}" />
        
        <text x="550" y="80" font-family="Segoe UI" font-size="12" fill="{COLORS['text']}" text-anchor="middle">Rule: Allow Port 80 to</text>
        <text x="550" y="100" font-family="Segoe UI" font-size="12" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">"WebServers"</text>
    </g>
""")

# 3. Content 3a: 03a-privatelink-flow.svg
create_svg("03a-privatelink-flow.svg", "Private Link Traffic Flow", f"""
    <g transform="translate(50, 100)">
        <!-- On-Prem -->
        <rect x="0" y="50" width="120" height="100" fill="#EFEFEF" stroke="#999" />
        <text x="60" y="105" font-family="Segoe UI" font-size="14" text-anchor="middle">On-Premises</text>
        
        <!-- VPN -->
        <line x1="120" y1="100" x2="200" y2="100" stroke="{COLORS['gray']}" stroke-width="4" stroke-dasharray="4"/>
        <text x="160" y="90" font-family="Segoe UI" font-size="10" text-anchor="middle">VPN</text>
        
        <!-- VNet -->
        <rect x="200" y="0" width="300" height="200" fill="{COLORS['light_blue']}" stroke="{COLORS['blue']}" />
        <text x="350" y="30" font-family="Segoe UI" font-size="14" fill="{COLORS['blue']}" text-anchor="middle">Azure VNet</text>
        
        <!-- Private Endpoint -->
        <rect x="380" y="80" width="100" height="50" rx="5" fill="{COLORS['green']}" />
        <text x="430" y="110" font-family="Segoe UI" font-size="12" fill="white" text-anchor="middle">Private Endpoint</text>
        <text x="430" y="125" font-family="Segoe UI" font-size="10" fill="white" text-anchor="middle">10.0.1.5</text>
        
        <!-- Flow Line -->
        <path d="M 120 100 L 380 105" stroke="{COLORS['green']}" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
        
        <!-- PaaS Service -->
        <rect x="550" y="50" width="150" height="100" fill="white" stroke="{COLORS['blue']}" stroke-width="2"/>
        <text x="625" y="90" font-family="Segoe UI" font-size="14" text-anchor="middle">Azure SQL</text>
        <text x="625" y="110" font-family="Segoe UI" font-size="10" fill="red" text-anchor="middle">Public Access: OFF</text>
        
        <!-- Link -->
        <line x1="480" y1="105" x2="550" y2="100" stroke="{COLORS['blue']}" stroke-width="2" />
    </g>
""")

# 4. Header 3b: 03b-hybrid-connectivity.svg
create_hero_svg("03b-hybrid-connectivity.svg", "Hybrid Connectivity", "VPN, ExpressRoute, and Virtual WAN", f"""
    <g transform="translate(130, 50)">
        <!-- VPN -->
        <g transform="translate(0, 0)">
            <rect x="0" y="0" width="300" height="250" rx="10" fill="white" stroke="{COLORS['gray']}" stroke-width="2"/>
            <rect x="0" y="0" width="300" height="40" rx="10" fill="{COLORS['gray']}" />
            <text x="150" y="28" font-family="Segoe UI" font-size="18" fill="white" text-anchor="middle">VPN Gateway</text>
            
            <text x="150" y="80" font-family="Segoe UI" font-size="14" text-anchor="middle">Encryption over Internet</text>
            <text x="150" y="120" font-family="Segoe UI" font-size="60" text-anchor="middle">🔒</text>
            <text x="150" y="180" font-family="Segoe UI" font-size="14" text-anchor="middle">Up to 10 Gbps</text>
        </g>
        
        <!-- ExpressRoute -->
        <g transform="translate(400, 0)">
            <rect x="0" y="0" width="300" height="250" rx="10" fill="white" stroke="{COLORS['blue']}" stroke-width="3"/>
            <rect x="0" y="0" width="300" height="40" rx="10" fill="{COLORS['blue']}" />
            <text x="150" y="28" font-family="Segoe UI" font-size="18" fill="white" text-anchor="middle">ExpressRoute</text>
            
            <text x="150" y="80" font-family="Segoe UI" font-size="14" text-anchor="middle">Private Dedicated Fiber</text>
            <text x="150" y="120" font-family="Segoe UI" font-size="60" text-anchor="middle">🚄</text>
            <text x="150" y="180" font-family="Segoe UI" font-size="14" text-anchor="middle">Up to 100 Gbps</text>
        </g>
    </g>
""")

# 5. Content 3b: 03b-virtual-wan.svg (Small)
create_svg("03b-virtual-wan.svg", "Virtual WAN Hub Architecture", f"""
    <g transform="translate(100, 60)">
        <!-- Hub -->
        <circle cx="300" cy="150" r="80" fill="{COLORS['light_blue']}" stroke="{COLORS['blue']}" stroke-width="3" />
        <text x="300" y="140" font-family="Segoe UI" font-size="16" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">Virtual WAN</text>
        <text x="300" y="160" font-family="Segoe UI" font-size="14" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">HUB</text>
        
        <!-- Spokes -->
        <circle cx="100" cy="50" r="40" fill="white" stroke="{COLORS['gray']}" />
        <text x="100" y="55" font-family="Segoe UI" font-size="12" text-anchor="middle">Branch</text>
        <line x1="135" y1="65" x2="230" y2="110" stroke="{COLORS['gray']}" stroke-width="2" stroke-dasharray="4"/>
        
        <circle cx="500" cy="50" r="40" fill="white" stroke="{COLORS['gray']}" />
        <text x="500" y="55" font-family="Segoe UI" font-size="12" text-anchor="middle">VNet 1</text>
        <line x1="465" y1="65" x2="370" y2="110" stroke="{COLORS['blue']}" stroke-width="2" />
        
        <circle cx="100" cy="250" r="40" fill="white" stroke="{COLORS['gray']}" />
        <text x="100" y="255" font-family="Segoe UI" font-size="12" text-anchor="middle">Remote User</text>
        <line x1="135" y1="235" x2="230" y2="190" stroke="{COLORS['gray']}" stroke-width="2" stroke-dasharray="4"/>
        
        <circle cx="500" cy="250" r="40" fill="white" stroke="{COLORS['gray']}" />
        <text x="500" y="255" font-family="Segoe UI" font-size="12" text-anchor="middle">VNet 2</text>
        <line x1="465" y1="235" x2="370" y2="190" stroke="{COLORS['blue']}" stroke-width="2" />
    </g>
""")

# 6. Header 3c: 03c-load-balancing-tree.svg
create_hero_svg("03c-load-balancing-tree.svg", "Traffic Management", "Load Balancing Decision Tree", f"""
    <g transform="translate(130, 50)">
        
        <text x="350" y="20" font-family="Segoe UI" font-size="20" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">Is your application Global or Regional?</text>
        
        <!-- GLOBAL -->
        <rect x="50" y="50" width="300" height="200" rx="10" fill="{COLORS['light_blue']}" stroke="{COLORS['blue']}" />
        <text x="200" y="80" font-family="Segoe UI" font-size="16" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">GLOBAL</text>
        
        <line x1="200" y1="90" x2="100" y2="150" stroke="{COLORS['blue']}" stroke-width="2"/>
        <line x1="200" y1="90" x2="300" y2="150" stroke="{COLORS['blue']}" stroke-width="2"/>
        
        <rect x="50" y="150" width="100" height="50" rx="5" fill="white" stroke="{COLORS['blue']}"/>
        <text x="100" y="180" font-family="Segoe UI" font-size="14" font-weight="bold" text-anchor="middle">Front Door</text>
        
        <rect x="250" y="150" width="100" height="50" rx="5" fill="white" stroke="{COLORS['gray']}"/>
        <text x="300" y="180" font-family="Segoe UI" font-size="14" text-anchor="middle">Traffic Mgr</text>
        
        <!-- REGIONAL -->
        <rect x="400" y="50" width="300" height="200" rx="10" fill="{COLORS['light_gray']}" stroke="{COLORS['gray']}" />
        <text x="550" y="80" font-family="Segoe UI" font-size="16" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">REGIONAL</text>
        
        <line x1="550" y1="90" x2="450" y2="150" stroke="{COLORS['gray']}" stroke-width="2"/>
        <line x1="550" y1="90" x2="650" y2="150" stroke="{COLORS['gray']}" stroke-width="2"/>
        
        <rect x="400" y="150" width="100" height="50" rx="5" fill="white" stroke="{COLORS['blue']}"/>
        <text x="450" y="180" font-family="Segoe UI" font-size="14" font-weight="bold" text-anchor="middle">App Gateway</text>
        
        <rect x="600" y="150" width="100" height="50" rx="5" fill="white" stroke="{COLORS['gray']}"/>
        <text x="650" y="180" font-family="Segoe UI" font-size="14" text-anchor="middle">Load Balancer</text>
    </g>
""")
