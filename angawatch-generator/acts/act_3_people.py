from utils import generate_header

def generate():
    slides = []

    # Slide 23: The People Opener
    s23 = """
<!-- ═══════════════ ACT III: THE PEOPLE ═══════════════ -->
<div class="s" style="min-height:60vh;background:#0F172A;display:flex;align-items:center;justify-content:center;text-align:center;color:#fff">
<div class="rv scaleIn">
<div class="mono" style="font-size:14px;letter-spacing:.3em;color:var(--mute);margin-bottom:24px">Section 03 · The People</div>
<div class="t1" style="color:#fff;margin:0;font-size:56px">Designed for nurses, teachers,<br><em style="color:var(--tb);border-color:transparent">and the self-employed.</em></div>
<div style="display:flex; gap:20px; justify-content:center; margin-top:60px;">
    <!-- Abstract Silhouettes -->
    <svg width="60" height="100" viewBox="0 0 60 100"><polygon points="30,0 60,30 60,100 0,100 0,30" fill="var(--td)"/><circle cx="30" cy="30" r="15" fill="#0F172A"/></svg>
    <svg width="60" height="100" viewBox="0 0 60 100"><polygon points="30,10 50,40 60,100 0,100 10,40" fill="#F59E0B"/><circle cx="30" cy="25" r="12" fill="#0F172A"/></svg>
    <svg width="60" height="100" viewBox="0 0 60 100"><polygon points="30,20 60,50 60,100 0,100 0,50" fill="#E2E8F0"/><circle cx="30" cy="35" r="18" fill="#0F172A"/></svg>
</div>
</div>
</div>
"""
    slides.append(s23)

    # Slide 24: Archetype 1 - The Rural Nurse
    s24 = f"""
<div class="s" id="s24">{generate_header("03.01 · The Rural Nurse")}
<div class="pad rv slideFromRight">
<div class="g2" style="gap:64px;margin-top:20px">
<div class="card transform-up" style="border-top:6px solid var(--td)">
<div style="width:80px;height:80px;border-radius:50%;background:var(--tl);display:flex;align-items:center;justify-content:center;margin-bottom:20px"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--td)" stroke-width="1.5"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></div>
<div style="font-family:'Playfair Display',serif;font-size:28px;font-weight:700;margin-bottom:4px">The Rural Nurse</div>
<div class="mono" style="font-size:12px;color:var(--td);margin-bottom:20px">~60% POPULATION \u00b7 3BR \u00b7 KES 95K\u2013134K DUAL INCOME</div>

<!-- Current vs Angawatch cost bars -->
<div style="margin-bottom:20px;">
    <div style="display:flex; justify-content:space-between; font-size:13px; font-weight:700; margin-bottom:4px;"><span>Current (Rent)</span><span>KES 12K - 18K</span></div>
    <div class="bar-w" style="margin-bottom:12px;"><div class="bar-f" style="width:40%; background:var(--mute);"></div></div>
    
    <div style="display:flex; justify-content:space-between; font-size:13px; font-weight:700; color:var(--td); margin-bottom:4px;"><span>Angawatch EMI</span><span>KES 40,803</span></div>
    <div class="bar-w"><div class="bar-f" style="width:100%; background:var(--td);"></div></div>
</div>

</div>
<div>
<div class="quote">"Tokens zinaisha haraka sana \u2014 na wakati wa load shedding, chakula inaharibika."<small>"Tokens run out too fast \u2014 and when there's load shedding, the food goes bad."</small></div>
<div class="quote" style="border-color:#EF4444;background:#FEF2F2">"Smoke from the jiko makes the children cough, but gas is too expensive to buy all at once \u2014 you cannot buy half a cylinder."<small style="color:#B91C1C">Cash-flow barriers force reliance on toxic charcoal.</small></div>
</div>
</div>
</div></div>
"""
    slides.append(s24)

    # Slide 25: Nurse Engineering response
    s25 = f"""
<div class="s" id="s25">{generate_header("03.01b · Engineering Response")}
<div class="pad rv unfold">
<div class="t1">The Engineering Response.</div>
<div class="dark" style="margin-top:40px;">
<table class="dt inv" style="font-size:16px;">
    <tr><th style="font-size:14px; color:#fff;">Problem / Pain Point</th><th style="font-size:14px; color:var(--tb);">Angawatch Solution</th></tr>
    <tr><td>Electricity cost: KES 7,200/mo (KPLC)</td><td style="color:var(--tl)">Community Solar: KES 930/mo</td></tr>
    <tr><td>Daily load shedding / power outages</td><td style="color:var(--tl)">99.6% guaranteed uptime (3,600 kWh BESS)</td></tr>
    <tr><td>Toxic charcoal / Upfront LPG cost barrier</td><td style="color:var(--tl)">SACCO bulk LPG at KES 1,260/mo (billed easily)</td></tr>
    <tr><td>Commute costs (KES 5,500 - 7,700/mo)</td><td style="color:var(--tl)">E-matatu fleet (KES 2,200/mo) or walking (CHC on site)</td></tr>
</table>
</div>
</div></div>
"""
    slides.append(s25)

    # Slide 26: Archetype 2 - Boda Boda
    s26 = f"""
<div class="s" id="s26">{generate_header("03.02 · The Boda Operator")}
<div class="pad rv slideFromLeft">
<div class="g2" style="gap:64px">
<div>
    <div class="quote" style="border-color:#F59E0B;background:#FEF3C7">"Boda ni kazi ngumu \u2014 petrol inapanda kila wiki, lakini hakuna alternative."<small style="color:#B45309">"Boda is hard work \u2014 petrol rises every week, but there is no alternative."</small></div>
    <div class="quote">"Nataka mahali salama \u2014 si lazima kubwa, lakini salama na stima inayofanya kazi."<small>"I want somewhere safe \u2014 not necessarily big, but safe and with electricity that works."</small></div>
    <div style="background:#FEF2F2;border-left:4px solid #EF4444;padding:20px;border-radius:0 16px 16px 0;margin-top:24px; box-shadow:0 4px 12px rgba(239,68,68,.1);"><div class="mono" style="font-size:12px;color:#B91C1C;margin-bottom:6px;font-weight:700">HONEST LIMITATION</div><p style="font-size:14px;color:#7F1D1D;line-height:1.5">At KES 30k\u201348k sole income, KMRC mortgage is unaffordable. Correct product: <strong>1BR Cooperative Rental at KES 10k\u201312k/month</strong>.</p></div>
</div>
<div class="card transform-up" style="border-top:6px solid #F59E0B;transform:rotate(1deg)">
    <div style="font-family:'Playfair Display',serif;font-size:28px;font-weight:700">The Boda Operator</div>
    <div class="mono" style="font-size:12px;color:#D97706;margin-bottom:20px">1BR RENTAL \u00b7 7.5% POPULATION \u00b7 KES 30K\u201348K</div>
    <div class="kv" style="border-color:var(--bl)"><span class="k" style="color:var(--mute)">Petrol cost</span><span class="v" style="color:#EF4444">KES 7,500\u201310K/mo</span></div>
    <div class="kv" style="border-color:transparent"><span class="k" style="color:var(--mute)">Roam Air swap</span><span class="v" style="color:var(--td)">KES 1,500/mo</span></div>
    <div style="margin-top:40px; padding:20px; background:var(--tl); border-radius:12px;">
        <p style="font-weight:700; color:var(--td); font-size:14px;">The e-boda transition literally pays for the 1BR rental.</p>
    </div>
</div>
</div>
</div></div>
"""
    slides.append(s26)

    # Slide 27: Archetype 3 - Deputy Principal
    s27 = f"""
<div class="s" id="s27">{generate_header("03.03 · The Deputy Principal")}
<div class="pad rv scaleIn">
<div class="g2" style="gap:64px">
<div class="card transform-up" style="background:linear-gradient(135deg,#1E293B,#0F172A);color:#fff;border-color:#334155;border-top:6px solid #FCD34D;box-shadow: 0 20px 40px rgba(0,0,0,.3)">
    <div style="font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:#FCD34D;margin-bottom:4px">The Deputy Principal</div>
    <div class="mono" style="font-size:12px;color:#93C5FD;margin-bottom:20px">4BR PREMIUM \u00b7 1% POPULATION \u00b7 KES 120K\u2013200K</div>
    <div class="kv" style="border-color:#334155"><span class="k" style="color:#94A3B8">Unit</span><span class="v">4BR Bungalow</span></div>
    <div class="kv" style="border-color:transparent"><span class="k" style="color:#94A3B8">EMI</span><span class="v" style="color:#FCD34D">KES 48,615</span></div>
</div>
<div>
    <div class="quote" style="background:var(--card);border-color:#334155;box-shadow:none">"The land is good and it is not far, but who will teach my children if all the good teachers are in Nairobi?"<small>Senior pros need quality schools on-site to relocate.</small></div>
    <div class="quote" style="background:var(--card);border-color:#334155;box-shadow:none">"I work night shifts \u2014 I need the lights and the fridge to work."<small>99.6% uptime is non-negotiable for this archetype.</small></div>
</div>
</div>
</div></div>
"""
    slides.append(s27)

    # Slide 28: Comparison Matrix
    s28 = f"""
<div class="s" id="s28">{generate_header("03.04 · Archetype Comparison")}
<div class="pad rv slideFromRight">
<div class="t1">Three Families. <em>Three Paths.</em></div>
<div style="display:grid; grid-template-columns: repeat(3, 1fr); gap: 20px; align-items: stretch; margin-top:40px;">
    
    <!-- Operator -->
    <div class="card" style="display:flex; flex-direction:column; border-top: 4px solid #F59E0B;">
        <h3 style="font-size:22px; font-weight:700; margin-bottom:12px; color:#F59E0B;">The Operator</h3>
        <p style="font-size:14px; margin-bottom:20px; color:var(--mute);">KES 30K - 48K</p>
        <ul style="list-style:none; padding:0; flex:1; font-size:14px; line-height:2;">
            <li><strong>Unit:</strong> 1BR Studio</li>
            <li><strong>Tenure:</strong> Rental</li>
            <li><strong>Monthly:</strong> KES 10K-12K</li>
            <li><strong>Key Saving:</strong> Fuel (E-boda)</li>
        </ul>
        <div style="margin-top:20px; padding-top:10px; border-top:1px solid #FCA5A5; color:#EF4444; font-size:12px; font-weight:700;">Limitation: Cannot afford KMRC deposit</div>
    </div>

    <!-- Nurse (Highlight) -->
    <div class="card" style="display:flex; flex-direction:column; border-top: 4px solid var(--td); background:var(--tl); transform:scale(1.05); box-shadow:0 20px 40px rgba(15,118,110,.15); z-index:10;">
        <h3 style="font-size:22px; font-weight:700; margin-bottom:12px; color:var(--td);">The Nurse Family</h3>
        <p style="font-size:14px; margin-bottom:20px; color:var(--td);">KES 95K - 134K</p>
        <ul style="list-style:none; padding:0; flex:1; font-size:14px; line-height:2;">
            <li><strong>Unit:</strong> 3BR Maisonette</li>
            <li><strong>Tenure:</strong> KMRC Mortgage</li>
            <li><strong>EMI:</strong> KES 40,803</li>
            <li><strong>Key Saving:</strong> Energy & Rent</li>
        </ul>
        <div style="margin-top:20px; padding-top:10px; border-top:1px solid var(--td); color:var(--ink); font-size:12px; font-weight:700;">The ultimate core population (~60%)</div>
    </div>

    <!-- Principal -->
    <div class="card" style="display:flex; flex-direction:column; border-top: 4px solid #FCD34D; background:#1E293B; color:#fff;">
        <h3 style="font-size:22px; font-weight:700; margin-bottom:12px; color:#FCD34D;">The Principal</h3>
        <p style="font-size:14px; margin-bottom:20px; color:#94A3B8;">KES 120K - 200K</p>
        <ul style="list-style:none; padding:0; flex:1; font-size:14px; line-height:2;">
            <li><strong>Unit:</strong> 4BR Bungalow</li>
            <li><strong>Tenure:</strong> Premium Mortgage</li>
            <li><strong>EMI:</strong> KES 48,615</li>
            <li><strong>Key Demand:</strong> Quality Schools</li>
        </ul>
        <div style="margin-top:20px; padding-top:10px; border-top:1px solid #334155; color:#FCD34D; font-size:12px; font-weight:700;">Critical for social anchor / leadership</div>
    </div>

</div>
</div></div>
"""
    slides.append(s28)

    # Slide 29: Salary Data
    s29 = f"""
<div class="s" id="s29">{generate_header("03.05 · Salary Verification")}
<div class="pad rv unfold">
<div class="t1">Anchored in Data.</div>
<div class="intro">Sources: KNBS 2019, TSC salary scales 2023, NCK nurse grades.</div>
<div class="dark">
    <div style="margin-bottom:30px; position:relative;">
        <div style="display:flex; justify-content:space-between; font-weight:700; margin-bottom:8px; font-size:14px;"><span>RN Nurse</span><span>KES 40K - 75K</span></div>
        <div class="bar-w" style="background:#1E293B;"><div class="bar-f" style="width:45%; margin-left:15%; background:linear-gradient(90deg, #F87171, #EF4444);"></div></div>
    </div>
    <div style="margin-bottom:30px; position:relative;">
        <div style="display:flex; justify-content:space-between; font-weight:700; margin-bottom:8px; font-size:14px;"><span>Teacher (TSC)</span><span>KES 37K - 77K</span></div>
        <div class="bar-w" style="background:#1E293B;"><div class="bar-f" style="width:50%; margin-left:12%; background:linear-gradient(90deg, #60A5FA, #3B82F6);"></div></div>
    </div>
    <div style="margin-bottom:30px; position:relative;">
        <div style="display:flex; justify-content:space-between; font-weight:700; margin-bottom:8px; font-size:14px;"><span>Dual Junior/Mid</span><span style="color:var(--td);">KES 87K - 110K</span></div>
        <div class="bar-w" style="background:#1E293B;"><div class="bar-f" style="width:30%; margin-left:35%; background:linear-gradient(90deg, var(--tb), var(--td));"></div></div>
    </div>
    <div style="position:relative;">
        <div style="display:flex; justify-content:space-between; font-weight:700; margin-bottom:8px; font-size:14px;"><span>Senior Duo</span><span style="color:#F59E0B">KES 120K - 140K+</span></div>
        <div class="bar-w" style="background:#1E293B;"><div class="bar-f" style="width:25%; margin-left:60%; background:linear-gradient(90deg, #FCD34D, #F59E0B);"></div></div>
    </div>
</div>
</div></div>
"""
    slides.append(s29)

    # Slide 30: Pull Factors
    s30 = f"""
<div class="s" id="s30">{generate_header("03.06 · Pull Factors")}
<div class="pad rv scaleIn">
<div class="t1" style="text-align:center;">8 Reasons They Will Move.</div>
<div style="display:grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-top:40px;">
    <div class="card transform-up" style="text-align:center; padding:24px 16px;"><div style="font-size:32px; margin-bottom:12px;">🚶</div><h4 style="font-size:15px; font-weight:700; margin-bottom:8px;">Walk to Work</h4><p style="font-size:12px; color:var(--mute); line-height:1.4;">Zero commute for 300+ professionals internally.</p></div>
    <div class="card transform-up" style="text-align:center; padding:24px 16px;"><div style="font-size:32px; margin-bottom:12px;">🔑</div><h4 style="font-size:15px; font-weight:700; margin-bottom:8px;">Ownership</h4><p style="font-size:12px; color:var(--mute); line-height:1.4;">Generational wealth building instead of dead rent.</p></div>
    <div class="card transform-up" style="text-align:center; padding:24px 16px;"><div style="font-size:32px; margin-bottom:12px;">🎒</div><h4 style="font-size:15px; font-weight:700; margin-bottom:8px;">Quality Schools</h4><p style="font-size:12px; color:var(--mute); line-height:1.4;">30 per class. Top tier infrastructure on site.</p></div>
    <div class="card transform-up" style="text-align:center; padding:24px 16px;"><div style="font-size:32px; margin-bottom:12px;">🤝</div><h4 style="font-size:15px; font-weight:700; margin-bottom:8px;">Community</h4><p style="font-size:12px; color:var(--mute); line-height:1.4;">A neighborhood of fellow professionals.</p></div>
    <div class="card transform-up" style="text-align:center; padding:24px 16px;"><div style="font-size:32px; margin-bottom:12px;">⚡</div><h4 style="font-size:15px; font-weight:700; margin-bottom:8px;">No Energy Stress</h4><p style="font-size:12px; color:var(--mute); line-height:1.4;">99.6% guaranteed uptime. Fridge never spoils.</p></div>
    <div class="card transform-up" style="text-align:center; padding:24px 16px;"><div style="font-size:32px; margin-bottom:12px;">🌬️</div><h4 style="font-size:15px; font-weight:700; margin-bottom:8px;">Clean Air</h4><p style="font-size:12px; color:var(--mute); line-height:1.4;">Zero charcoal. No more indoor toxic fumes.</p></div>
    <div class="card transform-up" style="text-align:center; padding:24px 16px;"><div style="font-size:32px; margin-bottom:12px;">📱</div><h4 style="font-size:15px; font-weight:700; margin-bottom:8px;">M-Pesa Yield</h4><p style="font-size:12px; color:var(--mute); line-height:1.4;">Net metering credit sent straight to M-Pesa.</p></div>
    <div class="card transform-up" style="text-align:center; padding:24px 16px;"><div style="font-size:32px; margin-bottom:12px;">🛡️</div><h4 style="font-size:15px; font-weight:700; margin-bottom:8px;">Gated Security</h4><p style="font-size:12px; color:var(--mute); line-height:1.4;">Child-safe courtyards and compound perimeter.</p></div>
</div>
</div></div>
"""
    slides.append(s30)

    return slides
