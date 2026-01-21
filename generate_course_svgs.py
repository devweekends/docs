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
    "red": "#FF5252",
    "green": "#4CAF50",
    "orange": "#FF9800",
    "purple": "#9C27B0",
    "teal": "#009688"
}

def create_svg(filename, title, content_svg, height=400):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 {height}">
    <!-- Background -->
    <rect width="800" height="{height}" fill="{COLORS['white']}" />
    <rect width="800" height="{height}" fill="none" stroke="{COLORS['blue']}" stroke-width="4"/>
    
    <!-- Header -->
    <rect width="800" height="60" fill="{COLORS['blue']}" />
    <text x="400" y="40" font-family="Segoe UI, sans-serif" font-size="22" font-weight="bold" fill="white" text-anchor="middle">{title}</text>
    
    <!-- Content -->
    {content_svg}
    
    <!-- Footer -->
    <text x="400" y="{height - 10}" font-family="Segoe UI, sans-serif" font-size="10" fill="{COLORS['gray']}" text-anchor="middle">@devweekends</text>
    </svg>"""
    
    with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {filename}")

# =============================================================================
# CHAPTER 07: AKS DIAGRAMS
# =============================================================================

# 1. Helm Architecture
create_svg("07-helm-architecture.svg", "Helm: Kubernetes Package Manager", f"""
    <g transform="translate(50, 80)">
        <!-- Helm Chart Box -->
        <rect x="50" y="20" width="250" height="200" rx="10" fill="{COLORS['light_blue']}" stroke="{COLORS['blue']}" stroke-width="2"/>
        <text x="175" y="50" font-family="Segoe UI" font-size="16" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">Helm Chart</text>
        
        <!-- Chart.yaml -->
        <rect x="70" y="70" width="90" height="50" rx="5" fill="white" stroke="{COLORS['gray']}"/>
        <text x="115" y="100" font-family="Segoe UI" font-size="11" text-anchor="middle">Chart.yaml</text>
        
        <!-- values.yaml -->
        <rect x="180" y="70" width="100" height="50" rx="5" fill="white" stroke="{COLORS['gray']}"/>
        <text x="230" y="100" font-family="Segoe UI" font-size="11" text-anchor="middle">values.yaml</text>
        
        <!-- templates/ -->
        <rect x="70" y="140" width="210" height="60" rx="5" fill="white" stroke="{COLORS['blue']}"/>
        <text x="175" y="160" font-family="Segoe UI" font-size="11" font-weight="bold" text-anchor="middle">templates/</text>
        <text x="175" y="180" font-family="Segoe UI" font-size="10" fill="{COLORS['gray']}" text-anchor="middle">deployment.yaml, service.yaml</text>
        
        <!-- Arrow -->
        <path d="M 300 120 L 380 120" stroke="{COLORS['blue']}" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
        <text x="340" y="110" font-family="Segoe UI" font-size="11" fill="{COLORS['blue']}" text-anchor="middle">helm install</text>
        
        <!-- Kubernetes Cluster -->
        <rect x="400" y="20" width="300" height="200" rx="10" fill="{COLORS['light_gray']}" stroke="{COLORS['gray']}" stroke-width="2"/>
        <text x="550" y="50" font-family="Segoe UI" font-size="16" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">Kubernetes Cluster</text>
        
        <!-- Resources -->
        <rect x="420" y="70" width="80" height="40" rx="5" fill="{COLORS['green']}" opacity="0.3" stroke="{COLORS['green']}"/>
        <text x="460" y="95" font-family="Segoe UI" font-size="11" text-anchor="middle">Deployment</text>
        
        <rect x="520" y="70" width="80" height="40" rx="5" fill="{COLORS['blue']}" opacity="0.3" stroke="{COLORS['blue']}"/>
        <text x="560" y="95" font-family="Segoe UI" font-size="11" text-anchor="middle">Service</text>
        
        <rect x="620" y="70" width="60" height="40" rx="5" fill="{COLORS['orange']}" opacity="0.3" stroke="{COLORS['orange']}"/>
        <text x="650" y="95" font-family="Segoe UI" font-size="11" text-anchor="middle">Ingress</text>
        
        <!-- Pods -->
        <circle cx="450" cy="160" r="25" fill="{COLORS['green']}" opacity="0.6"/>
        <text x="450" y="165" font-family="Segoe UI" font-size="10" fill="white" text-anchor="middle">Pod 1</text>
        
        <circle cx="530" cy="160" r="25" fill="{COLORS['green']}" opacity="0.6"/>
        <text x="530" y="165" font-family="Segoe UI" font-size="10" fill="white" text-anchor="middle">Pod 2</text>
        
        <circle cx="610" cy="160" r="25" fill="{COLORS['green']}" opacity="0.6"/>
        <text x="610" y="165" font-family="Segoe UI" font-size="10" fill="white" text-anchor="middle">Pod 3</text>
        
        <!-- Arrow marker -->
        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="{COLORS['blue']}" />
            </marker>
        </defs>
        
        <!-- Benefits -->
        <text x="175" y="260" font-family="Segoe UI" font-size="12" fill="{COLORS['text']}" text-anchor="middle">✓ Reusable</text>
        <text x="175" y="280" font-family="Segoe UI" font-size="12" fill="{COLORS['text']}" text-anchor="middle">✓ Versioned</text>
        <text x="550" y="260" font-family="Segoe UI" font-size="12" fill="{COLORS['text']}" text-anchor="middle">✓ Easy Rollback</text>
        <text x="550" y="280" font-family="Segoe UI" font-size="12" fill="{COLORS['text']}" text-anchor="middle">✓ Multi-env</text>
    </g>
""")

# 2. GitOps with ArgoCD
create_svg("07-gitops-argocd.svg", "GitOps: Git as Single Source of Truth", f"""
    <g transform="translate(50, 80)">
        <!-- Git Repository -->
        <rect x="20" y="50" width="180" height="150" rx="10" fill="{COLORS['light_gray']}" stroke="{COLORS['gray']}" stroke-width="2"/>
        <text x="110" y="80" font-family="Segoe UI" font-size="14" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">Git Repository</text>
        <text x="110" y="100" font-family="Segoe UI" font-size="11" fill="{COLORS['gray']}" text-anchor="middle">(Source of Truth)</text>
        
        <!-- Files in Git -->
        <rect x="40" y="120" width="140" height="60" rx="5" fill="white" stroke="{COLORS['gray']}"/>
        <text x="110" y="145" font-family="Segoe UI" font-size="10" text-anchor="middle">deployment.yaml</text>
        <text x="110" y="165" font-family="Segoe UI" font-size="10" text-anchor="middle">service.yaml</text>
        
        <!-- Arrow Git to ArgoCD -->
        <path d="M 200 125 L 280 125" stroke="{COLORS['blue']}" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
        <text x="240" y="115" font-family="Segoe UI" font-size="10" fill="{COLORS['blue']}" text-anchor="middle">Watch</text>
        
        <!-- ArgoCD -->
        <rect x="280" y="50" width="180" height="150" rx="10" fill="{COLORS['light_blue']}" stroke="{COLORS['blue']}" stroke-width="2"/>
        <text x="370" y="80" font-family="Segoe UI" font-size="14" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">ArgoCD</text>
        <text x="370" y="100" font-family="Segoe UI" font-size="11" fill="{COLORS['gray']}" text-anchor="middle">(GitOps Controller)</text>
        
        <rect x="300" y="120" width="140" height="60" rx="5" fill="white" stroke="{COLORS['blue']}"/>
        <text x="370" y="145" font-family="Segoe UI" font-size="10" text-anchor="middle">Detect Changes</text>
        <text x="370" y="165" font-family="Segoe UI" font-size="10" text-anchor="middle">Auto-Sync</text>
        
        <!-- Arrow ArgoCD to Cluster -->
        <path d="M 460 125 L 540 125" stroke="{COLORS['green']}" stroke-width="2" fill="none" marker-end="url(#arrow2)"/>
        <text x="500" y="115" font-family="Segoe UI" font-size="10" fill="{COLORS['green']}" text-anchor="middle">Deploy</text>
        
        <!-- Kubernetes Cluster -->
        <rect x="540" y="50" width="180" height="150" rx="10" fill="{COLORS['green']}" opacity="0.1" stroke="{COLORS['green']}" stroke-width="2"/>
        <text x="630" y="80" font-family="Segoe UI" font-size="14" font-weight="bold" fill="{COLORS['green']}" text-anchor="middle">Kubernetes</text>
        <text x="630" y="100" font-family="Segoe UI" font-size="11" fill="{COLORS['gray']}" text-anchor="middle">(Desired State)</text>
        
        <circle cx="590" cy="155" r="20" fill="{COLORS['green']}" opacity="0.5"/>
        <circle cx="630" cy="155" r="20" fill="{COLORS['green']}" opacity="0.5"/>
        <circle cx="670" cy="155" r="20" fill="{COLORS['green']}" opacity="0.5"/>
        
        <!-- Workflow Steps -->
        <text x="110" y="240" font-family="Segoe UI" font-size="11" fill="{COLORS['text']}" text-anchor="middle">1. Developer pushes</text>
        <text x="370" y="240" font-family="Segoe UI" font-size="11" fill="{COLORS['text']}" text-anchor="middle">2. ArgoCD syncs</text>
        <text x="630" y="240" font-family="Segoe UI" font-size="11" fill="{COLORS['text']}" text-anchor="middle">3. Cluster updated</text>
        
        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="{COLORS['blue']}" />
            </marker>
            <marker id="arrow2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="{COLORS['green']}" />
            </marker>
        </defs>
    </g>
""")

# 3. Service Mesh (Istio)
create_svg("07-service-mesh-istio.svg", "Service Mesh: Istio Architecture", f"""
    <g transform="translate(50, 80)">
        <!-- Istio Control Plane -->
        <rect x="200" y="10" width="300" height="60" rx="10" fill="{COLORS['purple']}" opacity="0.2" stroke="{COLORS['purple']}" stroke-width="2"/>
        <text x="350" y="45" font-family="Segoe UI" font-size="14" font-weight="bold" fill="{COLORS['purple']}" text-anchor="middle">Istio Control Plane (istiod)</text>
        
        <!-- Arrows from Control Plane -->
        <line x1="300" y1="70" x2="175" y2="120" stroke="{COLORS['purple']}" stroke-width="1" stroke-dasharray="4"/>
        <line x1="350" y1="70" x2="350" y2="120" stroke="{COLORS['purple']}" stroke-width="1" stroke-dasharray="4"/>
        <line x1="400" y1="70" x2="525" y2="120" stroke="{COLORS['purple']}" stroke-width="1" stroke-dasharray="4"/>
        
        <!-- Pod A -->
        <rect x="75" y="120" width="200" height="130" rx="10" fill="{COLORS['light_blue']}" stroke="{COLORS['blue']}" stroke-width="2"/>
        <text x="175" y="145" font-family="Segoe UI" font-size="12" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">Pod A</text>
        
        <rect x="90" y="160" width="80" height="40" rx="5" fill="white" stroke="{COLORS['gray']}"/>
        <text x="130" y="185" font-family="Segoe UI" font-size="10" text-anchor="middle">App Container</text>
        
        <rect x="180" y="160" width="80" height="40" rx="5" fill="{COLORS['teal']}" opacity="0.3" stroke="{COLORS['teal']}"/>
        <text x="220" y="185" font-family="Segoe UI" font-size="10" text-anchor="middle">Envoy Sidecar</text>
        
        <!-- Pod B -->
        <rect x="425" y="120" width="200" height="130" rx="10" fill="{COLORS['light_blue']}" stroke="{COLORS['blue']}" stroke-width="2"/>
        <text x="525" y="145" font-family="Segoe UI" font-size="12" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">Pod B</text>
        
        <rect x="440" y="160" width="80" height="40" rx="5" fill="white" stroke="{COLORS['gray']}"/>
        <text x="480" y="185" font-family="Segoe UI" font-size="10" text-anchor="middle">App Container</text>
        
        <rect x="530" y="160" width="80" height="40" rx="5" fill="{COLORS['teal']}" opacity="0.3" stroke="{COLORS['teal']}"/>
        <text x="570" y="185" font-family="Segoe UI" font-size="10" text-anchor="middle">Envoy Sidecar</text>
        
        <!-- Traffic Flow -->
        <path d="M 260 180 L 440 180" stroke="{COLORS['green']}" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
        <text x="350" y="170" font-family="Segoe UI" font-size="10" fill="{COLORS['green']}" text-anchor="middle">mTLS Traffic</text>
        
        <!-- Features -->
        <text x="100" y="285" font-family="Segoe UI" font-size="11" fill="{COLORS['text']}">✓ Traffic Management</text>
        <text x="280" y="285" font-family="Segoe UI" font-size="11" fill="{COLORS['text']}">✓ Security (mTLS)</text>
        <text x="500" y="285" font-family="Segoe UI" font-size="11" fill="{COLORS['text']}">✓ Observability</text>
        
        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="{COLORS['green']}" />
            </marker>
        </defs>
    </g>
""")

# 4. KEDA Event-Driven Autoscaling
create_svg("07-keda-autoscaling.svg", "KEDA: Event-Driven Autoscaling", f"""
    <g transform="translate(50, 80)">
        <!-- Event Source -->
        <rect x="30" y="70" width="180" height="120" rx="10" fill="{COLORS['orange']}" opacity="0.2" stroke="{COLORS['orange']}" stroke-width="2"/>
        <text x="120" y="100" font-family="Segoe UI" font-size="14" font-weight="bold" fill="{COLORS['orange']}" text-anchor="middle">Event Source</text>
        
        <!-- Queue visualization -->
        <rect x="50" y="120" width="140" height="50" rx="5" fill="white" stroke="{COLORS['orange']}"/>
        <text x="120" y="145" font-family="Segoe UI" font-size="11" text-anchor="middle">Service Bus Queue</text>
        <text x="120" y="160" font-family="Segoe UI" font-size="10" fill="{COLORS['gray']}" text-anchor="middle">50 messages</text>
        
        <!-- Arrow to KEDA -->
        <path d="M 210 130 L 280 130" stroke="{COLORS['blue']}" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
        <text x="245" y="120" font-family="Segoe UI" font-size="10" fill="{COLORS['blue']}" text-anchor="middle">Metrics</text>
        
        <!-- KEDA -->
        <rect x="280" y="70" width="180" height="120" rx="10" fill="{COLORS['light_blue']}" stroke="{COLORS['blue']}" stroke-width="2"/>
        <text x="370" y="100" font-family="Segoe UI" font-size="14" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">KEDA</text>
        <text x="370" y="125" font-family="Segoe UI" font-size="10" text-anchor="middle">ScaledObject</text>
        <text x="370" y="145" font-family="Segoe UI" font-size="10" fill="{COLORS['gray']}" text-anchor="middle">messageCount: 10</text>
        <text x="370" y="165" font-family="Segoe UI" font-size="10" fill="{COLORS['gray']}" text-anchor="middle">min: 1, max: 20</text>
        
        <!-- Arrow to Pods -->
        <path d="M 460 130 L 530 130" stroke="{COLORS['green']}" stroke-width="2" fill="none" marker-end="url(#arrow2)"/>
        <text x="495" y="120" font-family="Segoe UI" font-size="10" fill="{COLORS['green']}" text-anchor="middle">Scale</text>
        
        <!-- Pods (scaling) -->
        <rect x="530" y="70" width="180" height="120" rx="10" fill="{COLORS['green']}" opacity="0.1" stroke="{COLORS['green']}" stroke-width="2"/>
        <text x="620" y="100" font-family="Segoe UI" font-size="14" font-weight="bold" fill="{COLORS['green']}" text-anchor="middle">Deployment</text>
        
        <circle cx="560" cy="145" r="18" fill="{COLORS['green']}" opacity="0.6"/>
        <circle cx="595" cy="145" r="18" fill="{COLORS['green']}" opacity="0.6"/>
        <circle cx="630" cy="145" r="18" fill="{COLORS['green']}" opacity="0.6"/>
        <circle cx="665" cy="145" r="18" fill="{COLORS['green']}" opacity="0.6"/>
        <circle cx="700" cy="145" r="18" fill="{COLORS['green']}" opacity="0.6"/>
        
        <text x="620" y="180" font-family="Segoe UI" font-size="10" fill="{COLORS['text']}" text-anchor="middle">5 pods (50/10)</text>
        
        <!-- Formula -->
        <text x="350" y="230" font-family="Segoe UI" font-size="12" fill="{COLORS['text']}" text-anchor="middle">50 messages ÷ 10 per pod = 5 pods</text>
        <text x="350" y="255" font-family="Segoe UI" font-size="11" fill="{COLORS['gray']}" text-anchor="middle">Scales to 0 when queue is empty!</text>
        
        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="{COLORS['blue']}" />
            </marker>
            <marker id="arrow2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="{COLORS['green']}" />
            </marker>
        </defs>
    </g>
""")

# =============================================================================
# CHAPTER 12: COST OPTIMIZATION DIAGRAMS
# =============================================================================

# 5. FinOps Lifecycle
create_svg("12-finops-lifecycle.svg", "FinOps Lifecycle: Inform, Optimize, Operate", f"""
    <g transform="translate(50, 80)">
        <!-- Inform Phase -->
        <circle cx="150" cy="120" r="70" fill="{COLORS['blue']}" opacity="0.2" stroke="{COLORS['blue']}" stroke-width="3"/>
        <text x="150" y="110" font-family="Segoe UI" font-size="16" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">INFORM</text>
        <text x="150" y="135" font-family="Segoe UI" font-size="11" text-anchor="middle">Visibility</text>
        <text x="150" y="150" font-family="Segoe UI" font-size="11" text-anchor="middle">Allocation</text>
        
        <!-- Arrow 1 -->
        <path d="M 220 100 Q 280 60 340 100" stroke="{COLORS['gray']}" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
        
        <!-- Optimize Phase -->
        <circle cx="400" cy="120" r="70" fill="{COLORS['green']}" opacity="0.2" stroke="{COLORS['green']}" stroke-width="3"/>
        <text x="400" y="110" font-family="Segoe UI" font-size="16" font-weight="bold" fill="{COLORS['green']}" text-anchor="middle">OPTIMIZE</text>
        <text x="400" y="135" font-family="Segoe UI" font-size="11" text-anchor="middle">Right-size</text>
        <text x="400" y="150" font-family="Segoe UI" font-size="11" text-anchor="middle">Reserved Instances</text>
        
        <!-- Arrow 2 -->
        <path d="M 470 100 Q 530 60 590 100" stroke="{COLORS['gray']}" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
        
        <!-- Operate Phase -->
        <circle cx="650" cy="120" r="70" fill="{COLORS['orange']}" opacity="0.2" stroke="{COLORS['orange']}" stroke-width="3"/>
        <text x="650" y="110" font-family="Segoe UI" font-size="16" font-weight="bold" fill="{COLORS['orange']}" text-anchor="middle">OPERATE</text>
        <text x="650" y="135" font-family="Segoe UI" font-size="11" text-anchor="middle">Continuous</text>
        <text x="650" y="150" font-family="Segoe UI" font-size="11" text-anchor="middle">Automation</text>
        
        <!-- Loop back arrow -->
        <path d="M 650 190 Q 400 280 150 190" stroke="{COLORS['gray']}" stroke-width="2" fill="none" marker-end="url(#arrow)" stroke-dasharray="5"/>
        <text x="400" y="260" font-family="Segoe UI" font-size="11" fill="{COLORS['gray']}" text-anchor="middle">Continuous Improvement</text>
        
        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="{COLORS['gray']}" />
            </marker>
        </defs>
    </g>
""")

# 6. Cost Allocation with Tags
create_svg("12-cost-allocation-tags.svg", "Cost Allocation: Tagging Strategy", f"""
    <g transform="translate(50, 80)">
        <!-- Resource Group -->
        <rect x="50" y="20" width="600" height="250" rx="10" fill="{COLORS['light_gray']}" stroke="{COLORS['gray']}" stroke-width="2"/>
        <text x="350" y="50" font-family="Segoe UI" font-size="14" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">Azure Resources</text>
        
        <!-- VM Resource -->
        <rect x="80" y="80" width="150" height="100" rx="5" fill="white" stroke="{COLORS['blue']}" stroke-width="2"/>
        <text x="155" y="105" font-family="Segoe UI" font-size="12" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">Virtual Machine</text>
        
        <!-- VM Tags -->
        <rect x="90" y="115" width="60" height="20" rx="3" fill="{COLORS['blue']}" opacity="0.3"/>
        <text x="120" y="130" font-family="Segoe UI" font-size="9" text-anchor="middle">Team: Platform</text>
        
        <rect x="155" y="115" width="65" height="20" rx="3" fill="{COLORS['green']}" opacity="0.3"/>
        <text x="188" y="130" font-family="Segoe UI" font-size="9" text-anchor="middle">Env: Prod</text>
        
        <rect x="90" y="140" width="130" height="20" rx="3" fill="{COLORS['orange']}" opacity="0.3"/>
        <text x="155" y="155" font-family="Segoe UI" font-size="9" text-anchor="middle">CostCenter: Engineering</text>
        
        <!-- Storage Resource -->
        <rect x="275" y="80" width="150" height="100" rx="5" fill="white" stroke="{COLORS['blue']}" stroke-width="2"/>
        <text x="350" y="105" font-family="Segoe UI" font-size="12" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">Storage Account</text>
        
        <rect x="285" y="115" width="60" height="20" rx="3" fill="{COLORS['purple']}" opacity="0.3"/>
        <text x="315" y="130" font-family="Segoe UI" font-size="9" text-anchor="middle">Team: Data</text>
        
        <rect x="350" y="115" width="65" height="20" rx="3" fill="{COLORS['green']}" opacity="0.3"/>
        <text x="383" y="130" font-family="Segoe UI" font-size="9" text-anchor="middle">Env: Prod</text>
        
        <rect x="285" y="140" width="130" height="20" rx="3" fill="{COLORS['orange']}" opacity="0.3"/>
        <text x="350" y="155" font-family="Segoe UI" font-size="9" text-anchor="middle">CostCenter: Analytics</text>
        
        <!-- AKS Resource -->
        <rect x="470" y="80" width="150" height="100" rx="5" fill="white" stroke="{COLORS['blue']}" stroke-width="2"/>
        <text x="545" y="105" font-family="Segoe UI" font-size="12" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">AKS Cluster</text>
        
        <rect x="480" y="115" width="70" height="20" rx="3" fill="{COLORS['teal']}" opacity="0.3"/>
        <text x="515" y="130" font-family="Segoe UI" font-size="9" text-anchor="middle">Team: DevOps</text>
        
        <rect x="555" y="115" width="55" height="20" rx="3" fill="{COLORS['green']}" opacity="0.3"/>
        <text x="583" y="130" font-family="Segoe UI" font-size="9" text-anchor="middle">Env: Prod</text>
        
        <rect x="480" y="140" width="130" height="20" rx="3" fill="{COLORS['orange']}" opacity="0.3"/>
        <text x="545" y="155" font-family="Segoe UI" font-size="9" text-anchor="middle">CostCenter: Engineering</text>
        
        <!-- Cost Report -->
        <text x="350" y="210" font-family="Segoe UI" font-size="12" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">→ Cost Management Report by Tag</text>
        <text x="155" y="235" font-family="Segoe UI" font-size="11" fill="{COLORS['blue']}" text-anchor="middle">Platform: $5,000</text>
        <text x="350" y="235" font-family="Segoe UI" font-size="11" fill="{COLORS['purple']}" text-anchor="middle">Data: $3,000</text>
        <text x="545" y="235" font-family="Segoe UI" font-size="11" fill="{COLORS['teal']}" text-anchor="middle">DevOps: $8,000</text>
    </g>
""")

# =============================================================================
# CHAPTER 13: HA/DR DIAGRAMS (Placeholder for future)
# =============================================================================

# 7. Azure Site Recovery
create_svg("13-azure-site-recovery.svg", "Azure Site Recovery: Multi-Region DR", f"""
    <g transform="translate(50, 80)">
        <!-- Primary Region -->
        <rect x="50" y="40" width="250" height="180" rx="10" fill="{COLORS['light_blue']}" stroke="{COLORS['blue']}" stroke-width="2"/>
        <text x="175" y="70" font-family="Segoe UI" font-size="14" font-weight="bold" fill="{COLORS['blue']}" text-anchor="middle">Primary Region</text>
        <text x="175" y="90" font-family="Segoe UI" font-size="11" fill="{COLORS['gray']}" text-anchor="middle">East US</text>
        
        <!-- Primary VMs -->
        <rect x="80" y="110" width="80" height="50" rx="5" fill="white" stroke="{COLORS['green']}"/>
        <text x="120" y="140" font-family="Segoe UI" font-size="10" text-anchor="middle">Web VM</text>
        
        <rect x="180" y="110" width="80" height="50" rx="5" fill="white" stroke="{COLORS['green']}"/>
        <text x="220" y="140" font-family="Segoe UI" font-size="10" text-anchor="middle">API VM</text>
        
        <rect x="130" y="170" width="80" height="40" rx="5" fill="white" stroke="{COLORS['blue']}"/>
        <text x="170" y="195" font-family="Segoe UI" font-size="10" text-anchor="middle">SQL DB</text>
        
        <!-- ASR Arrow -->
        <path d="M 300 130 L 450 130" stroke="{COLORS['orange']}" stroke-width="3" fill="none" marker-end="url(#arrow)" stroke-dasharray="5"/>
        <text x="375" y="110" font-family="Segoe UI" font-size="11" font-weight="bold" fill="{COLORS['orange']}" text-anchor="middle">Azure Site Recovery</text>
        <text x="375" y="150" font-family="Segoe UI" font-size="10" fill="{COLORS['gray']}" text-anchor="middle">Continuous Replication</text>
        
        <!-- Secondary Region -->
        <rect x="450" y="40" width="250" height="180" rx="10" fill="{COLORS['light_gray']}" stroke="{COLORS['gray']}" stroke-width="2" stroke-dasharray="5"/>
        <text x="575" y="70" font-family="Segoe UI" font-size="14" font-weight="bold" fill="{COLORS['gray']}" text-anchor="middle">DR Region (Standby)</text>
        <text x="575" y="90" font-family="Segoe UI" font-size="11" fill="{COLORS['gray']}" text-anchor="middle">West US</text>
        
        <!-- Secondary VMs (faded) -->
        <rect x="480" y="110" width="80" height="50" rx="5" fill="white" stroke="{COLORS['gray']}" stroke-dasharray="3" opacity="0.5"/>
        <text x="520" y="140" font-family="Segoe UI" font-size="10" fill="{COLORS['gray']}" text-anchor="middle">Web VM</text>
        
        <rect x="580" y="110" width="80" height="50" rx="5" fill="white" stroke="{COLORS['gray']}" stroke-dasharray="3" opacity="0.5"/>
        <text x="620" y="140" font-family="Segoe UI" font-size="10" fill="{COLORS['gray']}" text-anchor="middle">API VM</text>
        
        <rect x="530" y="170" width="80" height="40" rx="5" fill="white" stroke="{COLORS['gray']}" stroke-dasharray="3" opacity="0.5"/>
        <text x="570" y="195" font-family="Segoe UI" font-size="10" fill="{COLORS['gray']}" text-anchor="middle">SQL Replica</text>
        
        <!-- Metrics -->
        <text x="175" y="255" font-family="Segoe UI" font-size="11" fill="{COLORS['text']}" text-anchor="middle">RPO: 5 minutes</text>
        <text x="575" y="255" font-family="Segoe UI" font-size="11" fill="{COLORS['text']}" text-anchor="middle">RTO: 2 hours</text>
        
        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="{COLORS['orange']}" />
            </marker>
        </defs>
    </g>
""")

print("\n✅ All SVG diagrams generated successfully!")
print("Generated 7 diagrams:")
print("  - 07-helm-architecture.svg")
print("  - 07-gitops-argocd.svg")
print("  - 07-service-mesh-istio.svg")
print("  - 07-keda-autoscaling.svg")
print("  - 12-finops-lifecycle.svg")
print("  - 12-cost-allocation-tags.svg")
print("  - 13-azure-site-recovery.svg")
