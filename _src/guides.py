"""Guides SEO : contenus de fond pour Google et les assistants IA.
Règle : aucune statistique ni aucun cas inventé ; seuls les cas clients réels du site sont cités."""
from blocks import SIGNATURE

def faq(items):
    return '<div class="faq">\n' + "\n".join(
        f'      <details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + "\n    </div>"

def guide(eyebrow, h1, lead, sections, faq_items, cta, updated="16 novembre 2026", cap=False):
    sec = "\n".join(f"""<section class="guide-sec">
  <h2>{h}</h2>
  {body}
</section>""" for h, body in sections)
    btn = "btn-cap" if cap else "btn-build"
    return f"""<main id="main">
<section class="page-hero">
  <div class="wrap narrow">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    <p class="guide-meta">Par <a href="/a-propos.html">Shirley Almosni Chiche</a>, recruteuse tech depuis 15 ans · Mis à jour le {updated}</p>
  </div>
</section>
<section class="section">
  <div class="wrap narrow guide">
{sec}
<section class="guide-sec">
  <h2>Questions fréquentes</h2>
  {faq(faq_items)}
</section>
  </div>
</section>
<section class="cta-band{' cap-band' if cap else ''}">
  <div class="wrap">
    <h2>{cta[0]}</h2>
    <p>{cta[1]}</p>
    <div class="cta-row"><a class="btn {'btn-ink' if cap else btn}" href="{cta[3]}">{cta[2]} <span class="arrow" aria-hidden="true">→</span></a></div>
  </div>
</section>
</main>"""

# ---------------------------------------------------------------- 1. RPO
RPO = guide(
    "Guide · RPO",
    "RPO : externaliser le recrutement tech <em>sans perdre la main</em>",
    "Le RPO (Recruitment Process Outsourcing) consiste à confier tout ou partie de son recrutement à un partenaire externe qui travaille au cœur de l'équipe. Quand l'utiliser, en quoi il diffère d'un cabinet, et comment en faire un levier durable.",
    [
        ("Qu'est-ce qu'un RPO ?", """<p>Un <strong>RPO</strong>, pour <em>Recruitment Process Outsourcing</em>, est une forme d'externalisation du recrutement&nbsp;: un ou plusieurs recruteurs externes prennent en charge le processus de recrutement d'une entreprise, en s'intégrant à ses outils, à ses rituels et à ses équipes.</p>
  <p>À la différence d'une mission ponctuelle, le RPO s'inscrit dans la durée et couvre souvent <strong>plusieurs postes en parallèle</strong>&nbsp;: définition des besoins, sourcing, entretiens, suivi des candidats, closing, et parfois la structuration du process lui-même.</p>"""),
        ("RPO, cabinet de recrutement, recruteur interne : quelles différences ?", """<ul class="checklist">
    <li><strong>Le cabinet de recrutement</strong> intervient poste par poste, depuis l'extérieur, et se rémunère en général au succès. Il est adapté à un besoin ponctuel et bien délimité.</li>
    <li><strong>Le recruteur interne</strong> connaît parfaitement l'entreprise, mais un recrutement prend du temps et une embauche engage sur la durée, même si le volume baisse ensuite.</li>
    <li><strong>Le RPO</strong> combine les deux&nbsp;: la proximité d'un recruteur intégré à l'équipe et la souplesse d'un partenaire externe, mobilisable rapidement et sur une période définie.</li>
  </ul>"""),
        ("Quand un RPO est-il pertinent ?", """<p>Le RPO prend tout son sens quand le recrutement devient un sujet de vitesse pour toute l'équipe&nbsp;:</p>
  <ul class="checklist">
    <li>plusieurs recrutements tech doivent avancer en même temps, par exemple après une levée de fonds&nbsp;;</li>
    <li>les managers passent plus de temps en entretiens qu'avec leur équipe&nbsp;;</li>
    <li>le process varie selon la personne qui recrute, et la qualité des décisions s'en ressent&nbsp;;</li>
    <li>des profils rares sont à trouver&nbsp;: sécurité, data, staff engineers, engineering managers&nbsp;;</li>
    <li>une équipe tech doit être construite, parfois from scratch.</li>
  </ul>"""),
        ("Le vrai enjeu : ce qui reste après la mission", """<p>Des recrutements réussis ne suffisent pas si, à la fin de la mission, le process, les outils et les réflexes repartent avec le prestataire. L'équipe doit pouvoir continuer à recruter seule, avec des critères de décision clairs et des managers autonomes.</p>
  <p>C'est pour éviter cet écueil que BUILD RH a conçu le <a href="/build-rh.html">RPO Impact</a>.</p>"""),
        ("Le RPO Impact : recruter maintenant, renforcer durablement", f"""<p><strong>{SIGNATURE}</strong> Il combine quatre dimensions&nbsp;:</p>
  <ul class="checklist">
    <li><strong>Immersion</strong>&nbsp;: comprendre le contexte, la culture, les rôles et les blocages avant de chercher.</li>
    <li><strong>Delivery</strong>&nbsp;: faire avancer les recrutements prioritaires dès le début, avec un sourcing augmenté par l'IA et des décisions humaines.</li>
    <li><strong>Build</strong>&nbsp;: un process qui aide à décider&nbsp;: scorecards de poste et de candidature, critères observables, rituels de décision.</li>
    <li><strong>Ancrage</strong>&nbsp;: transmettre les outils et les pratiques pour que l'équipe continue à recruter après la mission.</li>
  </ul>
  <p>Le forfait est global et construit autour des objectifs&nbsp;: <a href="/build-rh.html#forfait">un socle, une part par recrutement signé et une part liée aux impacts et à l'ancrage</a>. Chaque mission se termine par un bilan d'impact partagé.</p>"""),
        ("Exemples de missions RPO", """<p>Chez <strong>Sunday</strong>, une mission RPO de 3 mois a permis 18 recrutements, dont 11 backend et fullstack seniors, un Head of Security et un Engineering Manager. Chez <strong>Pix</strong>, une mission RPO a accompagné le passage à 9 millions d'utilisateurs avec 21 recrutements&nbsp;: Product Owners, RSSI, DevOps et développeurs fullstack JS.</p>
  <p><a class="link-arrow build" href="/cas-clients.html">Voir tous les cas clients</a></p>"""),
    ],
    [
        ("Combien de temps dure un RPO ?", "La durée dépend du nombre de recrutements, de leur criticité et du niveau de structuration nécessaire. Elle est définie au démarrage. À titre d'exemple, la mission menée chez Sunday a duré 3 mois."),
        ("Le RPO remplace-t-il l'équipe RH ?", "Non. Il travaille avec elle et avec les managers. L'entreprise garde la main sur ses décisions ; le RPO apporte de la capacité, de la méthode et un regard externe."),
        ("Comment est facturé le RPO Impact ?", "Par un forfait global construit autour des objectifs : un socle d'immersion, de cadrage, de structuration et de pilotage, une part par recrutement signé et une part liée aux impacts et à l'ancrage. Le RPO Impact ne facture pas des jours de recrutement."),
        ("Quels profils tech peut-on recruter en RPO ?", "Développeurs backend, frontend, fullstack et mobile, DevOps, profils sécurité (RSSI, Head of Security), data (Analytics Engineer), Product Owners et Product Managers, Engineering Managers."),
    ],
    ("Un RPO qui laisse une capacité durable ?", "Décrivez votre contexte en quelques lignes : le premier échange sert à définir ensemble les objectifs.", "Parler d'un RPO Impact", "/contact.html?besoin=recrutement"),
)

# ---------------------------------------------------------------- 2. Startups / scale-ups
STARTUP = guide(
    "Guide · Recrutement tech",
    "Recruter des profils tech <em>en startup et en scale-up</em>",
    "Faire entrer les bons développeurs, data et product, vite et sans baisser la barre : ce qui bloque le plus souvent, et la méthode qui fonctionne dans les équipes tech en croissance.",
    [
        ("Pourquoi le recrutement tech freine la croissance", """<p>Dans une startup ou une scale-up, chaque poste vacant ralentit la roadmap, et chaque mauvais recrutement coûte du temps, de l'énergie managériale et de la crédibilité auprès de l'équipe. Les difficultés reviennent souvent aux mêmes endroits&nbsp;:</p>
  <ul class="checklist">
    <li>un besoin flou&nbsp;: on cherche «&nbsp;un senior&nbsp;» sans savoir ce qu'il doit avoir réussi dans 6 ou 12 mois&nbsp;;</li>
    <li>des managers qui enchaînent les entretiens au détriment de leur équipe&nbsp;;</li>
    <li>des décisions qui dépendent de la personne qui fait passer l'entretien&nbsp;;</li>
    <li>des candidats qui décrochent en cours de route ou refusent au moment de l'offre.</li>
  </ul>"""),
        ("La méthode : clarifier, recruter, décider, transmettre", """<ul class="checklist">
    <li><strong>Clarifier ce qu'il faut réussir</strong>&nbsp;: une scorecard de poste précise la mission réelle, les résultats attendus, les critères indispensables et les points de vigilance.</li>
    <li><strong>Faire avancer les bons profils</strong>&nbsp;: sourcing et chasse ciblés, annonces transparentes, qualification et matching, coordination avec les managers.</li>
    <li><strong>Décider sur des critères observables</strong>&nbsp;: scorecards de candidature partagées, rôles et rituels de décision clairs.</li>
    <li><strong>Soigner l'expérience candidat jusqu'au closing</strong>&nbsp;: rythme, retours détaillés, négociation.</li>
    <li><strong>Transmettre</strong>&nbsp;: pour que l'équipe garde un process réutilisable après la mission.</li>
  </ul>"""),
        ("Les profils recrutés", """<p>Développeurs backend, frontend, fullstack (notamment JS) et mobile, staff engineers, DevOps, profils sécurité (RSSI, Head of Security), data (Analytics Engineer), Product Owners, Product Managers, Engineering Managers, ITSM et IT automation.</p>"""),
        ("Construire une équipe tech from scratch", """<p>Créer une équipe de zéro demande de recruter vite tout en posant les fondations&nbsp;: niveau d'exigence, culture technique, process de décision. Chez <strong>DeepReach</strong>, 20 recrutements en moins d'un an ont permis de constituer une équipe de développeurs fullstack JS.</p>"""),
        ("Recruter en croissance, après une levée de fonds", """<p>Après une levée, le volume augmente brutalement. Chez <strong>Elax Énergie</strong>, 3 profils clés ont été recrutés en 2 mois, avec un audit du process. Chez <strong>Ilek</strong>, 6 développeurs seniors ont rejoint l'équipe.</p>
  <p><a class="link-arrow build" href="/cas-clients.html">Voir les cas clients détaillés</a></p>"""),
    ],
    [
        ("Combien de temps faut-il pour recruter un développeur senior ?", "Cela dépend du profil, du marché et de la qualité du process. Les leviers les plus efficaces : un besoin clair dès le départ, peu d'étapes, des retours rapides aux candidats et une décision sur des critères partagés."),
        ("Faut-il une annonce pour recruter des profils tech ?", "Oui, à condition qu'elle soit transparente : contexte, enjeux techniques, rémunération, équipe. Elle complète la chasse directe, qui reste indispensable pour les profils rares."),
        ("Où intervient BUILD RH ?", "BUILD RH est basé à Paris et accompagne des startups, scale-ups et entreprises tech."),
        ("Mission ponctuelle ou dispositif plus large ?", "Pour plusieurs recrutements et un process à renforcer, le RPO Impact combine immersion, delivery, build et ancrage, avec un forfait construit autour des objectifs."),
    ],
    ("Un recrutement tech à lancer ?", "Quelques lignes suffisent pour démarrer : le contexte, les postes, le calendrier.", "Parler d'un recrutement", "/contact.html?besoin=recrutement"),
)

# ---------------------------------------------------------------- 3. Neurodiversité
NEURO = guide(
    "Guide · Recrutement inclusif",
    "Recrutement inclusif : <em>ne plus passer à côté des profils neuroatypiques</em>",
    "TDAH, dyslexie, autisme, haut potentiel : des talents passent à travers les mailles des process classiques. Ce qui exclut sans le vouloir, et ce qui aide concrètement à recruter et intégrer les personnes neuroatypiques.",
    [
        ("Un enjeu plus large qu'on ne le pense", """<p>On estime que 15 à 20&nbsp;% de la population présente un fonctionnement neurologique atypique. Pourtant, le monde du travail, et le recrutement en particulier, reste largement pensé pour un modèle unique. Les talents ne rentrent pas tous dans les mêmes cases, et c'est une chance.</p>"""),
        ("Où le recrutement exclut sans le vouloir", """<ul class="checklist">
    <li><strong>Des annonces floues ou surchargées</strong>, qui empêchent de savoir ce qui est vraiment attendu.</li>
    <li><strong>Des entretiens non structurés</strong>, qui récompensent l'aisance sociale plus que la compétence.</li>
    <li><strong>Des critères de «&nbsp;fit&nbsp;» implicites</strong>, jamais formulés, donc jamais vérifiables.</li>
    <li><strong>Des formats imposés sans explication</strong>&nbsp;: exercices chronométrés, questions surprises, enchaînements d'interlocuteurs.</li>
  </ul>"""),
        ("Ce qui aide, concrètement", """<ul class="checklist">
    <li><strong>Des critères observables</strong>, posés dans une scorecard de poste et partagés par tous les intervenants.</li>
    <li><strong>Un process annoncé à l'avance</strong>&nbsp;: étapes, durée, interlocuteurs, nature des exercices.</li>
    <li><strong>Des entretiens structurés</strong>, avec les mêmes questions pour chaque candidat et une décision collégiale.</li>
    <li><strong>La possibilité de demander un aménagement</strong>, sans avoir à se justifier.</li>
    <li><strong>Des retours écrits et précis</strong>, plutôt que des impressions générales.</li>
  </ul>
  <p>Ces pratiques ne profitent pas qu'aux personnes neuroatypiques&nbsp;: elles rendent le recrutement plus juste et plus fiable pour tout le monde. Ce sont aussi celles que le <a href="/build-rh.html">RPO Impact</a> met en place dans sa dimension Build.</p>"""),
        ("Pour aller plus loin", """<ul class="checklist">
    <li>La chaîne YouTube <a href="https://www.youtube.com/@TDArHH" rel="noopener">TDArH</a>&nbsp;: décryptages concrets et conseils pratiques pour les recruteurs et les managers.</li>
    <li>Sur le blog Prompt Humain&nbsp;: <a href="https://prompt-humain.ghost.io/je-ne-suis-pas-desorganisee-mon-cerveau-ne-fonctionne-pas-en-ligne-droite/" rel="noopener">«&nbsp;Je ne suis pas désorganisée&nbsp;: mon cerveau ne fonctionne pas en ligne droite&nbsp;»</a> et <a href="https://prompt-humain.ghost.io/quand-voir-les-problemes-devient-un-probleme-au-travail/" rel="noopener">«&nbsp;Quand voir les problèmes devient un problème au travail&nbsp;»</a>.</li>
  </ul>
  <p class="note">Ce guide ne constitue pas un avis médical. Les expériences varient d'une personne à l'autre.</p>"""),
    ],
    [
        ("Faut-il connaître le diagnostic d'un candidat ?", "Non. Le candidat n'a aucune obligation de le partager. L'objectif est un process clair et équitable pour tous, avec la possibilité de demander un aménagement sans se justifier."),
        ("Quels aménagements simples proposer en entretien ?", "Communiquer les étapes et les questions types à l'avance, proposer un format écrit pour certains exercices, laisser du temps de réflexion, limiter les enchaînements d'interlocuteurs."),
        ("Le recrutement inclusif ralentit-il le process ?", "Pas nécessairement. Des critères clairs et des entretiens structurés réduisent au contraire les hésitations et les allers-retours au moment de décider."),
    ],
    ("Rendre votre recrutement plus inclusif ?", "Parlons de votre process : ce qui exclut sans le vouloir, et ce qui peut changer rapidement.", "Échanger sur votre recrutement", "/contact.html?besoin=recrutement"),
)
