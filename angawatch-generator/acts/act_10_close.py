from utils import generate_header

def generate():
    slides = []

    # Slide 88: Act 10 Opener
    s88 = """
<!-- ═══════════════ ACT X: CONCLUSION ═══════════════ -->
<div class="s" style="min-height:80vh;background:#0F172A;color:#fff;display:flex;align-items:center;justify-content:center;text-align:center;">
<div class="rv scaleIn">
<div class="mono" style="font-size:16px;letter-spacing:.3em;color:var(--tb);margin-bottom:32px">The Angawatch Proposition</div>
<div style="font-family:'Playfair Display',serif;font-size:80px;font-weight:900;margin-bottom:24px;line-height:1.1;">Dignity is not a luxury.</div>
<div style="font-size:24px;color:#94A3B8;max-width:800px;margin:0 auto;line-height:1.6;">
    It is an engineering problem. And we have solved it.
</div>
</div>
</div>
"""
    slides.append(s88)

    # Slide 89: Impact Summary
    s89 = f"""
<div class="s" id="s89" style="background:#0F172A;color:#fff;">{generate_header("10.01 · The Impact")}
<div class="pad rv slideFromRight">
<div class="g4" style="margin-top:60px;">
    <!-- Metric 1 -->
    <div style="border-top:2px solid var(--tb);padding-top:20px;">
        <div style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;color:#fff;margin-bottom:10px;">8,090</div>
        <div class="mono" style="font-size:12px;color:#94A3B8;">LIVES ELEVATED</div>
    </div>
    <!-- Metric 2 -->
    <div style="border-top:2px solid #38BDF8;padding-top:20px;">
        <div style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;color:#fff;margin-bottom:10px;">Zero</div>
        <div class="mono" style="font-size:12px;color:#94A3B8;">CARBON EMISSIONS</div>
    </div>
    <!-- Metric 3 -->
    <div style="border-top:2px solid #F59E0B;padding-top:20px;">
        <div style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;color:#fff;margin-bottom:10px;">$25M</div>
        <div class="mono" style="font-size:12px;color:#94A3B8;">LOCAL ECONOMIC DRIVER</div>
    </div>
    <!-- Metric 4 -->
    <div style="border-top:2px solid #10B981;padding-top:20px;">
        <div style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;color:#fff;margin-bottom:10px;">100%</div>
        <div class="mono" style="font-size:12px;color:#94A3B8;">ENERGY & WATER AUTONOMY</div>
    </div>
</div>
</div></div>
"""
    slides.append(s89)

    # Slide 90: Final Call to Action
    s90 = f"""
<div class="s" id="s90" style="background:#0F172A;color:#fff;border-bottom:none;">
<div class="pad rv unfold">
<div style="text-align:center;padding:100px 0;">
    <svg viewBox="0 0 100 100" width="80" height="80" style="margin-bottom:40px;">
        <polygon points="50,10 90,30 90,70 50,90 10,70 10,30" fill="none" stroke="var(--tb)" stroke-width="4"/>
        <polygon points="50,25 70,40 70,70 50,85 30,70 30,40" fill="var(--tl)"/>
        <circle cx="50" cy="50" r="8" fill="var(--td)"/>
    </svg>
    <h2 style="font-family:'Playfair Display',serif;font-size:56px;font-weight:700;margin-bottom:30px;">This is Angawatch.</h2>
    <div class="mono" style="font-size:14px;letter-spacing:.2em;color:#94A3B8;">MACHAKOS COUNTY, KENYA</div>
    
    <div style="margin-top:60px;border-top:1px solid #1E293B;padding-top:40px;display:flex;justify-content:center;gap:40px;">
        <div class="mono" style="font-size:12px;color:#cbd5e1;">A VISION FOR TOMORROW'S AFRICA.</div>
    </div>
</div>
</div></div>
"""
    slides.append(s90)

    return slides
