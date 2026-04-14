from utils import generate_header

def generate():
    slides = []

    # Slide 15: The Problem Opener
    s15 = """
<!-- ═══════════════ ACT II: THE PROBLEM ═══════════════ -->
<div class="s" style="min-height:80vh;background:#0F172A;display:flex;align-items:center;justify-content:center;text-align:center;color:#fff">
<div class="rv scaleIn">
<div style="font-family:'Playfair Display',serif;font-size:200px;font-weight:900;color:#EF4444;line-height:.8;text-shadow:0 20px 40px rgba(239,68,68,.2);margin-bottom:24px">6</div>
<div class="t1" style="color:#fff;margin:0">Documented Needs.<br><em style="color:var(--tb);border-color:transparent">Six Engineered Responses.</em></div>
</div>
</div>
"""
    slides.append(s15)

    # Slide 16: Household Air Pollution (CSS Bar Chart)
    s16 = f"""
<div class="s" id="s16">{generate_header("02.01 · Air Pollution")}
<div class="pad rv slideFromRight">
<div class="t1">Household Air Pollution.</div>
<div class="intro">3.2 million deaths/year globally (WHO 2022). 70%+ of Machakos households cook on charcoal \u2014 exceeding WHO PM2.5 limits by up to 67\u00d7.</div>
<div class="glow-on-hover" style="position:relative;background:#fff;border-radius:32px;padding:64px 64px 64px 200px;box-shadow:0 20px 40px rgba(0,0,0,.05);margin-top:40px; transition:box-shadow .3s;">
<div style="position:absolute;left:238px;top:0;bottom:0;width:2px;border-left:2px dashed #EF4444;z-index:5"></div>
<div style="position:absolute;top:16px;left:248px;color:#EF4444;font-weight:700;font-size:13px">WHO Limit 15 \u00b5g/m\u00b3</div>
<div style="margin-bottom:28px;display:flex;align-items:center;position:relative;z-index:2"><div style="position:absolute;left:-160px;width:140px;font-weight:700;text-align:right;font-size:14px">Charcoal</div><div class="bar-w" style="height:28px;border-radius:14px"><div class="bar-f" style="width:100%;background:linear-gradient(90deg,#991B1B,#EF4444);border-radius:14px;display:flex;align-items:center;padding-left:12px;color:#fff;font-size:12px;font-weight:700">1,000 \u00b5g/m\u00b3</div></div></div>
<div style="margin-bottom:28px;display:flex;align-items:center;position:relative;z-index:2"><div style="position:absolute;left:-160px;width:140px;font-weight:700;text-align:right;font-size:14px">LPG (Phase 1)</div><div class="bar-w" style="height:28px;border-radius:14px"><div class="bar-f" style="width:12%;background:linear-gradient(90deg,#B45309,#F59E0B);border-radius:14px;display:flex;align-items:center;padding-left:12px;color:#fff;font-size:12px;font-weight:700">30</div></div></div>
<div style="margin-bottom:28px;display:flex;align-items:center;position:relative;z-index:2"><div style="position:absolute;left:-160px;width:140px;font-weight:700;text-align:right;font-size:14px">Biogas (Inst.)</div><div class="bar-w" style="height:28px;border-radius:14px"><div class="bar-f" style="width:4%;background:linear-gradient(90deg,#047857,#10B981);border-radius:14px;display:flex;align-items:center;padding-left:8px;color:#fff;font-size:12px;font-weight:700">&lt;10</div></div></div>
<div style="display:flex;align-items:center;position:relative;z-index:2"><div style="position:absolute;left:-160px;width:140px;font-weight:700;text-align:right;font-size:14px">Solar Induction</div><div class="bar-w" style="height:28px;border-radius:14px"><div class="bar-f" style="width:1%;background:var(--tb);border-radius:14px">&nbsp;</div></div><span class="mono" style="font-size:12px;color:var(--td);margin-left:8px;font-weight:700">~0</span></div>
</div>
</div></div>
"""
    slides.append(s16)

    # Slide 17: Three-Phase Cooking Transition
    s17 = f"""
<div class="s" id="s17">{generate_header("02.01b · Cooking Transition")}
<div class="pad rv unfold"><div class="t1">Three-Phase Cooking Transition.</div><div class="intro">We do not pretend 2,000 homes can cook on solar batteries immediately. We transition honestly.</div>
<div style="display:flex;align-items:center;justify-content:space-between;gap:20px;margin-top:40px;flex-wrap:wrap">
<div class="card transform-up" style="flex:1;min-width:240px;text-align:center;border-top:8px solid #F59E0B"><div class="mono" style="font-size:12px;color:#B45309;margin-bottom:8px">PHASE 1 (Yrs 1\u20135)</div><h3 style="font-size:18px;font-weight:700;margin-bottom:10px">SACCO LPG</h3><p style="font-size:13px;color:var(--mute);margin-bottom:12px">Bulk procurement. Monthly billing.</p><div style="font-weight:700;font-size:18px">KES 1,260/mo</div><div class="mono" style="font-size:10px;color:red;margin-top:5px;">10-30 \u00b5g/m\u00b3 PM2.5</div></div>
<div style="font-size:24px;color:var(--bm);flex-shrink:0">\u2192</div>
<div class="card transform-up" style="flex:1;min-width:240px;text-align:center;border-top:8px solid var(--tb)"><div class="mono" style="font-size:12px;color:var(--tb);margin-bottom:8px">PHASE 2 (Yrs 2+)</div><h3 style="font-size:18px;font-weight:700;margin-bottom:10px">Biogas Institutions</h3><p style="font-size:13px;color:var(--mute);margin-bottom:12px">CHC, schools, market on pipeline.</p><div style="font-weight:700;font-size:18px;color:var(--td)">Near-Zero PM2.5</div></div>
<div style="font-size:24px;color:var(--bm);flex-shrink:0">\u2192</div>
<div class="card transform-up" style="flex:1;min-width:240px;text-align:center;border-top:8px solid var(--td)"><div class="mono" style="font-size:12px;color:var(--td);margin-bottom:8px">PHASE 3 (Yr 10+)</div><h3 style="font-size:18px;font-weight:700;margin-bottom:10px">Solar Induction</h3><p style="font-size:13px;color:var(--mute);margin-bottom:12px">Homes migrate as surplus grows.</p><div style="font-weight:700;font-size:18px;color:var(--td)">~0 \u00b5g/m\u00b3</div></div>
</div></div></div>
"""
    slides.append(s17)

    # Slide 18: Energy Poverty
    s18 = f"""
<div class="s" id="s18">{generate_header("02.02 · Energy Poverty")}
<div class="pad rv slideFromLeft">
<div class="glow-on-hover" style="display:grid;grid-template-columns:1fr 1fr;border-radius:40px;overflow:hidden;box-shadow:0 20px 50px rgba(0,0,0,.1);position:relative;margin-top:40px; transition: box-shadow .3s;">
<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);font-family:'Playfair Display',serif;font-size:120px;font-weight:900;color:#fff;text-shadow:0 10px 30px rgba(0,0,0,.5);z-index:10;pointer-events:none">64%</div>
<div style="padding:80px 64px;background:#1E293B;color:#94A3B8">
<div class="mono" style="font-size:14px;letter-spacing:.1em;margin-bottom:16px;color:#EF4444">THE PROBLEM</div>
<h3 style="font-family:'Playfair Display',serif;font-size:32px;color:#fff;margin-bottom:24px">KPLC Grid</h3>
<p style="font-size:16px;line-height:1.8">KES 25\u201328/kWh tariff<br>15\u201325 outages/year<br>4\u20138 hour average duration<br>45\u201360% regional connection</p>
</div>
<div style="padding:80px 64px;background:var(--td);color:var(--tl)">
<div class="mono" style="font-size:14px;letter-spacing:.1em;margin-bottom:16px;color:var(--tl)">THE SOLUTION</div>
<h3 style="font-family:'Playfair Display',serif;font-size:32px;color:#fff;margin-bottom:24px">Angawatch</h3>
<p style="font-size:16px;line-height:1.8">KES 9/kWh community tariff<br>99.6% guaranteed uptime<br>Zero cooling load<br>100% connection</p>
</div>
</div>
</div></div>
"""
    slides.append(s18)

    # Slide 19: Cooking Cost
    s19 = f"""
<div class="s" id="s19">{generate_header("02.03 · Cooking Cost")}
<div class="pad rv unfold">
<div class="t1">The Upfront Barrier.</div>
<div class="intro">Cash-flow barriers force reliance on toxic charcoal. Retail LPG cylinder refills demand high single payments.</div>
<div class="g3">
    <div class="card transform-up" style="border-top: 8px solid #EF4444; border-radius: 12px; text-align:center;">
        <h3 style="font-size:24px;margin-bottom:16px;color:#EF4444;">Charcoal</h3>
        <div style="font-family:'Playfair Display', serif; font-size:48px; font-weight:700;">3,250<span style="font-size:16px;">/mo</span></div>
        <div class="mono" style="font-size:12px; color:var(--mute); margin-top:20px;">Health & Deforestation</div>
    </div>
    <div class="card transform-up" style="border-top: 8px solid #F59E0B; border-radius: 12px; text-align:center;">
        <h3 style="font-size:24px;margin-bottom:16px;color:#F59E0B;">Retail LPG</h3>
        <div style="font-family:'Playfair Display', serif; font-size:48px; font-weight:700;">1,560<span style="font-size:16px;">/mo</span></div>
        <div class="mono" style="font-size:12px; color:var(--mute); margin-top:20px;">1,500 KES upfront barrier</div>
    </div>
    <div class="card transform-up" style="border-top: 8px solid var(--td); border-radius: 12px; text-align:center; box-shadow: 0 10px 30px rgba(15,118,110,.2);">
        <h3 style="font-size:24px;margin-bottom:16px;color:var(--td);">SACCO LPG</h3>
        <div style="font-family:'Playfair Display', serif; font-size:48px; font-weight:700; color:var(--td);">1,260<span style="font-size:16px;">/mo</span></div>
        <div class="mono" style="font-size:12px; color:var(--mute); margin-top:20px;">Angawatch Solution</div>
    </div>
</div>
</div></div>
"""
    slides.append(s19)
    
    # Slide 20: Transport Poverty
    s20 = f"""
<div class="s" id="s20">{generate_header("02.04 · Transport Poverty")}
<div class="pad rv slideFromRight">
<div class="t1">Breaking Transport Poverty.</div>
<div class="g2" style="margin-top: 40px;">
    <!-- Matatu vs E-Matatu -->
    <div class="card transform-scale">
        <svg viewBox="0 0 100 40" width="100" height="40"><rect x="10" y="10" width="80" height="25" rx="5" fill="#3B82F6"/><circle cx="30" cy="35" r="5" fill="#0F172A"/><circle cx="70" cy="35" r="5" fill="#0F172A"/></svg>
        <h3 style="font-size: 20px; font-weight:700; margin: 10px 0;">Matatu Commute</h3>
        <div style="display:flex; justify-content:space-between; border-bottom:1px solid var(--bl); padding: 8px 0;"><span>Current ICE Matatu</span><strong>KES 6,600 / mo</strong></div>
        <div style="display:flex; justify-content:space-between; border-bottom:1px solid var(--bl); padding: 8px 0; color:var(--td);"><span>E-Matatu (Angawatch)</span><strong>KES 3,960 / mo</strong></div>
        <div style="font-weight:700; color:var(--td); margin-top:12px; text-align:right;">Saving: KES 2,640</div>
    </div>
    <!-- Boda vs E-Boda -->
    <div class="card transform-scale">
        <svg viewBox="0 0 100 40" width="80" height="40"><path d="M20 30 L40 10 L60 10 L80 30" stroke="#F59E0B" stroke-width="4" fill="none"/><circle cx="20" cy="30" r="8" fill="#0F172A"/><circle cx="80" cy="30" r="8" fill="#0F172A"/></svg>
        <h3 style="font-size: 20px; font-weight:700; margin: 10px 0;">Boda Boda Operator</h3>
        <div style="display:flex; justify-content:space-between; border-bottom:1px solid var(--bl); padding: 8px 0;"><span>Petrol Cost</span><strong>KES 7,500 / mo</strong></div>
        <div style="display:flex; justify-content:space-between; border-bottom:1px solid var(--bl); padding: 8px 0; color:var(--td);"><span>Roam Air Swap</span><strong>KES 1,500 / mo</strong></div>
        <div style="font-weight:700; color:var(--td); margin-top:12px; text-align:right;">Saving: KES 6,000</div>
    </div>
</div>
</div></div>
"""
    slides.append(s20)

    # Slide 21: Healthcare
    s21 = f"""
<div class="s" id="s21">{generate_header("02.05 · Healthcare")}
<div class="pad rv scaleIn">
<div class="t1">Healthcare Access.</div>
<div class="g2" style="align-items:center;">
    <div style="text-align:center;">
        <div style="position:relative; display:inline-block;">
            <div style="font-family:'Playfair Display', serif; font-size:96px; font-weight:900; color:var(--mute); text-decoration:line-through; opacity:0.5;">1:8,000</div>
            <div style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); background:#fff; padding:20px; border-radius:50%; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                <span style="font-size:64px;">🏥</span>
            </div>
        </div>
        <div class="mono" style="margin-top:20px; color:var(--mute);">MACHAKOS DOCTOR RATIO vs WHO (1:1,000)</div>
    </div>
    <div>
        <h3 style="font-size:28px; font-weight:700; margin-bottom:16px;">50-Bed Level 3 CHC</h3>
        <p style="font-size:18px; line-height:1.6; color:var(--body);">Located within walking distance inside the Angawatch community.</p>
        <ul style="list-style:none; padding:0; margin-top:20px;">
            <li style="margin-bottom:12px; padding-left:24px; position:relative;"><span style="position:absolute; left:0; color:var(--td);">✓</span> Uninterruptible power supply</li>
            <li style="margin-bottom:12px; padding-left:24px; position:relative;"><span style="position:absolute; left:0; color:var(--td);">✓</span> High-speed telemedicine link to Machakos L5</li>
            <li style="margin-bottom:12px; padding-left:24px; position:relative;"><span style="position:absolute; left:0; color:var(--td);">✓</span> High quality housing to attract medical staff</li>
        </ul>
    </div>
</div>
</div></div>
"""
    slides.append(s21)

    # Slide 22: Education
    s22 = f"""
<div class="s" id="s22">{generate_header("02.06 · Education")}
<div class="pad rv slideFromLeft">
<div class="t1">Education Crisis.</div>
<div class="g2">
    <div class="card transform-up">
        <h3 style="text-align:center; margin-bottom:16px;">National Average: 50+ per class</h3>
        <svg viewBox="0 0 100 60" width="100%" height="200" style="background:#FEE2E2; border-radius: 8px;">
            { "".join([f'<circle cx="{10 + (i%10)*9}" cy="{10 + (i//10)*10}" r="2.5" fill="#EF4444"/>' for i in range(50)]) }
        </svg>
    </div>
    <div class="card transform-up" style="border-top:8px solid var(--td);">
        <h3 style="text-align:center; margin-bottom:16px; color:var(--td);">Angawatch Target: 30 per class</h3>
        <svg viewBox="0 0 100 60" width="100%" height="200" style="background:var(--tl); border-radius: 8px;">
            { "".join([f'<circle cx="{10 + (i%6)*16}" cy="{10 + (i//6)*10}" r="3" fill="var(--td)"/>' for i in range(30)]) }
        </svg>
    </div>
</div>
<div style="margin-top:40px; text-align:center; font-size:18px;">Nearly 300 resident teacher families. The ability to walk to work in a safe, fully-powered environment. Minimum commute, maximum impact.</div>
</div></div>
"""
    slides.append(s22)

    return slides
