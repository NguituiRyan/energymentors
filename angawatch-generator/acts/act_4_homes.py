from utils import generate_header

def generate():
    slides = []

    # Slide 31: The Homes Opener
    s31 = """
<!-- ═══════════════ ACT IV: THE HOMES ═══════════════ -->
<div class="s" style="min-height:60vh;background:var(--td);display:flex;align-items:center;justify-content:center;text-align:center;color:#fff">
<div class="rv scaleIn">
<div class="mono" style="font-size:14px;letter-spacing:.3em;color:var(--tl);margin-bottom:24px">Section 04 · Nyumba Ya Angawatch</div>
<div style="font-family:'Playfair Display',serif;font-size:64px;font-weight:900;margin-bottom:16px">4 Unit Types. 2,000 Families.</div>
<div style="font-size:18px;color:var(--tl)">Built entirely around solar capability.</div>
<div style="display:flex; align-items:flex-end; justify-content:center; gap:10px; margin-top:40px;">
    <!-- Abstract 5-storey and G+2 ->
    <svg width="200" height="200" viewBox="0 0 200 200">
        <!-- G+2 maisonette -->
        <rect x="20" y="140" width="60" height="60" fill="var(--tl)"/>
        <line x1="20" y1="160" x2="80" y2="160" stroke="#0F172A" stroke-width="2"/>
        <line x1="20" y1="180" x2="80" y2="180" stroke="#0F172A" stroke-width="2"/>
        
        <!-- 5-Storey block -->
        <rect x="100" y="50" width="80" height="150" fill="var(--tb)"/>
        <line x1="100" y1="80" x2="180" y2="80" stroke="#0F172A" stroke-width="2"/>
        <line x1="100" y1="110" x2="180" y2="110" stroke="#0F172A" stroke-width="2"/>
        <line x1="100" y1="140" x2="180" y2="140" stroke="#0F172A" stroke-width="2"/>
        <line x1="100" y1="170" x2="180" y2="170" stroke="#0F172A" stroke-width="2"/>
    </svg>
</div>
</div>
</div>
"""
    slides.append(s31)

    # Slide 32: 1BR Floor Plan
    s32 = f"""
<div class="s" id="s32">{generate_header("04.01 · 1BR Floor Plan")}
<div class="pad rv slideFromRight">
<div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:20px;flex-wrap:wrap;gap:12px">
<div><div class="t1" style="margin-bottom:2px;font-size:40px">Unit 1: 1BR Studio</div><div class="mono" style="color:var(--td);font-size:13px">42m\u00b2 · 150 Units · Cooperative Rental</div></div>
<div style="text-align:right"><div style="font-size:22px;font-weight:700">KES 10k\u201312k<span style="font-size:13px;color:var(--mute)">/mo</span></div></div>
</div>
<div class="fp-box glow-on-hover"><svg class="draw on" viewBox="0 0 400 300" style="width:100%;max-width:500px;height:auto">
<rect x="25" y="25" width="200" height="200" class="fp-room"/>
<text x="125" y="118" class="fp-t">LIVING / SLEEPING</text>
<text x="125" y="132" class="fp-d">18.0 m\u00b2</text>
<rect x="25" y="225" width="120" height="50" class="fp-room"/>
<text x="85" y="252" class="fp-t">KITCHEN 5.4m\u00b2</text>
<rect x="145" y="225" width="80" height="50" class="fp-room"/>
<text x="185" y="252" class="fp-t">BATH 3.5m\u00b2</text>
<rect x="225" y="25" width="60" height="200" class="fp-room" style="fill:rgba(14,165,233,.08)"/>
<text x="255" y="120" class="fp-t">BALCONY</text>
<rect x="25" y="25" width="260" height="250" class="fp-wall"/>
<line x1="225" y1="25" x2="225" y2="225" class="fp-wall"/><line x1="25" y1="225" x2="225" y2="225" class="fp-wall"/><line x1="145" y1="225" x2="145" y2="275" class="fp-wall"/>
<line x1="285" y1="50" x2="285" y2="150" class="fp-win"/><line x1="25" y1="100" x2="25" y2="150" class="fp-win"/>
<rect x="100" y="222" width="20" height="6" fill="var(--ink)"/> <!-- door -->
<rect x="180" y="222" width="15" height="6" fill="var(--ink)"/> <!-- door -->
<polygon points="310,25 320,25 315,10" fill="var(--td)"/>
<text x="315" y="40" class="mono" style="font-size:10px; text-anchor:middle;">N</text>
</svg></div>
<div style="margin-top:20px;font-size:13px;color:var(--mute)"><strong>Peak:</strong> 2,936W. <strong>Daily:</strong> 2.406 kWh. <strong>Monthly:</strong> 72.2 kWh. <strong>Annual (×150):</strong> 131.8 MWh.</div>
</div></div>
"""
    slides.append(s32)

    # Slide 33: 1BR Load Schedule
    s33 = f"""
<div class="s" id="s33">{generate_header("04.01b · 1BR Load Schedule")}
<div class="pad rv scaleIn">
<div class="t1">1BR Electrical Load Schedule.</div>
<table class="dt" style="margin-top:20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
    <tr><th style="width:25%">Appliance</th><th style="width:15%">Watts</th><th style="width:40%">Scale</th><th style="width:20%">Daily kWh</th></tr>
    <tr><td>LED Lights (4)</td><td>36</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:5%; background:var(--tb);"></div></div></td><td>0.144</td></tr>
    <tr><td>Ceiling Fan</td><td>50</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:10%; background:var(--tb);"></div></div></td><td>0.300</td></tr>
    <tr><td>Fridge</td><td>60</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:12%; background:var(--tb);"></div></div></td><td>0.480</td></tr>
    <tr><td>TV & Devices</td><td>115</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:20%; background:var(--tb);"></div></div></td><td>0.460</td></tr>
    <tr><td>Kettle (Peak)</td><td>1,800</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:90%; background:#EF4444;"></div></div></td><td>0.300</td></tr>
    <tr><td>Iron (Peak)</td><td>1,000</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:60%; background:#F59E0B;"></div></div></td><td>0.166</td></tr>
    <tr style="background:var(--card); font-weight:700;"><td>Total Daily Load</td><td>~3.0kW Peak</td><td>Breaker Size: 16A</td><td>2.406 kWh</td></tr>
</table>
</div></div>
"""
    slides.append(s33)

    # Slide 34: 2BR Floor Plan
    s34 = f"""
<div class="s" id="s34">{generate_header("04.02 · 2BR Floor Plan")}
<div class="pad rv slideFromLeft">
<div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:20px;flex-wrap:wrap;gap:12px">
<div><div class="t1" style="margin-bottom:2px;font-size:40px">Unit 2: 2BR Apartment</div><div class="mono" style="color:var(--td);font-size:13px">75m\u00b2 · 1,130 Units · KMRC Mortgage</div></div>
<div style="text-align:right"><div style="font-size:22px;font-weight:700">KES 33,015<span style="font-size:13px;color:var(--mute)">/mo EMI</span></div></div>
</div>
<div class="fp-box glow-on-hover"><svg class="draw on" viewBox="0 0 500 350" style="width:100%;max-width:560px;height:auto">
<rect x="20" y="20" width="460" height="310" class="fp-wall" fill="none"/>
<rect x="20" y="20" width="200" height="150" class="fp-room"/>
<text x="120" y="90" class="fp-t">MASTER BED</text>
<rect x="220" y="20" width="160" height="150" class="fp-room"/>
<text x="300" y="90" class="fp-t">BEDROOM 2</text>
<rect x="20" y="170" width="250" height="160" class="fp-room"/>
<text x="145" y="250" class="fp-t">LIVING / DINING</text>
<rect x="270" y="170" width="130" height="100" class="fp-room"/>
<text x="335" y="225" class="fp-t">KITCHEN</text>
<rect x="270" y="270" width="130" height="60" class="fp-room"/>
<text x="335" y="305" class="fp-t">BATH</text>
<rect x="380" y="20" width="100" height="310" class="fp-room" style="fill:rgba(14,165,233,.08)"/>
<text x="430" y="175" class="fp-t">BALCONY</text>
<line x1="220" y1="20" x2="220" y2="170" class="fp-wall"/><line x1="20" y1="170" x2="380" y2="170" class="fp-wall"/><line x1="270" y1="170" x2="270" y2="330" class="fp-wall"/><line x1="380" y1="20" x2="380" y2="330" class="fp-wall"/><line x1="270" y1="270" x2="380" y2="270" class="fp-wall"/>
<line x1="480" y1="50" x2="480" y2="280" class="fp-win"/>
<polygon points="410,320 420,320 415,305" fill="var(--td)"/>
<text x="415" y="335" class="mono" style="font-size:10px;text-anchor:middle;">N</text>
</svg></div>
<div style="margin-top:20px;font-size:13px;color:var(--mute)"><strong>Daily:</strong> 3.565 kWh. <strong>Monthly:</strong> ~107 kWh. <strong>Annual (×1,130):</strong> 1,397 MWh.</div>
</div></div>
"""
    slides.append(s34)

    # Slide 35: 2BR Load Schedule
    s35 = f"""
<div class="s" id="s35">{generate_header("04.02b · 2BR Load Schedule")}
<div class="pad rv unfold">
<div class="t1">2BR Electrical Load Schedule.</div>
<table class="dt" style="margin-top:20px;">
    <tr><th style="width:25%">Appliance</th><th style="width:15%">Watts</th><th style="width:40%">Scale</th><th style="width:20%">Daily kWh</th></tr>
    <tr><td>LED Lights (8)</td><td>72</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:8%; background:var(--tb);"></div></div></td><td>0.288</td></tr>
    <tr><td>Ceiling Fans (2)</td><td>100</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:15%; background:var(--tb);"></div></div></td><td>0.600</td></tr>
    <tr><td>Larger Fridge</td><td>120</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:18%; background:var(--tb);"></div></div></td><td>0.960</td></tr>
    <tr><td>Entertainment & IT</td><td>200</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:25%; background:var(--tb);"></div></div></td><td>0.900</td></tr>
    <tr><td>Kettle + Iron (Peak)</td><td>2,800</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:95%; background:#EF4444;"></div></div></td><td>0.500</td></tr>
    <tr><td>Miscellaneous</td><td>150</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:20%; background:var(--tb);"></div></div></td><td>0.317</td></tr>
    <tr style="background:var(--card); font-weight:700;"><td>Total Daily Load</td><td>~4.0kW Peak</td><td>Breaker Size: 20A</td><td>3.565 kWh</td></tr>
</table>
</div></div>
"""
    slides.append(s35)

    # Slide 36: 3BR Floor Plan
    s36 = f"""
<div class="s" id="s36">{generate_header("04.03 · 3BR Floor Plan")}
<div class="pad rv slideFromRight">
<div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:20px;flex-wrap:wrap;gap:12px">
<div><div class="t1" style="margin-bottom:2px;font-size:40px">Unit 3: 3BR Maisonette</div><div class="mono" style="color:var(--td);font-size:13px">95m\u00b2 · G+2 · 700 Units · KMRC Core</div></div>
<div style="text-align:right"><div style="font-size:22px;font-weight:700">KES 40,803<span style="font-size:13px;color:var(--mute)">/mo EMI</span></div></div>
</div>
<div class="fp-box glow-on-hover" style="min-height:400px"><svg class="draw on" viewBox="0 0 580 340" style="width:100%;max-width:600px;height:auto">
<g transform="translate(20,20)"><text x="0" y="-5" class="mono" style="font-size:11px;fill:var(--ink);font-weight:700">GROUND FLOOR</text>
<rect x="0" y="0" width="200" height="250" class="fp-wall" fill="none"/>
<rect x="0" y="0" width="200" height="100" class="fp-room"/>
<text x="100" y="55" class="fp-t">LIVING / DINING</text>
<rect x="0" y="100" width="130" height="80" class="fp-room"/>
<text x="65" y="145" class="fp-t">KITCHEN</text>
<rect x="130" y="100" width="70" height="45" class="fp-room"/>
<text x="165" y="128" class="fp-t">WC</text>
<rect x="0" y="180" width="200" height="70" class="fp-room" style="fill:rgba(34,197,94,.08)"/>
<text x="100" y="220" class="fp-t">GARDEN</text>
<line x1="0" y1="100" x2="200" y2="100" class="fp-wall"/><line x1="130" y1="100" x2="130" y2="180" class="fp-wall"/><line x1="0" y1="180" x2="200" y2="180" class="fp-wall"/>
</g>
<g transform="translate(280,20)"><text x="0" y="-5" class="mono" style="font-size:11px;fill:var(--ink);font-weight:700">FIRST FLOOR</text>
<rect x="0" y="0" width="200" height="180" class="fp-wall" fill="none"/>
<rect x="0" y="0" width="200" height="80" class="fp-room"/>
<text x="100" y="45" class="fp-t">MASTER BED</text>
<rect x="0" y="80" width="100" height="100" class="fp-room"/>
<text x="50" y="135" class="fp-t">BED 2</text>
<rect x="100" y="80" width="100" height="100" class="fp-room"/>
<text x="150" y="135" class="fp-t">BED 3</text>
<line x1="0" y1="80" x2="200" y2="80" class="fp-wall"/><line x1="100" y1="80" x2="100" y2="180" class="fp-wall"/>
</g>
</svg></div>
<div style="margin-top:20px;font-size:13px;color:var(--mute)"><strong>Daily:</strong> 4.507 kWh. <strong>Monthly:</strong> ~135 kWh. <strong>Annual (×700):</strong> 1,084 MWh.</div>
</div></div>
"""
    slides.append(s36)

    # Slide 37: 3BR Load
    s37 = f"""
<div class="s" id="s37">{generate_header("04.03b · 3BR Load Schedule")}
<div class="pad rv scaleIn">
<div class="t1">3BR Electrical Load Schedule.</div>
<table class="dt" style="margin-top:20px;">
    <tr><th style="width:25%">Appliance</th><th style="width:15%">Watts</th><th style="width:40%">Scale</th><th style="width:20%">Daily kWh</th></tr>
    <tr><td>LED Lights (12)</td><td>108</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:12%; background:var(--tb);"></div></div></td><td>0.540</td></tr>
    <tr><td>Ceiling Fans (4)</td><td>200</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:25%; background:var(--tb);"></div></div></td><td>1.200</td></tr>
    <tr><td>Family Fridge</td><td>180</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:20%; background:var(--tb);"></div></div></td><td>1.440</td></tr>
    <tr><td>Multiple Entertainment</td><td>300</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:30%; background:var(--tb);"></div></div></td><td>1.200</td></tr>
    <tr><td>Peak Loads (Kettle/Iron)</td><td>3,500</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:100%; background:#EF4444;"></div></div></td><td>1.000</td></tr>
    <tr><td>Miscellaneous</td><td>250</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:28%; background:var(--tb);"></div></div></td><td>0.127</td></tr>
    <tr style="background:var(--card); font-weight:700;"><td>Total Daily Load</td><td>~5.0kW Peak</td><td>Breaker Size: 25A</td><td>4.507 kWh</td></tr>
</table>
</div></div>
"""
    slides.append(s37)

    # Slide 38: 4BR Floor Plan
    s38 = f"""
<div class="s" id="s38">{generate_header("04.04 · 4BR Floor Plan")}
<div class="pad rv slideFromLeft">
<div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:20px;flex-wrap:wrap;gap:12px">
<div><div class="t1" style="margin-bottom:2px;font-size:40px; color:#F59E0B;">Unit 4: 4BR Bungalow</div><div class="mono" style="color:var(--mute);font-size:13px">115m\u00b2 · G+1 · 20 Units · Premium</div></div>
<div style="text-align:right"><div style="font-size:22px;font-weight:700; color:#F59E0B;">KES 48,615<span style="font-size:13px;color:var(--mute)">/mo EMI</span></div></div>
</div>
<div class="fp-box glow-on-hover" style="border:1px solid #F59E0B; box-shadow:0 20px 40px rgba(245,158,11,0.1);"><svg class="draw on" viewBox="0 0 600 350" style="width:100%;max-width:560px;height:auto">
<!-- Premium Ground Floor Layout -->
<rect x="20" y="20" width="560" height="310" fill="none" stroke="#F59E0B" stroke-width="4"/>
<rect x="20" y="20" width="200" height="200" class="fp-room"/>
<text x="120" y="110" class="fp-t" style="fill:#F59E0B;">LIVING / DINING</text>
<rect x="220" y="20" width="160" height="120" class="fp-room"/>
<text x="300" y="80" class="fp-t">KITCHEN</text>
<rect x="380" y="20" width="200" height="120" class="fp-room"/>
<text x="480" y="80" class="fp-t">MASTER SUITE</text>
<rect x="20" y="220" width="160" height="110" class="fp-room"/>
<text x="100" y="280" class="fp-t">BEDROOM 2</text>
<rect x="180" y="220" width="160" height="110" class="fp-room"/>
<text x="260" y="280" class="fp-t">BEDROOM 3</text>
<rect x="340" y="220" width="140" height="110" class="fp-room"/>
<text x="410" y="280" class="fp-t">STUDY / BED 4</text>
<rect x="480" y="220" width="100" height="110" class="fp-room"/>
<text x="530" y="280" class="fp-t">GUEST BATH</text>

<line x1="220" y1="20" x2="220" y2="220" stroke="#F59E0B" stroke-width="2"/>
<line x1="380" y1="20" x2="380" y2="140" stroke="#F59E0B" stroke-width="2"/>
<line x1="20" y1="220" x2="580" y2="220" stroke="#F59E0B" stroke-width="2"/>
<line x1="180" y1="220" x2="180" y2="330" stroke="#F59E0B" stroke-width="2"/>
<line x1="340" y1="220" x2="340" y2="330" stroke="#F59E0B" stroke-width="2"/>
<line x1="480" y1="220" x2="480" y2="330" stroke="#F59E0B" stroke-width="2"/>
</svg></div>
<div style="margin-top:20px;font-size:13px;color:var(--mute)"><strong>Daily:</strong> ~5.2 kWh. <strong>Monthly:</strong> ~146 kWh. <strong>Annual (×20):</strong> 35 MWh.</div>
</div></div>
"""
    slides.append(s38)

    # Slide 39: 4BR Load
    s39 = f"""
<div class="s" id="s39">{generate_header("04.04b · 4BR Load Schedule")}
<div class="pad rv unfold">
<div class="t1">4BR Electrical Load Schedule.</div>
<div class="dark" style="margin-top:20px; border-top: 4px solid #F59E0B;">
<table class="dt inv" style="margin-top:20px;">
    <tr><th style="width:25%">Appliance</th><th style="width:15%">Watts</th><th style="width:40%">Scale</th><th style="width:20%">Daily kWh</th></tr>
    <tr><td>LED Lights (18)</td><td>162</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:15%; background:#F59E0B;"></div></div></td><td>0.810</td></tr>
    <tr><td>Ceiling Fans (5)</td><td>250</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:25%; background:#F59E0B;"></div></div></td><td>1.500</td></tr>
    <tr><td>Large Double Fridge</td><td>220</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:22%; background:#F59E0B;"></div></div></td><td>1.760</td></tr>
    <tr><td>Multiple Entertainment</td><td>400</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:40%; background:#F59E0B;"></div></div></td><td>1.600</td></tr>
    <tr><td>Heavy Kitchen Appliances</td><td>3,800</td><td style="padding:10px;"><div class="bar-w"><div class="bar-f" style="width:100%; background:#EF4444;"></div></div></td><td>1.200</td></tr>
    <tr style="background:#1E293B; font-weight:700;"><td>Total Daily Load</td><td style="color:#F59E0B;">~6.0kW Peak</td><td>Breaker Size: 32A</td><td>~6.87 kWh</td></tr>
</table>
</div>
</div></div>
"""
    slides.append(s39)

    # Slide 40: Portfolio Side by Side
    s40 = f"""
<div class="s" id="s40">{generate_header("04.05 · Portfolio")}
<div class="pad rv slideFromRight">
<div class="t1" style="text-align:center">Housing Portfolio</div>
<div class="g4" style="margin-top:40px">
<div class="card transform-up"><div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;margin-bottom:10px">1BR</div><div class="kv" style="border-color:var(--bl);font-size:13px"><span class="k" style="color:var(--mute)">Area</span><span class="v" style="color:var(--ink)">42m\u00b2</span></div><div class="kv" style="border-color:var(--bl);font-size:13px"><span class="k" style="color:var(--mute)">Cost</span><span class="v" style="color:var(--td)">10\u201312k/mo</span></div><div class="kv" style="border-color:transparent;font-size:13px"><span class="k" style="color:var(--mute)">Units</span><span class="v" style="color:var(--ink)">150</span></div></div>
<div class="card transform-up" style="border-color:var(--tb);box-shadow:0 10px 20px rgba(20,184,166,.1)"><div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;margin-bottom:10px">2BR</div><div class="kv" style="border-color:var(--bl);font-size:13px"><span class="k" style="color:var(--mute)">Area</span><span class="v" style="color:var(--ink)">75m\u00b2</span></div><div class="kv" style="border-color:var(--bl);font-size:13px"><span class="k" style="color:var(--mute)">EMI</span><span class="v" style="color:var(--td)">33,015</span></div><div class="kv" style="border-color:transparent;font-size:13px"><span class="k" style="color:var(--mute)">Units</span><span class="v" style="color:var(--ink)">1,130</span></div></div>
<div class="card transform-up"><div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;margin-bottom:10px">3BR</div><div class="kv" style="border-color:var(--bl);font-size:13px"><span class="k" style="color:var(--mute)">Area</span><span class="v" style="color:var(--ink)">95m\u00b2</span></div><div class="kv" style="border-color:var(--bl);font-size:13px"><span class="k" style="color:var(--mute)">EMI</span><span class="v" style="color:var(--td)">40,803</span></div><div class="kv" style="border-color:transparent;font-size:13px"><span class="k" style="color:var(--mute)">Units</span><span class="v" style="color:var(--ink)">700</span></div></div>
<div class="card transform-up" style="border-color:#F59E0B"><div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#B45309;margin-bottom:10px">4BR</div><div class="kv" style="border-color:var(--bl);font-size:13px"><span class="k" style="color:var(--mute)">Area</span><span class="v" style="color:var(--ink)">115m\u00b2</span></div><div class="kv" style="border-color:var(--bl);font-size:13px"><span class="k" style="color:var(--mute)">EMI</span><span class="v" style="color:#B45309">48,615</span></div><div class="kv" style="border-color:transparent;font-size:13px"><span class="k" style="color:var(--mute)">Units</span><span class="v" style="color:var(--ink)">20</span></div></div>
</div>
</div></div>
"""
    slides.append(s40)

    # Slide 41: KMRC Affordability Table
    s41 = f"""
<div class="s" id="s41">{generate_header("04.06 · Financial Viability")}
<div class="pad rv unfold">
<div class="t1">KMRC Affordability Matrix.</div>
<div class="dark">
<table class="dt inv" style="font-size:13px;">
    <tr><th>Unit</th><th>Build Cost (KES 46.5k/m\u00b2) + Land</th><th>EMI @ 8.99% 25YR</th><th>DTI @ KES 87K Gross</th><th>DTI @ KES 110K Gross</th></tr>
    <tr><td>2BR (75m\u00b2)</td><td>3,937,500</td><td style="color:var(--tb);font-weight:700;">33,015</td><td style="color:var(--tb);">38% (\u2713)</td><td style="color:var(--tb);">30% (\u2713)</td></tr>
    <tr><td>3BR (95m\u00b2)</td><td>4,867,500</td><td style="color:var(--tb);font-weight:700;">40,803</td><td style="color:#EF4444;">47% (\u2717)</td><td style="color:var(--tb);">37% (\u2713)</td></tr>
    <tr><td>4BR (115m\u00b2)</td><td>5,797,500</td><td style="color:#F59E0B;font-weight:700;">48,615</td><td style="color:#EF4444;">56% (\u2717)</td><td style="color:#EF4444;">44% (\u2717)</td></tr>
</table>
<div style="margin-top:20px; color:#94A3B8; font-size:12px;">*AHP subsidy required for 3BR if income < KES 100K. Maximum safe DTI threshold is 40%.</div>
</div>
</div></div>
"""
    slides.append(s41)

    # Slide 42: Population Verification
    s42 = f"""
<div class="s" id="s42">{generate_header("04.07 · Population Data")}
<div class="pad rv scaleIn">
<div style="text-align:center;margin-top:48px"><div style="font-family:'Playfair Display',serif;font-size:120px;font-weight:900;color:var(--ink);line-height:1">8,090</div>
<div class="mono" style="font-size:16px;color:var(--mute);margin-top:8px">TOTAL RESIDENTS · 2,000 FAMILIES · 91.5% CORE FAMILY UNITS</div>
<div class="glow-on-hover" style="display:flex;height:60px;border-radius:30px;overflow:hidden;box-shadow:0 12px 24px rgba(0,0,0,.08);margin-top:40px;max-width:900px;margin-left:auto;margin-right:auto; transition:box-shadow .3s;">
<div style="width:3.7%;background:#64748B" title="1BR: 300"></div>
<div style="width:55.9%;background:var(--td);display:flex;align-items:center;justify-content:center;color:#fff;font-size:16px;font-weight:700" title="2BR: 4,520">4,520 Residents in 2BR</div>
<div style="width:38.9%;background:var(--tb);display:flex;align-items:center;justify-content:center;color:#fff;font-size:16px;font-weight:700" title="3BR: 3,150">3,150 Residents in 3BR</div>
<div style="width:1.5%;background:#F59E0B" title="4BR: 120"></div>
</div></div>
</div></div>
"""
    slides.append(s42)

    # Slide 43: Ekeja Cluster Model (SVG Isometric)
    s43 = f"""
<div class="s" id="s43">{generate_header("04.08 · Ekeja Cluster Model")}
<div class="pad rv slideFromRight">
<div class="t1">The Ekeja Five-Storey Block.</div>
<div class="g2" style="align-items:center;">
<div>
    <p class="intro">Gated apartment clusters. Single entry. Shared courtyards. 4 apartments per floor around central stairwell + lift. Ground floor: 2 commercial units. Floors 2\u20135: residential.</p>
</div>
<div class="glow-on-hover" style="text-align:center; background:var(--card); border-radius:32px; padding:40px; border:1px solid var(--bl); transition:box-shadow .3s;">
    <!-- BUILD AN SVG ISOMETRIC/2.5D BUILDING DIAGRAM -->
    <svg viewBox="0 0 200 250" width="100%" height="300" style="filter: drop-shadow(0 20px 30px rgba(0,0,0,0.1));">
        <!-- Isometric projection polygons -->
        <!-- Front Face -->
        <polygon points="100,50 160,80 160,200 100,170" fill="var(--td)" stroke="#fff" stroke-width="1"/>
        <!-- Left Face -->
        <polygon points="40,80 100,50 100,170 40,200" fill="var(--tb)" stroke="#fff" stroke-width="1"/>
        <!-- Roof -->
        <polygon points="100,20 160,50 100,80 40,50" fill="var(--tl)" stroke="var(--td)" stroke-width="2"/>
        
        <!-- Floor lines -->
        <line x1="40" y1="170" x2="100" y2="140" stroke="#fff" stroke-width="1"/> <line x1="100" y1="140" x2="160" y2="170" stroke="#fff" stroke-width="1"/>
        <line x1="40" y1="140" x2="100" y2="110" stroke="#fff" stroke-width="1"/> <line x1="100" y1="110" x2="160" y2="140" stroke="#fff" stroke-width="1"/>
        <line x1="40" y1="110" x2="100" y2="80" stroke="#fff" stroke-width="1"/>  <line x1="100" y1="80" x2="160" y2="110" stroke="#fff" stroke-width="1"/>
        
        <!-- Solar Panels on Roof -->
        <polygon points="100,30 140,50 100,70 60,50" fill="#0F172A"/>
        
        <!-- Commercial Ground floor highlight -->
        <polygon points="40,200 100,170 160,200 100,230" fill="#F59E0B" opacity="0.8"/>
        
        <!-- Labels -->
        <text x="100" y="245" class="mono" style="font-size:10px;fill:var(--ink);text-anchor:middle;">COMMERCIAL BASE</text>
        <text x="100" y="10" class="mono" style="font-size:10px;fill:var(--ink);text-anchor:middle;">SOLAR ROOF</text>
    </svg>
</div>
</div>
</div></div>
"""
    slides.append(s43)

    # Slide 44: Construction Cutaway
    s44 = f"""
<div class="s" id="s44">{generate_header("04.09 · Passive Design")}
<div class="pad rv slideFromLeft">
<div class="t1">Built for the Climate.</div>
<div class="g2">
    <!-- SVG Cross-section -->
    <div style="background:var(--card); border-radius:32px; padding:20px; display:flex; justify-content:center; align-items:center;">
        <svg viewBox="0 0 200 300" width="100%" height="100%" class="draw on">
            <!-- Roof -->
            <polygon points="10,80 100,20 190,80" fill="none" stroke="#1E293B" stroke-width="6"/>
            <!-- Solar Water -->
            <rect x="50" y="30" width="30" height="10" transform="rotate(33 50 30)" fill="#F59E0B"/>
            <!-- Walls -->
            <rect x="20" y="80" width="20" height="200" fill="#B45309"/>
            <rect x="160" y="80" width="20" height="200" fill="#B45309"/>
            <!-- Render -->
            <line x1="15" y1="80" x2="15" y2="280" stroke="#FEF3C7" stroke-width="4"/>
            <line x1="185" y1="80" x2="185" y2="280" stroke="#FEF3C7" stroke-width="4"/>
            <!-- Window -->
            <rect x="16" y="120" width="28" height="60" fill="none" class="sankey-flow" stroke="#38BDF8" stroke-width="4"/>
            <!-- Interior slab -->
            <rect x="40" y="260" width="120" height="20" fill="var(--bl)"/>
        </svg>
    </div>
    
    <div style="display:flex;flex-direction:column;gap:8px;">
        <div class="layer transform-up" style="border-left-color:#1E293B"><div><h4>Ventilated Roof Cavity</h4><p>150mm air gap. Ridge vents. Slab 8\u201312\u00b0C cooler.</p></div></div>
        <div class="layer transform-up" style="border-left-color:#F59E0B"><div><h4>Solar Water Heating</h4><p>2m\u00b2 flat-plate per unit. Eliminates 3kW geyser spike.</p></div></div>
        <div class="layer transform-up" style="border-left-color:#38BDF8"><div><h4>Louvred Windows</h4><p>Aluminium. Cross-ventilation: 3\u20135 air changes/hr. Insect screened (malaria).</p></div></div>
        <div class="layer transform-up" style="border-left-color:#D97706"><div><h4>Laterite-Lime Render</h4><p>15mm breathable skin. 60% solar reflectance. Not cement plaster.</p></div></div>
        <div class="layer transform-up" style="border-left-color:#B45309"><div><h4>CSEB Thermal Mass</h4><p>300mm laterite. 5% cement. Interior stays 20\u201326\u00b0C year-round.</p></div></div>
    </div>
</div>
</div></div>
"""
    slides.append(s44)

    return slides
