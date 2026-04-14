from utils import generate_header

def generate():
    slides = []

    # Slide 84: Act 9 Opener
    s84 = """
<!-- ═══════════════ ACT IX: IMPLEMENTATION & TIMELINE ═══════════════ -->
<div class="s" style="min-height:60vh;background:linear-gradient(135deg,#3B82F6,#1D4ED8);display:flex;align-items:center;justify-content:center;text-align:center;color:#fff">
<div class="rv slideFromLeft">
<div class="mono" style="font-size:14px;letter-spacing:.3em;color:#BFDBFE;margin-bottom:24px">Section 09 · Timetable</div>
<div style="font-family:'Playfair Display',serif;font-size:80px;font-weight:900;margin-bottom:16px;">Phased Execution.</div>
<div style="font-size:24px;color:rgba(255,255,255,.9)">Moving from rendering to reality in 36 months.</div>
</div>
</div>
"""
    slides.append(s84)

    # Slide 85: Phase 1 & 2
    s85 = f"""
<div class="s" id="s85">{generate_header("09.01 · Phase 1")}
<div class="pad rv scaleIn">
<div class="t1">Months 1 to 18 : The Core.</div>
<div class="g2">
    <div>
        <p style="font-size:16px;line-height:1.7;color:var(--body);margin-bottom:20px;">We do not build houses first. We build the engine first.</p>
        <ul style="font-size:15px;line-height:2;padding-left:20px;">
            <li><strong>Q1-Q2 (Civil):</strong> Land prep, Yatta Canal intake, perimeter wall, primary subterranean utility trunks (1000V DC, Water mains, Fiber).</li>
            <li><strong>Q3-Q4 (Energy Hub):</strong> Master Substation built. BESS containers installed. 1.5MW of solar deployed.</li>
            <li><strong>Q5-Q6 (Cluster A):</strong> First 3 Ekeja residential clusters (300 units) erected. Digester 1 commissioned. YattaFarm begins planting.</li>
        </ul>
    </div>
    <div style="background:#F8FAFC;border:1px solid var(--bl);border-radius:24px;padding:32px;">
        <div style="font-family:'Playfair Display',serif;font-size:24px;font-weight:700;margin-bottom:20px;color:var(--td);">Gantt Projection</div>
        <div style="margin-bottom:12px;">
            <div style="display:flex;justify-content:space-between;font-size:12px;" class="mono"><span style="color:var(--mute)">INFRASTRUCTURE</span><span>100%</span></div>
            <div class="bar-w" style="height:8px;margin-top:4px;"><div class="bar-f" style="width:100%;background:var(--ink)"></div></div>
        </div>
        <div style="margin-bottom:12px;">
            <div style="display:flex;justify-content:space-between;font-size:12px;" class="mono"><span style="color:var(--mute)">HOUSING</span><span>20%</span></div>
            <div class="bar-w" style="height:8px;margin-top:4px;"><div class="bar-f" style="width:20%;background:var(--tb)"></div></div>
        </div>
        <div style="margin-bottom:12px;">
            <div style="display:flex;justify-content:space-between;font-size:12px;" class="mono"><span style="color:var(--mute)">COMMUNITY HUB</span><span>50%</span></div>
            <div class="bar-w" style="height:8px;margin-top:4px;"><div class="bar-f" style="width:50%;background:#3B82F6)"></div></div>
        </div>
    </div>
</div>
</div></div>
"""
    slides.append(s85)

    # Slide 86: Phase 3 & 4
    s86 = f"""
<div class="s" id="s86">{generate_header("09.02 · Phase 2")}
<div class="pad rv slideFromRight">
<div class="t1">Months 19 to 36 : The Expansion.</div>
<div class="g2">
    <div>
        <p style="font-size:16px;line-height:1.7;color:var(--body);margin-bottom:20px;">Leveraging revenue from Phase 1 to accelerate the remaining deployment.</p>
        <ul style="font-size:15px;line-height:2;padding-left:20px;">
            <li><strong>Q7-Q8:</strong> Ekeja Clusters 4-10. Expanding the solar array to 2.5MW. Commissioning the Health Centre and School.</li>
            <li><strong>Q9-Q10:</strong> Final Ekeja Clusters 11-18. Completing the 3.6MW solar array.</li>
            <li><strong>Q11-Q12:</strong> Final landscaping, EV Hub full commissioning, handover to the SACCO management.</li>
        </ul>
    </div>
    <div style="background:#1E293B;color:#fff;border-radius:24px;padding:32px;display:flex;flex-direction:column;justify-content:center;align-items:center;">
        <div style="font-family:'Playfair Display',serif;font-size:80px;font-weight:900;color:#38BDF8;line-height:1">18</div>
        <div class="mono" style="font-size:14px;color:#94A3B8;margin-top:10px;">EKEJA CLUSTERS COMPLETED</div>
        <div style="margin-top:30px;color:var(--tb);font-weight:700;">FULL HABITATION ACHIEVED</div>
    </div>
</div>
</div></div>
"""
    slides.append(s86)

    # Slide 87: End Act 9
    s87 = f"""
<div class="s" id="s87">{generate_header("09.03 · Replication")}
<div class="pad rv unfold">
<div class="g2" style="align-items:center;">
    <div style="background:var(--card);padding:40px;border-radius:32px;border:1px solid var(--bl);">
        <h3 style="font-family:'Playfair Display',serif;font-size:32px;font-weight:700;margin-bottom:20px;color:var(--ink);">A Blueprint, Not a Monolith.</h3>
        <p style="font-size:16px;line-height:1.7;color:var(--body);">Angawatch is designed as a highly reproducible blueprint. The microgrid math, the EPS construction schematics, and the SACCO financial model can be lifted and placed in Naivasha, Kisumu, or Thika.</p>
        <div style="margin-top:20px;display:flex;gap:10px;">
            <div class="tag" style="background:#EFF6FF;color:#2563EB;">OPEN SOURCE ARCHITECTURE</div>
        </div>
    </div>
    <div style="display:flex;justify-content:center;">
        <svg viewBox="0 0 200 200" width="150" height="150">
            <!-- Replication abstract -->
            <rect x="50" y="50" width="40" height="40" fill="var(--ink)" rx="4"/>
            <rect x="110" y="50" width="40" height="40" fill="var(--ink)" rx="4" opacity="0.6"/>
            <rect x="50" y="110" width="40" height="40" fill="var(--ink)" rx="4" opacity="0.3"/>
            <rect x="110" y="110" width="40" height="40" fill="var(--ink)" rx="4" opacity="0.1"/>
        </svg>
    </div>
</div>
</div></div>
"""
    slides.append(s87)

    return slides
