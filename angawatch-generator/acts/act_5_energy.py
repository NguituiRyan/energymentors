from utils import generate_header

def generate():
    slides = []

    # Slide 45: Energy Opener
    s45 = """
<!-- ═══════════════ ACT V: ENERGY SYSTEM ═══════════════ -->
<div class="s" style="min-height:60vh;background:#0F172A;display:flex;align-items:center;justify-content:center;text-align:center;color:#fff">
<div class="rv unfold">
<div class="mono" style="font-size:14px;letter-spacing:.3em;color:var(--mute);margin-bottom:24px">Section 05 · The Engine</div>
<div style="font-family:'Playfair Display',serif;font-size:80px;font-weight:900;color:var(--td);margin-bottom:16px;text-shadow:0 10px 30px rgba(15,118,110,.4);">The Energy System.</div>
<div style="font-size:24px;color:var(--tl)">3.36 MWp Solar \u00b7 6.4 MWh Storage \u00b7 6,400 kVA Conversion</div>
<svg class="draw on" width="100%" height="200" viewBox="0 0 1000 200" style="margin-top:40px;opacity:.2">
    <!-- Grid/Energy wave abstract -->
    <path class="sankey-flow" d="M0 100 Q 250 10 500 100 T 1000 100" fill="none" stroke="var(--tl)" stroke-width="2"/>
    <path class="sankey-flow" d="M0 100 Q 250 190 500 100 T 1000 100" fill="none" stroke="var(--tb)" stroke-width="4"/>
</svg>
</div>
</div>
"""
    slides.append(s45)

    # Slide 46: Load Profile Synthesis
    s46 = f"""
<div class="s" id="s46">{generate_header("05.01 · Load Synthesis")}
<div class="pad rv scaleIn">
<div class="t1">Community Load Synthesis.</div>
<div class="g2">
    <div>
        <p class="intro">Aggregating 2,000 homes, YattaFarm water pumping, E-Matatu charging, and community hubs creates a distinct 24-hour load shape.</p>
        <ul style="font-size:15px;line-height:1.8;color:var(--body);margin-top:20px;padding-left:20px;">
            <li><strong style="color:var(--ink)">Base Load:</strong> ~600 kW (Fridges, Security, Server)</li>
            <li><strong style="color:#EF4444">Morning Peak:</strong> 1.8 MW (6:00-8:30) Kettles, Showers</li>
            <li><strong style="color:var(--td)">Midday E-Matatu charging:</strong> Timed to solar maximum</li>
            <li><strong style="color:#F59E0B">Evening Peak:</strong> 3.1 MW (19:00-21:30) Lighting, TVs, Evening Routines</li>
        </ul>
    </div>
    <div style="background:var(--card);border-radius:24px;padding:24px;border:1px solid var(--bl);">
        <svg viewBox="0 0 500 300" width="100%" height="auto" class="draw on">
            <!-- Grid lines -->
            { "".join([f'<line x1="50" y1="{50+i*50}" x2="480" y2="{50+i*50}" stroke="var(--bl)" stroke-dasharray="4 4"/>' for i in range(5)]) }
            <text x="35" y="55" class="mono" style="font-size:10px;text-anchor:end">3MW</text>
            <text x="35" y="105" class="mono" style="font-size:10px;text-anchor:end">2MW</text>
            <text x="35" y="155" class="mono" style="font-size:10px;text-anchor:end">1MW</text>
            <text x="35" y="255" class="mono" style="font-size:10px;text-anchor:end">0MW</text>
            <!-- X Axis Ticks -->
            <text x="50" y="275" class="mono" style="font-size:10px;text-anchor:middle">00h</text>
            <text x="140" y="275" class="mono" style="font-size:10px;text-anchor:middle">06h</text>
            <text x="265" y="275" class="mono" style="font-size:10px;text-anchor:middle">12h</text>
            <text x="390" y="275" class="mono" style="font-size:10px;text-anchor:middle">18h</text>
            <text x="480" y="275" class="mono" style="font-size:10px;text-anchor:middle">24h</text>
            
            <!-- Load Curve -->
            <!-- 0->06(base)->08(peak)->10(drop)->15(base+charging)->18(rise)->20(peak)->24(base) -->
            <path class="sankey-flow" d="M50 200 C 100 200, 120 200, 140 100 C 160 200, 200 150, 265 140 C 330 150, 370 200, 390 50 C 420 50, 440 200, 480 200" fill="none" stroke="var(--td)" stroke-width="4"/>
            <!-- Solar Fill Overlay -->
            <path d="M140 250 C 200 40, 330 40, 390 250 Z" fill="rgba(245,158,11,0.2)"/>
            <text x="265" y="100" class="mono" style="font-size:12px;fill:#B45309;font-weight:700;text-anchor:middle">SOLAR CURVE</text>
        </svg>
    </div>
</div>
</div></div>
"""
    slides.append(s46)

    # Slide 47: Night Peak Architecture
    s47 = f"""
<div class="s" id="s47">{generate_header("05.02 · The Night Peak")}
<div class="pad rv slideFromRight">
<div class="t1">The 3.1 MW Night Peak.</div>
<div class="g2">
    <div style="background:#0F172A;color:#fff;padding:40px;border-radius:32px;">
        <h3 style="font-size:24px;margin-bottom:16px;">The "Duck Curve" Problem</h3>
        <p style="font-size:16px;line-height:1.6;color:var(--mute);">When the sun sets at 18:30, solar generation drops to zero exactly as 2,000 households switch on lights, TVs, and evening appliances.</p>
        <div style="font-family:'Playfair Display',serif;font-size:64px;font-weight:700;margin-top:24px;color:#EF4444;">3.1 MW</div>
        <div class="mono" style="font-size:12px;color:#FCA5A5;">PREDICTED 19:30 DEMAND</div>
    </div>
    <div>
        <h3 style="font-size:24px;margin-bottom:16px;">The Engineering Buffer</h3>
        <p style="font-size:16px;line-height:1.6;color:var(--body);margin-bottom:24px;">Lead-acid batteries cannot discharge 3.1 MW instantly without voltage collapse. The system demands high C-rate lithium architecture.</p>
        <div class="kv"><span class="k">Required Storage</span><span class="v" style="color:var(--td);font-weight:700;">6,400 kWh (6.4 MWh)</span></div>
        <div class="kv"><span class="k">Chemistry</span><span class="v">LiFePO4 (LFP)</span></div>
        <div class="kv"><span class="k">Max Discharge Rate</span><span class="v">>0.5C (3.2 MW capable)</span></div>
    </div>
</div>
</div></div>
"""
    slides.append(s47)

    # Slide 48: Irradiance Matching
    s48 = f"""
<div class="s" id="s48">{generate_header("05.03 · Irradiance Matching")}
<div class="pad rv unfold">
<div class="t1">Sizing the Array.</div>
<div class="intro">Target daily consumption: 15,300 kWh (15.3 MWh). System losses (inverter, wiring, battery round-trip): ~18%. Required generation: 18,650 kWh/day.</div>
<div class="g3" style="margin-top:40px;">
    <div class="card transform-up" style="border-top:4px solid var(--td);text-align:center;">
        <h3 style="font-size:16px;color:var(--td);margin-bottom:10px;">PVGIS Irradiance</h3>
        <div style="font-family:'Playfair Display',serif;font-size:40px;font-weight:700;">5.18</div>
        <div class="mono" style="font-size:10px;color:var(--mute);">kWh/m\u00b2/day EQUIVALENT</div>
    </div>
    <div class="card transform-up" style="border-top:4px solid var(--ink);text-align:center;">
        <h3 style="font-size:16px;color:var(--ink);margin-bottom:10px;">DC Capacity Sizing</h3>
        <div style="font-family:'Playfair Display',serif;font-size:40px;font-weight:700;">3,600</div>
        <div class="mono" style="font-size:10px;color:var(--mute);">kWp REQUIRED</div>
    </div>
    <div class="card transform-up" style="border-top:4px solid var(--tb);text-align:center;">
        <h3 style="font-size:16px;color:var(--tb);margin-bottom:10px;">Panel Count (580W)</h3>
        <div style="font-family:'Playfair Display',serif;font-size:40px;font-weight:700;">6,206</div>
        <div class="mono" style="font-size:10px;color:var(--mute);">TIER-1 MONO BIFACIAL</div>
    </div>
</div>
</div></div>
"""
    slides.append(s48)

    # Slide 49: Storage Matrix
    s49 = f"""
<div class="s" id="s49">{generate_header("05.04 · Storage Selection")}
<div class="pad rv slideFromLeft">
<div class="t1">Storage Chemistry Matrix.</div>
<table class="dt" style="margin-top:20px; font-size:14px;">
    <tr style="background:#F8FAFC;"><th style="width:25%;">Parameter</th><th>Lead Acid (Tubular)</th><th>NMC Lithium</th><th style="color:var(--td);background:var(--tl)">LiFePO4 (LFP) - CHOSEN</th></tr>
    <tr><td>Cycle Life @ 80% DoD</td><td>1,200 (3-4 years)</td><td>3,000 (8 years)</td><td style="font-weight:700;color:var(--td);background:var(--tl)">6,000+ (15+ years)</td></tr>
    <tr><td>Thermal Runaway Risk</td><td>Low (Hydrogen gas)</td><td style="color:#EF4444;">High (Fire hazard)</td><td style="font-weight:700;color:var(--td);background:var(--tl)">Effectively Zero</td></tr>
    <tr><td>High Temp Degrade</td><td style="color:#EF4444;">Severe (>25\u00b0C kills)</td><td>Moderate</td><td style="font-weight:700;color:var(--td);background:var(--tl)">Highly Tolerant (up to 45\u00b0C)</td></tr>
    <tr><td>Max C-Rate</td><td style="color:#EF4444;">0.1C - 0.2C</td><td>1.0C</td><td style="font-weight:700;color:var(--td);background:var(--tl)">1.0C (Safely 0.5C)</td></tr>
    <tr><td>Cost per kWh (Capex)</td><td style="color:var(--tb);">Low (~$120)</td><td>High (~$300)</td><td style="font-weight:700;background:var(--tl)">Moderate (~$180 - $220)</td></tr>
    <tr><td>Cost per Cycle (Opex)</td><td style="color:#EF4444;">Highest</td><td>Moderate</td><td style="font-weight:700;color:var(--td);background:var(--tl)">Lowest</td></tr>
</table>
</div></div>
"""
    slides.append(s49)

    # Slide 50: LFP Specs
    s50 = f"""
<div class="s" id="s50">{generate_header("05.05 · Storage Specs")}
<div class="pad rv scaleIn">
<div class="g2">
    <div>
        <div class="t1" style="font-size:40px;">BESS Enclosures.</div>
        <div class="intro">We utilize containerized Utility-Scale Battery Energy Storage Systems (BESS). Drop-in ready, pre-wired with HVAC and fire suppression.</div>
        <ul style="margin-top:20px;line-height:1.8;padding-left:20px;font-size:16px;">
            <li>Format: Liquid-cooled 10ft / 20ft ISO containers</li>
            <li>Voltage: 1000V - 1500V DC high voltage string</li>
            <li>BMS: Cell-level active balancing</li>
            <li>Augmentation: Modular expansion without replacing entire bank</li>
        </ul>
    </div>
    <div style="background:linear-gradient(135deg,#0F172A,#1E293B);padding:40px;border-radius:32px;color:#fff;text-align:center;box-shadow:0 20px 40px rgba(0,0,0,.2);">
        <div style="font-family:'Playfair Display',serif;font-size:72px;font-weight:700;color:var(--td);">6.4</div>
        <div class="mono" style="font-size:14px;color:var(--tl);margin-bottom:32px;">MEGAWATT HOURS REQUIRED</div>
        <p style="font-size:14px;color:var(--mute);line-height:1.6;margin-bottom:20px;">Sufficient to carry the entire community from sunset to 08:00 AM completely autonomously, with a 20% reserve daily buffer.</p>
        <div style="display:inline-block;padding:8px 16px;background:rgba(255,255,255,.1);border-radius:100px;font-size:12px;font-weight:700;">8,000 CYCLES @ 80% DoD</div>
    </div>
</div>
</div></div>
"""
    slides.append(s50)

    # Slide 51: Topology DC Microgrid
    s51 = f"""
<div class="s" id="s51">{generate_header("05.06 · Topology")}
<div class="pad rv slideFromRight">
<div class="t1">The Topology: Distributed DC.</div>
<div class="intro">A centralized 3.36MW inverter bank forces massive thick AC cable runs. Instead, we distribute 300kW containerized Energy Hubs across the 102 hectares.</div>
<div class="glow-on-hover" style="background:#fff;border-radius:32px;padding:40px;border:1px solid var(--bl);margin-top:40px; transition:box-shadow .3s;">
    <!-- SVG Distributed Topology diagram -->
    <svg viewBox="0 0 800 250" width="100%" height="auto">
        <!-- Central Arrays (DC) -->
        <rect x="50" y="50" width="100" height="150" fill="var(--td)" rx="8"/>
        <text x="100" y="120" style="fill:#fff;font-size:14px;font-weight:700;text-anchor:middle;">SOLAR</text>
        <text x="100" y="140" style="fill:#fff;font-size:12px;text-anchor:middle;">ARRAY</text>
        
        <!-- DC Bus -->
        <line x1="150" y1="125" x2="250" y2="125" stroke="#EF4444" stroke-width="4" stroke-dasharray="8 4"/>
        <text x="200" y="115" class="mono" style="font-size:10px;fill:#EF4444;text-anchor:middle;">1000V DC BUS</text>
        
        <!-- BESS -->
        <rect x="250" y="75" width="80" height="100" fill="#1E293B" rx="4"/>
        <text x="290" y="125" style="fill:#fff;font-size:14px;font-weight:700;text-anchor:middle;">BESS</text>
        
        <!-- DC to AC Hubs -->
        <line x1="330" y1="125" x2="450" y2="125" stroke="#EF4444" stroke-width="4" stroke-dasharray="8 4"/>
        
        <!-- Hub 1 -->
        <rect x="450" y="20" width="100" height="60" fill="var(--tb)" rx="4"/>
        <text x="500" y="50" style="fill:#fff;font-size:12px;font-weight:700;text-anchor:middle;">INVERTER A</text>
        <line x1="400" y1="125" x2="400" y2="50" stroke="#EF4444" stroke-width="2"/>
        <line x1="400" y1="50" x2="450" y2="50" stroke="#EF4444" stroke-width="2"/>
        
        <!-- Hub 2 -->
        <rect x="450" y="95" width="100" height="60" fill="var(--tb)" rx="4"/>
        <text x="500" y="125" style="fill:#fff;font-size:12px;font-weight:700;text-anchor:middle;">INVERTER B</text>
        <line x1="330" y1="125" x2="450" y2="125" stroke="#EF4444" stroke-width="2"/>
        
        <!-- Hub 3 -->
        <rect x="450" y="170" width="100" height="60" fill="var(--tb)" rx="4"/>
        <text x="500" y="200" style="fill:#fff;font-size:12px;font-weight:700;text-anchor:middle;">INVERTER C</text>
        <line x1="400" y1="125" x2="400" y2="200" stroke="#EF4444" stroke-width="2"/>
        <line x1="400" y1="200" x2="450" y2="200" stroke="#EF4444" stroke-width="2"/>
        
        <!-- Homes (AC) -->
        <line x1="550" y1="50" x2="650" y2="50" stroke="#3B82F6" stroke-width="2"/>
        <polygon points="650,40 670,50 650,60" fill="#3B82F6"/>
        <text x="710" y="55" style="fill:var(--ink);font-size:12px;font-weight:700;text-anchor:middle;">HOMES (1-500)</text>

        <line x1="550" y1="125" x2="650" y2="125" stroke="#3B82F6" stroke-width="2"/>
        <polygon points="650,115 670,125 650,135" fill="#3B82F6"/>
        <text x="710" y="130" style="fill:var(--ink);font-size:12px;font-weight:700;text-anchor:middle;">HOMES (501-1K)</text>

        <line x1="550" y1="200" x2="650" y2="200" stroke="#3B82F6" stroke-width="2"/>
        <polygon points="650,190 670,200 650,210" fill="#3B82F6"/>
        <text x="710" y="205" style="fill:var(--ink);font-size:12px;font-weight:700;text-anchor:middle;">HOMES (1K-1.5K)</text>
    </svg>
</div>
</div></div>
"""
    slides.append(s51)

    # Slide 52: Why Not AC Microgrid?
    s52 = f"""
<div class="s" id="s52">{generate_header("05.07 · AC vs DC Framework")}
<div class="pad rv unfold">
<div class="t1">The Copper Cost Avoided.</div>
<div class="g2" style="margin-top:40px;">
    <div style="background:#FEF2F2;border:1px solid #FCA5A5;padding:32px;border-radius:24px;">
        <h3 style="font-size:20px;color:#B91C1C;margin-bottom:16px;">Standard AC Topology (Flawed)</h3>
        <p style="font-size:14px;line-height:1.6;margin-bottom:20px;">If 3.36 MW is inverted entirely at the central solar farm to 415V AC, pushing that AC power to house clusters 800 meters away requires extremely thick, heavy, expensive armored copper cable to combat AC voltage drop.</p>
        <div style="color:#EF4444;font-weight:700;font-size:24px;">Cable Capex = Fatal</div>
    </div>
    <div style="background:var(--card);border:1px solid var(--tb);padding:32px;border-radius:24px;box-shadow:0 10px 30px rgba(20,184,166,.1);">
        <h3 style="font-size:20px;color:var(--td);margin-bottom:16px;">Angawatch DC Topology</h3>
        <p style="font-size:14px;line-height:1.6;margin-bottom:20px;">We transmit power at 1000V DC from the BESS/Solar arrays to neighborhood "Inverter Kiosks". High voltage DC uses thin, cheap cable with minimal loss. Inversion to 415V/240V AC happens right next to the homes.</p>
        <div style="color:var(--td);font-weight:700;font-size:24px;">Cable Capex reduced ~60%</div>
    </div>
</div>
</div></div>
"""
    slides.append(s52)

    # Slide 53: HVDC Backbone
    s53 = f"""
<div class="s" id="s53">{generate_header("05.08 · HVDC Backbone")}
<div class="pad rv slideFromLeft">
<div class="g2" style="align-items:center;">
    <div>
        <div class="t1">High Voltage DC Backbone.</div>
        <p style="font-size:16px;line-height:1.8;margin-bottom:20px;">Reticulation map of the 102 hectares utilizing underground armored 1000V DC trunklines. Immune to lightning strikes. Immune to copper theft. Zero visual pollution from poles.</p>
        <ul style="list-style:none;padding:0;">
            <li style="margin-bottom:10px;font-size:14px;"><strong style="color:var(--td);">Trunk:</strong> 150mm\u00b2 XLPE Aluminum</li>
            <li style="margin-bottom:10px;font-size:14px;"><strong style="color:var(--td);">Distance:</strong> Max 1,200m radius</li>
            <li style="margin-bottom:10px;font-size:14px;"><strong style="color:var(--td);">Efficiency:</strong> 99.2% transmission efficiency over 1km.</li>
        </ul>
    </div>
    <!-- Simple abstract map representation -->
    <div style="width:100%;height:400px;background:var(--bl);border-radius:32px;position:relative;overflow:hidden;box-shadow:inset 0 10px 20px rgba(0,0,0,.05);">
        <svg class="draw on" width="100%" height="100%" viewBox="0 0 400 400">
            <!-- Grid bg -->
            <path d="M0 100 L400 100 M0 200 L400 200 M0 300 L400 300 M100 0 L100 400 M200 0 L200 400 M300 0 L300 400" stroke="#CBD5E1" stroke-width="1" fill="none"/>
            <!-- Solar Farm -->
            <rect x="150" y="150" width="100" height="100" fill="var(--td)"/>
            <!-- Trunks -->
            <path class="sankey-flow" d="M200 150 L200 50 L100 50" stroke="#EF4444" stroke-width="4" fill="none"/>
            <path class="sankey-flow" d="M150 200 L50 200 L50 300" stroke="#EF4444" stroke-width="4" fill="none"/>
            <path class="sankey-flow" d="M250 200 L350 200 L350 100" stroke="#EF4444" stroke-width="4" fill="none"/>
            <path class="sankey-flow" d="M200 250 L200 350 L300 350" stroke="#EF4444" stroke-width="4" fill="none"/>
            <!-- Nodes -->
            <circle cx="100" cy="50" r="12" fill="#1E293B" stroke="#fff" stroke-width="2"/>
            <circle cx="50" cy="300" r="12" fill="#1E293B" stroke="#fff" stroke-width="2"/>
            <circle cx="350" cy="100" r="12" fill="#1E293B" stroke="#fff" stroke-width="2"/>
            <circle cx="300" cy="350" r="12" fill="#1E293B" stroke="#fff" stroke-width="2"/>
        </svg>
    </div>
</div>
</div></div>
"""
    slides.append(s53)

    # Slide 54: Inverter Distribution
    s54 = f"""
<div class="s" id="s54">{generate_header("05.09 · Inverter Kiosks")}
<div class="pad rv scaleIn">
<div class="g2">
    <div style="background:var(--card);border-radius:32px;padding:40px;border:1px solid var(--bl);">
        <h3 style="font-family:'Playfair Display',serif;font-size:32px;margin-bottom:20px;">The 300kW Hubs</h3>
        <p style="font-size:16px;line-height:1.7;color:var(--body);margin-bottom:20px;">Instead of one massive central inverter, we use 22 distribution nodes. Each node takes the 1000V DC trunk and drops it to 415V 3-Phase AC, serving ~90 homes within a 150m radius.</p>
        <ul style="list-style:none;padding:0;margin-top:20px;line-height:1.8;">
            <li><strong>Input:</strong> 1000V DC (Backbone)</li>
            <li><strong>Output:</strong> 415V/240V AC</li>
            <li><strong>Capacity:</strong> 300 kW per kiosk</li>
            <li><strong>Max AC Run:</strong> Under 150 meters to the furthest home.</li>
        </ul>
    </div>
    <div style="display:flex;align-items:center;justify-content:center;">
        <svg viewBox="0 0 300 300" width="100%" height="auto">
            <!-- Node abstract -->
            <rect x="100" y="50" width="100" height="200" rx="10" fill="var(--tb)"/>
            <!-- DC in -->
            <line x1="150" y1="0" x2="150" y2="50" stroke="#EF4444" stroke-width="6"/>
            <!-- AC out multiple -->
            <line x1="200" y1="100" x2="300" y2="100" stroke="#3B82F6" stroke-width="4"/>
            <line x1="200" y1="150" x2="300" y2="150" stroke="#3B82F6" stroke-width="4"/>
            <line x1="200" y1="200" x2="300" y2="200" stroke="#3B82F6" stroke-width="4"/>
            
            <circle cx="150" cy="150" r="30" fill="#fff"/>
            <text x="150" y="155" class="mono" style="font-size:12px;fill:var(--ink);text-anchor:middle;">DC-AC</text>
        </svg>
    </div>
</div>
</div></div>
"""
    slides.append(s54)

    # Slide 55: Substation Architecture
    s55 = f"""
<div class="s" id="s55">{generate_header("05.10 · Substation")}
<div class="pad rv slideFromRight">
<div class="t1">The Substation & Switchgear.</div>
<div style="background:#0F172A;border-radius:32px;padding:40px;margin-top:40px;color:#fff;display:flex;gap:40px;">
    <div style="flex:1;">
        <h3 style="font-size:24px;margin-bottom:20px;color:var(--tl)">12MVA Core Infrastructure</h3>
        <p style="font-size:15px;line-height:1.7;color:var(--mute);margin-bottom:20px;">The central master switch room processes the raw DC power and manages the intertie with KPLC and backup generation.</p>
        <div class="kv" style="border-color:#334155"><span class="k" style="color:#94A3B8">Step-Up Transformer</span><span class="v">12 MVA (11kV KPLC export)</span></div>
        <div class="kv" style="border-color:#334155"><span class="k" style="color:#94A3B8">Relay Protection</span><span class="v">SEL-751 Feeder Protection</span></div>
        <div class="kv" style="border-color:transparent"><span class="k" style="color:#94A3B8">SCADA System</span><span class="v">Ignition / Modbus TCP</span></div>
    </div>
    <div style="flex:1;background:#1E293B;border-radius:24px;padding:32px;border:1px solid #334155;">
        <div style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;color:var(--tb);">99.6%</div>
        <div class="mono" style="font-size:12px;color:var(--mute);margin-bottom:20px;">GUARANTEED UPTIME PLATFORM</div>
        <p style="font-size:14px;color:#94A3B8;line-height:1.6;">Automated transfer switches (ATS) shift between Solar\u2192Battery\u2192Grid\u2192Diesel in under 20 milliseconds. Complete resilience.</p>
    </div>
</div>
</div></div>
"""
    slides.append(s55)

    # Slide 56: Energy Balance
    s56 = f"""
<div class="s" id="s56">{generate_header("05.11 · The Worst Case Week")}
<div class="pad rv unfold">
<div class="t1">The Worst Case Week.</div>
<div class="intro">Designing for November 'short rains' \u2014 consecutive overcast days with irradiance plummeting to 3.2 kWh/m\u00b2.</div>
<div class="card" style="margin-top:40px;">
    <!-- Abstract 7-day battery SoC bar chart -->
    <div style="display:flex;align-items:flex-end;height:250px;gap:10px;padding:20px;border-bottom:2px solid var(--bl);">
        <div style="flex:1;display:flex;flex-direction:column;align-items:center;"><div style="width:100%;background:var(--td);height:100%;max-height:90%;"></div><div style="margin-top:10px;" class="mono">DAY 1</div></div>
        <div style="flex:1;display:flex;flex-direction:column;align-items:center;"><div style="width:100%;background:var(--tb);height:100%;max-height:75%;"></div><div style="margin-top:10px;" class="mono">DAY 2</div></div>
        <div style="flex:1;display:flex;flex-direction:column;align-items:center;"><div style="width:100%;background:#FCD34D;height:100%;max-height:55%;"></div><div style="margin-top:10px;" class="mono">DAY 3</div></div>
        <div style="flex:1;display:flex;flex-direction:column;align-items:center;"><div style="width:100%;background:#F59E0B;height:100%;max-height:35%;"></div><div style="margin-top:10px;" class="mono">DAY 4</div></div>
        <div style="flex:1;display:flex;flex-direction:column;align-items:center;"><div style="width:100%;background:#EF4444;height:100%;max-height:20%;"></div><div style="margin-top:10px;" class="mono">DAY 5</div></div>
        <div style="flex:1;display:flex;flex-direction:column;align-items:center;"><div style="width:100%;background:var(--tb);height:100%;max-height:60%;"></div><div style="margin-top:10px;" class="mono">DAY 6</div></div>
        <div style="flex:1;display:flex;flex-direction:column;align-items:center;"><div style="width:100%;background:var(--td);height:100%;max-height:85%;"></div><div style="margin-top:10px;" class="mono">DAY 7</div></div>
    </div>
    <div style="margin-top:20px;display:flex;justify-content:space-between;color:var(--mute);font-size:13px;">
        <span>Starts 100% SoC</span>
        <span style="color:#EF4444;font-weight:700;">Bottoms at 20% SoC (DoD Limit Protect)</span>
        <span>Recovers rapidly with grid/diesel assist</span>
    </div>
</div>
</div></div>
"""
    slides.append(s56)

    # Slide 57: Grid Intertie Strategy
    s57 = f"""
<div class="s" id="s57">{generate_header("05.12 · Grid Intertie")}
<div class="pad rv scaleIn">
<div class="g2">
    <div>
        <div class="t1">The KPLC Intertie.</div>
        <p style="font-size:16px;line-height:1.7;color:var(--body);margin-bottom:20px;">We do not island. The 11kV KPLC line 4km away is our battery's battery. We intertie under the Energy Act 2019 Net Metering regulations.</p>
        <div class="kv"><span class="k">Export (Day)</span><span class="v" style="color:var(--td);font-weight:700;">Up to 1.5MW Surplus</span></div>
        <div class="kv"><span class="k">Import (Night/Rain)</span><span class="v" style="color:#EF4444;">When SoC < 20%</span></div>
        <p style="font-size:14px;color:var(--mute);line-height:1.6;margin-top:20px;border-left:4px solid var(--tb);padding-left:16px;">This ensures that even during a 2-week rain storm, power never fails. The grid is treated as a secondary backup to the primary solar microgrid.</p>
    </div>
    <div style="display:flex;align-items:center;justify-content:center;">
        <svg viewBox="0 0 300 200" width="100%" height="auto">
            <!-- Grid Intertie Diagram -->
            <rect x="20" y="50" width="80" height="100" fill="var(--td)" rx="8"/>
            <text x="60" y="105" style="fill:#fff;font-size:12px;font-weight:700;text-anchor:middle;">ANGAWATCH</text>
            
            <rect x="200" y="50" width="80" height="100" fill="#1E293B" rx="8"/>
            <text x="240" y="105" style="fill:#fff;font-size:12px;font-weight:700;text-anchor:middle;">KPLC GRID</text>
            
            <!-- Bidirectional arrows -->
            <line x1="100" y1="80" x2="200" y2="80" stroke="var(--td)" stroke-width="6"/>
            <polygon points="190,70 205,80 190,90" fill="var(--td)"/>
            <text x="150" y="70" style="font-size:10px;fill:var(--td);text-anchor:middle;">DAY SURPLUS</text>
            
            <line x1="200" y1="120" x2="100" y2="120" stroke="#EF4444" stroke-width="6"/>
            <polygon points="110,110 95,120 110,130" fill="#EF4444"/>
            <text x="150" y="145" style="font-size:10px;fill:#EF4444;text-anchor:middle;">NIGHT BACKUP</text>
        </svg>
    </div>
</div>
</div></div>
"""
    slides.append(s57)

    # Slide 58: LCOE
    s58 = f"""
<div class="s" id="s58">{generate_header("05.13 · Levelized Cost (LCOE)")}
<div class="pad rv slideFromRight">
<div class="t1">Levelized Cost of Energy.</div>
<div class="intro">Why we can sell power at KES 9/kWh while KPLC charges KES 25\u201328/kWh.</div>
<div class="glow-on-hover" style="display:flex;margin-top:40px;background:var(--card);border-radius:24px;border:1px solid var(--bl);overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,.05); transition:box-shadow .3s;">
    <div style="flex:1;padding:40px;border-right:1px solid var(--bl);">
        <div style="font-family:'Playfair Display',serif;font-size:56px;font-weight:900;color:var(--ink);">$0.041</div>
        <div class="mono" style="font-size:12px;color:var(--mute);margin-bottom:20px;">LCOE (USD/kWh) OVER 25 YRS</div>
        <p style="font-size:14px;line-height:1.6;color:var(--body);">Calculated using NREL SAM model factoring 6% discount rate, module degradation, and battery replacement at year 15.</p>
    </div>
    <div style="flex:1;padding:40px;background:#fff;">
        <h4 style="font-size:16px;margin-bottom:20px;">Tariff Comparison (KES/kWh)</h4>
        <div style="margin-bottom:20px;">
            <div style="display:flex;justify-content:space-between;font-size:13px;font-weight:700;margin-bottom:4px;"><span>KPLC (Avg)</span><span>26.50</span></div>
            <div class="bar-w"><div class="bar-f" style="width:100%;height:16px;background:linear-gradient(90deg,#94A3B8,#1E293B);"></div></div>
        </div>
        <div style="margin-bottom:20px;">
            <div style="display:flex;justify-content:space-between;font-size:13px;font-weight:700;margin-bottom:4px;color:var(--td);"><span>Angawatch Tariff</span><span>9.00</span></div>
            <div class="bar-w"><div class="bar-f" style="width:34%;height:16px;background:linear-gradient(90deg,var(--tl),var(--td));"></div></div>
        </div>
        <div style="display:flex;justify-content:space-between;font-size:13px;font-weight:700;margin-bottom:4px;color:#16A34A;"><span>Our LCOE Cost</span><span>5.50</span></div>
        <div class="bar-w"><div class="bar-f" style="width:20%;height:16px;background:#22C55E;"></div></div>
    </div>
</div>
</div></div>
"""
    slides.append(s58)

    # Slide 59: Payback & ROI
    s59 = f"""
<div class="s" id="s59">{generate_header("05.14 · Payback & ROI")}
<div class="pad rv slideFromLeft">
<div class="g2" style="align-items:center;">
    <div style="background:var(--td);color:#fff;padding:40px;border-radius:32px;text-align:center;">
        <div style="font-family:'Playfair Display',serif;font-size:72px;font-weight:700;margin-bottom:10px;">6.8</div>
        <div class="mono" style="font-size:14px;color:var(--tl);margin-bottom:20px;">YEARS PAYBACK</div>
        <p style="font-size:14px;opacity:0.9;">Project IRR: 14.2%<br>NPV @ 8%: KES 450M</p>
    </div>
    <div>
        <h3 style="font-size:32px;margin-bottom:20px;font-weight:700;">Financial Engine.</h3>
        <p style="font-size:16px;line-height:1.7;color:var(--body);margin-bottom:20px;padding-right:20px;">The margin between KES 5.50 (cost) and KES 9.00 (sale) generated across 18.6 MWh daily yields a profound cash flow. This margin fully covers the SACCO administration, security, landscaping, and water pumping for the entire town. <br><br><strong style="color:var(--ink);">The energy pays for the city's maintenance.</strong></p>
    </div>
</div>
</div></div>
"""
    slides.append(s59)

    # Slide 60: M-Pesa Integration
    s60 = f"""
<div class="s" id="s60">{generate_header("05.15 · Billing Architecture")}
<div class="pad rv scaleIn">
<div class="t1">M-Pesa Smart Metering.</div>
<div style="display:flex; gap:20px; margin-top:40px; flex-wrap:wrap;">
    <!-- Meter -->
    <div class="card transform-up" style="flex:1;text-align:center;">
        <div style="font-size:40px;margin-bottom:16px;">⏱️</div>
        <h3 style="font-weight:700;margin-bottom:8px;">Smart Meters</h3>
        <p style="font-size:13px;color:var(--mute);">Hexing / Shenzen LoRaWAN IoT meters on every door.</p>
    </div>
    <!-- Server -->
    <div class="card transform-up" style="flex:1;text-align:center;">
        <div style="font-size:40px;margin-bottom:16px;">📡</div>
        <h3 style="font-weight:700;margin-bottom:8px;">Head-End System</h3>
        <p style="font-size:13px;color:var(--mute);">Local server processes meter data every 15 minutes.</p>
    </div>
    <!-- M-pesa -->
    <div class="card transform-up" style="flex:1;text-align:center;border-color:#16A34A;">
        <div style="font-size:40px;margin-bottom:16px;">📱</div>
        <h3 style="font-weight:700;color:#16A34A;margin-bottom:8px;">M-Pesa Daraja API</h3>
        <p style="font-size:13px;color:var(--mute);">Paybill integration. Tokens instantly sent to meter via LoRa.</p>
    </div>
</div>
<div style="margin-top:30px;padding:20px;background:var(--tl);border-radius:12px;font-size:14px;color:var(--td);text-align:center;font-weight:600;">NO VENDORS. NO COMMISSIONS. 100% OF REVENUE STAYS IN THE COOPERATIVE.</div>
</div></div>
"""
    slides.append(s60)

    # Slide 61: Hardware Bill of Materials
    s61 = f"""
<div class="s" id="s61">{generate_header("05.16 · Energy BoM")}
<div class="pad rv unfold">
<div class="t1">Key Equipment Specifications.</div>
<table class="dt" style="margin-top:20px; font-size:13px;">
    <tr style="background:var(--ink);color:#fff;"><th>Component</th><th>Specification</th><th>Supplier Ecosystem</th></tr>
    <tr><td><strong style="color:var(--td)">Solar Modules</strong></td><td>580W N-Type TOPCon Bifacial (6,206 units)</td><td>Jinko / LONGi / Trina</td></tr>
    <tr><td><strong style="color:var(--td)">BESS Enclosures</strong></td><td>3.2 MWh Liquid-Cooled LFP Containers (x2)</td><td>Huawei / Sungrow / CATL</td></tr>
    <tr><td><strong style="color:var(--td)">String Inverters</strong></td><td>300kW Max 1500V DC (x22 units)</td><td>Huawei SUN2000 / Sungrow SG350</td></tr>
    <tr><td><strong style="color:var(--td)">Mounting</strong></td><td>Galvanized Steel, 15\u00b0 Tilt, Ground Mount</td><td>Schletter / Local Fabricators</td></tr>
    <tr><td><strong style="color:var(--td)">Smart Meters</strong></td><td>STS Compliant, LoRaWAN module</td><td>Hexing / Conlog</td></tr>
    <tr><td><strong style="color:var(--td)">Transformer</strong></td><td>12 MVA 1000/415V/11kV Step-up</td><td>ABB / Schneider / Local KPLC spec</td></tr>
</table>
</div></div>
"""
    slides.append(s61)

    # Slide 62: The Dark Day Protocol
    s62 = f"""
<div class="s" id="s62" style="background:#0F172A;color:#fff;">{generate_header("05.17 · Emergency Protocol")}
<div class="pad rv slideFromRight" style="padding-top:100px;">
<div style="border-left:8px solid #EF4444;padding-left:40px;">
    <div style="font-family:'Playfair Display',serif;font-size:64px;font-weight:900;margin-bottom:20px;color:#EF4444;">The 'Dark Day' Protocol.</div>
    <ul style="font-size:20px;line-height:2;color:#CBD5E1;list-style:none;padding:0;">
        <li style="margin-bottom:16px;"><strong>Level 1 (BESS < 30%):</strong> Automatic non-critical load shed (streetlights dim 50%, YattaFarm pumps halt).</li>
        <li style="margin-bottom:16px;"><strong>Level 2 (BESS < 20%):</strong> ATS engages KPLC intertie. Grid charges BESS at max 1MW.</li>
        <li style="margin-bottom:16px;"><strong>Level 3 (Grid down + BESS < 10%):</strong> Automatic startup of 1.5MVA standby diesel genset. Prioritizes clinic, security, and residential core circuits.</li>
        <li style="margin-bottom:16px;color:#FCA5A5;font-weight:700;">Zero blackouts. No matter the weather. No matter the grid.</li>
    </ul>
</div>
</div></div>
"""
    slides.append(s62)

    return slides

