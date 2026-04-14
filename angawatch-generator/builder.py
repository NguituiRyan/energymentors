import os
import importlib

# Ensure the acts package exists
if not os.path.exists("acts"):
    os.makedirs("acts")
    open("acts/__init__.py", "w").close()

# The base HTML format given by user rules
HTML_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Angawatch Eco-Community \u2014 Complete Engineering Narrative</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,900;1,400;1,600&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&family=DM+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{--bg:#F1F5F9;--white:#FFFFFF;--ink:#0F172A;--body:#334155;--mute:#64748B;--td:#0F766E;--tl:#CCFBF1;--tb:#14B8A6;--bl:#E2E8F0;--bm:#CBD5E1;--card:#F8FAFC}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'DM Sans',sans-serif;background:var(--bg);color:var(--body);overflow-x:hidden;padding:0;scroll-behavior:smooth;-webkit-font-smoothing:antialiased}
.deck{width:100%;max-width:1400px;margin:40px auto 120px;background:var(--white);box-shadow:0 25px 50px -12px rgba(0,0,0,.1);border-radius:32px;display:flex;flex-direction:column;overflow:hidden}
.s{position:relative;padding:100px 0;border-bottom:1px solid var(--bl);display:flex;flex-direction:column;background:var(--white);overflow:hidden;min-height:50vh;}
.s:last-child{border-bottom:none}
.hdr{padding:0 80px 60px;display:flex;align-items:center;justify-content:space-between;z-index:10;position:relative}
.logo{display:flex;align-items:center;gap:12px}
.logo svg{width:32px;height:32px}
.logo span{font-family:'Playfair Display',serif;font-size:20px;font-weight:700;color:var(--ink)}
.tag{font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--td);font-weight:600;background:var(--tl);padding:8px 16px;border-radius:100px}
.pad{padding:0 80px;position:relative;z-index:2}
.t1{font-family:'Playfair Display',serif;font-size:56px;font-weight:700;line-height:1.1;letter-spacing:-.02em;margin-bottom:24px;color:var(--ink)}
.t1 em{font-style:italic;color:var(--td);border-bottom:4px solid var(--tl)}
.intro{font-size:18px;color:var(--body);line-height:1.7;margin-bottom:40px;max-width:900px}
.big{font-family:'Playfair Display',serif;font-weight:900;color:var(--td);line-height:1}
.mono{font-family:'DM Mono',monospace}
.quote{font-family:'Playfair Display',serif;font-style:italic;font-size:22px;color:var(--ink);line-height:1.5;border-left:4px solid var(--td);background:var(--tl);padding:24px 32px;margin:24px 0;border-radius:0 16px 16px 0;box-shadow:4px 8px 24px rgba(20,184,166,.1)}
.quote small{display:block;font-family:'DM Sans',sans-serif;font-style:normal;font-size:14px;color:var(--mute);margin-top:12px}
@keyframes morph{0%,100%{border-radius:40% 60% 70% 30%/40% 50% 60% 50%}34%{border-radius:70% 30% 50% 50%/30% 30% 70% 70%}67%{border-radius:100% 60% 60% 100%/100% 100% 60% 60%}}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-20px)}}
@keyframes up{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:translateY(0)}}
@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}
@keyframes draw{to{stroke-dashoffset:0}}
@keyframes fadeSlideUp{from{opacity:0;transform:translateY(60px)}to{opacity:1;transform:translateY(0)}}
@keyframes shimmer{0%{background-position:-200% 0}100%{background-position:200% 0}}
@keyframes unfold{from{transform:perspective(500px) rotateX(-90deg);opacity:0}to{transform:perspective(500px) rotateX(0deg);opacity:1}}
@keyframes countUp{from{transform:translateY(20px);opacity:0}to{transform:translateY(0);opacity:1}}
@keyframes slideFromLeft{from{transform:translateX(-100px);opacity:0}to{transform:translateX(0);opacity:1}}
@keyframes slideFromRight{from{transform:translateX(100px);opacity:0}to{transform:translateX(0);opacity:1}}
@keyframes scaleIn{from{transform:scale(0.8);opacity:0}to{transform:scale(1);opacity:1}}
.rv{opacity:0}.rv.on{animation:fadeSlideUp .8s cubic-bezier(.16,1,.3,1) forwards}
.draw.on path, .draw.on line, .draw.on circle, .draw.on rect {animation:draw 4s ease-out forwards;}
.unfold.on {animation:unfold 1s cubic-bezier(.16,1,.3,1) forwards;}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:48px}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:32px}
.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:24px}
.dark{background:var(--ink);color:#fff;border-radius:32px;padding:64px;position:relative;overflow:hidden}
.dark .cross{position:absolute;width:20px;height:20px;opacity:.2}
.dark .cross::before,.dark .cross::after{content:'';position:absolute;background:#fff}
.dark .cross::before{top:50%;left:0;width:100%;height:1px}
.dark .cross::after{left:50%;top:0;height:100%;width:1px}
.kv{display:flex;justify-content:space-between;padding:14px 0;border-bottom:1px solid rgba(255,255,255,.1);font-size:15px}
.kv:last-child{border-bottom:none}
.kv .k{color:#CBD5E1}.kv .v{font-weight:600;color:#fff;font-family:'DM Mono',monospace;font-size:14px}
.kv .v.hi{background:var(--tb);color:#fff;padding:4px 10px;border-radius:6px}
table.dt{width:100%;border-collapse:collapse;font-size:14px;background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 4px 6px rgba(0,0,0,.02)}
table.dt th,table.dt td{padding:16px 20px;text-align:left;border-bottom:1px solid var(--bl)}
table.dt th{background:var(--card);font-weight:700;color:var(--ink);font-family:'DM Mono',monospace;font-size:12px;text-transform:uppercase;letter-spacing:.05em}
table.dt.inv{background:#0F172A;color:#fff}
table.dt.inv th{background:#1E293B;color:#94A3B8}
table.dt.inv td{border-color:#1E293B}
.bar-w{height:12px;background:var(--bl);border-radius:6px;overflow:hidden;flex:1}
.bar-f{height:100%;border-radius:6px}
.pill{background:#fff;border:1px solid var(--bm);border-radius:16px;padding:20px;display:flex;gap:16px;align-items:center;transition:all .3s;box-shadow:4px 4px 0 var(--bl)}
.pill:hover{transform:translateY(-4px);border-color:var(--tb);box-shadow:6px 6px 0 var(--tl)}
.pill .n{font-family:'Playfair Display',serif;font-size:40px;font-weight:900;color:var(--tb);line-height:.8;opacity:.5}
.card{background:var(--card);padding:32px;border-radius:24px;border:1px solid var(--bl);transition:all .3s}
.card:hover{transform:translateY(-6px);box-shadow:0 20px 40px rgba(15,118,110,.1);border-color:var(--tl)}
.zone{border-radius:12px;padding:16px;color:#fff;display:flex;flex-direction:column;justify-content:flex-end;transition:all .3s;cursor:crosshair;position:relative;overflow:hidden}
.zone:hover{transform:scale(1.02);z-index:10;box-shadow:0 20px 40px rgba(0,0,0,.15)}
.zone::after{content:'';position:absolute;inset:0;background:linear-gradient(rgba(255,255,255,.2),transparent);pointer-events:none}
.fp-box{background:#fff;border-radius:32px;padding:48px;border:1px solid var(--bl);box-shadow:0 20px 40px rgba(0,0,0,.03);display:flex;align-items:center;justify-content:center;min-height:420px;position:relative}
.fp-wall{fill:none;stroke:var(--ink);stroke-width:4;stroke-linecap:square;transition:stroke 0.3s;}
.fp-wall:hover{stroke:var(--td);}
.fp-win{fill:none;stroke:var(--tb);stroke-width:6;stroke-dasharray:8 4}
.fp-room{fill:rgba(20,184,166,.05);transition:fill .3s, transform .3s; transform-origin:center;}
.fp-room:hover{fill:rgba(20,184,166,.15);transform:scale(1.01);}
.fp-t{font-family:'DM Mono',monospace;font-size:10px;fill:var(--ink);text-anchor:middle;font-weight:600;pointer-events:none}
.fp-d{font-size:8px;fill:var(--mute)}
.ol-box{background:#0F172A;border-radius:32px;padding:40px;min-height:600px;display:flex;align-items:center;justify-content:center;overflow:hidden}
.ol-line{stroke:#38BDF8;stroke-width:3;fill:none}
.ol-node{fill:#1E293B;stroke:#38BDF8;stroke-width:2;transition:all 0.3s;}
.ol-node:hover{fill:#38BDF8;scale:1.05;}
.ol-t{font-family:'DM Mono',monospace;font-size:12px;fill:#94A3B8;text-anchor:middle}
.ol-tb{font-weight:700;fill:#F8FAFC}
.phone{width:300px;height:580px;background:#fff;border-radius:44px;box-shadow:0 25px 50px -12px rgba(0,0,0,.2),inset 0 0 0 10px #0F172A;margin:0 auto;position:relative;overflow:hidden;display:flex;flex-direction:column}
.phone .notch{position:absolute;top:10px;left:50%;transform:translateX(-50%);width:100px;height:26px;background:#0F172A;border-radius:0 0 14px 14px;z-index:10}
.phone .screen{padding:54px 20px 20px;flex:1;background:var(--card);display:flex;flex-direction:column;gap:12px}
.bubble{background:var(--bl);padding:10px 14px;border-radius:14px 14px 14px 4px;font-size:13px;color:var(--ink);font-family:monospace;transition:transform 0.3s;}
.bubble:hover{transform:scale(1.02);}
.bubble.r{background:var(--tb);color:#fff;border-radius:14px 14px 4px 14px;align-self:flex-end}
.token{background:#fff;border:2px dashed var(--td);padding:14px;border-radius:12px;text-align:center;margin-top:auto;transition:box-shadow 0.3s;}
.token:hover{box-shadow: 0 10px 20px rgba(20,184,166,0.2);}
.token .num{font-family:'DM Mono',monospace;font-size:16px;font-weight:700;color:var(--ink);letter-spacing:2px;margin-bottom:6px}
.layer{background:#fff;border-radius:16px;padding:24px 40px;display:flex;align-items:center;gap:40px;box-shadow:0 4px 12px rgba(0,0,0,.02);border-left:8px solid var(--bm);transition:transform .3s, border-left-color .3s;}
.layer:hover{transform:translateX(10px);border-left-color:var(--td) !important;}
.layer h4{font-size:18px;font-weight:700;margin-bottom:6px;color:var(--ink)}
.layer p{font-size:14px;color:var(--body);line-height:1.5}

/* Additional specific utility classes for hover effects and animations */
.glow-on-hover:hover { box-shadow: 0 0 20px var(--tl); }
.transform-up:hover { transform: translateY(-10px); }
.transform-scale:hover { transform: scale(1.05); }

/* SVG Animation specific */
.sankey-flow { stroke-dasharray: 2000; stroke-dashoffset: 2000; }
.draw.on .sankey-flow { animation: drawPathAnim 3s ease-out forwards; }
@keyframes drawPathAnim { to { stroke-dashoffset: 0; } }

@media(max-width:1024px){
  .pad{padding:0 40px}
  .hdr{padding:0 40px 40px}
  .g2,.g3,.g4{grid-template-columns:1fr}
}
@media(max-width:768px){
  .t1{font-size:40px}
  .quote{font-size:18px;padding:16px}
}
</style>
</head>
<body>
<div class="deck" id="deck">
"""

HTML_FOOT = """
</div><!-- /deck -->

<script>
const obs=new IntersectionObserver(e=>{
    e.forEach(en=>{
        if(en.isIntersecting){
            en.target.querySelectorAll('.rv, .draw, .unfold, .slideFromLeft, .slideFromRight, .scaleIn').forEach(el=>el.classList.add('on'))
        }
    })
},{rootMargin:'-10% 0px -10% 0px',threshold:.15});

document.querySelectorAll('.s').forEach(s=>obs.observe(s));
</script>
</body>
</html>
"""


def main():
    import acts.act_0_cover as act_0_cover
    import acts.act_1_land as act_1_land
    import acts.act_2_problem as act_2_problem
    import acts.act_3_people as act_3_people
    import acts.act_4_homes as act_4_homes
    import acts.act_5_energy as act_5_energy
    import acts.act_6_water as act_6_water
    import acts.act_7_community as act_7_community
    import acts.act_8_money as act_8_money
    import acts.act_9_proof as act_9_proof
    import acts.act_10_close as act_10_close

    generated_slides = []

    # Compile the acts
    generated_slides.extend(act_0_cover.generate())
    generated_slides.extend(act_1_land.generate())
    generated_slides.extend(act_2_problem.generate())
    generated_slides.extend(act_3_people.generate())
    generated_slides.extend(act_4_homes.generate())
    generated_slides.extend(act_5_energy.generate())
    generated_slides.extend(act_6_water.generate())
    generated_slides.extend(act_7_community.generate())
    generated_slides.extend(act_8_money.generate())
    generated_slides.extend(act_9_proof.generate())
    generated_slides.extend(act_10_close.generate())
    
    # Write to final output file
    target_path = r"c:\Users\phant\Desktop\Angawatch\angawatch_visual_narrative.html"
    
    with open(target_path, "w", encoding="utf-8") as file:
        file.write(HTML_HEAD)
        for slide in generated_slides:
            file.write(slide + "\\n")
        file.write(HTML_FOOT)
        
    print(f"Generated {len(generated_slides)} slides successfully into {target_path}")

if __name__ == "__main__":
    main()
