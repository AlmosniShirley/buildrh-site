TODO_MODALITE = "Mission au succès."

# Toutes les données ci-dessous proviennent de l'ancien site (index.html) ou de l'ancien llms.txt.
CASES = [
    dict(name="Sunday", logo="sunday.png", w=0, big="18", unit="recrutements<br>en 3 mois",
         ctx="Scale-up.",
         need="Recruter en parallèle des développeurs seniors et plusieurs rôles clés, sur un calendrier serré.",
         inter="Mission RPO de 3 mois (septembre à décembre 2025)&nbsp;: sourcing, entretiens et closing.",
         res="11 backend et fullstack seniors, 1 PM, 1 ITSM technical specialist, 1 IT automation &amp; IA specialist, 1 Head of Security, 1 Staff Mobile, 1 Analytics Engineer, 1 Engineering Manager."),
    dict(name="Pix", logo="pix.svg", big="21", unit="recrutements<br>tous profils",
         ctx="Scalabilité de la plateforme, avec le passage à 9 millions d'utilisateurs.",
         need="Renforcer en même temps le produit, la sécurité, l'infrastructure et le développement.",
         inter="Mission RPO.",
         res="Product Owners, RSSI, DevOps, développeurs fullstack JS juniors et seniors."),
    dict(name="DeepReach", logo="deepreach.png", big="20", unit="recrutements<br>en moins d'un an",
         ctx="Création d'une équipe tech from scratch.",
         need="Constituer une équipe de développement complète, sans base existante.",
         inter=TODO_MODALITE,
         res="Une équipe de développeurs fullstack JS constituée."),
    dict(name="Elax Énergie", logo="elax.png", big="3", unit="recrutements<br>en 2 mois, et un audit",
         ctx="Croissance après une levée de fonds.",
         need="Recruter vite trois profils clés et fiabiliser le process de recrutement.",
         inter="Build + Delivery&nbsp;: audit du process et recrutements.",
         res="1 Analytics Engineer, 1 référent technique itinérant, 1 ingénieur DevOps."),
    dict(name="Ilek", logo="ilek.svg", big="6", unit="recrutements<br>seniors",
         ctx="Scale-up, après une levée de fonds.",
         need="Renforcer l'équipe de développement avec des profils seniors.",
         inter=TODO_MODALITE,
         res="6 développeurs seniors recrutés."),
    dict(name="Moments Lab", logo="momentslab.png", big="3", unit="recrutements<br>réalisés",
         ctx="Changement de paradigme produit.",
         need="Recruter des développeurs capables de porter la nouvelle direction produit.",
         inter=TODO_MODALITE,
         res="2 développeurs backend, 1 développeur frontend."),
]


def case_card(c, level="h3"):
    return f"""<article class="card case">
  <div class="case-head"><{level}>{c['name']}</{level}><span class="case-logo"><img src="/assets/logos/{c['logo']}" alt="" loading="lazy" decoding="async"></span></div>
  <p class="case-result"><span class="big">{c['big']}</span><span class="unit">{c['unit']}</span></p>
  <dl>
    <div><dt>Contexte</dt><dd>{c['ctx']}</dd></div>
    <div><dt>Besoin</dt><dd>{c['need']}</dd></div>
    <div><dt>Intervention</dt><dd>{c['inter']}</dd></div>
    <div><dt>Résultat</dt><dd>{c['res']}</dd></div>
  </dl>
</article>"""


def cases_grid(subset=None):
    items = CASES if subset is None else [c for c in CASES if c["name"] in subset]
    return '<div class="cases">\n' + "\n".join(case_card(c) for c in items) + "\n</div>"


OFFERS = """<div class="grid grid-3">
  <article class="card offer-card">
    <span class="tag tag-build">Build</span>
    <h3>Construire le dispositif</h3>
    <p>Vous recrutez, mais le process ne suit pas&nbsp;: délais qui s'allongent, entretiens inégaux, candidats qui décrochent.</p>
    <ul>
      <li>Conception ou refonte du process</li>
      <li>Audit et rapport d'étonnement</li>
      <li>Annonces, grilles d'entretien, expérience candidat</li>
      <li>Accompagnement des managers et des équipes</li>
    </ul>
  </article>
  <article class="card offer-card">
    <span class="tag tag-build">Delivery</span>
    <h3>Recruter, de bout en bout</h3>
    <p>Le besoin est clair&nbsp;: il faut des personnes en poste, au bon niveau.</p>
    <ul>
      <li>Sourcing et chasse</li>
      <li>Qualification et entretiens</li>
      <li>Suivi des candidats et retours détaillés</li>
      <li>Closing et négociation</li>
    </ul>
  </article>
  <article class="card offer-card featured">
    <span class="tag tag-build">Build + Delivery</span>
    <h3>Structurer en recrutant</h3>
    <p>Recruter maintenant, tout en posant des bases qui tiendront après la mission.</p>
    <ul>
      <li>Les recrutements avancent dès le démarrage</li>
      <li>Le process s'améliore sur le terrain, pas sur le papier</li>
      <li>Vos équipes gardent un dispositif réutilisable</li>
    </ul>
  </article>
</div>"""

COMPARE = """<h3 class="compare-title" id="formules">Un seul format d'engagement, deux natures d'intervention</h3>
<div class="matrix">
  <div class="matrix-col">
    <span class="kicker">Le format d'engagement</span>
    <div class="matrix-item">
      <h4>RPO impact</h4>
      <p class="sub">Un dispositif intégré, orienté objectifs et impacts</p>
      <p>Un bras armé recrutement intégré à votre équipe, sur la durée, avec un forfait qui marie les deux formats&nbsp;: un socle pour l'intégration et la structuration, une part liée à chaque recrutement signé, comme une mission au succès.</p>
    </div>
    <div class="matrix-item">
      <h4>Ce qu'il prend à chacun</h4>
      <p><strong>Au RPO classique</strong>&nbsp;: l'intégration dans vos équipes, la structuration et le pilotage, sur la durée.</p>
      <p><strong>À la mission au succès</strong>&nbsp;: une rémunération qui avance avec les recrutements signés.</p>
      <p><strong>Ce qu'il ajoute</strong>&nbsp;: une part liée aux impacts durables sur votre organisation.</p>
    </div>
  </div>
  <div class="matrix-col">
    <span class="kicker">Nature de l'intervention</span>
    <div class="matrix-item">
      <h4>Build</h4>
      <p class="sub">Structurer et améliorer le recrutement</p>
      <p>Conception, amélioration et audit du process, accompagnement des managers et des équipes.</p>
    </div>
    <div class="matrix-item">
      <h4>Delivery</h4>
      <p class="sub">Exécuter, du sourcing jusqu'au closing</p>
      <p>Sourcing, chasse, qualification, entretiens et closing. Les deux natures se combinent&nbsp;: Build + Delivery.</p>
    </div>
  </div>
</div>"""

HYBRID = """<div class="hybrid" aria-label="Le RPO impact combine le RPO et la mission au succès">
  <div class="hy-part">
    <span class="hy-label">Du RPO</span>
    <strong>L'intégration</strong>
    <p>Un bras armé recrutement dans votre équipe&nbsp;: structuration du process, pilotage, accompagnement des managers.</p>
    <span class="hy-pay">→ rémunéré par un <b>socle</b></span>
  </div>
  <div class="hy-part">
    <span class="hy-label">De la mission au succès</span>
    <strong>L'alignement sur les résultats</strong>
    <p>Une part du forfait n'est due qu'à chaque recrutement signé, et pèse davantage sur les postes critiques.</p>
    <span class="hy-pay">→ rémunéré <b>par recrutement</b></span>
  </div>
  <div class="hy-part">
    <span class="hy-label">Vos objectifs</span>
    <strong>Les impacts obtenus</strong>
    <p>Une part importante du forfait, liée aux objectifs définis ensemble&nbsp;: délais de recrutement, charge des managers, appropriation du process.</p>
    <span class="hy-pay">→ une <b>part impact</b></span>
  </div>
  <div class="hy-part hy-result">
    <span class="hy-label">Le RPO impact BUILD RH</span>
    <strong>Un forfait global construit autour de trois éléments&nbsp;:</strong>
    <ul class="hy-list"><li>le dispositif mis en place&nbsp;;</li><li>les recrutements réalisés&nbsp;;</li><li>les impacts obtenus.</li></ul>
  </div>
</div>"""

FORFAIT = """<div class="forfait">
  <div class="forfait-main">
    <span class="kicker">Le forfait RPO Impact</span>
    <h3>Un forfait global, construit ensemble autour de vos objectifs.</h3>
    <p>Nous définissons le problème à résoudre, les résultats attendus et les impacts souhaités. Le périmètre, les indicateurs de suivi et le forfait sont ensuite précisés au démarrage.</p>
    <p class="forfait-note">Le dispositif est suivi régulièrement et ajusté lorsque le contexte évolue.</p>
  </div>
  <div class="forfait-factors">
    <p class="factors-title">Un forfait global construit autour de trois éléments&nbsp;:</p>
    <ul class="forfait-three">
      <li><strong>Le dispositif mis en place</strong><span>Un socle d'immersion, de cadrage, de structuration et de pilotage.</span></li>
      <li><strong>Les recrutements réalisés</strong><span>Une part liée aux recrutements effectivement signés.</span></li>
      <li class="key"><strong>Les impacts et l'ancrage obtenus</strong><span>Une part importante, liée aux objectifs définis ensemble.</span></li>
    </ul>
    <p class="forfait-formula">Socle d'immersion + recrutements + impact et ancrage</p>
  </div>
</div>"""

RPO_STEPS = """<ol class="method">
  <li><strong>Comprendre le contexte</strong><p>Immersion au sein de vos équipes&nbsp;: l'entreprise, la roadmap, les rôles à recruter et ce qui freine aujourd'hui.</p></li>
  <li><strong>Définir les objectifs et les impacts attendus</strong><p>Ce qui doit avoir changé à la fin&nbsp;: postes pourvus, délais, charge des managers, qualité du process.</p></li>
  <li><strong>Construire le périmètre du dispositif</strong><p>Build, Delivery ou les deux&nbsp;; rôles de chacun, rituels, outils, niveau d'autonomie visé.</p></li>
  <li><strong>Définir le forfait et les indicateurs de suivi</strong><p>Un forfait adossé aux objectifs, et des indicateurs partagés pour suivre l'avancement.</p></li>
  <li><strong>Exécuter, mesurer et ajuster</strong><p>Le dispositif est suivi régulièrement et ajusté lorsque le contexte évolue.</p></li>
</ol>"""

PARCOURS = """<div class="grid grid-3">
  <article class="card parcours">
    <span class="for">Encore en poste</span>
    <h3>CAP Clarifier</h3>
    <span class="duration">7 à 10 jours</span>
    <p>Pour décider de rester, d'ajuster ou de partir, quand une personne ne sait plus où elle en est dans son poste.</p>
    <p class="path-line">Cadrer → Éclairer → Décider</p>
  </article>
  <article class="card parcours">
    <span class="for">Un départ se prépare</span>
    <h3>CAP Traverser</h3>
    <span class="duration">3 à 6 semaines</span>
    <p>Pour préparer une sortie propre&nbsp;: fin de période d'essai, séparation, départ après plusieurs années.</p>
    <p class="path-line">Cadrer → Éclairer → Décider → Préparer la sortie</p>
  </article>
  <article class="card parcours">
    <span class="for">Après une rupture</span>
    <h3>CAP Rebond</h3>
    <span class="duration">3 à 6 semaines</span>
    <p>Pour reconstruire la suite professionnelle, tirer les enseignements de la transition et préparer un nouveau projet.</p>
    <p class="path-line">Cadrer → Éclairer → Décider → Construire la suite</p>
  </article>
</div>"""

PRINCIPLES = """<div class="principles">
  <div class="principle"><strong>Confidentialité</strong><p>Aucun verbatim transmis, aucun compte rendu individuel envoyé automatiquement. Les règles sont fixées avant de commencer.</p></div>
  <div class="principle"><strong>Neutralité</strong><p>Nous ne cherchons à convaincre personne de rester ou de partir. Chacun reste maître de sa décision.</p></div>
  <div class="principle"><strong>Responsabilité</strong><p>L'entreprise reste responsable de ses décisions et de son management. Elle se donne un cadre pour les exercer.</p></div>
  <div class="principle"><strong>Un espace externe</strong><p>La personne dispose d'un lieu hors de l'entreprise pour prendre du recul. Elle n'est ni évaluée ni surveillée.</p></div>
</div>"""

ISNOT = """<div class="isnot">
  <span class="label">CAP Bascule n'est pas&nbsp;:</span>
  <span class="x">une thérapie</span>
  <span class="x">un conseil juridique</span>
  <span class="x">un dispositif de surveillance</span>
  <span class="x">un moyen de convaincre de rester ou de partir</span>
</div>"""

METHOD = """<ol class="method">
  <li><strong>Comprendre le contexte</strong><p>Immersion dans l'entreprise, l'équipe, la roadmap et le marché visé.</p></li>
  <li><strong>Clarifier le besoin</strong><p>Ce que le poste doit vraiment résoudre, le niveau attendu, ce qui est négociable et ce qui ne l'est pas.</p></li>
  <li><strong>Construire ou renforcer le dispositif</strong><p>Annonce transparente, étapes du process, grilles d'entretien, rôle de chacun.</p></li>
  <li><strong>Exécuter avec les équipes</strong><p>Sourcing, entretiens, comptes rendus détaillés, closing. Les managers interviennent là où ils apportent le plus.</p></li>
  <li><strong>Mesurer et ajuster</strong><p>Suivi des candidats, retours qualitatifs et quantitatifs, ajustements jusqu'à l'intégration.</p></li>
</ol>
<div class="method-cap">
  <span class="tag tag-cap">CAP Bascule</span>
  <span class="flow">Cadrer → Éclairer → Décider → Traverser</span>
  <p>Pour CAP Bascule, la logique reste celle des quatre temps&nbsp;: chaque étape doit produire une clarification, une conversation ou une décision.</p>
</div>"""

# Recommandations LinkedIn — texte intégral, repris tel quel de l'ancien site.
TESTIMONIALS = [
    ("Océane Roudier", "Collègue de Shirley, Arolla", "En tant que cliente de Shirley, j'ai beaucoup apprécié son travail. C'est grâce à sa rigueur, sa ténacité et sa connaissance du marché de l'IT que nous avons effectué de très beaux recrutements pour Arolla&nbsp;!"),
    ("Olivier Moglia", "Founder &amp; CEO, Arolla", "J'ai eu la joie de travailler avec Shirley. C'est une personne très impliquée, professionnelle et avec un talent inné pour la performance. Elle connaît très bien l'écosystème de l'IT et n'a jamais été avare de conseil auprès de nos clients et des candidats."),
    ("Nathalie Wirth Ikedjian", "Co-fondatrice, One RH &amp; One Portage · collègue de Shirley", "J'ai eu le plaisir de travailler avec Shirley lors de mon expérience chez Altimate. En véritable professionnelle du recrutement, elle a su comprendre mes attentes et me proposer systématiquement de très bons profils, que nous avons eu la chance d'intégrer. D'une efficacité redoutable, Shirley a toujours été disponible et à l'écoute de nos besoins, même les plus pressants, le tout dans une atmosphère de collaboration toujours très agréable."),
    ("Laure Bucas", "Responsable Recrutement/Formation, France Loisirs et Chapitre.com · collègue de Shirley", "J'ai le plaisir de recommander Shirley, avec qui j'ai collaboré efficacement de 2011 à 2013, en tant que Responsable Recrutement et Mobilité Interne, dans le cadre de recrutement outsourcé chez Skillink, d'ingénieurs de développement .net / java, sur un marché tendu. Shirley a fait preuve de ténacité et de réactivité. Experte du sourcing et du web 2.0, elle a une véritable expertise technique des SI. J'ai pu apprécier sa perspicacité dans la compréhension des enjeux et l'évaluation des candidats, son sens du service, toujours à la recherche de solutions, pour valoriser tant le client que le candidat."),
    ("Jonathan Guazzelli", "Développeur Fullstack · collègue de Shirley", "Quelqu'un qui pèse très lourd dans le milieu du recrutement. Shirley sait fournir un travail sérieux et concis, elle ne fait pas les choses à moitié. Très bonne en communication elle saura très vite synthétiser un besoin et apportera une bonne visibilité à vos projets de recrutement. Au delà de ses capacités de recruteuse, c'est aussi un très bon agent de carrière qui fait preuve d'un bon relationnel."),
    ("Damien Cavaillès", "Auteur &amp; journaliste · a travaillé avec Shirley", "Shirley fait preuve d'une empathie professionnelle rare dans le monde du travail 😀 Et en même temps, elle sait prendre du recul et dire à ses interlocuteurs ce qu'ils doivent entendre pour atteindre leurs objectifs et être heureux. On a besoin de plus de Shirleys&nbsp;! 💙"),
    ("Camille Khalaghi", "Développeur senior &amp; chef de projet", "Shirley m'a vraiment donné envie d'en connaître plus sur les missions qu'elle me conseillait à l'époque. Ce n'est pas «&nbsp;juste une placeuse&nbsp;»&nbsp;: elle prend vraiment en compte les envies et les goûts de ses consultants, et sait différencier les bonnes missions des missions foireuses. Avec Shirley, une coopération de long terme peut s'installer, et non un one-shot lucratif court-termiste."),
    ("Jonathan Eude", "Consultant, chef de projet, développeur freelance · collègue de Shirley", "Grâce à sa sympathie, son dynamisme et son accueil, Shirley a réussi à m'enlever l'appréhension que l'on peut avoir lors d'une phase de recrutement. Relationnel et écoute plus qu'appréciable, surtout dans un marché où beaucoup nous considèrent comme un «&nbsp;numéro&nbsp;». Et en plus, notre rencontre s'est terminée avec une note positive… J'ai trouvé un poste qui me correspondait&nbsp;!"),
    ("Sébastien Bronner", "Business Manager, Takima · même équipe que Shirley", "Shirley est une professionnelle passionnée du recrutement «&nbsp;geek&nbsp;», comme il en existe peu&nbsp;! Dotée d'un réel talent pour approcher les meilleurs profils IT et leur proposer des offres qui «&nbsp;matchent&nbsp;» à leurs attentes, elle sait aussi brillamment les conseiller, les orienter, les accompagner dans leurs carrières. Sa force est de toujours parfaitement s'identifier aux profils qu'elle recrute en sachant parler le même «&nbsp;langage&nbsp;» qu'eux. Active, motrice, disponible, toujours pleine d'initiatives, elle apporte une forte valeur ajoutée au sein d'une équipe RH / Recrutement."),
    ("Ghalia Ghorab", "Responsable recrutement · même équipe que Shirley", "Shirley est une personne avec laquelle j'ai eu plaisir à travailler. Intègre, professionnelle, Shirley est soucieuse d'un travail rendu bien fait&nbsp;! C'est une personne qui apprécie particulièrement interagir avec ses collègues et être force de proposition. Elle peut être un atout essentiel dans l'entreprise par sa maîtrise des techniques de chasse et ses connaissances du marché IT."),
    ("Zakaria El Marouri", "Senior Technical Lead, Agoda", "J'ai eu l'occasion de rencontrer Shirley en tant que candidat. Shirley fait partie de la nouvelle génération RH&nbsp;: pour moi elle est l'une des rares personnes capables d'avoir une aisance naturelle sur une multitude de domaines IT tout en ayant une excellente approche RH. Elle a su développer un important réseau composé des meilleurs acteurs de l'IT à Paris. Grâce à elle chaque candidat aura la chance de trouver son «&nbsp;perfect match&nbsp;»."),
    ("Aude Amarrurtu", "Insertion professionnelle", "Shirley a développé un réseau hors du commun dans le milieu de l'informatique grâce à sa compréhension très fine des différents sujets. Elle est toujours de bon conseil et attentive aux souhaits de ses candidats."),
]


def quote(t):
    name, who, text = t
    return f"""<figure class="quote">
  <blockquote><p class="mt-0">{text}</p></blockquote>
  <figcaption><span class="name">{name}</span><span class="who">{who}</span></figcaption>
</figure>"""


def quotes(n=None, all_layout=False):
    items = TESTIMONIALS if n is None else TESTIMONIALS[:n]
    cls = "quotes-all" if all_layout else "quotes"
    return f'<div class="{cls}">\n' + "\n".join(quote(t) for t in items) + "\n</div>"


SHIRLEY_LI = "https://www.linkedin.com/in/shirley-almosni-chiche/"
CORALIE_LI = "https://www.linkedin.com/in/coralienohel/"
CAP_SITE = "https://almosnishirley.github.io/capbascule/"


def person_shirley(short=True):
    more = '<a class="link-arrow build" href="/a-propos.html">Parcours complet <span aria-hidden="true">→</span></a>' if short else ''
    return f"""<article class="card person">
  <div class="photo"><img src="/assets/shirley.png" alt="Portrait de Shirley Almosni Chiche" width="610" height="546" loading="lazy" decoding="async"></div>
  <div>
    <h3>Shirley Almosni Chiche</h3>
    <span class="role">Fondatrice de BUILD RH · co-fondatrice de CAP Bascule</span>
    <p>Recruteuse tech depuis 15 ans, j'interviens auprès de startups et de scale-ups, dans des contextes où il faut délivrer vite sans baisser le niveau.</p>
    <ul>
      <li>Stratégie, process, relation et exécution&nbsp;: je travaille sur les quatre à la fois.</li>
      <li>Autrice de trois livres sur le recrutement IT, intervenante en conférences tech.</li>
      <li>L'IA fait partie de mes outils de sourcing et de matching&nbsp;: un levier pour gagner du temps, jamais un substitut au jugement.</li>
    </ul>
    <div class="cta-row">{more}<a class="link-arrow" href="{SHIRLEY_LI}" rel="noopener">LinkedIn <span aria-hidden="true">↗</span></a></div>
  </div>
</article>"""


PERSON_CORALIE = f"""<article class="card person cap-person">
  <div class="monogram" aria-hidden="true">CN</div>
  <div>
    <h3>Coralie Nohel</h3>
    <span class="role">Co-fondatrice de CAP Bascule</span>
    <p>Une expérience en recrutement IT et en ESN, dans des environnements où les sujets humains, techniques et business sont impossibles à séparer.</p>
    <p><span class="todo">Bio détaillée de Coralie à compléter</span></p>
    <div class="cta-row"><a class="link-arrow" href="{CORALIE_LI}" rel="noopener">LinkedIn <span aria-hidden="true">↗</span></a></div>
  </div>
</article>"""

# Exemple chiffré FICTIF (validé par Shirley comme illustration, montants indicatifs).
EXAMPLE = """<div class="example" id="exemple">
  <div class="example-head">
    <span class="tag tag-fictif">Exemple fictif</span>
    <h3>Exemple concret</h3>
    <p><strong>Nova</strong>, une scale-up qui vient de lever des fonds, doit recruter <strong>8 profils tech en 4 mois</strong>. Ses managers sont très sollicités et son process de recrutement doit être fiabilisé.</p>
  </div>
  <div class="example-block">
    <h4>Nous définissons ensemble un forfait composé de trois éléments&nbsp;:</h4>
    <div class="ex-parts ex-parts-3">
      <div class="ex-part"><span class="ex-label">Le socle</span><strong class="ex-amount">12&nbsp;000&nbsp;€&nbsp;HT</strong><span class="ex-detail">Pour l'immersion au sein des équipes, le cadrage du besoin, la structuration du process et le pilotage de la mission.</span></div>
      <div class="ex-part"><span class="ex-label">Les recrutements</span><strong class="ex-sub">Une part par recrutement signé</strong>
        <span class="ex-rate"><strong class="ex-amount">2&nbsp;000&nbsp;€&nbsp;HT</strong> par poste standard</span>
        <span class="ex-rate"><strong class="ex-amount">4&nbsp;000&nbsp;€&nbsp;HT</strong> par poste stratégique ou critique pour l'organisation</span></div>
      <div class="ex-part ex-key"><span class="ex-label">L'impact et l'ancrage</span><strong class="ex-amount">jusqu'à 8&nbsp;000&nbsp;€&nbsp;HT</strong><span class="ex-detail">Une part liée aux objectifs définis ensemble&nbsp;: délais de recrutement, réduction de la charge des managers et appropriation du process par l'équipe.</span></div>
    </div>
    <p class="ex-rule">Le niveau de chaque poste est défini ensemble au démarrage selon sa criticité pour l'organisation. La part correspondante est due uniquement lorsqu'un recrutement est signé. Si un recrutement est suspendu ou supprimé, la part correspondante n'est pas due.</p>
    <div class="ex-calc">
      <p class="ex-calc-title">Pour Nova&nbsp;:</p>
      <ul>
        <li><span>6 postes standards × 2&nbsp;000&nbsp;€&nbsp;HT</span><strong>12&nbsp;000&nbsp;€&nbsp;HT</strong></li>
        <li><span>2 postes stratégiques ou critiques × 4&nbsp;000&nbsp;€&nbsp;HT</span><strong>8&nbsp;000&nbsp;€&nbsp;HT</strong></li>
        <li class="sum"><span>Total possible lié aux recrutements</span><strong>20&nbsp;000&nbsp;€&nbsp;HT</strong></li>
      </ul>
    </div>
  </div>
  <div class="example-block">
    <ul class="ex-outcomes">
      <li>Si les 8 recrutements sont réalisés et que les impacts attendus sont atteints, le forfait maximum est de <strong>40&nbsp;000&nbsp;€&nbsp;HT</strong>.</li>
      <li>Si le nombre de recrutements ou les priorités évoluent, le périmètre et les objectifs sont réajustés ensemble lors des points de suivi.</li>
    </ul>
    <blockquote class="ex-quote">Le forfait est construit autour du dispositif mis en place, des recrutements réalisés et des impacts obtenus — pas autour d'un nombre de jours à consommer.</blockquote>
  </div>
  <p class="ex-disclaimer"><strong>Exemple fictif, montants indicatifs. Chaque forfait est construit au cas par cas selon le contexte, les objectifs et le périmètre de l'intervention.</strong></p>
</div>"""


# ---------------- RPO Impact ----------------
SIGNATURE = "Un dispositif de recrutement en immersion, orienté résultats et conçu pour laisser une capacité durable."

def _dim(n, verb, name, promise, intro, items, extra="", key=False, lead_in=""):
    lis = "".join(f"<li>{x}</li>" for x in items)
    cls = "card dim dim-key" if key else "card dim"
    li_intro = f'<p class="dim-listhead">{lead_in}</p>' if lead_in else ""
    return f"""<article class="{cls}">
  <div class="dim-top"><span class="dim-num">{n}</span><span class="dim-verb">{verb}</span></div>
  <h3>{name}</h3>
  <p class="dim-title">{promise}</p>
  <p class="dim-intro">{intro}</p>
  {li_intro}<ul>{lis}</ul>
  {extra}
</article>"""

SCORECARD = """<figure class="scorecard" aria-label="Exemple de scorecard de poste">
  <figcaption><span>Scorecard du poste</span><span class="sc-ex">Exemple</span></figcaption>
  <dl>
    <div><dt>Mission</dt><dd>Construire et faire grandir l'équipe data</dd></div>
    <div><dt>Résultats attendus</dt><dd><span class="sc-tag">Pipeline fiable</span><span class="sc-tag">Équipe autonome</span></dd></div>
    <div><dt>Critères clés</dt><dd><span class="sc-tag">Expertise</span><span class="sc-tag">Leadership</span><span class="sc-tag">Contexte scale-up</span></dd></div>
    <div><dt>Points de vigilance</dt><dd><span class="sc-tag sc-warn">Niveau d'autonomie</span><span class="sc-tag sc-warn">Capacité de transmission</span></dd></div>
  </dl>
</figure>"""

DIMENSIONS = '<div class="dims">\n' + "\n".join([
  _dim("01", "Comprendre", "Immersion", "Comprendre ce qu'il faut réussir avant de chercher.",
       "L'intervention commence par une immersion au sein de vos équipes et dans votre environnement de travail.",
       ["La mission réelle du poste", "Les résultats attendus à 6 ou 12 mois", "Les critères indispensables", "Les signaux qui permettront de reconnaître le bon profil", "Les points de vigilance liés au contexte"],
       extra=SCORECARD, lead_in="La scorecard du poste permet de clarifier&nbsp;:"),
  _dim("02", "Recruter", "Delivery", "Faire avancer les bons profils.",
       "Les recrutements avancent dès le début de la mission, avec un sourcing augmenté par l'IA et un suivi humain à chaque étape.",
       ["Sourcing et chasse ciblés", "Qualification et matching", "Coordination avec les managers", "Suivi candidat et closing"],
       extra='<p class="dim-note">L\'IA accélère la recherche et l\'analyse. Les décisions restent humaines.</p>'),
  _dim("03", "Décider", "Build", "Un process qui aide à décider.",
       "Le process est amélioré sur le terrain, au contact des recrutements réels.",
       ["Scorecards de poste et de candidature partagées", "Critères de décision clairs et observables", "Rôles et rituels de décision", "Suivi du pipeline, des délais et des conversions", "Expérience candidat et accompagnement des managers"]),
  _dim("04", "Transmettre", "Ancrage", "Ce qui reste après la mission.",
       "À la fin de la mission, votre équipe conserve une capacité durable à recruter.",
       ["Outils et pratiques transmis", "Scorecards, rituels et documentation réutilisables", "Autonomie progressive des managers", "Process réutilisable après la mission", "Bilan d'impact et recommandations pour la suite"],
       extra='<p class="dim-capacity"><strong>Une capacité qui reste.</strong> Votre équipe dispose d\'un process, d\'outils et de critères de décision qu\'elle peut continuer à utiliser.</p>', key=True),
]) + "\n</div>"

FLOW = """<ol class="flow" aria-label="Le fil conducteur du RPO Impact">
  <li>Comprendre</li><li>Recruter</li><li>Décider</li><li>Transmettre</li>
</ol>"""

STACK = """<div class="stack">
  <div class="stack-head">
    <span class="kicker">Une stack augmentée par l'IA</span>
    <h3>Des outils au service de la méthode</h3>
    <p>Les outils accélèrent la recherche, l'analyse, la rédaction et la transmission. Le jugement, la relation et la décision restent humains.</p>
  </div>
  <ul class="stack-tools">
    <li><strong>Dust</strong><span>Rechercher, contextualiser, structurer</span></li>
    <li><strong>Claude</strong><span>Analyser, synthétiser, challenger</span></li>
    <li><strong>ChatGPT</strong><span>Explorer, rédiger, prototyper</span></li>
    <li><strong>VSCode</strong><span>Automatiser, connecter, outiller</span></li>
  </ul>
  <p class="stack-foot">L'IA accélère le travail. Elle ne remplace ni la compréhension du contexte, ni la qualité du jugement.</p>
</div>"""

DIMENSIONS_SHORT = """<div class="dims dims-short">
  <div class="card dim"><div class="dim-top"><span class="dim-num">01</span><span class="dim-verb">Comprendre</span></div><h3>Immersion</h3><p>Comprendre ce qu'il faut réussir avant de chercher, au sein de vos équipes.</p></div>
  <div class="card dim"><div class="dim-top"><span class="dim-num">02</span><span class="dim-verb">Recruter</span></div><h3>Delivery</h3><p>Faire avancer les bons profils dès le début, avec un sourcing augmenté par l'IA.</p></div>
  <div class="card dim"><div class="dim-top"><span class="dim-num">03</span><span class="dim-verb">Décider</span></div><h3>Build</h3><p>Un process qui aide à décider&nbsp;: scorecards, critères clairs, rituels.</p></div>
  <div class="card dim dim-key"><div class="dim-top"><span class="dim-num">04</span><span class="dim-verb">Transmettre</span></div><h3>Ancrage</h3><p>Ce qui reste après la mission&nbsp;: une capacité durable à recruter.</p></div>
</div>"""

CHANGE = """<div class="change">
  <div class="change-item"><span class="dim-num">01</span><strong>Recrutements réalisés</strong><p>Les postes prioritaires sont pourvus, au niveau d'exigence défini ensemble.</p></div>
  <div class="change-item"><span class="dim-num">02</span><strong>Managers moins sollicités</strong><p>Ils interviennent là où leur regard compte, plutôt qu'à chaque étape.</p></div>
  <div class="change-item"><span class="dim-num">03</span><strong>Process réutilisable par l'équipe</strong><p>Outils, pratiques et rituels restent en place après la mission.</p></div>
</div>
<p class="note">Selon les objectifs définis ensemble, l'impact peut aussi porter sur la vitesse d'avancement des processus, la qualité du pipe candidat, la qualité des décisions d'entretien ou l'autonomie de l'équipe.</p>"""

BILAN = """<div class="bilan" id="bilan">
  <div class="bilan-main">
    <span class="kicker">Fin de mission</span>
    <h3>Le bilan d'impact</h3>
    <p>Chaque mission se termine par un bilan d'impact partagé&nbsp;: ce qui a été recruté, ce qui a été amélioré, ce qui a été transmis et ce que l'équipe peut désormais continuer à faire seule.</p>
  </div>
  <ul class="bilan-list">
    <li>Les objectifs définis au démarrage</li>
    <li>Les recrutements réalisés</li>
    <li>Les améliorations apportées</li>
    <li>Les outils transmis</li>
    <li>Les indicateurs observés</li>
    <li>Les prochaines recommandations</li>
  </ul>
</div>"""
