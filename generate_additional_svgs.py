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
    "green": "#4CAF50",
    "orange": "#FF9800",
    "purple": "#9C27B0"
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

# 1. k6 Load Test Stages
create_svg("17-k6-load-stages.svg", "k6 Load Test Stages", f"""
    <g transform="translate(50, 80)">
        <!-- Timeline -->
        <line x1="50" y1="250" x2="700" y2="250" stroke="{COLORS['gray']}" stroke-width="2"/>
        
        <!-- Stage 1: Ramp Up -->
        <rect x="50" y="150" width="100" height="100" fill="{COLORS['light_blue']}" stroke="{COLORS['blue']}"/>
        <text x="100" y="200" font-family="Segoe UI" font-size="12" text-anchor="middle">Ramp Up</text>
        <text x="100" y="220" font-family="Segoe UI" font-size="11" text-anchor="middle">0 → 100 users</text>
        <text x="100" y="270" font-family="Segoe UI" font-size="10" fill="{COLORS['gray']}" text-anchor="middle">2 min</text>
        
        <!-- Stage 2: Sustained Load -->
        <rect x="150" y="100" width="150" height="150" fill="{COLORS['green']}" opacity="0.3" stroke="{COLORS['green']}"/>
        <text x="225" y="175" font-family="Segoe UI" font-size="12" text-anchor="middle">Sustained</text>
        <text x="225" y="195" font-family="Segoe UI" font-size="11" text-anchor="middle">100 users</text>
        <text x="225" y="270" font-family="Segoe UI" font-size="10" fill="{COLORS['gray']}" text-anchor="middle">5 min</text>
        
        <!-- Stage 3: Spike -->
        <rect x="300" y="50" width="100" height="200" fill="{COLORS['orange']}" opacity="0.4" stroke="{COLORS['orange']}"/>
        <text x="350" y="150" font-family="Segoe UI" font-size="12" font-weight="bold" text-anchor="middle">SPIKE</text>
        <text x="350" y="170" font-family="Segoe UI" font-size="11" text-anchor="middle">200 users</text>
        <text x="350" y="270" font-family="Segoe UI" font-size="10" fill="{COLORS['gray']}" text-anchor="middle">2 min</text>
        
        <!-- Stage 4: Recovery -->
        <rect x="400" y="100" width="150" height="150" fill="{COLORS['green']}" opacity="0.3" stroke="{COLORS['green']}"/>
        <text x="475" y="175" font-family="Segoe UI" font-size="12" text-anchor="middle">Recovery</text>
        <text x="475" y="195" font-family="Segoe UI" font-size="11" text-anchor="middle">100 users</text>
        <text x="475" y="270" font-family="Segoe UI" font-size="10" fill="{COLORS['gray']}" text-anchor="middle">5 min</text>
        
        <!-- Stage 5: Ramp Down -->
        <rect x="550" y="150" width="100" height="100" fill="{COLORS['light_blue']}" stroke="{COLORS['blue']}"/>
        <text x="600" y="200" font-family="Segoe UI" font-size="12" text-anchor="middle">Ramp Down</text>
        <text x="600" y="220" font-family="Segoe UI" font-size="11" text-anchor="middle">100 → 0</text>
        <text x="600" y="270" font-family="Segoe UI" font-size="10" fill="{COLORS['gray']}" text-anchor="middle">2 min</text>
        
        <!-- Load Line -->
        <polyline points="50,250 150,150 300,150 300,50 400,50 400,150 550,150 650,250" 
                  fill="none" stroke="{COLORS['blue']}" stroke-width="3"/>
    </g>
""")

# 2. CQRS Architecture
create_svg("14-cqrs-architecture.svg", "CQRS: Separate Read & Write Models", f"""
    <g transform="translate(50, 80)">
        <!-- Client -->
        <rect x="0" y="80" width="100" height="60" rx="5" fill="{COLORS['light_gray']}" stroke="{COLORS['gray']}"/>
        <text x="50" y="115" font-family="Segoe UI" font-size="14" text-anchor="middle">Client</text>
        
        <!-- Commands (Write) -->
        <rect x="200" y="20" width="150" height="80" rx="5" fill="{COLORS['light_blue']}" stroke="{COLORS['blue']}"/>
        <text x="275" y="50" font-family="Segoe UI" font-size="14" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">Write API</text>
        <text x="275" y="70" font-family="Segoe UI" font-size="11" text-anchor="middle">(Commands)</text>
        
        <!-- Queries (Read) -->
        <rect x="200" y="140" width="150" height="80" rx="5" fill="{COLORS['green']}" opacity="0.2" stroke="{COLORS['green']}"/>
        <text x="275" y="170" font-family="Segoe UI" font-size="14" font-weight="bold" fill="{COLORS['green']}" text-anchor="middle">Read API</text>
        <text x="275" y="190" font-family="Segoe UI" font-size="11" text-anchor="middle">(Queries)</text>
        
        <!-- Write DB -->
        <rect x="450" y="20" width="120" height="80" rx="5" fill="white" stroke="{COLORS['blue']}" stroke-width="2"/>
        <text x="510" y="50" font-family="Segoe UI" font-size="12" font-weight="bold" text-anchor="middle">SQL DB</text>
        <text x="510" y="70" font-family="Segoe UI" font-size="10" text-anchor="middle">(Normalized)</text>
        
        <!-- Read DB -->
        <rect x="450" y="140" width="120" height="80" rx="5" fill="white" stroke="{COLORS['green']}" stroke-width="2"/>
        <text x="510" y="170" font-family="Segoe UI" font-size="12" font-weight="bold" text-anchor="middle">Cosmos DB</text>
        <text x="510" y="190" font-family="Segoe UI" font-size="10" text-anchor="middle">(Denormalized)</text>
        
        <!-- Event Bus -->
        <rect x="600" y="80" width="120" height="60" rx="5" fill="{COLORS['orange']}" opacity="0.3" stroke="{COLORS['orange']}"/>
        <text x="660" y="115" font-family="Segoe UI" font-size="12" font-weight="bold" text-anchor="middle">Event Bus</text>
        
        <!-- Arrows -->
        <path d="M 100 110 L 200 60" stroke="{COLORS['blue']}" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
        <path d="M 100 110 L 200 180" stroke="{COLORS['green']}" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
        <path d="M 350 60 L 450 60" stroke="{COLORS['blue']}" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
        <path d="M 350 180 L 450 180" stroke="{COLORS['green']}" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
        <path d="M 570 60 L 600 110" stroke="{COLORS['orange']}" stroke-width="2" fill="none" marker-end="url(#arrow)" stroke-dasharray="4"/>
        <path d="M 660 140 L 570 180" stroke="{COLORS['orange']}" stroke-width="2" fill="none" marker-end="url(#arrow)" stroke-dasharray="4"/>
        
        <!-- Arrow marker -->
        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="{COLORS['gray']}" />
            </marker>
        </defs>
    </g>
""")

# 3. Database Sharding Strategy
create_svg("14-database-sharding.svg", "Database Sharding by Hash", f"""
    <g transform="translate(50, 80)">
        <!-- Application -->
        <rect x="250" y="0" width="200" height="60" rx="5" fill="{COLORS['light_blue']}" stroke="{COLORS['blue']}"/>
        <text x="350" y="35" font-family="Segoe UI" font-size="14" font-weight="bold" text-anchor="middle">Application</text>
        
        <!-- Shard Router -->
        <rect x="250" y="80" width="200" height="50" rx="5" fill="{COLORS['orange']}" opacity="0.3" stroke="{COLORS['orange']}"/>
        <text x="350" y="110" font-family="Segoe UI" font-size="12" font-weight="bold" text-anchor="middle">Shard Router</text>
        <text x="350" y="125" font-family="Segoe UI" font-size="10" text-anchor="middle">hash(userId) % 3</text>
        
        <!-- Shard 1 -->
        <rect x="50" y="180" width="150" height="100" rx="5" fill="white" stroke="{COLORS['blue']}" stroke-width="2"/>
        <text x="125" y="210" font-family="Segoe UI" font-size="14" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">Shard 1</text>
        <text x="125" y="230" font-family="Segoe UI" font-size="11" text-anchor="middle">Users: A-G</text>
        <text x="125" y="250" font-family="Segoe UI" font-size="10" fill="{COLORS['gray']}" text-anchor="middle">db-shard-1</text>
        
        <!-- Shard 2 -->
        <rect x="275" y="180" width="150" height="100" rx="5" fill="white" stroke="{COLORS['blue']}" stroke-width="2"/>
        <text x="350" y="210" font-family="Segoe UI" font-size="14" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">Shard 2</text>
        <text x="350" y="230" font-family="Segoe UI" font-size="11" text-anchor="middle">Users: H-P</text>
        <text x="350" y="250" font-family="Segoe UI" font-size="10" fill="{COLORS['gray']}" text-anchor="middle">db-shard-2</text>
        
        <!-- Shard 3 -->
        <rect x="500" y="180" width="150" height="100" rx="5" fill="white" stroke="{COLORS['blue']}" stroke-width="2"/>
        <text x="575" y="210" font-family="Segoe UI" font-size="14" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">Shard 3</text>
        <text x="575" y="230" font-family="Segoe UI" font-size="11" text-anchor="middle">Users: Q-Z</text>
        <text x="575" y="250" font-family="Segoe UI" font-size="10" fill="{COLORS['gray']}" text-anchor="middle">db-shard-3</text>
        
        <!-- Arrows -->
        <path d="M 350 130 L 125 180" stroke="{COLORS['blue']}" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
        <path d="M 350 130 L 350 180" stroke="{COLORS['blue']}" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
        <path d="M 350 130 L 575 180" stroke="{COLORS['blue']}" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
        
        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="{COLORS['blue']}" />
            </marker>
        </defs>
    </g>
""")

# 4. Cache-Aside Pattern
create_svg("14-cache-aside-pattern.svg", "Cache-Aside (Lazy Loading) Pattern", f"""
    <g transform="translate(50, 80)">
        <!-- Application -->
        <rect x="0" y="80" width="120" height="60" rx="5" fill="{COLORS['light_blue']}" stroke="{COLORS['blue']}"/>
        <text x="60" y="115" font-family="Segoe UI" font-size="14" font-weight="bold" text-anchor="middle">App</text>
        
        <!-- Cache (Redis) -->
        <rect x="250" y="20" width="150" height="80" rx="5" fill="{COLORS['orange']}" opacity="0.2" stroke="{COLORS['orange']}"/>
        <text x="325" y="50" font-family="Segoe UI" font-size="14" font-weight="bold" fill="{COLORS['orange']}" text-anchor="middle">Redis Cache</text>
        <text x="325" y="70" font-family="Segoe UI" font-size="11" text-anchor="middle">In-Memory</text>
        
        <!-- Database -->
        <rect x="250" y="140" width="150" height="80" rx="5" fill="{COLORS['blue']}" opacity="0.2" stroke="{COLORS['blue']}"/>
        <text x="325" y="170" font-family="Segoe UI" font-size="14" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">Database</text>
        <text x="325" y="190" font-family="Segoe UI" font-size="11" text-anchor="middle">Persistent</text>
        
        <!-- Flow Steps -->
        <text x="550" y="40" font-family="Segoe UI" font-size="12" font-weight="bold" fill="{COLORS['text']}">Flow:</text>
        <text x="550" y="65" font-family="Segoe UI" font-size="11" fill="{COLORS['text']}">1. Check cache first</text>
        <text x="550" y="85" font-family="Segoe UI" font-size="11" fill="{COLORS['green']}">2a. Cache HIT → Return</text>
        <text x="550" y="105" font-family="Segoe UI" font-size="11" fill="{COLORS['red']}">2b. Cache MISS:</text>
        <text x="570" y="125" font-family="Segoe UI" font-size="10" fill="{COLORS['text']}">→ Query database</text>
        <text x="570" y="140" font-family="Segoe UI" font-size="10" fill="{COLORS['text']}">→ Store in cache</text>
        <text x="570" y="155" font-family="Segoe UI" font-size="10" fill="{COLORS['text']}">→ Return data</text>
        
        <!-- Arrows -->
        <path d="M 120 110 L 250 60" stroke="{COLORS['orange']}" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
        <text x="180" y="75" font-family="Segoe UI" font-size="10" fill="{COLORS['orange']}">1. Check</text>
        
        <path d="M 120 110 L 250 180" stroke="{COLORS['blue']}" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
        <text x="180" y="155" font-family="Segoe UI" font-size="10" fill="{COLORS['blue']}">2. Query</text>
        
        <path d="M 325 100 L 325 140" stroke="{COLORS['orange']}" stroke-width="2" fill="none" marker-end="url(#arrow)" stroke-dasharray="4"/>
        <text x="340" y="125" font-family="Segoe UI" font-size="10" fill="{COLORS['orange']}">3. Store</text>
        
        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="{COLORS['gray']}" />
            </marker>
        </defs>
    </g>
""")

print("\n✅ All additional SVG diagrams generated successfully!")
