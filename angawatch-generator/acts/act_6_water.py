from utils import generate_header

def generate():
    slides = []

    # Slide 63: Water Opener
    s63 = """
<!-- ═══════════════ ACT VI: WATER & SANITATION ═══════════════ -->
<div class="s" style="min-height:60vh;background:linear-gradient(135deg,#0369A1,#0ea5e9);display:flex;align-items:center;justify-content:center;text-align:center;color:#fff">
<div class="rv scaleIn">
<div class="mono" style="font-size:14px;letter-spacing:.3em;color:var(--tl);margin-bottom:24px">Section 06 · The Water Cycle</div>
<div style="font-family:'Playfair Display',serif;font-size:80px;font-weight:900;margin-bottom:16px;text-shadow:0 10px 30px rgba(0,0,0,.2);">Gravity, Biology, Solar.</div>
<div style="font-size:24px;color:rgba(255,255,255,.9)">Zero diesel pumping. Zero raw wastewater discharge.</div>
<svg class="draw on" width="100%" height="200" viewBox="0 0 1000 200" style="margin-top:40px;opacity:.2">
    <!-- Water wave abstract -->
    <path class="sankey-flow" d="M0 100 Q 125 50 250 100 T 500 100 T 750 100 T 1000 100" fill="none" stroke="#fff" stroke-width="4"/>
    <path class="sankey-flow" d="M0 120 Q 125 70 250 120 T 500 120 T 750 120 T 1000 120" fill="none" stroke="#fff" stroke-width="2"/>
</svg>
</div>
</div>
"""
    slides.append(s63)

    # Slide 64: Water Demand Profile
    s64 = f"""
<div class="s" id="s64">{generate_header("06.01 · Demand Profile")}
<div class="pad rv slideFromRight">
<div class="t1">Water Demand Matrix.</div>
<div class="g2" style="margin-top:40px;">
    <!-- Values -->
    <div style="padding-right:20px;">
        <h3 style="font-size:20px;font-weight:700;margin-bottom:16px;">Daily Volumetric Need</h3>
        <p style="font-size:15px;line-height:1.7;color:var(--body);margin-bottom:20px;">Calculated using WHO baseline of 100 Liters Per Capita per Day (LPCD).</p>
        <div class="kv"><span class="k">Residential (8,090 pax)</span><span class="v" style="color:#0ea5e9;font-weight:700;">809,000 L/day</span></div>
        <div class="kv"><span class="k">Commercial & CHC</span><span class="v" style="color:var(--ink);">50,000 L/day</span></div>
        <div class="kv"><span class="k">System Losses (5%)</span><span class="v" style="color:#EF4444;">~43,000 L/day</span></div>
        <div class="kv" style="border-top:2px solid var(--ink);margin-top:20px;"><span class="k" style="font-weight:700;color:var(--ink);">Total Daily Demand</span><span class="v" style="font-size:24px;color:#0ea5e9;font-weight:700;">902 m\u00b3 / day</span></div>
    </div>
    
    <!-- Yatta farm intro -->
    <div class="card transform-up" style="background:#F8FAFC;border-top:6px solid #166534;border-color:#166534;">
        <h3 style="font-size:24px;font-weight:700;margin-bottom:12px;color:#166534">YattaFarm Irrigation</h3>
        <p style="font-size:15px;line-height:1.6;margin-bottom:20px;">The 20-hectare intensive agriculture zone is decoupled from the potable system.</p>
        <div class="mono" style="font-size:12px;color:#064E3B;margin-bottom:8px;">IRRIGATION SOURCE</div>
        <div style="font-size:20px;font-weight:700;color:#15803D;margin-bottom:20px;">Greywater + Direct Canal</div>
        <p style="font-size:14px;color:var(--mute);">Agricultural demand peaks at 960 m\u00b3/day. Met almost entirely via nutrient-rich polished greywater.</p>
    </div>
</div>
</div></div>
"""
    slides.append(s64)

    # Slide 65: Sourcing Canal
    s65 = f"""
<div class="s" id="s65">{generate_header("06.02 · Intake Topology")}
<div class="pad rv unfold">
<div class="t1">The Yatta Canal Intake.</div>
<div class="g2" style="align-items:center;">
    <div style="background:var(--card);border-radius:32px;padding:40px;text-align:center;border:1px solid var(--bl);">
        <svg viewBox="0 0 100 100" width="120" height="120" style="margin-bottom:20px;">
            <!-- Canal to pipe abstract -->
            <path d="M10 50 Q 50 20 90 50 T 170 50" stroke="#0ea5e9" stroke-width="8" fill="none"/>
            <circle cx="50" cy="50" r="15" fill="var(--td)"/>
        </svg>
        <div style="font-family:'Playfair Display',serif;font-size:64px;font-weight:700;color:#0ea5e9;">0.4%</div>
        <div class="mono" style="font-size:14px;color:var(--mute);margin-top:10px;">OF CANAL FLOW REQUIRED</div>
    </div>
    <div>
        <p class="intro">Located 2km west, the permanent Yatta Canal flows at ~3.0 cubic meters per second. Our 902 m\u00b3/day extraction requires less than half a percent of its capacity.</p>
        <ul style="font-size:15px;line-height:1.8;padding-left:20px;margin-top:20px;">
            <li><strong>Intake:</strong> Submerged sump with coarse filtration screen</li>
            <li><strong>Pumping:</strong> 45kW Solar VP Pump (Lorentz)</li>
            <li><strong>Schedule:</strong> Pumps strictly between 09:00 - 15:00 using dedicated direct-drive solar array (No battery strain).</li>
            <li><strong>Storage:</strong> 2,000 m\u00b3 elevated pressed steel tank (2 days autonomy)</li>
        </ul>
    </div>
</div>
</div></div>
"""
    slides.append(s65)

    # Slide 66: Treatment Architecture
    s66 = f"""
<div class="s" id="s66">{generate_header("06.03 · Potable Treatment")}
<div class="pad rv scaleIn">
<div class="t1">Potable Treatment Module.</div>
<div class="glow-on-hover" style="background:#1E293B;color:#fff;border-radius:32px;padding:40px;margin-top:40px;display:flex;justify-content:space-between;align-items:center; transition:box-shadow .3s;">
    <!-- Treatment flow -->
    <div class="card" style="background:#0F172A;border-color:#334155;text-align:center;flex:1;margin:0 10px;">
        <div class="mono" style="color:var(--mute);margin-bottom:8px;">STAGE 1</div>
        <h4 style="font-size:16px;font-weight:700;color:#38BDF8;">Flocculation</h4>
        <p style="font-size:12px;color:#94A3B8;margin-top:10px;">Removal of canal turbidity</p>
    </div>
    <div style="color:#334155;">\u279c</div>
    <div class="card" style="background:#0F172A;border-color:#334155;text-align:center;flex:1;margin:0 10px;">
        <div class="mono" style="color:var(--mute);margin-bottom:8px;">STAGE 2</div>
        <h4 style="font-size:16px;font-weight:700;color:#38BDF8;">Sand Filter</h4>
        <p style="font-size:12px;color:#94A3B8;margin-top:10px;">Rapid gravity polishing</p>
    </div>
    <div style="color:#334155;">\u279c</div>
    <div class="card" style="background:#0F172A;border-color:#334155;text-align:center;flex:1;margin:0 10px;">
        <div class="mono" style="color:var(--mute);margin-bottom:8px;">STAGE 3</div>
        <h4 style="font-size:16px;font-weight:700;color:#38BDF8;">RO + UV</h4>
        <p style="font-size:12px;color:#94A3B8;margin-top:10px;">Pathogen / Heavy metal clearing</p>
    </div>
    <div style="color:#334155;">\u279c</div>
    <div class="card" style="background:#0F172A;border-color:var(--td);text-align:center;flex:1;margin:0 10px;border-width:2px;">
        <div class="mono" style="color:var(--tb);margin-bottom:8px;">FINAL</div>
        <h4 style="font-size:16px;font-weight:700;color:#fff;">Gravity Dist.</h4>
        <p style="font-size:12px;color:#94A3B8;margin-top:10px;">Pressurized via tower</p>
    </div>
</div>
</div></div>
"""
    slides.append(s66)

    # Slide 67: Waste & Biogas
    s67 = f"""
<div class="s" id="s67">{generate_header("06.04 · Wastewater as Asset")}
<div class="pad rv slideFromLeft">
<div class="g2">
    <div>
        <div class="t1">The Digester Core.</div>
        <div class="intro">Blackwater is not waste; it is a critical energy feedstock.</div>
        <p style="font-size:15px;line-height:1.7;color:var(--body);margin-top:20px;">All blackwater (WC effluent) feeds into three massive decentralized anaerobic dome digesters.</p>
        <div class="kv" style="margin-top:20px;"><span class="k">Gas Yield</span><span class="v" style="color:#F59E0B;font-weight:700;">220 m\u00b3 / day</span></div>
        <div class="kv"><span class="k">Equivalent Energy</span><span class="v">1,320 kWh / day</span></div>
        <div class="kv"><span class="k">End Use</span><span class="v" style="color:var(--td);">Institutions & Phase 2 Homes</span></div>
    </div>
    <div style="background:#F8FAFC;border-radius:32px;padding:40px;border:1px solid var(--bl);">
        <svg viewBox="0 0 300 250" width="100%" height="auto">
            <!-- Digester Dome Abstract -->
            <path d="M50 200 C 50 100, 250 100, 250 200 Z" fill="#D97706"/>
            <rect x="50" y="200" width="200" height="20" fill="#1E293B"/>
            <!-- In -->
            <path class="sankey-flow" d="M0 180 L50 180" stroke="#1E293B" stroke-width="4"/>
            <text x="20" y="170" class="mono" style="font-size:10px;text-anchor:middle;">IN</text>
            <!-- Out (Gas) -->
            <path class="sankey-flow" d="M150 115 L150 50 L250 50" stroke="#F59E0B" stroke-width="4" fill="none"/>
            <text x="200" y="40" class="mono" style="font-size:10px;fill:#F59E0B;text-anchor:middle;">CH4 TO KITCHENS</text>
            <!-- Out (Slurry) -->
            <path class="sankey-flow" d="M250 190 L300 190" stroke="#713F12" stroke-width="4" fill="none"/>
            <text x="280" y="180" class="mono" style="font-size:10px;fill:#713F12;text-anchor:middle;">NPK FERTILIZER</text>
        </svg>
    </div>
</div>
</div></div>
"""
    slides.append(s67)

    # Slide 68: Greywater & YattaFarm
    s68 = f"""
<div class="s" id="s68">{generate_header("06.05 · Greywater Loop")}
<div class="pad rv scaleIn">
<div class="t1" style="text-align:center;">Closing the Loop: YattaFarm.</div>
<div class="card" style="margin-top:40px;background:#FEFCE8;border:1px solid #FEF08A;text-align:center;">
    <h3 style="font-family:'Playfair Display',serif;font-size:28px;color:#A16207;margin-bottom:20px;">600,000 Liters Daily</h3>
    <p style="font-size:16px;color:#713F12;line-height:1.6;max-width:800px;margin:0 auto 30px;">Greywater (showers, sinks) bypasses the digester. It is routed through constructed reed-bed wetlands, physically polished, and pumped to YattaFarm via solar drip irrigation.</p>
    <div style="display:flex;justify-content:center;gap:40px;">
        <div style="text-align:center;">
            <div style="font-size:40px">🚿</div>
            <div class="mono" style="font-size:12px;color:#ca8a04;margin-top:10px;font-weight:700">SHOWER</div>
        </div>
        <div style="color:var(--bm);font-size:32px;display:flex;align-items:center;">\u2192</div>
        <div style="text-align:center;">
            <div style="font-size:40px">🌿</div>
            <div class="mono" style="font-size:12px;color:#ca8a04;margin-top:10px;font-weight:700">WETLAND POLISH</div>
        </div>
        <div style="color:var(--bm);font-size:32px;display:flex;align-items:center;">\u2192</div>
        <div style="text-align:center;">
            <div style="font-size:40px">🌽</div>
            <div class="mono" style="font-size:12px;color:#ca8a04;margin-top:10px;font-weight:700">YATTAFARM</div>
        </div>
    </div>
</div>
</div></div>
"""
    slides.append(s68)

    return slides
