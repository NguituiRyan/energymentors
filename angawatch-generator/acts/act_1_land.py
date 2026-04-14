from utils import generate_header

def generate():
    slides = []

    # Slide 5: The Land - Full Width
    s5 = """
<!-- ═══════════════ ACT I: THE LAND ═══════════════ -->
<div class="s" style="min-height:80vh;background:linear-gradient(135deg,var(--td),#064E3B);display:flex;align-items:center;justify-content:center;padding:0">
<svg class="draw on" style="position:absolute;inset:0;width:100%;height:100%;opacity:.12;pointer-events:none" viewBox="0 0 1000 500" preserveAspectRatio="none"><path class="sankey-flow" d="M0 250Q250 100 500 250T1000 250" fill="none" stroke="#fff" stroke-width="1.5"/><path class="sankey-flow" d="M0 300Q250 150 500 300T1000 300" fill="none" stroke="#fff" stroke-width="1"/><path class="sankey-flow" d="M0 350Q250 200 500 350T1000 350" fill="none" stroke="#fff" stroke-width="2"/></svg>
<div class="rv scaleIn" style="position:relative;z-index:2;text-align:center;color:#fff">
<div class="mono" style="font-size:14px;letter-spacing:.3em;text-transform:uppercase;color:var(--tl);margin-bottom:24px">Section 01 · The Land</div>
<div style="font-family:'Playfair Display',serif;font-size:clamp(64px,10vw,120px);font-weight:900;margin-bottom:16px;letter-spacing:-.02em;text-shadow:0 20px 40px rgba(0,0,0,.3)">1.17°S, 37.45°E</div>
<div class="mono" style="font-size:20px;letter-spacing:.2em;text-transform:uppercase;color:var(--tl)">Yatta Plateau · Machakos County · Kenya</div>
</div>
</div>
"""
    slides.append(s5)

    # Slide 6: Geolocation & Coordinates
    s6 = f"""
<div class="s" id="s6">{generate_header("01.01 · Geolocation")}
<div class="pad rv slideFromLeft">
<div class="t1">Connected, but <em>independent.</em></div>
<div class="intro">60km from Nairobi CBD via A109 highway. 25km from Athi River SGR station. Strategic proximity to infrastructure without the cost burden of the metropolis. Elevation: 1,450\u20131,550m ASL.</div>
<div class="draw on" style="position:relative;height:400px;background:var(--card);border-radius:32px;border:1px solid var(--bl);overflow:hidden;margin-top:40px;box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
<svg style="width:100%;height:100%;position:absolute;inset:0;z-index:1" viewBox="0 0 1000 400"><path class="sankey-flow" d="M150 320Q300 320 450 200T750 120" fill="none" stroke="var(--tl)" stroke-width="8" stroke-dasharray="16 16"/></svg>
<div class="transform-scale" style="position:absolute;z-index:2;left:15%;top:75%;transform:translate(-50%,-50%);text-align:center;transition:scale 0.3s;"><div style="width:24px;height:24px;border-radius:50%;background:#fff;border:4px solid var(--ink);margin:0 auto 8px"></div><div style="background:rgba(255,255,255,.9);padding:6px 14px;border-radius:8px;font-weight:700;font-size:13px">Nairobi CBD</div></div>
<div class="transform-scale" style="position:absolute;z-index:2;left:40%;top:85%;transform:translate(-50%,-50%);text-align:center;transition:scale 0.3s;"><div style="width:20px;height:20px;border-radius:50%;background:#fff;border:4px solid #F59E0B;margin:0 auto 8px"></div><div style="background:rgba(255,255,255,.9);padding:6px 14px;border-radius:8px;font-weight:700;font-size:13px">Athi River SGR</div><div class="mono" style="font-size:11px;color:var(--td);margin-top:2px">25km</div></div>
<div class="transform-scale" style="position:absolute;z-index:2;left:72%;top:28%;transform:translate(-50%,-50%);text-align:center;transition:scale 0.3s;"><div style="width:32px;height:32px;border-radius:50%;background:var(--td);border:4px solid var(--tb);animation:pulse 2s infinite;margin:0 auto 8px"></div><div style="background:rgba(255,255,255,.95);padding:8px 16px;border-radius:8px;font-weight:700;font-size:14px">Angawatch Site</div><div class="mono" style="font-size:11px;color:var(--td);margin-top:2px">60km from CBD via A109</div></div>
</div>
</div></div>
"""
    slides.append(s6)

    # Slide 7: Verified Site Parameters
    s7 = f"""
<div class="s" id="s7">{generate_header("01.02 · Site Parameters")}
<div class="pad rv unfold">
<div class="dark glow-on-hover" style="transform:rotate(-1deg);max-width:900px;transition: transform 0.3s, box-shadow 0.3s;">
<div class="cross" style="top:20px;left:20px"></div><div class="cross" style="bottom:20px;right:20px"></div>
<div class="t1" style="color:#fff;margin-bottom:40px;border-bottom:1px solid rgba(255,255,255,.1);padding-bottom:24px">Verified Site Parameters</div>
<div class="g2">
<div>
<div class="kv"><span class="k">Google Earth Area</span><span class="v hi">101.9 ha</span></div>
<div class="kv"><span class="k">Perimeter</span><span class="v">4,508.92 m</span></div>
<div class="kv"><span class="k">Elevation Range</span><span class="v">1,273\u20131,326m ASL</span></div>
<div class="kv"><span class="k">Elevation Median</span><span class="v">1,298m ASL</span></div>
</div>
<div>
<div class="kv"><span class="k">Current Use</span><span class="v">Agricultural / Scrub</span></div>
<div class="kv"><span class="k">Solar Irradiance</span><span class="v hi">5.18 kWh/m\u00b2/day</span></div>
<div class="kv"><span class="k">Rainfall</span><span class="v">700\u2013900mm bimodal</span></div>
<div class="kv"><span class="k">Soil</span><span class="v">Basaltic laterite (Yatta Fm.)</span></div>
</div>
</div>
</div>
</div></div>
"""
    slides.append(s7)

    # Slide 8: Why This Exact Spot — 8 Reasons
    s8 = f"""
<div class="s" id="s8">{generate_header("01.03 · 8 Reasons")}
<div class="pad rv slideFromRight">
<div class="g2">
<div><div class="t1">Why this <em>exact spot.</em></div><div class="intro">Every constraint \u2014 affordability, energy, climate, water, soil, access \u2014 converges at these coordinates. Not a compromise. The mathematical optimum.</div></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
<div class="pill transform-scale"><div class="n">1</div><div><div style="font-weight:700;font-size:15px">Elevation</div><span class="mono" style="font-size:12px;color:var(--td)">Zero AC load (17\u201327\u00b0C)</span></div></div>
<div class="pill transform-scale"><div class="n">2</div><div><div style="font-weight:700;font-size:15px">Solar</div><span class="mono" style="font-size:12px;color:var(--td)">5.18 kWh/m\u00b2/day</span></div></div>
<div class="pill transform-scale"><div class="n">3</div><div><div style="font-weight:700;font-size:15px">Laterite Soil</div><span class="mono" style="font-size:12px;color:var(--td)">5% cement CSEB</span></div></div>
<div class="pill transform-scale"><div class="n">4</div><div><div style="font-weight:700;font-size:15px">Yatta Canal</div><span class="mono" style="font-size:12px;color:var(--td)">2km, gravity irr.</span></div></div>
<div class="pill transform-scale"><div class="n">5</div><div><div style="font-weight:700;font-size:15px">KPLC Substation</div><span class="mono" style="font-size:12px;color:var(--td)">4km grid link</span></div></div>
<div class="pill transform-scale"><div class="n">6</div><div><div style="font-weight:700;font-size:15px">A109 Highway</div><span class="mono" style="font-size:12px;color:var(--td)">Direct to Nairobi</span></div></div>
<div class="pill transform-scale"><div class="n">7</div><div><div style="font-weight:700;font-size:15px">Bimodal Rain</div><span class="mono" style="font-size:12px;color:var(--td)">700\u2013900mm/year</span></div></div>
<div class="pill transform-scale"><div class="n">8</div><div><div style="font-weight:700;font-size:15px">Thwake Dam</div><span class="mono" style="font-size:12px;color:var(--td)">20MW grid backup</span></div></div>
</div>
</div>
</div></div>
"""
    slides.append(s8)

    # Slide 9: Land Use Master Plan — 102 Hectares
    s9 = f"""
<div class="s" id="s9">{generate_header("01.04 · Master Plan")}
<div class="pad rv">
<div class="t1">102 Hectares. <em>Mapped.</em></div>
<div class="unfold" style="display:grid;grid-template-columns:repeat(12,1fr);grid-template-rows:repeat(6,56px);gap:10px;margin-top:40px">
<div class="zone" style="grid-column:span 5;grid-row:span 3;background:var(--td)"><div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700">Residential</div><div class="mono" style="font-size:13px;opacity:.9">37ha · 36%</div></div>
<div class="zone" style="grid-column:span 4;grid-row:span 4;background:#166534"><div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700">YattaFarm</div><div class="mono" style="font-size:13px;opacity:.9">20ha · 22%</div></div>
<div class="zone" style="grid-column:span 3;grid-row:span 2;background:#3B82F6"><div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700">Community Hub</div><div class="mono" style="font-size:12px;opacity:.9">12ha · 13%</div></div>
<div class="zone" style="grid-column:span 4;grid-row:span 2;background:#22C55E"><div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700">Green Space</div><div class="mono" style="font-size:12px;opacity:.9">10ha · 11%</div></div>
<div class="zone" style="grid-column:span 3;grid-row:span 2;background:#F59E0B"><div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700">Jua Kali</div><div class="mono" style="font-size:12px;opacity:.9">8ha · 9%</div></div>
<div class="zone" style="grid-column:span 3;grid-row:span 1;background:#64748B"><div class="mono" style="font-size:12px">Roads 7ha</div></div>
<div class="zone" style="grid-column:span 2;grid-row:span 1;background:#8B5CF6"><div class="mono" style="font-size:12px">Commercial 5ha</div></div>
<div class="zone" style="grid-column:span 2;grid-row:span 1;background:#EF4444"><div class="mono" style="font-size:12px">Energy 3ha</div></div>
</div>
</div></div>
"""
    slides.append(s9)

    # Slide 10: Nearby Infrastructure — Not Empty, Surrounded
    s10 = f"""
<div class="s" id="s10">{generate_header("01.05 · Surroundings")}
<div class="pad rv scaleIn">
<div class="t1">Not Empty. <em>Surrounded.</em></div>
<div class="ol-box glow-on-hover" style="background:#0F172A;border-radius:32px;padding:40px;min-height:400px;display:flex;align-items:center;justify-content:center;overflow:hidden;margin-top:20px;">
<svg class="draw on" viewBox="0 0 800 400" style="width:100%;height:100%">
<g transform="translate(400, 200)">
    <circle cx="0" cy="0" r="40" fill="var(--td)" />
    <text x="0" y="5" class="ol-tb" style="text-anchor:middle;">SITE</text>
    
    <!-- Nodes -->
    <path class="sankey-flow ol-line" d="M0,0 L-200,-100" />
    <circle cx="-200" cy="-100" r="20" class="ol-node" />
    <text x="-200" y="-130" class="ol-t">Kithimani Parish</text>
    <text x="-200" y="-70" class="ol-t" style="font-size:10px;fill:var(--tb)">Boundary</text>
    
    <path class="sankey-flow ol-line" d="M0,0 L200,-140" />
    <circle cx="200" cy="-140" r="20" class="ol-node" />
    <text x="200" y="-170" class="ol-t">Rimaal Prime Hospital</text>
    <text x="200" y="-110" class="ol-t" style="font-size:10px;fill:var(--tb)">Boundary</text>
    
    <path class="sankey-flow ol-line" d="M0,0 L-250,50" />
    <circle cx="-250" cy="50" r="20" class="ol-node" />
    <text x="-250" y="30" class="ol-t">Yatta Canal</text>
    <text x="-250" y="80" class="ol-t" style="font-size:10px;fill:var(--tb)">2km West</text>

    <path class="sankey-flow ol-line" d="M0,0 L-100,150" />
    <circle cx="-100" cy="150" r="20" class="ol-node" />
    <text x="-100" y="130" class="ol-t">A109 Highway</text>
    <text x="-100" y="180" class="ol-t" style="font-size:10px;fill:var(--tb)">West Edge</text>

    <path class="sankey-flow ol-line" d="M0,0 L150,150" />
    <circle cx="150" cy="150" r="20" class="ol-node" />
    <text x="150" y="130" class="ol-t">Matuu KPLC Substation</text>
    <text x="150" y="180" class="ol-t" style="font-size:10px;fill:var(--tb)">4km</text>
    
    <path class="sankey-flow ol-line" d="M0,0 L300,50" />
    <circle cx="300" cy="50" r="20" class="ol-node" />
    <text x="300" y="30" class="ol-t">Thwake Dam Phase I</text>
    <text x="300" y="80" class="ol-t" style="font-size:10px;fill:var(--tb)">50km SE</text>
</g>
</svg>
</div>
</div></div>
"""
    slides.append(s10)

    # Slide 11: The Clean Slate Advantage
    s11 = f"""
<div class="s" id="s11">{generate_header("01.06 · Construction Cost")}
<div class="pad rv slideFromRight">
<div class="glow-on-hover" style="background:linear-gradient(135deg,var(--tl),#fff);border-radius:32px;padding:64px;display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center;box-shadow:0 20px 40px rgba(0,0,0,.05); transition: box-shadow 0.3s;">
<div>
<div class="t1">The Clean Slate.</div>
<p style="font-size:16px;line-height:1.7;color:var(--body);margin-bottom:32px">No demolition. No relocation. Cable routes, drainage, and solar pitch optimized from first principles.</p>
<div style="font-family:'Playfair Display',serif;font-size:72px;font-weight:900;color:var(--td);line-height:1;margin-bottom:12px">46,500<span style="font-size:24px;opacity:.5"> KES/m\u00b2</span></div>
<div class="mono" style="font-size:12px;color:var(--td);font-weight:600">VAT-INCLUSIVE \u00b7 25\u201328% BELOW CONCRETE</div>
</div>
<div style="background:#fff;padding:32px;border-radius:24px;box-shadow:0 10px 20px rgba(0,0,0,.03)">
<div style="display:flex;align-items:center;margin-bottom:24px;gap:16px"><div style="width:140px;font-size:14px;font-weight:600">Nairobi Concrete</div><div class="bar-w"><div class="bar-f" style="width:100%;background:#EF4444"></div></div><div class="mono" style="font-size:12px;color:#EF4444">~120K</div></div>
<div style="display:flex;align-items:center;gap:16px"><div style="width:140px;font-size:14px;font-weight:600">Angawatch CSEB</div><div class="bar-w"><div class="bar-f" style="width:38%;background:var(--tb)"></div></div><div class="mono" style="font-size:12px;color:var(--td);font-weight:700">46.5K</div></div>
</div>
</div>
</div></div>
"""
    slides.append(s11)

    # Slide 12: Climate Profile
    s12 = f"""
<div class="s" id="s12">{generate_header("01.07 · Climate")}
<div class="pad rv slideFromLeft">
<div class="t1">Bimodal Rainfall. <em>Perfect Comfort.</em></div>
<div class="intro">Year-round temperatures 17\u201327\u00b0C (elevation eliminates cooling load). Rain: 700-900mm.</div>
<div class="card unfold" style="min-height: 300px; display:flex; align-items:flex-end; gap: 10px; padding: 20px 40px;">
    { "".join([f'<div style="flex:1; display:flex; flex-direction:column; align-items:center; justify-content:flex-end;"><div style="width:100%; max-width:40px; background:var(--tb); border-radius: 4px 4px 0 0; height:{h}px; transition: height 0.5s;"></div><div class="mono" style="margin-top:10px; font-size:10px;">{m}</div></div>' for m, h in zip(['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'], [40, 50, 100, 200, 150, 20, 10, 10, 20, 80, 180, 100])]) }
</div>
<div style="text-align:center; font-family:'DM Mono',monospace; font-size:12px; margin-top:20px; color:var(--mute);">Monthly Average Rainfall (mm equivalent). Horizontal temperature band: 17\u201327\u00b0C.</div>
</div></div>
"""
    slides.append(s12)

    # Slide 13: Solar Resource
    s13 = f"""
<div class="s" id="s13">{generate_header("01.08 · Solar Resource")}
<div class="pad rv scaleIn" style="text-align:center;">
<div class="t1">Solar Irradiance.</div>
<div class="intro" style="margin: 0 auto 40px auto;">Annual average 5.18 kWh/m\u00b2/day. PVGIS v5.2 verified.</div>
<div style="position:relative; width:400px; height:400px; margin: 0 auto;">
    <svg class="draw on" viewBox="0 0 100 100" style="width:100%; height:100%; filter: drop-shadow(0 0 30px rgba(20,184,166,0.3));">
        <!-- Sunburst abstract -->
        { "".join([f'<path d="M50 50 L{50 + 40 * __import__("math").cos(i * 3.14159 / 6)} {50 + 40 * __import__("math").sin(i * 3.14159 / 6)}" stroke="var(--tb)" stroke-width="2" class="sankey-flow"/>' for i in range(12)]) }
        <circle cx="50" cy="50" r="30" fill="var(--td)" />
    </svg>
    <div style="position:absolute; inset:0; display:flex; flex-direction:column; align-items:center; justify-content:center; color:#fff; pointer-events:none;">
        <div style="font-family:'Playfair Display', serif; font-size:48px; font-weight:900; line-height:1;">5.18</div>
        <div class="mono" style="font-size:12px; letter-spacing:0.1em; opacity:0.8;">kWh/m\u00b2/day</div>
    </div>
</div>
</div></div>
"""
    slides.append(s13)

    # Slide 14: Soil & Water Resources
    s14 = f"""
<div class="s" id="s14">{generate_header("01.09 · Soil & Water")}
<div class="pad rv">
<div class="t1">Earth and Water.</div>
<div class="g2" style="margin-top:40px;">
<div class="card transform-up" style="border-top:6px solid #8B5CF6; min-height: 250px;">
    <div style="font-family:'Playfair Display',serif;font-size:28px;font-weight:700;margin-bottom:10px;">Basaltic Laterite</div>
    <div class="mono" style="font-size:12px;color:var(--mute);margin-bottom:20px;">YATTA FORMATION \u00b7 CSEB SUITABLE</div>
    <p style="font-size:15px;line-height:1.6;">Perfect soil profile for Compressed Stabilised Earth Blocks (CSEB). KS 02-1070 compliant. Requires only <strong>5% cement binder</strong> for structural integrity.</p>
</div>
<div class="card transform-up" style="border-top:6px solid #38BDF8; min-height: 250px;">
    <div style="font-family:'Playfair Display',serif;font-size:28px;font-weight:700;margin-bottom:10px;">Yatta Canal</div>
    <div class="mono" style="font-size:12px;color:var(--mute);margin-bottom:20px;">3 M\u00b3/SEC FLOW \u00b7 2KM WEST</div>
    <p style="font-size:15px;line-height:1.6;">A permanent water source. The entire YattaFarm requires merely <strong>0.4%</strong> of the canal's flow, establishing robust food security.</p>
</div>
</div>
</div></div>
"""
    slides.append(s14)

    return slides
