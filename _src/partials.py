SITE = "https://build-rh.io"
FONTS = "https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&family=Open+Sans:wght@800&display=swap"

NAV = [
    ("index", "/", "Accueil", ""),
    ("build-rh", "/build-rh.html", "RPO Impact", ""),
    ("cap-bascule", "/cap-bascule.html", "CAP Bascule", "nav-cap"),
    ("cas-clients", "/cas-clients.html", "Cas clients", ""),
    ("a-propos", "/a-propos.html", "À propos", ""),
    ("contact", "/contact.html", "Contact", ""),
]


def head(title, desc, path, jsonld="", noindex=False):
    url = SITE + path
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}<link rel="canonical" href="{url}">
<meta name="theme-color" content="#FBF7F8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#191115" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="BUILD RH">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="BUILD RH : sécuriser les moments où une équipe tech gagne ou perd de la vitesse. RPO Impact et CAP Bascule.">
<meta name="twitter:card" content="summary_large_image">
<meta name="author" content="Shirley Almosni Chiche">
<meta name="google-site-verification" content="nvf2lEdFUN5xLHKZI7ZcgeKEf2Aeo15o3mJqzMciFgk">
<link rel="icon" href="/assets/logo/buildrh-avatar.svg" type="image/svg+xml">
<link rel="icon" href="/assets/logo/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/logo/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
{jsonld}</head>
"""


def header(current):
    links = []
    mlinks = []
    for key, href, label, cls in NAV:
        cur = ' aria-current="page"' if key == current else ""
        c = f' class="{cls}"' if cls else ""
        links.append(f'<li><a href="{href}"{c}{cur}>{label}</a></li>')
        mlinks.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return f"""<a class="skip" href="#main">Aller au contenu</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/" aria-label="BUILD RH, accueil"><img class="logo-img logo-light" src="/assets/logo/buildrh-logo-couleur.svg" alt="BUILD RH" width="113" height="35"><img class="logo-img logo-dark" src="/assets/logo/buildrh-logo-blanc.svg" alt="" aria-hidden="true" width="113" height="35"></a>
    <nav class="main-nav" aria-label="Navigation principale">
      <ul>
        {chr(10).join('        ' + l for l in links).strip()}
      </ul>
    </nav>
    <a class="btn btn-ink btn-sm header-cta" href="/contact.html">Parler d'une situation</a>
    <button class="menu-btn" id="menu-btn" type="button" aria-expanded="false" aria-controls="mobile-menu">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      <span class="label">Menu</span>
    </button>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu" hidden>
  <div class="paths">
    <a class="path build" href="/contact.html?besoin=recrutement"><span class="tag tag-build">RPO Impact</span><strong>Recruter sans ralentir</strong></a>
    <a class="path cap" href="/contact.html?besoin=situation"><span class="tag tag-cap">CAP Bascule</span><strong>Gérer une situation sensible</strong></a>
  </div>
  <nav aria-label="Navigation mobile">
    <ul>
      {chr(10).join('      ' + l for l in mlinks).strip()}
    </ul>
  </nav>
</div>
"""


FOOTER = """<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand" href="/" aria-label="BUILD RH, accueil"><img class="logo-img logo-light" src="/assets/logo/buildrh-logo-couleur.svg" alt="BUILD RH" width="142" height="44"><img class="logo-img logo-dark" src="/assets/logo/buildrh-logo-blanc.svg" alt="" aria-hidden="true" width="142" height="44"></a>
        <p class="tagline">Sécuriser les moments où une équipe tech gagne ou perd de la vitesse.</p>
        <p class="tagline"><a href="https://aiforgood.page/" rel="noopener"><strong>IA FOR GOOD</strong> : agents IA et ressources sur l'IA au travail et le neuroatypisme <span aria-hidden="true">↗</span></a></p>
      </div>
      <div>
        <h2>BUILD RH</h2>
        <ul>
          <li><a href="/build-rh.html">Recrutement tech</a></li>
          <li><a href="/build-rh.html">Le RPO Impact</a></li>
          <li><a href="/build-rh.html#dimensions">Immersion · Delivery · Build · Ancrage</a></li>
          <li><a href="/build-rh.html#forfait">Le forfait</a></li>
          <li><a href="/cas-clients.html">Cas clients</a></li>
        </ul>
      </div>
      <div>
        <h2>CAP Bascule</h2>
        <ul>
          <li><a href="/cap-bascule.html">Les trois parcours</a></li>
          <li><a href="/cap-bascule.html#confidentialite">Confidentialité</a></li>
          <li><a href="https://almosnishirley.github.io/capbascule/" rel="noopener">Site CAP Bascule <span aria-hidden="true">↗</span></a></li>
        </ul>
      </div>
      <div>
        <h2>Contact</h2>
        <ul>
          <li><a href="/contact.html">Formulaire de contact</a></li>
          <li><a href="mailto:shirley.chiche@buildrh.co">shirley.chiche@buildrh.co</a></li>
          <li><a href="https://www.linkedin.com/in/shirley-almosni-chiche/" rel="noopener">LinkedIn <span aria-hidden="true">↗</span></a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 BUILD RH · Shirley Almosni Chiche · Paris</span>
      <a href="/conditions-generales.html">Conditions générales</a>
    </div>
  </div>
</footer>

<button class="a11y-btn" id="a11y-toggle" type="button" title="Confort de lecture" aria-expanded="false" aria-controls="a11y-panel">
  <span class="ico" aria-hidden="true">Aa</span><span class="sr-only">Confort de lecture</span>
</button>
<div class="a11y-panel" id="a11y-panel" hidden role="dialog" aria-label="Réglages de confort de lecture">
  <div class="a11y-head"><span>Confort de lecture</span><button type="button" id="a11y-close" aria-label="Fermer">&times;</button></div>
  <div class="a11y-group"><div class="a11y-label" id="a11y-l1">Taille du texte</div>
    <div class="a11y-seg" data-a11y-control="size" role="group" aria-labelledby="a11y-l1"><button type="button" data-value="normal">A</button><button type="button" data-value="large">A+</button><button type="button" data-value="xlarge">A++</button></div></div>
  <div class="a11y-group"><div class="a11y-label" id="a11y-l2">Espacement du texte</div>
    <div class="a11y-seg" data-a11y-control="spacing" role="group" aria-labelledby="a11y-l2"><button type="button" data-value="normal">Normal</button><button type="button" data-value="loose">Confortable</button></div></div>
  <div class="a11y-group"><div class="a11y-label" id="a11y-l3">Fond de lecture</div>
    <div class="a11y-seg" data-a11y-control="contrast" role="group" aria-labelledby="a11y-l3"><button type="button" data-value="normal">Standard</button><button type="button" data-value="soft">Doux</button></div></div>
  <div class="a11y-group"><div class="a11y-label" id="a11y-l4">Animations</div>
    <div class="a11y-seg" data-a11y-control="motion" role="group" aria-labelledby="a11y-l4"><button type="button" data-value="normal">Activées</button><button type="button" data-value="reduced">Réduites</button></div></div>
  <div class="a11y-group"><div class="a11y-label" id="a11y-l5">Police</div>
    <div class="a11y-seg" data-a11y-control="font" role="group" aria-labelledby="a11y-l5"><button type="button" data-value="normal">Standard</button><button type="button" data-value="lisible">Très lisible</button></div></div>
  <div class="a11y-group"><div class="a11y-label" id="a11y-l6">Guide de lecture</div>
    <div class="a11y-seg" data-a11y-control="guide" role="group" aria-labelledby="a11y-l6"><button type="button" data-value="normal">Désactivé</button><button type="button" data-value="on">Activé</button></div></div>
  <div class="a11y-group"><div class="a11y-label" id="a11y-l7">Mode concentration</div>
    <div class="a11y-seg" data-a11y-control="focus" role="group" aria-labelledby="a11y-l7"><button type="button" data-value="normal">Désactivé</button><button type="button" data-value="on">Activé</button></div></div>
  <p class="a11y-help">Police Atkinson Hyperlegible, bande de lecture qui suit le pointeur, lignes plus courtes et sans italique.</p>
  <button type="button" id="a11y-reset" class="a11y-reset">Réinitialiser</button>
</div>

<div class="reading-guide" aria-hidden="true"><div class="rg-top"></div><div class="rg-bottom"></div></div>
<script src="/assets/site.js" defer></script>
</body>
</html>
"""


def contact_form(fid):
    return f"""<div>
  <form class="form" id="{fid}" data-contact novalidate>
    <div class="form-error-summary" role="alert" hidden></div>
    <fieldset>
      <legend>Votre demande concerne…</legend>
      <div class="choices">
        <label class="choice build">
          <input type="radio" name="parcours" value="recrutement" aria-describedby="{fid}-parcours-err">
          <span class="box"><strong>J'ai un besoin de recrutement ou de structuration</strong><span>BUILD RH · un ou plusieurs postes, un process à construire ou à auditer</span></span>
        </label>
        <label class="choice cap">
          <input type="radio" name="parcours" value="situation" aria-describedby="{fid}-parcours-err">
          <span class="box"><strong>Je veux parler d'une situation professionnelle sensible</strong><span>CAP Bascule · prise de poste difficile, période d'essai, départ, rebond</span></span>
        </label>
      </div>
      <div class="field"><p class="err" id="{fid}-parcours-err"></p></div>
    </fieldset>

    <div class="cap-warning" hidden>
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>
      <p><strong>Pas de détail médical ni d'information trop sensible ici.</strong> Quelques lignes de contexte suffisent, sans nommer la personne si vous préférez. Le reste se dit pendant l'échange, dans un cadre confidentiel.</p>
    </div>

    <div class="fields">
      <div class="field">
        <label for="{fid}-nom">Prénom et nom</label>
        <input id="{fid}-nom" name="nom" type="text" autocomplete="name" required aria-describedby="{fid}-nom-err">
        <p class="err" id="{fid}-nom-err"></p>
      </div>
      <div class="field">
        <label for="{fid}-entreprise">Entreprise</label>
        <input id="{fid}-entreprise" name="entreprise" type="text" autocomplete="organization" required aria-describedby="{fid}-entreprise-err">
        <p class="err" id="{fid}-entreprise-err"></p>
      </div>
      <div class="field">
        <label for="{fid}-role">Rôle</label>
        <input id="{fid}-role" name="role" type="text" autocomplete="organization-title" placeholder="CTO, DRH, fondatrice…" required aria-describedby="{fid}-role-err">
        <p class="err" id="{fid}-role-err"></p>
      </div>
      <div class="field">
        <label for="{fid}-email">E-mail professionnel</label>
        <input id="{fid}-email" name="email" type="email" autocomplete="email" inputmode="email" required aria-describedby="{fid}-email-err">
        <p class="err" id="{fid}-email-err"></p>
      </div>
      <div class="field full">
        <label for="{fid}-besoin">Type de besoin</label>
        <select id="{fid}-besoin" name="besoin" required aria-describedby="{fid}-besoin-err">
          <option value="">Choisir…</option>
          <optgroup label="Recrutement et structuration · BUILD RH" data-parcours="recrutement">
            <option>Recruter un ou plusieurs profils tech</option>
            <option>Mettre en place un RPO Impact</option>
            <option>Structurer, améliorer ou auditer le process de recrutement</option>
            <option>Je ne sais pas encore</option>
          </optgroup>
          <optgroup label="Situation sensible · CAP Bascule" data-parcours="situation">
            <option>Une personne en poste qui hésite à rester, ajuster ou partir</option>
            <option>Une prise de poste ou une période d'essai incertaine</option>
            <option>Un départ à préparer</option>
            <option>Reconstruire la suite après une rupture</option>
            <option>Je ne sais pas encore</option>
          </optgroup>
        </select>
        <p class="err" id="{fid}-besoin-err"></p>
      </div>
      <div class="field full">
        <label for="{fid}-message">Quelques lignes sur la situation</label>
        <textarea id="{fid}-message" name="message" rows="5" required aria-describedby="{fid}-message-hint {fid}-message-err"></textarea>
        <span class="hint" id="{fid}-message-hint">Le contexte, ce qui bloque, ce qui est déjà envisagé.</span>
        <p class="err" id="{fid}-message-err"></p>
      </div>
      <div class="field full">
        <label for="{fid}-urgence">Niveau d'urgence <span class="opt">(facultatif)</span></label>
        <select id="{fid}-urgence" name="urgence">
          <option value="">Non précisé</option>
          <option>Pas d'urgence particulière</option>
          <option>Dans les prochaines semaines</option>
          <option>Cette semaine</option>
        </select>
      </div>
    </div>

    <div class="form-foot">
      <button class="btn btn-ink" type="submit">Préparer mon message <span class="arrow" aria-hidden="true">→</span></button>
      <small>Le bouton ouvre votre messagerie avec un e-mail pré-rempli, adressé à Shirley (et à Coralie pour CAP Bascule). Aucune donnée n'est enregistrée sur ce site.</small>
    </div>
  </form>

  <div class="form form-done" hidden aria-live="polite">
    <span class="tag tag-neutral">Message prêt</span>
    <h3 class="mt-s">Votre messagerie devrait s'ouvrir.</h3>
    <p>Relisez le message puis envoyez-le. Shirley répond généralement sous 24&nbsp;h.</p>
    <div class="cta-row">
      <a class="btn btn-ink btn-sm" data-mail-link href="mailto:shirley.chiche@buildrh.co">Rouvrir la messagerie</a>
      <button class="btn btn-outline btn-sm" type="button" data-copy>Copier le message</button>
      <button class="btn btn-outline btn-sm" type="button" data-back>Modifier</button>
    </div>
    <p class="mt-s">Rien ne s'ouvre&nbsp;? Écrivez directement à <a href="mailto:shirley.chiche@buildrh.co">shirley.chiche@buildrh.co</a>.</p>
  </div>
</div>"""


CONTACT_ASIDE = """<div class="contact-aside">
  <p>Deux portes d'entrée, un seul formulaire. Choisissez celle qui correspond à votre situation&nbsp;: la suite de l'échange sera adaptée.</p>
  <ul class="checklist mt-m">
    <li><strong>Recrutement ou structuration.</strong> Un premier échange pour comprendre le contexte, les postes et le calendrier.</li>
    <li class="cap-item"><strong>Situation sensible.</strong> 30 minutes pour décrire la situation. Nous vous disons honnêtement si un accompagnement est pertinent.</li>
  </ul>
  <p class="direct">Vous préférez écrire directement&nbsp;: <a href="mailto:shirley.chiche@buildrh.co">shirley.chiche@buildrh.co</a></p>
</div>"""


def page(name, title, desc, body, current=None, jsonld="", body_class="", noindex=False):
    path = "/" if name == "index" else f"/{name}.html"
    cls = f' class="{body_class}"' if body_class else ""
    return head(title, desc, path, jsonld, noindex) + f"<body{cls}>\n" + header(current or name) + body + "\n" + FOOTER
