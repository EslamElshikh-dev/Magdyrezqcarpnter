from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SITE_NAME = "أفضل نجار تفصيل خزائن ودواليب بالرياض | النجار مجدي رزق"
LOGO_URL = "https://imgg.io/images/2026/03/19/c79d40338dd22427f1c7089e42d61749.png"

NORTH = "حطين، الملقا، الياسمين، النرجس، العارض، القيروان، الصحافة، الربيع، الغدير، النخيل، المحمدية، الرائد، العقيق"
EAST = "قرطبة، غرناطة، المونسية، الرمال، إشبيلية، اليرموك، الروضة، الخليج"
WEST = "السفارات، عرقة، ظهرة لبن، المهدية، طويق، نمار"
CENTER_SOUTH = "العليا، السليمانية، الملك فهد، الملز، الشفا، الربوة، العزيزية"
ALL_AREAS = f"{NORTH}، {EAST}، {WEST}، {CENTER_SOUTH}"

ROOT_AREAS_SECTION = f'''\n    <section id="riyadh-neighborhoods" class="section-deep neighborhoods-section">\n        <h2 class="section-title reveal"><span class="ar">نجار يخدم أحياء الرياض</span><span class="en">Carpentry Services Across Riyadh</span></h2>\n        <p class="section-lead reveal"><span class="ar">يقدم النجار مجدي رزق خدمات تفصيل الخزائن والدواليب وأعمال النجارة حسب المقاس في أحياء الرياض، مع البدء بالأحياء الراقية في شمال المدينة ثم شرقها وغربها ووسطها وجنوبها، وفق موقع المشروع وطبيعة العمل.</span><span class="en">Custom carpentry, cabinets, and wardrobes are available across Riyadh, subject to project location and scope.</span></p>\n        <div class="neighborhoods-grid reveal">\n            <article class="neighborhood-card"><i class="fas fa-star" aria-hidden="true"></i><h3>الأحياء الراقية في شمال الرياض</h3><p>{NORTH}</p></article>\n            <article class="neighborhood-card"><i class="fas fa-compass" aria-hidden="true"></i><h3>أحياء شرق الرياض</h3><p>{EAST}</p></article>\n            <article class="neighborhood-card"><i class="fas fa-map-signs" aria-hidden="true"></i><h3>أحياء غرب الرياض</h3><p>{WEST}</p></article>\n            <article class="neighborhood-card"><i class="fas fa-city" aria-hidden="true"></i><h3>وسط وجنوب الرياض</h3><p>{CENTER_SOUTH}</p></article>\n        </div>\n        <p class="neighborhood-note reveal"><span class="ar">وجود اسم الحي ضمن القائمة لا يعني وجود فرع مستقل داخله؛ الخدمة تُنسق كنطاق خدمة داخل مدينة الرياض بعد إرسال الموقع ونوع العمل.</span><span class="en">Areas are served by appointment based on project location and scope.</span></p>\n    </section>\n'''

INNER_AREAS_SECTION = f'''\n        <section class="section section-alt neighborhoods-section" id="riyadh-neighborhoods">\n            <div class="container">\n                <div class="section-heading center">\n                    <p class="eyebrow">نطاق خدمة داخل مدينة الرياض</p>\n                    <h2>خدمات النجارة وتفصيل الخزائن في أحياء الرياض</h2>\n                    <p>يصل النجار مجدي رزق إلى الأحياء الراقية في شمال الرياض وباقي مناطق المدينة لتنفيذ تفصيل الخزائن والدواليب والديكورات الخشبية والصيانة حسب المقاس، وفق موقع المشروع وطبيعة العمل.</p>\n                </div>\n                <div class="neighborhoods-grid">\n                    <article class="neighborhood-card"><i class="fas fa-star" aria-hidden="true"></i><h3>شمال الرياض</h3><p>{NORTH}</p></article>\n                    <article class="neighborhood-card"><i class="fas fa-compass" aria-hidden="true"></i><h3>شرق الرياض</h3><p>{EAST}</p></article>\n                    <article class="neighborhood-card"><i class="fas fa-map-signs" aria-hidden="true"></i><h3>غرب الرياض</h3><p>{WEST}</p></article>\n                    <article class="neighborhood-card"><i class="fas fa-city" aria-hidden="true"></i><h3>وسط وجنوب الرياض</h3><p>{CENTER_SOUTH}</p></article>\n                </div>\n                <p class="neighborhood-note">تُحدد إمكانية المعاينة والتنفيذ بعد إرسال اسم الحي وموقع المشروع ونوع الخدمة. هذه الأحياء تمثل نطاق خدمة وليست فروعًا مستقلة.</p>\n            </div>\n        </section>\n'''

ROOT_CSS = '''\n        /* Riyadh neighborhoods and homepage brand */\n        .site-brand { display: inline-flex; align-items: center; gap: 10px; min-width: 0; }\n        .site-logo { width: 42px; height: 42px; flex: 0 0 42px; border-radius: 50%; object-fit: cover; background: #fff; border: 1px solid rgba(122, 73, 38, 0.22); box-shadow: 0 5px 16px rgba(66, 43, 29, 0.12); }\n        .neighborhoods-section { text-align: center; }\n        .neighborhoods-grid { width: min(1120px, 100%); margin: 0 auto; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 18px; padding: 0 5%; }\n        .neighborhood-card { height: 100%; padding: 26px 20px; border-radius: 18px; border: 1px solid rgba(122, 73, 38, 0.18); background: rgba(255,255,255,0.92); box-shadow: 0 10px 30px rgba(66,43,29,0.08); }\n        .neighborhood-card i { width: 46px; height: 46px; display: grid; place-items: center; margin: 0 auto 14px; border-radius: 14px; color: var(--gold-primary); background: rgba(154,87,40,0.09); }\n        .neighborhood-card h3 { margin-bottom: 10px; color: var(--gold-light); font-size: 1.08rem; }\n        .neighborhood-card p { color: var(--text-muted); font-size: 0.92rem; line-height: 1.9; }\n        .neighborhood-note { max-width: 900px; margin: 22px auto 0; padding: 0 5%; color: var(--text-muted); font-size: 0.86rem; line-height: 1.8; }\n        @media (max-width: 980px) { .neighborhoods-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }\n        @media (max-width: 620px) { .header-right { gap: 9px; } .site-brand { gap: 7px; } .site-logo { width: 36px; height: 36px; flex-basis: 36px; } .neighborhoods-grid { grid-template-columns: 1fr; padding: 0 4%; } }\n'''

SHARED_CSS = '''\n\n/* Riyadh service areas */\n.neighborhoods-grid {\n    display: grid;\n    grid-template-columns: repeat(4, minmax(0, 1fr));\n    gap: 18px;\n}\n.neighborhood-card {\n    height: 100%;\n    padding: 25px 20px;\n    border: 1px solid var(--line);\n    border-radius: 20px;\n    background: rgba(255, 255, 255, 0.92);\n    box-shadow: 0 10px 30px rgba(66, 43, 29, 0.08);\n    text-align: center;\n}\n.neighborhood-card i {\n    width: 48px;\n    height: 48px;\n    display: grid;\n    place-items: center;\n    margin: 0 auto 14px;\n    border-radius: 14px;\n    background: rgba(154, 87, 40, 0.09);\n    color: var(--gold-light);\n}\n.neighborhood-card h3 { margin: 0 0 10px; color: var(--gold-light); font-size: 1.08rem; }\n.neighborhood-card p { margin: 0; color: var(--muted); font-size: 0.92rem; line-height: 1.9; }\n.neighborhood-note { max-width: 900px; margin: 24px auto 0; color: var(--muted); text-align: center; font-size: 0.88rem; }\n@media (max-width: 980px) { .neighborhoods-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }\n@media (max-width: 620px) { .neighborhoods-grid { grid-template-columns: 1fr; } }\n'''

AREAS_SCHEMA = f'''\n    <script type="application/ld+json" id="riyadh-service-areas-schema">\n    {{\n      "@context": "https://schema.org",\n      "@type": "ItemList",\n      "@id": "https://magdyrezqfaninejara.com/#riyadh-service-areas",\n      "name": "أحياء الرياض التي تشملها خدمات النجار مجدي رزق",\n      "itemListElement": [\n        {{"@type": "ListItem", "position": 1, "name": "شمال الرياض: {NORTH}"}},\n        {{"@type": "ListItem", "position": 2, "name": "شرق الرياض: {EAST}"}},\n        {{"@type": "ListItem", "position": 3, "name": "غرب الرياض: {WEST}"}},\n        {{"@type": "ListItem", "position": 4, "name": "وسط وجنوب الرياض: {CENTER_SOUTH}"}}\n      ]\n    }}\n    </script>\n'''


def set_meta(html: str, name: str, content: str) -> str:
    pattern = rf'(<meta\s+name=["\']{re.escape(name)}["\']\s+content=["\'])[^"\']*(["\'])'
    if re.search(pattern, html, flags=re.I):
        return re.sub(pattern, rf'\g<1>{content}\g<2>', html, count=1, flags=re.I)
    return html.replace('</head>', f'    <meta name="{name}" content="{content}">\n</head>', 1)


def set_property(html: str, prop: str, content: str) -> str:
    pattern = rf'(<meta\s+property=["\']{re.escape(prop)}["\']\s+content=["\'])[^"\']*(["\'])'
    if re.search(pattern, html, flags=re.I):
        return re.sub(pattern, rf'\g<1>{content}\g<2>', html, count=1, flags=re.I)
    return html.replace('</head>', f'    <meta property="{prop}" content="{content}">\n</head>', 1)


def update_common_metadata(html: str) -> str:
    html = set_property(html, 'og:site_name', SITE_NAME)
    html = set_meta(html, 'application-name', SITE_NAME)
    html = set_meta(html, 'apple-mobile-web-app-title', 'النجار مجدي رزق')
    return html


def inject_schema(html: str) -> str:
    if 'riyadh-service-areas-schema' not in html:
        html = html.replace('</head>', AREAS_SCHEMA + '</head>', 1)
    return html


def inject_areas(html: str, root_page: bool) -> str:
    if 'id="riyadh-neighborhoods"' in html:
        return html
    section = ROOT_AREAS_SECTION if root_page else INNER_AREAS_SECTION
    marker = re.search(r'\n\s*<section[^>]*id=["\']faq["\'][^>]*>', html, flags=re.I)
    if marker:
        return html[:marker.start()] + '\n' + section + html[marker.start():]
    return html.replace('</main>', section + '\n    </main>', 1)


def update_service_area_answers(html: str) -> str:
    replacements = {
        'تقدم الخدمة داخل مدينة الرياض وفق موقع المشروع وطبيعة العمل وحجم المعاينة أو التركيب. يمكن إرسال اسم الحي ونوع الخدمة والصور عبر واتساب لتأكيد إمكانية التنسيق والموعد المناسب.':
        f'تقدم الخدمة داخل مدينة الرياض وتشمل الأحياء الراقية في شمال الرياض مثل {NORTH}، إضافة إلى أحياء الشرق والغرب والوسط والجنوب. يمكن إرسال اسم الحي ونوع الخدمة والصور عبر واتساب لتأكيد إمكانية التنسيق والموعد المناسب.',
        'تقدم الخدمة داخل مدينة الرياض وفق موقع المشروع وطبيعة العمل وحجم المعاينة أو التركيب. يفضل إرسال الحي ونوع الخدمة مع الصور لتأكيد إمكانية التنسيق والموعد المناسب.':
        f'تقدم الخدمة داخل مدينة الرياض، بدءًا من أحياء شمال الرياض مثل {NORTH}، وتمتد إلى أحياء الشرق والغرب والوسط والجنوب. يفضل إرسال اسم الحي ونوع الخدمة مع الصور لتأكيد إمكانية التنسيق والموعد المناسب.'
    }
    for old, new in replacements.items():
        html = html.replace(old, new)
    return html


def update_root_index(path: Path) -> None:
    html = path.read_text(encoding='utf-8')
    html = update_common_metadata(html)
    html = set_meta(html, 'description', 'أفضل نجار تفصيل خزائن ودواليب بالرياض النجار مجدي رزق، لتنفيذ خزائن ودواليب وغرف نوم وديكورات خشبية حسب المقاس مع صيانة النجارة وخدمة أحياء الرياض.')
    html = set_meta(html, 'keywords', f'أفضل نجار بالرياض, نجار تفصيل خزائن ودواليب بالرياض, النجار مجدي رزق, تفصيل خزائن بالرياض, تفصيل دواليب بالرياض, نجار شمال الرياض, {ALL_AREAS}')
    html = set_property(html, 'og:title', SITE_NAME)
    html = set_meta(html, 'twitter:title', SITE_NAME)
    html = re.sub(r'<title>.*?</title>', f'<title>{SITE_NAME}</title>', html, count=1, flags=re.S)
    html = html.replace('"alternateName": "مجدي رزق نجار وتفصيل خزائن"', f'"alternateName": "{SITE_NAME}"')
    html = html.replace('"name": "مجدي رزق فني نجارة",\n          "inLanguage"', f'"name": "{SITE_NAME}",\n          "inLanguage"')

    old_area = '''"areaServed": {\n             "@type": "City",\n             "name": "الرياض"\n           },'''
    new_area = f'''"areaServed": [\n             {{"@type": "City", "name": "الرياض"}},\n             {{"@type": "Place", "name": "شمال الرياض: {NORTH}"}},\n             {{"@type": "Place", "name": "شرق الرياض: {EAST}"}},\n             {{"@type": "Place", "name": "غرب الرياض: {WEST}"}},\n             {{"@type": "Place", "name": "وسط وجنوب الرياض: {CENTER_SOUTH}"}}\n           ],'''
    html = html.replace(old_area, new_area)

    old_header = '''            <div class="site-title">\n                <span class="ar">مجدي رزق فني نجارة</span>\n                <span class="en">Magdi Rizk Carpentry</span>\n            </div>'''
    new_header = f'''            <div class="site-brand">\n                <img class="site-logo" src="{LOGO_URL}" width="42" height="42" alt="شعار النجار مجدي رزق لتفصيل الخزائن والدواليب بالرياض">\n                <div class="site-title">\n                    <span class="ar">النجار مجدي رزق</span>\n                    <span class="en">Magdi Rizk Carpentry</span>\n                </div>\n            </div>'''
    html = html.replace(old_header, new_header)
    html = html.replace('مجدي رزق فني <strong>نجار</strong> في الرياض يقدم خدمات', 'النجار مجدي رزق في الرياض يقدم خدمات')
    html = update_service_area_answers(html)
    html = inject_areas(html, True)
    html = inject_schema(html)
    if '/* Riyadh neighborhoods and homepage brand */' not in html:
        html = html.replace('    </style>', ROOT_CSS + '    </style>', 1)
    path.write_text(html, encoding='utf-8')


def update_inner_html(path: Path) -> None:
    html = path.read_text(encoding='utf-8')
    html = update_common_metadata(html)
    html = update_service_area_answers(html)
    html = inject_areas(html, False)
    html = inject_schema(html)
    html = html.replace('<span>مجدي رزق فني نجارة<small>', '<span>النجار مجدي رزق<small>')
    html = html.replace('>مجدي رزق فني نجارة</h2>', '>النجار مجدي رزق</h2>')
    path.write_text(html, encoding='utf-8')


def main() -> None:
    update_root_index(ROOT / 'index.html')

    for html_path in sorted(ROOT.rglob('index.html')):
        if html_path == ROOT / 'index.html':
            continue
        if '.git' in html_path.parts:
            continue
        update_inner_html(html_path)

    css_path = ROOT / 'assets' / 'services.css'
    css = css_path.read_text(encoding='utf-8')
    if '/* Riyadh service areas */' not in css:
        css_path.write_text(css.rstrip() + SHARED_CSS + '\n', encoding='utf-8')

    for rel in ('scripts/apply-magdy-site-updates.py', '.github/workflows/apply-magdy-site-updates.yml'):
        target = ROOT / rel
        if target.exists():
            target.unlink()


if __name__ == '__main__':
    main()
