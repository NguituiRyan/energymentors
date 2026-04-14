from utils import generate_header

def generate():
    slides = []

    # Slide 69: Community Opener
    s69 = """
<!-- ═══════════════ ACT VII: COMMUNITY & ECONOMY ═══════════════ -->
<div class="s" style="min-height:60vh;background:linear-gradient(135deg,var(--td),#047857);display:flex;align-items:center;justify-content:center;text-align:center;color:#fff">
<div class="rv unfold">
<div class="mono" style="font-size:14px;letter-spacing:.3em;color:var(--tl);margin-bottom:24px">Section 07 · Ecosystem</div>
<div style="font-family:'Playfair Display',serif;font-size:80px;font-weight:900;margin-bottom:16px;">The Socio-Economic Engine.</div>
<div style="font-size:24px;color:rgba(255,255,255,.9)">Schools, clinics, EVs, and data connectivity.</div>
</div>
</div>
"""
    slides.append(s69)

    # Slide 70: YattaFarm & Food Security
    s70 = f"""
<div class="s" id="s70">{generate_header("07.01 · YattaFarm")}
<div class="pad rv slideFromLeft">
<div class="t1">20 Hectares of Food Security.</div>
<div class="g2">
    <div>
        <p class="intro">A centralized, cooperatively managed high-yield agricultural zone powered by solar irrigation and nutrient-rich greywater.</p>
        <ul style="font-size:15px;line-height:1.8;padding-left:20px;margin-top:20px;">
            <li><strong>Crop Profile:</strong> High-margin horticulture (tomatoes, onions, capsicum) + staple drought-resistant grains.</li>
            <li><strong>Cooling:</strong> On-site solar cold storage eliminates 40% post-harvest loss.</li>
            <li><strong>Economy:</strong> Sold directly at the Angawatch market hub. Surpluses sold to Machakos.</li>
        </ul>
    </div>
    <div class="card transform-up" style="border-top:6px solid #166534;background:#FEFCE8;border-color:#FEF08A;">
        <h3 style="font-family:'Playfair Display',serif;font-size:32px;color:#166534;margin-bottom:12px;">Circular Yields</h3>
        <div class="kv"><span class="k">Fertilizer Source</span><span class="v" style="color:#166534;">Digester NPK Slurry</span></div>
        <div class="kv"><span class="k">Water Source</span><span class="v" style="color:#166534;">Greywater Loop</span></div>
        <div class="kv"><span class="k">Revenue Flow</span><span class="v" style="color:#166534;font-weight:700;">SACCO Retained</span></div>
    </div>
</div>
</div></div>
"""
    slides.append(s70)

    # Slide 71: Education & Healthcare
    s71 = f"""
<div class="s" id="s71">{generate_header("07.02 · Social Anchors")}
<div class="pad rv scaleIn">
<div class="g2">
    <!-- School -->
    <div class="card transform-up" style="border-left:8px solid var(--tb);">
        <h3 style="font-size:24px;margin-bottom:16px;">The Angawatch Academy</h3>
        <p style="font-size:14px;color:var(--mute);margin-bottom:20px;">Primary & Secondary campus serving 1,200 students. Anchoring the Deputy Principal archetype.</p>
        <div class="kv"><span class="k">Class Size</span><span class="v" style="font-weight:700;">30 Max</span></div>
        <div class="kv"><span class="k">Labs</span><span class="v">100% Solar Powered</span></div>
        <div class="kv"><span class="k">Internet</span><span class="v">Starlink / Fiber node</span></div>
    </div>
    <!-- Clinic -->
    <div class="card transform-up" style="border-left:8px solid #EF4444;">
        <h3 style="font-size:24px;margin-bottom:16px;">Level 3 Health Centre</h3>
        <p style="font-size:14px;color:var(--mute);margin-bottom:20px;">50-bed maternity and outpatient clinic. Anchoring the Rural Nurse archetype.</p>
        <div class="kv"><span class="k">Uptime</span><span class="v" style="font-weight:700;color:#EF4444;">99.9% (Triple Redundant)</span></div>
        <div class="kv"><span class="k">Sterilization</span><span class="v">Electric Autoclaves</span></div>
        <div class="kv"><span class="k">Cold Chain</span><span class="v">Vaccine refrigerators guarantee</span></div>
    </div>
</div>
</div></div>
"""
    slides.append(s71)

    # Slide 72: High Speed Connectivity
    s72 = f"""
<div class="s" id="s72">{generate_header("07.03 · Connectivity")}
<div class="pad rv slideFromRight">
<div class="t1">The Fiber-Wireless Grid.</div>
<div class="intro">Smart meters demand reliable backhaul. Residents demand modern broadband. We deploy a unified network.</div>
<div style="display:flex;gap:40px;margin-top:40px;align-items:center;">
    <div style="flex:1;">
        <div style="border-left:4px solid var(--td);padding-left:16px;margin-bottom:24px;">
            <h4 style="font-weight:700;font-size:18px;">Backbone: Starlink + NOFBI</h4>
            <p style="font-size:14px;color:var(--mute);">Dual-WAN load balancing. National Optic Fibre Backbone connection supplemented by Starlink Business for 100% resilience.</p>
        </div>
        <div style="border-left:4px solid var(--tb);padding-left:16px;">
            <h4 style="font-weight:700;font-size:18px;">Last Mile: Wi-Fi 6 + LoRa</h4>
            <p style="font-size:14px;color:var(--mute);">Commercial Wi-Fi mesh across apartment blocks for resident broadband subscriptions. Dedicated LoRaWAN for smart meters avoids Wi-Fi congestion.</p>
        </div>
    </div>
    <div style="flex:1;background:#0F172A;padding:40px;border-radius:24px;text-align:center;">
        <div style="font-family:'Playfair Display',serif;font-size:64px;font-weight:700;color:#38BDF8;">1 Gbps</div>
        <div class="mono" style="font-size:12px;color:var(--mute);">COMMUNITY INGEST CAPACITY</div>
    </div>
</div>
</div></div>
"""
    slides.append(s72)

    # Slide 73: E-Mobility Fleet
    s73 = f"""
<div class="s" id="s73">{generate_header("07.04 · E-Mobility")}
<div class="pad rv unfold">
<div class="t1" style="color:var(--td);">Electric Fleet Integration.</div>
<div class="g2">
    <div>
        <p class="intro">Solving the Transport Poverty archetype via the Roam / BasiGo ecosystem. Fully charged via midday solar surplus.</p>
        <div style="background:var(--card);padding:24px;border-radius:16px;margin-top:20px;border-left:4px solid #F59E0B;">
            <h4 style="font-weight:700;font-size:16px;margin-bottom:8px;">Roam Air (E-Boda) Hub</h4>
            <p style="font-size:14px;line-height:1.5;">Battery swap station located at the Commercial Hub. 100 batteries charged exactly during peak solar irradiance (10:00-14:00).</p>
        </div>
        <div style="background:var(--card);padding:24px;border-radius:16px;margin-top:20px;border-left:4px solid #3B82F6;">
            <h4 style="font-weight:700;font-size:16px;margin-bottom:8px;">E-Matatu Route (Machakos-Nairobi)</h4>
            <p style="font-size:14px;line-height:1.5;">Dedicated 60kW DC fast chargers for 4 co-op owned E-Matatus. Reduces daily resident commute cost by 40%.</p>
        </div>
    </div>
    <div style="text-align:center;display:flex;align-items:center;justify-content:center;">
        <svg viewBox="0 0 200 200" width="100%" height="auto">
            <circle cx="100" cy="100" r="80" fill="none" stroke="var(--bl)" stroke-width="2"/>
            <!-- Arc representing solar charging curve -->
            <path d="M40 100 A60 60 0 0 1 160 100" stroke="#F59E0B" stroke-width="8" fill="none"/>
            <text x="100" y="80" class="mono" style="font-size:12px;font-weight:700;fill:#F59E0B;text-anchor:middle">CHARGING</text>
            <text x="100" y="95" class="mono" style="font-size:10px;fill:var(--mute);text-anchor:middle">10:00 - 15:00</text>
        </svg>
    </div>
</div>
</div></div>
"""
    slides.append(s73)

    # Slide 74: Solid Waste
    s74 = f"""
<div class="s" id="s74">{generate_header("07.05 · Solid Waste")}
<div class="pad rv scaleIn">
<div class="t1">Zero-Landfill Philosophy.</div>
<div style="display:flex;gap:20px;margin-top:40px;">
    <div class="card transform-up" style="flex:1;border-top:4px solid #10B981;text-align:center;">
        <div style="font-size:32px;margin-bottom:12px;">♻️</div>
        <h4 style="font-weight:700;margin-bottom:10px">Organic (60%)</h4>
        <p style="font-size:13px;color:var(--mute);">Directly blended into the anaerobic digester network alongside blackwater and farm waste. Maximizes biogas yield.</p>
    </div>
    <div class="card transform-up" style="flex:1;border-top:4px solid #3B82F6;text-align:center;">
        <div style="font-size:32px;margin-bottom:12px;">📦</div>
        <h4 style="font-weight:700;margin-bottom:10px">Plastics / Metals (25%)</h4>
        <p style="font-size:13px;color:var(--mute);">Source-separated at Ekeja clusters. Processed at Jua Kali zone using solar-powered shredders / balers. Sold to Nairobi recyclers.</p>
    </div>
    <div class="card transform-up" style="flex:1;border-top:4px solid #EF4444;text-align:center;">
        <div style="font-size:32px;margin-bottom:12px;">🔥</div>
        <h4 style="font-weight:700;margin-bottom:10px">Residual (15%)</h4>
        <p style="font-size:13px;color:var(--mute);">High-temperature medical incinerator at the Health Centre (with scrubber) safely destroys biohazards and non-recyclables.</p>
    </div>
</div>
</div></div>
"""
    slides.append(s74)

    # Slide 75: Security & Lighting
    s75 = f"""
<div class="s" id="s75">{generate_header("07.06 · Security")}
<div class="pad rv slideFromRight">
<div class="t1">Lit. Patrolled. Secured.</div>
<div class="g2" style="background:#1E293B;color:#fff;border-radius:32px;padding:40px;margin-top:40px;gap:60px;">
    <div>
        <h3 style="font-size:24px;margin-bottom:16px;color:#FCD34D;">Perimeter & Street Lighting</h3>
        <p style="font-size:15px;line-height:1.7;color:#cbd5e1;margin-bottom:20px;">900 LED streetlights integrated into the DC microgrid. Not susceptible to isolated solar-streetlight battery theft. Controlled centrally via SCADA.</p>
        <div style="display:flex;align-items:center;gap:16px;">
            <div style="width:40px;height:40px;border-radius:50%;background:#FCD34D;box-shadow:0 0 30px rgba(252,211,77,.5);"></div>
            <span class="mono" style="font-size:12px;">40W LED · 50M SPACING</span>
        </div>
    </div>
    <div>
        <h3 style="font-size:24px;margin-bottom:16px;color:#38BDF8;">Smart Surveillance</h3>
        <p style="font-size:15px;line-height:1.7;color:#cbd5e1;margin-bottom:20px;">CCTV network covering the 4.5km perimeter wire and all Ekeja cluster access control points. Powered directly from the optical fiber network (PoE) with battery backup.</p>
    </div>
</div>
</div></div>
"""
    slides.append(s75)

    # Slide 76: Governance
    s76 = f"""
<div class="s" id="s76">{generate_header("07.07 · SACCO Governance")}
<div class="pad rv scaleIn">
<div class="t1">The Cooperative Model.</div>
<div class="intro">Infrastructure this profound cannot be managed by a standard HOA. It requires the financial and legal structure of a Savings and Credit Cooperative Organization (SACCO).</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:40px;">
    <div class="card" style="border-left:6px solid var(--td);">
        <h4 style="font-weight:700;font-size:18px;margin-bottom:8px;">Equity Ownership</h4>
        <p style="font-size:14px;color:var(--mute);line-height:1.6;">Every resident buys a share in the Angawatch SACCO. The SACCO owns the microgrid, the water plant, and the YattaFarm. Profits are paid as dividends or tariff subsidies.</p>
    </div>
    <div class="card" style="border-left:6px solid var(--tb);">
        <h4 style="font-weight:700;font-size:18px;margin-bottom:8px;">Asset Management</h4>
        <p style="font-size:14px;color:var(--mute);line-height:1.6;">The SACCO employs a full-time engineering and landscaping team. O&M contracts for the Huawei BESS and solar arrays are centralized.</p>
    </div>
    <div class="card" style="border-left:6px solid #F59E0B;">
        <h4 style="font-weight:700;font-size:18px;margin-bottom:8px;">Default Protection</h4>
        <p style="font-size:14px;color:var(--mute);line-height:1.6;">Shared liability. Smart meters can dynamically cap power to tier-1 baseline (lights/fridge) if cooperative dues are delayed, rather than complete shutoff.</p>
    </div>
    <div class="card" style="border-left:6px solid #3B82F6;">
        <h4 style="font-weight:700;font-size:18px;margin-bottom:8px;">KMRC Alignment</h4>
        <p style="font-size:14px;color:var(--mute);line-height:1.6;">KMRC distributes wholesale mortgage funds through SACCOs. The Angawatch SACCO is the perfect vessel for taking 5% wholesale funds and distributing 8.99% mortgages.</p>
    </div>
</div>
</div></div>
"""
    slides.append(s76)

    return slides
