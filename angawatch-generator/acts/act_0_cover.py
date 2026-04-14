def generate():
    slides = []

    # Slide 1: The Master Cover
    slide1 = """
<!-- ═══════════════ ACT 0: COVER (Slides 1-4) ═══════════════ -->
<div class="s" id="s1" style="padding-top:64px;padding-bottom:0; min-height: 100vh;">
<div style="position:absolute;inset:0;opacity:.5;pointer-events:none;background-image:radial-gradient(var(--bm) 1px,transparent 1px);background-size:40px 40px"></div>
<div class="glow-on-hover" style="position:absolute;right:-10%;top:-15%;width:800px;height:800px;background:linear-gradient(135deg,var(--tl),rgba(20,184,166,.15));animation:morph 15s ease-in-out infinite;pointer-events:none;transition:box-shadow 0.5s;"></div>
<div style="position:relative;z-index:2;padding:0 80px;display:flex;justify-content:space-between;align-items:flex-start">
<div class="logo"><svg viewBox="0 0 32 32" fill="none"><polygon points="16,2 28,9 28,23 16,30 4,23 4,9" fill="none" stroke="#0F172A" stroke-width="2"/><polygon points="16,7 23,11 23,21 16,25 9,21 9,11" fill="#CCFBF1"/><circle cx="16" cy="16" r="3" fill="#0F766E"/></svg><span>Angawatch</span></div>
<div style="font-family:'DM Mono',monospace;font-size:13px;letter-spacing:.15em;text-transform:uppercase;color:var(--td);font-weight:600;background:rgba(255,255,255,.8);backdrop-filter:blur(4px);padding:10px 20px;border-radius:100px;border:1px solid var(--tl);transition: transform 0.3s;" class="transform-scale">Power the Community 2026<br><span style="color:var(--mute);font-size:11px;text-transform:none;letter-spacing:0">Energy Mentors International</span></div>
</div>
<div class="rv on" style="position:relative;z-index:2;text-align:center;max-width:900px;margin:120px auto;padding:0 40px">
<div style="font-family:'Playfair Display',serif;font-size:clamp(64px,8vw,96px);font-weight:900;line-height:1.05;letter-spacing:-.02em;color:var(--ink);margin-bottom:24px">Angawatch<br><em style="font-style:italic;color:var(--tb);position:relative;display:inline-block">Eco-Community</em></div>
<div style="font-size:22px;color:var(--body);line-height:1.6;max-width:700px;margin:0 auto">A first-principles, solar-and-biogas powered community for 2,000 families on the Yatta Plateau, Kenya.</div>
</div>
</div>
"""
    slides.append(slide1)
    
    # Slide 2: Metrics block spread out into full slide frame
    slide2 = """
<div class="s" id="s2" style="min-height: 80vh; display:flex; flex-direction:column; justify-content:center;">
<div class="pad rv">
<div class="t1" style="text-align:center;">The Scale of Ambition.</div>
<div style="position:relative;z-index:2;background:rgba(255,255,255,.9);backdrop-filter:blur(10px);display:flex;border-top:2px dashed var(--tl);border-bottom:2px dashed var(--tl);flex-wrap:wrap; margin-top:60px;">
<div class="transform-up" style="flex:1;min-width:180px;padding:60px 48px;border-right:2px dashed var(--tl);transition:transform 0.3s;"><div style="font-family:'Playfair Display',serif;font-size:64px;font-weight:700;color:var(--ink);line-height:1;margin-bottom:12px">8,090</div><div class="mono" style="font-size:14px;color:var(--mute);letter-spacing:.1em;text-transform:uppercase;font-weight:600">Total Residents</div></div>
<div class="transform-up" style="flex:1;min-width:180px;padding:60px 48px;border-right:2px dashed var(--tl);transition:transform 0.3s;"><div style="font-family:'Playfair Display',serif;font-size:64px;font-weight:700;color:var(--ink);line-height:1;margin-bottom:12px">3,360<span style="color:var(--tb);font-size:32px">kWp</span></div><div class="mono" style="font-size:14px;color:var(--mute);letter-spacing:.1em;text-transform:uppercase;font-weight:600">Solar Installed</div></div>
</div>
</div></div>
"""
    slides.append(slide2)
    
    # Slide 3: Secondary Metrics block
    slide3 = """
<div class="s" id="s3" style="min-height: 80vh; display:flex; flex-direction:column; justify-content:center;">
<div class="pad rv">
<div style="position:relative;z-index:2;background:rgba(255,255,255,.9);backdrop-filter:blur(10px);display:flex;border-top:2px dashed var(--tl);border-bottom:2px dashed var(--tl);flex-wrap:wrap;">
<div class="transform-up" style="flex:1;min-width:180px;padding:60px 48px;border-right:2px dashed var(--tl);transition:transform 0.3s;"><div style="font-family:'Playfair Display',serif;font-size:64px;font-weight:700;color:var(--ink);line-height:1;margin-bottom:12px">5,734</div><div class="mono" style="font-size:14px;color:var(--mute);letter-spacing:.1em;text-transform:uppercase;font-weight:600">MWh/year Generated</div></div>
<div class="transform-up" style="flex:1;min-width:180px;padding:60px 48px;transition:transform 0.3s;"><div style="font-family:'Playfair Display',serif;font-size:64px;font-weight:700;color:var(--ink);line-height:1;margin-bottom:12px">35k<span style="color:var(--tb);font-size:32px">KES</span></div><div class="mono" style="font-size:14px;color:var(--mute);letter-spacing:.1em;text-transform:uppercase;font-weight:600">Monthly Family Saving</div></div>
</div>
</div></div>
"""
    slides.append(slide3)
    
    # Slide 4: Brief design philosophy
    slide4 = """
<div class="s" id="s4" style="background:#0F172A;color:#fff;display:flex;align-items:center;justify-content:center; text-align:center;">
<div class="rv unfold">
<div style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;margin-bottom:24px;">An Engineering Narrative.</div>
<div style="font-size:20px;color:#94A3B8;max-width:800px;margin:0 auto;line-height:1.6;">Before we show you what we're building, we show you WHERE and WHY. This is a journey through data, light, structure, and impact.</div>
</div>
</div>
"""
    slides.append(slide4)

    return slides
