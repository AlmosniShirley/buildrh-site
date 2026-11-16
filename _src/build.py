import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from partials import page, contact_form, CONTACT_ASIDE, SITE
from blocks import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

def ld(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, ensure_ascii=False, indent=2) + "\n</script>\n"

ORG = {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "@id": SITE + "/#org",
    "name": "BUILD RH",
    "url": SITE + "/",
    "image": SITE + "/assets/shirley.png",
    "email": "shirley.chiche@buildrh.co",
    "description": "Recrutement tech (RPO Impact, structuration du process) et accompagnement des transitions professionnelles sensibles avec CAP Bascule.",
    "areaServed": {"@type": "Country", "name": "France"},
    "address": {"@type": "PostalAddress", "addressLocality": "Paris", "addressCountry": "FR"},
    "inLanguage": "fr",
    "founder": {"@type": "Person", "name": "Shirley Almosni Chiche", "jobTitle": "Recruteuse tech, fondatrice de BUILD RH",
                "sameAs": [SHIRLEY_LI, "https://github.com/AlmosniShirley", "https://prompt-humain.ghost.io/"]},
    "knowsAbout": ["Recrutement tech", "RPO", "Process de recrutement", "Transitions professionnelles"],
    "hasOfferCatalog": {
        "@type": "OfferCatalog", "name": "Offres BUILD RH",
        "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "BUILD RH — RPO Impact", "serviceType": "Recruitment Process Outsourcing",
             "description": "Un dispositif de recrutement en immersion, orienté résultats et conçu pour laisser une capacité durable : immersion, delivery, build et ancrage, avec un forfait global construit autour des objectifs."}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "CAP Bascule", "serviceType": "Accompagnement des transitions professionnelles",
             "description": "Accompagnement externe et confidentiel, financé par l'entreprise : CAP Clarifier, CAP Traverser, CAP Rebond."}},
        ],
    },
}

def crumbs(name, path):
    return ld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": SITE + path}]})

def cta_band(title, text, primary, secondary=None, cap=False):
    cls = "cta-band cap-band" if cap else "cta-band"
    sec = f'<a class="btn btn-outline" href="{secondary[1]}">{secondary[0]}</a>' if secondary else ""
    btn = "btn-ink" if cap else "btn-build"
    return f"""<section class="{cls}">
  <div class="wrap">
    <h2>{title}</h2>
    <p>{text}</p>
    <div class="cta-row"><a class="btn {btn}" href="{primary[1]}">{primary[0]} <span class="arrow" aria-hidden="true">→</span></a>{sec}</div>
  </div>
</section>"""

CTA_BUILD = '<a class="btn btn-build" href="/contact.html?besoin=recrutement">Parler d\'un recrutement ou d\'un besoin de structuration <span class="arrow" aria-hidden="true">→</span></a>'
CTA_CAP = '<a class="btn btn-cap" href="/contact.html?besoin=situation">Parler d\'une situation sensible <span class="arrow" aria-hidden="true">→</span></a>'

# =====================================================================
# ACCUEIL
# =====================================================================
index_body = f"""<main id="main">

<!-- HERO -->
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">Recrutement tech &amp; transitions professionnelles</span>
      <h1>Sécuriser les moments où une équipe tech gagne ou perd de la vitesse.</h1>
      <p class="lead">J'aide les startups, scale-ups et entreprises tech à faire entrer les bonnes personnes, puis à traiter les situations où une relation de travail ne tient plus comme prévu.</p>
      <div class="cta-row">
        <a class="btn btn-build" href="/build-rh.html">Recruter sans ralentir <span class="arrow" aria-hidden="true">→</span></a>
        <a class="btn btn-cap" href="/cap-bascule.html">Gérer une situation sensible <span class="arrow" aria-hidden="true">→</span></a>
      </div>
      <p class="secondary"><a class="link-arrow" href="#cas-clients">Voir les cas clients <span aria-hidden="true">↓</span></a></p>
    </div>
    <aside class="trajectory" aria-label="Où interviennent le RPO Impact et CAP Bascule">
      <span class="kicker">La vie d'une relation de travail</span>
      <ol class="traj-list">
        <li class="build"><span class="step">Un besoin s'ouvre</span><span class="who">Poste à créer, équipe à construire</span></li>
        <li class="build"><span class="step">Sourcing, entretiens, closing</span><span class="who">Le bon profil, sans baisser la barre</span></li>
        <li class="build"><span class="step">Prise de poste</span><span class="who">Ce qui a été promis rencontre le réel</span></li>
        <li class="cap pivot"><span class="step">La relation bascule</span><span class="who">Doute, tension, période d'essai incertaine</span></li>
        <li class="cap"><span class="step">Décider et traverser</span><span class="who">Rester, ajuster, partir ou rebondir</span></li>
      </ol>
      <div class="traj-legend"><span class="tag tag-build">RPO Impact · l'entrée</span><span class="tag tag-cap">CAP Bascule · le maintien et la sortie</span></div>
    </aside>
  </div>
</section>

<!-- 1. LES DEUX MOMENTS CRITIQUES -->
<section class="section" id="moments" aria-labelledby="moments-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Deux moments critiques</span>
      <h2 id="moments-title">Où en est votre équipe aujourd'hui&nbsp;?</h2>
    </div>
    <div class="grid grid-2">
      <article class="card moment build">
        <span class="tag tag-build">RPO Impact</span>
        <h3>Faire entrer les bonnes personnes</h3>
        <p>Votre équipe doit grandir, mais vous ne voulez ni ralentir la roadmap ni baisser la barre sur les profils recrutés.</p>
        <p class="when">Recrutements tech et stratégiques · immersion, delivery, build, ancrage</p>
        <div class="card-foot"><a class="btn btn-build" href="/build-rh.html">Découvrir le RPO Impact <span class="arrow" aria-hidden="true">→</span></a></div>
      </article>
      <article class="card moment cap">
        <span class="tag tag-cap">CAP Bascule</span>
        <h3>Gérer une relation de travail qui bascule</h3>
        <p>Une prise de poste ne fonctionne pas, une tension s'installe, une période d'essai devient incertaine ou un départ doit être préparé.</p>
        <p class="when">Accompagnement externe et confidentiel · financé par l'entreprise · de 7 jours à 6 semaines</p>
        <div class="card-foot"><a class="btn btn-cap" href="/cap-bascule.html">Découvrir CAP Bascule <span class="arrow" aria-hidden="true">→</span></a></div>
      </article>
    </div>
  </div>
</section>

<!-- 2. LE COÛT DE L'INACTION -->
<section class="section" aria-labelledby="cout-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Le coût de l'inaction</span>
      <h2 id="cout-title">Ce qu'on laisse en attente finit par coûter de la vitesse.</h2>
      <p class="lead">Ces coûts, toutes les équipes tech les connaissent. Ils sont simplement rarement regardés ensemble.</p>
    </div>
    <div class="costs">
      <div class="cost"><span class="num">01</span><h3>Un poste vacant</h3><p>La roadmap attend. Les autres absorbent la charge, les arbitrages se repoussent.</p></div>
      <div class="cost"><span class="num">02</span><h3>Un mauvais casting</h3><p>Du temps, de l'énergie managériale et de la crédibilité dépensés pour un recrutement qui ne tient pas.</p></div>
      <div class="cost"><span class="num">03</span><h3>Une situation non traitée</h3><p>Elle finit par mobiliser le management, les RH et l'équipe, bien au-delà de la personne concernée.</p></div>
      <div class="cost"><span class="num">04</span><h3>Un départ subi ou conflictuel</h3><p>Il entame la confiance de celles et ceux qui restent, et la marque employeur.</p></div>
    </div>
  </div>
</section>

<!-- 3. BUILD RH -->
<section class="section alt" id="build-rh" aria-labelledby="build-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">BUILD RH · la stratégie à l'entrée</span>
      <h2 id="build-title">Faire entrer les bonnes personnes, vite et sans rogner sur la qualité.</h2>
      <p class="lead">Pour les startups, scale-ups et entreprises tech qui recrutent des profils techniques ou stratégiques, et qui veulent alléger la charge de leurs managers sans baisser leur niveau d'exigence.</p>
    </div>
    <h3 class="compare-title mt-0">RPO Impact&nbsp;: recruter maintenant, renforcer durablement</h3>
    <p class="muted" style="max-width:70ch;margin-top:-6px">{SIGNATURE}</p>
    {DIMENSIONS_SHORT}
    <p class="note">Un forfait global construit autour de trois éléments&nbsp;: le dispositif mis en place, les recrutements réalisés, les impacts et l'ancrage obtenus. <a class="link-arrow build" href="/build-rh.html#forfait">Comment le forfait est construit</a> · <a class="link-arrow build" href="/build-rh.html#exemple">Voir l'exemple</a></p>
    <div class="section-foot cta-row">{CTA_BUILD}<a class="link-arrow" href="/build-rh.html">Découvrir le RPO Impact</a></div>
  </div>
</section>

<!-- 4. CAP BASCULE -->
<section class="section cap-zone" id="cap-bascule" aria-labelledby="cap-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker" style="color:var(--cap)">CAP Bascule · la stratégie à la sortie et au maintien</span>
      <h2 id="cap-title">Quand le travail ne tient plus comme avant.</h2>
      <p class="lead">Clarifier une situation professionnelle sensible, décider de la suite et traverser la transition proprement. L'entreprise finance l'accompagnement&nbsp;; la personne bénéficie d'un espace externe, confidentiel et neutre.</p>
      <p class="muted mt-s">Co-porté par Shirley Almosni Chiche et Coralie Nohel.</p>
    </div>
    {PARCOURS}
    {PRINCIPLES}
    {ISNOT}
    <div class="section-foot cta-row">{CTA_CAP}<a class="link-arrow cap" href="/cap-bascule.html">Tout sur CAP Bascule</a></div>
  </div>
</section>

<!-- 5. LA SYNERGIE -->
<section class="section" aria-labelledby="synergie-title">
  <div class="wrap">
    <span class="kicker">Pourquoi les deux</span>
    <h2 id="synergie-title" class="synergy-quote"><span>Un recrutement ne se termine pas le jour de la signature.</span> <span>Une situation de départ ne commence pas toujours le jour de la rupture.</span></h2>
    <p class="lead mt-m">Les deux offres restent distinctes&nbsp;: vous choisissez la porte d'entrée qui correspond à votre situation. Mais elles se répondent.</p>
    <div class="bridges">
      <div class="bridge">
        <div class="route"><span class="tag tag-build">RPO Impact</span><span class="to" aria-hidden="true">→</span><span class="sr-only">mène vers</span><span class="tag tag-cap">CAP Bascule</span></div>
        <p><strong>Quand une prise de poste ne fonctionne pas.</strong> Si un recrutement ou une relation de travail se dégrade, CAP Bascule donne un cadre pour clarifier la situation plutôt que de la laisser s'enliser.</p>
      </div>
      <div class="bridge">
        <div class="route"><span class="tag tag-cap">CAP Bascule</span><span class="to" aria-hidden="true">→</span><span class="sr-only">mène vers</span><span class="tag tag-build">RPO Impact</span></div>
        <p><strong>Quand un poste doit être remplacé.</strong> Le RPO Impact reprend le recrutement avec les enseignements de la situation précédente&nbsp;: ce qui était promis, ce qui manquait, ce qu'il faut vérifier autrement. Toujours dans le respect du cadre de confidentialité convenu.</p>
      </div>
    </div>
  </div>
</section>

<!-- 6. CAS CLIENTS -->
<section class="section alt" id="cas-clients" aria-labelledby="cas-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Cas clients</span>
      <h2 id="cas-title">Biggest achievements</h2>
      <p class="lead">Six missions BUILD RH, avec le contexte, le besoin, l'intervention et le résultat.</p>
    </div>
    {cases_grid()}
    <div class="section-foot"><a class="link-arrow build" href="/cas-clients.html">Cas clients et recommandations <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<!-- 7. MÉTHODE -->
<section class="section" id="methode" aria-labelledby="methode-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Méthode</span>
      <h2 id="methode-title">Comment ça marche</h2>
      <p class="lead">Avant toute exécution, nous définissons ensemble le problème à résoudre, les objectifs et les impacts attendus. Le forfait vient ensuite.</p>
    </div>
    {RPO_STEPS}
    <div class="method-cap">{METHOD.split('<div class="method-cap">')[1]}
  </div>
</section>

<!-- 8. À PROPOS -->
<section class="section alt" id="a-propos" aria-labelledby="apropos-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">À propos</span>
      <h2 id="apropos-title">Qui intervient</h2>
    </div>
    <div class="people">
      {person_shirley()}
      {PERSON_CORALIE}
    </div>
    <h3 class="compare-title">Ce qu'en disent celles et ceux qui ont travaillé avec Shirley</h3>
    {quotes(3)}
    <div class="section-foot"><a class="link-arrow build" href="/a-propos.html#recommandations">Lire les 12 recommandations <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<!-- 9. CONTACT -->
<section class="section" id="contact" aria-labelledby="contact-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Contact</span>
      <h2 id="contact-title">Par quoi voulez-vous commencer&nbsp;?</h2>
    </div>
    <div class="contact-grid">
      {CONTACT_ASIDE}
      {contact_form("form-home")}
    </div>
  </div>
</section>

</main>"""

# =====================================================================
# BUILD RH
# =====================================================================
build_body = f"""<main id="main">
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">BUILD RH · RPO Impact</span>
    <h1>RPO Impact&nbsp;: <em>recruter maintenant, renforcer durablement.</em></h1>
    <p class="lead">{SIGNATURE}</p>
    <div class="cta-row">{CTA_BUILD}<a class="link-arrow build" href="#forfait">Comment le forfait est construit <span aria-hidden="true">↓</span></a></div>
  </div>
</section>

<!-- 1. CE QU'EST LE RPO IMPACT -->
<section class="section" aria-labelledby="quoi-title">
  <div class="wrap two-col">
    <div>
      <span class="kicker">L'offre</span>
      <h2 id="quoi-title" style="font-size:clamp(1.8rem,3.6vw,2.5rem)">Recruter maintenant, sans simplement ajouter une ressource.</h2>
      <p class="lead mt-s">Vous avez besoin de recruter maintenant, mais vous ne voulez pas simplement ajouter une ressource pendant quelques mois.</p>
    </div>
    <div>
      <p class="mt-0"><strong>RPO Impact combine&nbsp;:</strong></p>
      <ul class="checklist">
        <li>l'<strong>immersion</strong> dans votre environnement et vos équipes&nbsp;;</li>
        <li>le <strong>delivery</strong> des recrutements prioritaires&nbsp;;</li>
        <li>le <strong>build</strong> d'un process plus solide&nbsp;;</li>
        <li>l'<strong>ancrage</strong> des pratiques auprès de vos managers.</li>
      </ul>
      <p class="mt-s"><strong>Les recrutements avancent pendant que votre dispositif se renforce.</strong></p>
    </div>
  </div>
  <div class="wrap">
    <blockquote class="pull-quote">Vous ne financez pas des jours de recrutement. Vous financez une capacité à recruter, qui produit des résultats et laisse quelque chose derrière elle.</blockquote>
  </div>
</section>

<!-- 2. LES QUATRE DIMENSIONS -->
<section class="section alt" id="dimensions" aria-labelledby="dims-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Ce que fait Shirley, concrètement</span>
      <h2 id="dims-title">Immersion, Delivery, Build, Ancrage</h2>
      <p class="lead">Une méthode de travail en quatre temps&nbsp;: l'immersion dans les équipes, l'exécution des recrutements, l'amélioration du process et la transmission d'une capacité durable à recruter.</p>
    </div>
    {DIMENSIONS}
    <h3 class="compare-title" id="deroule">Comment se déroule un RPO Impact</h3>
    <p class="muted" style="max-width:70ch;margin-top:-8px">Les quatre dimensions ci-dessus, dans l'ordre où elles interviennent pendant la mission.</p>
    {RPO_STEPS}
    {STACK}
  </div>
</section>

<!-- 3. CE QUI DOIT AVOIR CHANGÉ -->
<section class="section" id="impact" aria-labelledby="change-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">L'impact</span>
      <h2 id="change-title">Ce qui doit avoir changé à la fin</h2>
      <p class="lead">Les objectifs sont définis ensemble au démarrage. Trois dimensions comptent dans la plupart des missions&nbsp;:</p>
    </div>
    {CHANGE}
    {BILAN}
  </div>
</section>

<!-- 4. LE FORFAIT -->
<section class="section alt" id="forfait" aria-labelledby="forfait-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Comment le forfait est construit</span>
      <h2 id="forfait-title">Le forfait découle du dispositif, pas d'un nombre de jours.</h2>
    </div>
    {FORFAIT}
    {EXAMPLE}
  </div>
</section>

<section class="section" aria-labelledby="sit-title">
  <div class="wrap two-col">
    <div>
      <span class="kicker">Pour qui</span>
      <h2 id="sit-title" style="font-size:clamp(1.8rem,3.6vw,2.5rem)">Vous reconnaissez-vous&nbsp;?</h2>
      <p class="lead mt-s">Le RPO Impact s'adresse aux équipes pour qui le recrutement est devenu un sujet de vitesse.</p>
    </div>
    <ul class="checklist">
      <li>La roadmap attend des recrutements qui n'avancent pas.</li>
      <li>Les managers passent plus de temps en entretiens qu'avec leur équipe.</li>
      <li>Des candidats décrochent en cours de process ou refusent au closing.</li>
      <li>Le niveau des recrutements dépend de qui fait passer les entretiens.</li>
      <li>Une équipe tech doit être construite, parfois from scratch.</li>
      <li>Des profils rares sont à recruter&nbsp;: sécurité, data, staff, management.</li>
    </ul>
  </div>
</section>

<section class="section alt" aria-labelledby="bcas-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Preuves</span>
      <h2 id="bcas-title">Trois missions parmi d'autres</h2>
    </div>
    {cases_grid(["Sunday", "Pix", "DeepReach"])}
    <div class="section-foot"><a class="link-arrow build" href="/cas-clients.html">Voir les six cas clients <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<section class="section" aria-labelledby="bfaq-title">
  <div class="wrap narrow">
    <div class="section-head"><span class="kicker">Questions fréquentes</span><h2 id="bfaq-title">Avant de se parler</h2></div>
    <div class="faq">
      <details><summary>Qu'est-ce qui distingue le RPO Impact&nbsp;?</summary><p>Vous ne financez pas des jours de recrutement&nbsp;: vous financez une capacité à recruter. Les recrutements avancent pendant que le process se renforce, et la mission se termine par l'ancrage des pratiques et un bilan d'impact partagé.</p></details>
      <details><summary>Comment le forfait est-il construit&nbsp;?</summary><p>Nous définissons ensemble le problème à résoudre, les résultats attendus et les impacts souhaités. Le forfait tient compte du contexte de l'entreprise, du nombre et de la criticité des recrutements, du niveau de structuration nécessaire, de l'autonomie des équipes, de la durée et du périmètre de l'intervention.</p></details>
      <details><summary>L'immersion se fait-elle sur site&nbsp;?</summary><p>Lorsque c'est pertinent, oui. L'objectif est d'être au plus près de vos équipes et de votre environnement de travail pour comprendre comment les décisions se prennent réellement.</p></details>
      <details><summary>Que contient le bilan d'impact&nbsp;?</summary><p>Les objectifs définis au démarrage, les recrutements réalisés, les améliorations apportées, les outils transmis, les indicateurs observés et les prochaines recommandations.</p></details>
      <details><summary>Peut-on faire appel à BUILD RH uniquement pour le process&nbsp;?</summary><p>Oui. C'est l'intervention Build&nbsp;: conception, amélioration ou audit du process de recrutement, et accompagnement des managers et des équipes.</p></details>
      <details><summary>Quels profils recrutez-vous&nbsp;?</summary><p>Des profils tech et produit&nbsp;: développeurs backend, frontend, fullstack et mobile, DevOps, sécurité (RSSI, Head of Security), data (Analytics Engineer), Product Owners et Product Managers, Engineering Managers.</p></details>
    </div>
  </div>
</section>

{cta_band("Un recrutement à lancer, un process à remettre d'aplomb&nbsp;?", "Décrivez le contexte en quelques lignes. Le premier échange sert à comprendre le besoin et à définir ensemble les objectifs.", ("Parler d'un recrutement ou d'un besoin de structuration", "/contact.html?besoin=recrutement"))}
</main>"""

# =====================================================================
# CAP BASCULE
# =====================================================================
cap_body = f"""<main id="main">
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">CAP Bascule · la stratégie à la sortie et au maintien</span>
    <h1>Quand le travail <em>ne tient plus comme avant.</em></h1>
    <p class="lead">Clarifier une situation professionnelle sensible, décider de la suite et traverser la transition proprement. Un accompagnement externe et confidentiel, financé par l'entreprise, pour la personne concernée.</p>
    <div class="cta-row">{CTA_CAP}<a class="btn btn-outline" href="{CAP_SITE}" rel="noopener">Site CAP Bascule <span aria-hidden="true">↗</span></a></div>
    <p class="muted mt-m">Co-porté par Shirley Almosni Chiche et Coralie Nohel.</p>
  </div>
</section>

<section class="section" aria-labelledby="csit-title">
  <div class="wrap two-col">
    <div>
      <span class="kicker">Les situations</span>
      <h2 id="csit-title" style="font-size:clamp(1.8rem,3.6vw,2.5rem)">Une relation de travail qui bascule</h2>
      <p class="lead mt-s">Ces situations sont difficiles à traiter de l'intérieur&nbsp;: chacun a sa version, personne n'est neutre, et l'urgence finit par décider à votre place.</p>
    </div>
    <ul class="checklist cap">
      <li>Une prise de poste ne correspond pas à la promesse.</li>
      <li>Une personne doute, s'épuise ou ne se projette plus.</li>
      <li>Les attentes, les priorités ou les moyens restent flous.</li>
      <li>La relation avec le manager ou l'équipe se dégrade.</li>
      <li>Une fin de période d'essai se prépare.</li>
      <li>Un départ après plusieurs années doit être accompagné.</li>
      <li>Une personne doit reconstruire la suite après une rupture professionnelle.</li>
    </ul>
  </div>
</section>

<section class="section cap-zone" aria-labelledby="temps-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Le cadre</span>
      <h2 id="temps-title">Un accompagnement en quatre temps</h2>
      <p class="lead">Pas de checklist&nbsp;: chaque étape doit permettre une clarification, une conversation ou une décision.</p>
    </div>
    <ol class="steps4">
      <li><strong>Cadrer</strong><p>Poser la situation, la question à résoudre, les personnes concernées et les règles de confidentialité.</p></li>
      <li><strong>Éclairer</strong><p>Donner à la personne un espace externe pour distinguer les faits, les ressentis et les options.</p></li>
      <li><strong>Décider</strong><p>Faire émerger une direction réaliste&nbsp;: rester, ajuster, partir ou rebondir. Sans décider uniquement sous pression.</p></li>
      <li><strong>Traverser</strong><p>Transformer la décision en étapes concrètes&nbsp;: conversation avec le manager, sortie, transition ou rebond.</p></li>
    </ol>
  </div>
</section>

<section class="section" aria-labelledby="parc-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Les parcours</span>
      <h2 id="parc-title">Une seule porte d'entrée, trois parcours possibles</h2>
      <p class="lead">Vous n'avez pas à choisir un parcours avant de nous appeler. Le parcours se dessine pendant le cadrage. Périmètre, livrables, confidentialité et prix sont définis avant le démarrage.</p>
    </div>
    {PARCOURS}
  </div>
</section>

<section class="section alt" aria-labelledby="fin-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Qui finance, qui est accompagné</span>
      <h2 id="fin-title">L'entreprise finance. La personne est accompagnée.</h2>
    </div>
    <div class="grid grid-3">
      <div class="card"><span class="tag tag-neutral">Client et sponsor</span><h3>L'entreprise</h3><p>Elle pose la question à traiter, valide le cadre et reçoit uniquement la synthèse convenue au démarrage.</p></div>
      <div class="card"><span class="tag tag-cap">Bénéficiaire directe</span><h3>La personne</h3><p>Elle dispose d'un espace confidentiel. Elle n'est ni évaluée ni surveillée.</p></div>
      <div class="card"><span class="tag tag-neutral">Tiers externe</span><h3>CAP Bascule</h3><p>Nous tenons le cadre écrit, les entretiens et la préparation des conversations.</p></div>
    </div>
    <p class="note">L'entreprise ne délègue pas sa responsabilité managériale. Elle se donne un cadre pour l'exercer.</p>
  </div>
</section>

<section class="section" id="confidentialite" aria-labelledby="conf-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Confidentialité et limites</span>
      <h2 id="conf-title">Un espace confidentiel, pas un dispositif de surveillance</h2>
    </div>
    <div class="two-col">
      <div>
        <h3 class="mt-0" style="margin-bottom:12px">Ce qui reste entre la personne et nous</h3>
        <ul class="checklist cap">
          <li>Aucun verbatim n'est transmis.</li>
          <li>Aucun compte rendu individuel n'est envoyé automatiquement.</li>
          <li>La personne n'est pas évaluée.</li>
        </ul>
      </div>
      <div>
        <h3 class="mt-0" style="margin-bottom:12px">Ce qui est défini avant le démarrage</h3>
        <ul class="checklist cap">
          <li>Les règles de remontée d'information.</li>
          <li>Les destinataires d'une éventuelle synthèse.</li>
          <li>Les situations pouvant donner lieu à une alerte.</li>
        </ul>
      </div>
    </div>
    {PRINCIPLES}
    {ISNOT}
  </div>
</section>

<section class="section alt" aria-labelledby="nous-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Qui accompagne</span>
      <h2 id="nous-title">Nous connaissons les deux côtés de la relation</h2>
      <p class="lead">Notre expérience vient du recrutement IT, des ESN et des environnements tech. Nous avons vu des recrutements réussis sur le papier se défaire, des managers sans bande passante et des départs mal préparés.</p>
    </div>
    <div class="people">
      {person_shirley()}
      {PERSON_CORALIE}
    </div>
  </div>
</section>

<section class="section" aria-labelledby="cfaq-title">
  <div class="wrap narrow">
    <div class="section-head"><span class="kicker">Questions fréquentes</span><h2 id="cfaq-title">Ce que l'on nous demande souvent</h2></div>
    <div class="faq">
      <details><summary>Qui paie l'accompagnement&nbsp;?</summary><p>L'entreprise, au forfait. Le périmètre et le prix sont définis avant le démarrage.</p></details>
      <details><summary>Est-ce que l'entreprise reçoit ce que la personne dit&nbsp;?</summary><p>Non. Aucun verbatim ni compte rendu individuel n'est transmis automatiquement. Seule une synthèse limitée aux éléments convenus au démarrage est partagée, avec les destinataires définis à l'avance.</p></details>
      <details><summary>Est-ce du coaching ou de la thérapie&nbsp;?</summary><p>Ni l'un ni l'autre. Ce n'est pas une thérapie ni un accompagnement médical, et ce n'est pas du coaching&nbsp;: c'est un accompagnement concret, centré sur une situation et une décision, avec un début et une fin.</p></details>
      <details><summary>Que se passe-t-il si la personne veut partir&nbsp;?</summary><p>C'est une option légitime. Nous l'aidons à préparer les conversations nécessaires et une sortie propre, dans le cadre convenu.</p></details>
      <details><summary>Et si l'entreprise souhaite qu'elle reste&nbsp;?</summary><p>Nous pouvons éclairer les conditions d'un maintien, mais nous ne cherchons pas à convaincre la personne. Chacun reste maître de sa décision.</p></details>
      <details><summary>Que se passe-t-il si la situation relève du juridique ou du médical&nbsp;?</summary><p>Nous le disons clairement et orientons vers les professionnels compétents. Nous ne nous substituons ni à un avocat ni à un médecin.</p></details>
      <details><summary>Peut-on accompagner une personne qui a déjà quitté l'entreprise&nbsp;?</summary><p>Oui, si l'entreprise finance l'accompagnement dans le cadre de la séparation. C'est l'objet de CAP Rebond.</p></details>
    </div>
  </div>
</section>

{cta_band("Une situation professionnelle est en train de basculer&nbsp;?", "Échangeons 30 minutes. Décrivez-nous la situation, sans détail médical ni nominatif&nbsp;: nous vous dirons honnêtement si un accompagnement est pertinent.", ("Parler d'une situation sensible", "/contact.html?besoin=situation"), cap=True)}
</main>"""

# =====================================================================
# CAS CLIENTS
# =====================================================================
cases_body = f"""<main id="main">
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">Cas clients</span>
    <h1>Des équipes tech construites, <em>poste après poste.</em></h1>
    <p class="lead">Six missions BUILD RH, racontées par le problème à résoudre&nbsp;: le contexte, le besoin, l'intervention et le résultat.</p>
  </div>
</section>

<section class="section" aria-labelledby="liste-title">
  <div class="wrap">
    <h2 id="liste-title" class="sr-only">Les six missions</h2>
    {cases_grid()}
    <p class="note">Les cas CAP Bascule sont présentés de façon anonymisée. <span class="todo">Cas anonymisés CAP Bascule à ajouter</span></p>
  </div>
</section>

<section class="section alt" aria-labelledby="reco-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Recommandations LinkedIn</span>
      <h2 id="reco-title">Ce qu'en disent celles et ceux qui ont travaillé avec Shirley</h2>
    </div>
    {quotes(4, all_layout=True)}
    <div class="section-foot"><a class="link-arrow build" href="/a-propos.html#recommandations">Toutes les recommandations <span aria-hidden="true">→</span></a></div>
  </div>
</section>

{cta_band("Votre situation ressemble à l'une de celles-ci&nbsp;?", "Parlons du contexte, du besoin et du calendrier. Vous saurez rapidement quelle formule a du sens.", ("Parler d'un recrutement", "/contact.html?besoin=recrutement"), ("Parler d'une situation sensible", "/contact.html?besoin=situation"))}
</main>"""

# =====================================================================
# À PROPOS
# =====================================================================
POSTS = [
    ("ia-et-developpement-pour-olivier-nouguier-lenjeu-est-de-garder-le-controle/", "1.jpg", "IA et développement : pour Olivier Nouguier, l'enjeu est de garder le contrôle", "1 sept. 2026"),
    ("ia-generative-en-entreprise-ce-nest-pas-juste-un-outil-en-plus-cest-un-seisme-culturel-temoignage-de-jerome-duchemin-dsi-dacs/", "2.png", "« IA générative en entreprise : ce n'est pas juste un outil en plus » — Jérôme Duchemin, DSI d'ACS", "24 août 2026"),
    ("repenser-la-valeur-les-metiers-et-lorganisation-a-lere-de-lia-entretien-avec-mathilde-rigabert-ctpo/", "3.jpg", "Repenser la valeur, les métiers et l'organisation à l'ère de l'IA — Mathilde Rigabert (CTPO)", "18 août 2026"),
    ("un-an-pour-faire-basculer-plus-de-300-ingenieurs-vers-lia-il-etait-une-fois-le-temoignage-de-nicolas-martignole-back-market/", "4.png", "Un an pour faire basculer plus de 300 ingénieurs vers l'IA — Nicolas Martignole (Back Market)", "24 juil. 2026"),
    ("ton-code-nest-pas-toi-mais-bientot-ce-sera-toujours-toi-qui-paiera-quand-lia-se-trompe/", "5.jpg", "Ton code n'est pas toi (mais bientôt, ce sera toujours toi) — qui paiera quand l'IA se trompe ?", "22 juil. 2026"),
    ("sur-une-journee-type-je-code-peut-etre-10-du-temps-quelle-realite-derriere-le-mot-ia-interview-de-cedric-locchi/", "6.png", "« Sur une journée type, je code peut-être 10 % du temps » — Cédric Locchi", "21 juil. 2026"),
    ("on-est-passes-de-driven-by-ai-a-ai-first-puis-a-ai-only-plongee-dans-la-transformation-ia-de-sfeir/", "7.webp", "« On est passés de driven by AI à AI first, puis à AI only » — la transformation IA de SFEIR", "13 juil. 2026"),
    ("le-loup-et-le-chien/", "8.jpg", "Le Loup et le chien", "9 juil. 2026"),
]
posts_html = '<div class="posts">\n' + "\n".join(
    f'<a class="post" href="https://prompt-humain.ghost.io/{u}" rel="noopener"><img src="/assets/blog/{img}" alt="" loading="lazy" decoding="async"><span class="meta"><span class="t">{t}</span><span class="d">{d}</span></span></a>'
    for u, img, t, d in POSTS) + "\n</div>"

about_body = f"""<main id="main">
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">À propos</span>
    <h1>Le recrutement tech, <em>vu des deux côtés de la table.</em></h1>
    <p class="lead">BUILD RH, c'est Shirley Almosni Chiche&nbsp;: 15 ans de recrutement IT, aux côtés des équipes tech comme des candidats. CAP Bascule est co-porté avec Coralie Nohel.</p>
  </div>
</section>

<section class="section" aria-labelledby="shirley-title">
  <div class="wrap two-col">
    <div>
      <div class="person" style="grid-template-columns:1fr">
        <div class="photo" style="width:168px;height:168px"><img src="/assets/shirley-portrait.png" alt="Portrait de Shirley Almosni Chiche" width="400" height="400" decoding="async"></div>
      </div>
      <h2 id="shirley-title" class="mt-m" style="font-size:clamp(1.8rem,3.6vw,2.4rem)">Shirley Almosni Chiche</h2>
      <p class="muted mt-s">Fondatrice de BUILD RH · co-fondatrice de CAP Bascule · Paris</p>
      <div class="facts">
        <div><strong>15 ans</strong><span>de recrutement IT</span></div>
        <div><strong>3 livres</strong><span>sur le recrutement IT</span></div>
      </div>
      <div class="cta-row mt-m"><a class="link-arrow" href="{SHIRLEY_LI}" rel="noopener">LinkedIn <span aria-hidden="true">↗</span></a><a class="link-arrow" href="https://github.com/AlmosniShirley" rel="noopener">GitHub <span aria-hidden="true">↗</span></a></div>
    </div>
    <div>
      <p class="lead mt-0" style="color:var(--ink)">J'interviens auprès de startups et de scale-ups tech, dans des contextes où il faut délivrer vite sans baisser le niveau.</p>
      <p>Ma valeur tient dans le fait de travailler à la fois sur la <strong>stratégie</strong> (ce que l'équipe doit devenir), le <strong>process</strong> (comment on recrute), la <strong>relation</strong> (managers, candidats, équipes) et l'<strong>exécution</strong> (sourcing, entretiens, closing).</p>
      <p>Autrice de <em>Les joies du recruteur</em>, <em>Startuffe Nation</em> et <em>The Pragmatic Recruiter</em>, je suis intervenue à BlendWebMix, Sunny Tech, Devoxx et à la Journée de la Tech.</p>
      <div class="chips mt-m" aria-label="Valeurs"><span class="chip">Empathie</span><span class="chip">Satisfaction</span><span class="chip">Ténacité</span></div>
    </div>
  </div>
</section>

<section class="section alt" aria-labelledby="forces-title">
  <div class="wrap">
    <div class="section-head"><span class="kicker">Ce que j'apporte</span><h2 id="forces-title">Quatre forces, au service de vos équipes</h2></div>
    <div class="grid grid-4">
      <div class="card"><h3>Une forte capacité d'entretiens</h3><p>J'absorbe un volume important de rendez-vous dans des contextes de scale-up où il faut délivrer vite et bien.</p></div>
      <div class="card"><h3>Le matching</h3><p>Expérience, outils d'IA et intelligence émotionnelle combinés pour amener les bonnes personnes dans le process.</p></div>
      <div class="card"><h3>Qualité et expérience candidat</h3><p>Rythme, culture du feedback, annonces détaillées et transparentes&nbsp;: chaque étape du parcours candidat est soignée.</p></div>
      <div class="card"><h3>Conseil et amélioration continue</h3><p>Immersion dans les équipes et audit pour accompagner le changement. Le freelancing comme démarche d'impact.</p></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="ia-title">
  <div class="wrap two-col">
    <div>
      <span class="kicker">Outils</span>
      <h2 id="ia-title" style="font-size:clamp(1.6rem,3.2vw,2.2rem)">L'IA comme levier, pas comme promesse</h2>
    </div>
    <div>
      <p>J'utilise l'IA pour affiner le sourcing, préparer les entretiens et gagner du temps sur ce qui peut l'être. Le jugement, la relation et la décision restent humains.</p>
      <div class="chips mt-s"><span class="chip">LinkedIn Recruiter</span><span class="chip">Jarvi</span><span class="chip">Claude</span><span class="chip">Dust</span></div>
      <p class="mt-m muted">Communautés dont je fais partie&nbsp;:</p>
      <div class="chips">
        <a class="chip logo" href="https://takomu.ai/" rel="noopener"><img src="/assets/logos/takomu.svg" alt="" loading="lazy">TAKOMU · IA</a>
        <a class="chip logo" href="https://www.arboriia.tech/" rel="noopener"><img src="/assets/logos/arboriia.svg" alt="Arboriia" loading="lazy" style="height:14px"></a>
      </div>
    </div>
  </div>
</section>

<section class="section cap-zone" aria-labelledby="coralie-title">
  <div class="wrap">
    <div class="section-head"><span class="kicker" style="color:var(--cap)">CAP Bascule</span><h2 id="coralie-title">Co-porté avec Coralie Nohel</h2></div>
    <div class="people" style="grid-template-columns:minmax(0,1fr)">{person_coralie(short=False)}</div>
  </div>
</section>

<section class="section" aria-labelledby="blog-title">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Contenu et prise de parole</span>
      <h2 id="blog-title">Prompt Humain, le blog</h2>
      <p class="lead">Des entretiens avec des leaders tech sur l'IA, les métiers et l'organisation.</p>
    </div>
    {posts_html}
    <div class="section-foot cta-row"><a class="link-arrow build" href="https://prompt-humain.ghost.io/" rel="noopener">Tous les articles <span aria-hidden="true">↗</span></a><a class="link-arrow" href="https://github.com/AlmosniShirley" rel="noopener">Projets et expérimentations sur GitHub <span aria-hidden="true">↗</span></a></div>
  </div>
</section>

<section class="section alt" id="recommandations" aria-labelledby="allreco-title">
  <div class="wrap">
    <div class="section-head"><span class="kicker">Recommandations LinkedIn</span><h2 id="allreco-title">Ce qu'en disent collègues et candidats</h2></div>
    {quotes(all_layout=True)}
  </div>
</section>

{cta_band("Travaillons ensemble", "Un recrutement à lancer ou une situation à clarifier&nbsp;: choisissez votre porte d'entrée.", ("Parler d'un recrutement", "/contact.html?besoin=recrutement"), ("Parler d'une situation sensible", "/contact.html?besoin=situation"))}
</main>"""

# =====================================================================
# CONTACT
# =====================================================================
contact_body = f"""<main id="main">
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">Contact</span>
    <h1>Par quoi voulez-vous <em>commencer&nbsp;?</em></h1>
    <p class="lead">Un recrutement à lancer, un process à structurer ou une situation professionnelle sensible&nbsp;: quelques lignes suffisent pour démarrer.</p>
  </div>
</section>
<section class="section">
  <div class="wrap contact-grid">
    {CONTACT_ASIDE}
    {contact_form("form-contact")}
  </div>
</section>
<section class="section alt" aria-labelledby="next-title">
  <div class="wrap">
    <div class="section-head"><span class="kicker">Ensuite</span><h2 id="next-title">Ce qui se passe après votre message</h2></div>
    <ol class="method" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr))">
      <li><strong>Une réponse rapide</strong><p>Shirley répond généralement sous 24&nbsp;h pour proposer un premier échange.</p></li>
      <li><strong>Un premier échange</strong><p>Comprendre le contexte, le besoin et l'urgence. Sans engagement.</p></li>
      <li><strong>Une proposition claire</strong><p>Périmètre, durée, indicateurs et forfait, définis ensemble avant tout démarrage.</p></li>
    </ol>
  </div>
</section>
</main>"""

# =====================================================================
# 404
# =====================================================================
nf_body = """<main id="main">
<section class="page-hero" style="border-bottom:none">
  <div class="wrap">
    <span class="eyebrow">Erreur 404</span>
    <h1>Cette page n'existe pas <em>ou a changé d'adresse.</em></h1>
    <p class="lead">Le site BUILD RH a été réorganisé. Voici les principaux points d'entrée.</p>
    <div class="cta-row">
      <a class="btn btn-build" href="/build-rh.html">Recruter sans ralentir</a>
      <a class="btn btn-cap" href="/cap-bascule.html">Gérer une situation sensible</a>
      <a class="btn btn-outline" href="/">Retour à l'accueil</a>
    </div>
  </div>
</section>
</main>"""

PAGES = [
    ("index", "Recrutement tech &amp; transitions professionnelles | BUILD RH",
     "BUILD RH aide les startups et scale-ups à recruter les bons profils tech, structurer leur recrutement et traiter les situations professionnelles sensibles avec CAP Bascule.",
     index_body, ld(ORG), "", False),
    ("build-rh", "RPO Impact, recrutement tech en immersion | BUILD RH",
     "RPO Impact : un dispositif de recrutement en immersion, orienté résultats et conçu pour laisser une capacité durable. Immersion, Delivery, Build et Ancrage, pour un forfait construit autour de vos objectifs.",
     build_body, crumbs("BUILD RH", "/build-rh.html"), "", False),
    ("cap-bascule", "CAP Bascule, transitions professionnelles sensibles | BUILD RH",
     "CAP Bascule : un accompagnement externe et confidentiel, financé par l'entreprise, pour clarifier une situation professionnelle sensible, décider et traverser la transition.",
     cap_body, crumbs("CAP Bascule", "/cap-bascule.html"), "theme-cap", False),
    ("cas-clients", "Cas clients recrutement tech : Sunday, Pix, DeepReach | BUILD RH",
     "Sunday, Pix, DeepReach, Elax Énergie, Ilek, Moments Lab : contexte, besoin, intervention et résultat de six missions de recrutement tech BUILD RH.",
     cases_body, crumbs("Cas clients", "/cas-clients.html"), "", False),
    ("a-propos", "Shirley Almosni Chiche, recruteuse tech | BUILD RH",
     "15 ans de recrutement IT auprès de startups et scale-ups. Stratégie, process, relation et exécution. CAP Bascule co-porté avec Coralie Nohel.",
     about_body, crumbs("À propos", "/a-propos.html"), "", False),
    ("contact", "Contact : recrutement ou situation sensible | BUILD RH",
     "Un besoin de recrutement, de structuration ou une situation professionnelle sensible ? Décrivez votre contexte en quelques lignes.",
     contact_body, crumbs("Contact", "/contact.html"), "", False),
    ("404", "Page introuvable | BUILD RH", "Cette page n'existe pas ou a changé d'adresse.", nf_body, "", "", True),
]

for name, title, desc, body, jsonld, cls, noindex in PAGES:
    html = page(name, title, desc, body, current=name, jsonld=jsonld, body_class=cls, noindex=noindex)
    with open(os.path.join(OUT, f"{name}.html"), "w") as f:
        f.write(html)
    print("wrote", name)
