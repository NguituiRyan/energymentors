from utils import generate_header

def generate():
    slides = []

    # Slide 77: Act 8 Opener
    s77 = """
<!-- ═══════════════ ACT VIII: FINANCIAL VIABILITY ═══════════════ -->
<div class="s" style="min-height:60vh;background:linear-gradient(135deg,#0F172A,#1E293B);display:flex;align-items:center;justify-content:center;text-align:center;color:#fff">
<div class="rv slideFromRight">
<div class="mono" style="font-size:14px;letter-spacing:.3em;color:var(--td);margin-bottom:24px">Section 08 · Financial Architecture</div>
<div style="font-family:'Playfair Display',serif;font-size:80px;font-weight:900;margin-bottom:16px;">The Matrix of Return.</div>
<div style="font-size:24px;color:rgba(255,255,255,.7)">Predictable cash flows. De-risked off-take.</div>
</div>
</div>
"""
    slides.append(s77)

    # Slide 78: CAPEX Breakdown
    s78 = f"""
<div class="s" id="s78">{generate_header("08.01 · CAPEX Structure")}
<div class="pad rv scaleIn">
<div class="t1">Capital Expenditure Matrix.</div>
<div class="g2">
    <div>
        <p class="intro">Total development cost estimated at <strong>KES 3.8 Billion (~USD 27.5M)</strong>. Extensively modeled against material rates in the Machakos/Nairobi corridor.</p>
        <table class="dt" style="margin-top:20px;">
            <tr><th>Component</th><th>KES (Millions)</th><th>% of Total</th></tr>
            <tr><td>Land Acquisition (400 Acres)</td><td>250</td><td>6.6%</td></tr>
            <tr><td>Housing Construction (1,618)</td><td>2,450</td><td>64.5%</td></tr>
            <tr><td>Solar Microgrid (3.6MW)</td><td>420</td><td>11.0%</td></tr>
            <tr><td>Water & Digester Bio-System</td><td>180</td><td>4.7%</td></tr>
            <tr><td>Roads & Social Infra</td><td>350</td><td>9.2%</td></tr>
            <tr><td>Contingency (4%)</td><td>150</td><td>4.0%</td></tr>
        </table>
    </div>
    <div style="display:flex;align-items:center;justify-content:center;">
        <div style="width:300px;background:#F8FAFC;border-radius:50%;padding:40px;box-shadow:inset 0 0 50px rgba(0,0,0,.05);position:relative;">
            <!-- Abstract Donut -->
            <svg viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="40" fill="none" stroke="var(--bl)" stroke-width="20"/>
                <!-- Housing (64%) -->
                <circle cx="50" cy="50" r="40" fill="none" stroke="var(--ink)" stroke-width="20" stroke-dasharray="251.2" stroke-dashoffset="90"/>
                <!-- Energy (11%) -->
                <circle cx="50" cy="50" r="40" fill="none" stroke="var(--tb)" stroke-width="20" stroke-dasharray="251.2" stroke-dashoffset="223"/>
            </svg>
            <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center;">
                <div style="font-family:'Playfair Display',serif;font-size:24px;font-weight:900;">3.8B</div>
                <div class="mono" style="font-size:10px;">KES TOTAL</div>
            </div>
        </div>
    </div>
</div>
</div></div>
"""
    slides.append(s78)

    # Slide 79: OPEX & Margins
    s79 = f"""
<div class="s" id="s79">{generate_header("08.02 · Revenue Operations")}
<div class="pad rv slideFromLeft">
<div class="t1">The Margin Engine.</div>
<div class="g3" style="margin-top:40px;">
    <div class="card" style="border-top:4px solid var(--tb);">
        <h4 style="font-weight:700;font-size:18px;margin-bottom:8px;">Utility Sales (Energy + Water)</h4>
        <p style="font-size:14px;color:var(--mute);line-height:1.6;margin-bottom:16px;">Sold internally at cost+ margins. Yields KES 85M annually.</p>
        <div class="mono" style="font-size:20px;font-weight:700;color:var(--td);">KES 85M / YR</div>
    </div>
    <div class="card" style="border-top:4px solid #F59E0B;">
        <h4 style="font-weight:700;font-size:18px;margin-bottom:8px;">YattaFarm Yields</h4>
        <p style="font-size:14px;color:var(--mute);line-height:1.6;margin-bottom:16px;">High-margin horticulture leveraging free municipal water and power.</p>
        <div class="mono" style="font-size:20px;font-weight:700;color:#D97706;">KES 120M / YR</div>
    </div>
    <div class="card" style="border-top:4px solid #3B82F6;">
        <h4 style="font-weight:700;font-size:18px;margin-bottom:8px;">Commercial Leases</h4>
        <p style="font-size:14px;color:var(--mute);line-height:1.6;margin-bottom:16px;">Supermarket, EV hub, and clinic rentals collected by the SACCO.</p>
        <div class="mono" style="font-size:20px;font-weight:700;color:#2563EB;">KES 45M / YR</div>
    </div>
</div>
<div style="background:#0F172A;color:#fff;border-radius:16px;padding:24px 40px;margin-top:30px;display:flex;justify-content:space-between;align-items:center;">
    <div><div class="mono" style="color:var(--mute);font-size:12px;">GROSS REVENUE</div><div style="font-size:24px;font-weight:700;">KES 250M / YR</div></div>
    <div>➖</div>
    <div><div class="mono" style="color:var(--mute);font-size:12px;">OPEX & DEV FUND</div><div style="font-size:24px;font-weight:700;color:#EF4444;">KES 90M / YR</div></div>
    <div>=</div>
    <div><div class="mono" style="color:var(--mute);font-size:12px;">SACCO NET SURPLUS</div><div style="font-size:24px;font-weight:700;color:var(--tb);">KES 160M / YR</div></div>
</div>
</div></div>
"""
    slides.append(s79)

    # Slide 80: Mortgage Structure
    s80 = f"""
<div class="s" id="s80">{generate_header("08.03 · Affordable Mortgages")}
<div class="pad rv scaleIn">
<div class="t1">The KMRC Debt Pipeline.</div>
<div class="intro">We partner directly with the Kenya Mortgage Refinance Company to slash end-user debt service ratios.</div>
<div style="display:flex;border:1px solid var(--bl);border-radius:24px;overflow:hidden;margin-top:20px;">
    <!-- Offtaker -->
    <div style="flex:1;background:var(--card);padding:40px;text-align:center;">
        <div style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;color:var(--ink);">8.99%</div>
        <div class="mono" style="font-size:12px;color:var(--mute);margin-top:10px;">FIXED INTEREST FOR BUYERS</div>
        <p style="font-size:14px;color:var(--mute);margin-top:20px;">Buyers pay 8.99% fixed for 20 years. Ensures the Nurse and Teacher can afford the 2-BR unit without exceeding 30% of gross income.</p>
    </div>
    <!-- Pipeline -->
    <div style="flex:1;background:#DFFAFA;padding:40px;border-left:1px solid var(--bl);border-right:1px solid var(--bl);text-align:center;">
        <div style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;color:var(--td);">5.00%</div>
        <div class="mono" style="font-size:12px;color:var(--mute);margin-top:10px;">KMRC WHOLESALE RATE</div>
        <p style="font-size:14px;color:var(--mute);margin-top:20px;">The Angawatch SACCO borrows the development debt from KMRC at 5%. The ~4% spread covers defaults and SACCO liquidity.</p>
    </div>
</div>
</div></div>
"""
    slides.append(s80)

    # Slide 81: Repayment Waterfall
    s81 = f"""
<div class="s" id="s81">{generate_header("08.04 · Repayment Mechanics")}
<div class="pad rv slideFromRight">
<div class="g2">
    <div>
        <h3 style="font-size:32px;font-weight:700;margin-bottom:20px;">The Waterfall.</h3>
        <p style="font-size:16px;line-height:1.7;color:var(--body);margin-bottom:20px;">How a single M-Pesa transaction covers everything. Residents pay a consolidated monthly "AngaBill". The system programmatically splits the funds.</p>
        <ul style="font-size:15px;line-height:2;padding-left:20px;">
            <li><strong style="color:var(--ink);">Tier 1 (Senior):</strong> KMRC Mortgage Service (65%)</li>
            <li><strong style="color:var(--ink);">Tier 2 (Utility):</strong> Energy & Water Consumption (15%)</li>
            <li><strong style="color:var(--ink);">Tier 3 (Sub):</strong> SACCO Maintenance / Admin Fee (10%)</li>
            <li><strong style="color:var(--ink);">Tier 4 (Equity):</strong> Resident Sinking Fund (10%)</li>
        </ul>
    </div>
    <div style="background:#1E293B;padding:40px;border-radius:32px;">
        <svg viewBox="0 0 300 300" width="100%" height="auto">
            <!-- M-PESA Input -->
            <rect x="100" y="20" width="100" height="40" rx="10" fill="#16A34A"/>
            <text x="150" y="45" class="mono" style="fill:#fff;font-size:14px;font-weight:700;text-anchor:middle">M-PESA PAYBILL</text>
            
            <line x1="150" y1="60" x2="150" y2="100" stroke="#fff" stroke-width="4"/>
            <!-- Tiers -->
            <rect x="50" y="100" width="200" height="30" rx="5" fill="none" stroke="#fff" stroke-width="2"/>
            <text x="150" y="120" style="fill:#fff;font-size:12px;text-anchor:middle">1. MORTGAGE</text>
            
            <line x1="150" y1="130" x2="150" y2="160" stroke="#fff" stroke-width="2"/>
            <rect x="50" y="160" width="200" height="30" rx="5" fill="none" stroke="#38BDF8" stroke-width="2"/>
            <text x="150" y="180" style="fill:#38BDF8;font-size:12px;text-anchor:middle">2. UTILITIES (SMART METER)</text>
            
            <line x1="150" y1="190" x2="150" y2="220" stroke="#fff" stroke-width="2"/>
            <rect x="50" y="220" width="200" height="30" rx="5" fill="none" stroke="#F59E0B" stroke-width="2"/>
            <text x="150" y="240" style="fill:#F59E0B;font-size:12px;text-anchor:middle">3. SACCO FEES & SINKING</text>
        </svg>
    </div>
</div>
</div></div>
"""
    slides.append(s81)

    # Slide 82: Risk Matrix
    s82 = f"""
<div class="s" id="s82">{generate_header("08.05 · Risk & Mitigation")}
<div class="pad rv scaleIn">
<div class="t1">Risk Mitigation.</div>
<table class="dt" style="margin-top:20px;">
    <tr><th>Risk Profile</th><th>Severity</th><th>Angawatch Mitigation Strategy</th></tr>
    <tr><td><strong style="color:#EF4444">Resident Default</strong></td><td>High</td><td>The SACCO holds the title until clearance. Utilities are dynamically throttled to basic life-support levels (10W LED + Water) to enforce payment without inhumane shutoffs.</td></tr>
    <tr><td><strong style="color:#F59E0B">Battery Degradation</strong></td><td>Med</td><td>LCOE model fully bakes in replacing all CATL LFP modules at Year 15 via the Sinking Fund.</td></tr>
    <tr><td><strong style="color:#F59E0B">Construction Cost Overrun</strong></td><td>Med</td><td>Use of EPS (Expanded Polystyrene) panels prevents supply chain variability of cement. Standardized modular designs globally source components.</td></tr>
    <tr><td><strong style="color:var(--td)">Grid Instability (KPLC)</strong></td><td>Low</td><td>Primary architecture is an independent microgrid. KPLC is only required during 7+ day rain events. Even a complete KPLC collapse only triggers the standby diesels.</td></tr>
</table>
</div></div>
"""
    slides.append(s82)

    # Slide 83: End Act 8
    s83 = f"""
<div class="s" id="s83">{generate_header("08.06 · Bankability")}
<div class="pad rv unfold">
<div class="g2" style="align-items:center;">
    <div style="background:var(--ink);padding:60px 40px;border-radius:32px;text-align:center;">
        <div style="font-family:'Playfair Display',serif;font-size:80px;font-weight:700;color:var(--tl);line-height:1;">IFC</div>
        <div class="mono" style="font-size:16px;color:var(--mute);margin-top:10px;">EDGE ADVANCED CERTIFIED</div>
    </div>
    <div>
        <h3 style="font-size:32px;font-weight:700;margin-bottom:20px;">Institutional Grade.</h3>
        <p style="font-size:18px;line-height:1.7;color:var(--body);">The financial model bridges the gap between massive global green bonds and the Kenyan affordability crisis. By securitizing the utility cash flows and hedging the mortgage debt via KMRC, Angawatch becomes an entirely bankable asset for DFIs, pension funds, and impact investors.</p>
    </div>
</div>
</div></div>
"""
    slides.append(s83)

    return slides
