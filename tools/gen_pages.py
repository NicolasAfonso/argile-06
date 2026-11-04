# Génère les pages statiques d'Argile 06 dans ~/argiles-info
import os
OUT = os.path.expanduser('~/argiles-info')
NOM = 'Argile 06'
CONTACT = 'contact@exemple.fr'  # À REMPLACER avant publication

PAGES = [
    ('index.html', 'Accueil'),
    ('comprendre.html', 'Comprendre'),
    ('vence.html', 'Vence et Alpes-Maritimes'),
    ('mon-adresse.html', 'Mon adresse'),
    ('demarche.html', 'Démarche CatNat'),
    ('recours.html', 'Refus et recours'),
    ('se-faire-entendre.html', 'Se faire entendre'),
    ('experts.html', 'Trouver un expert'),
    ('entraide.html', 'Entraide et ressources'),
]

LOGO = '''<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="8" fill="#a8512f"/><path d="M4 14h24v14H4z" fill="#d49a3f"/><path d="M4 14l8 0 3 5 3-4 3 6 7-7" stroke="#fbf7f0" stroke-width="2" fill="none" stroke-linejoin="round"/><path d="M8 13l8-7 8 7" stroke="#fbf7f0" stroke-width="2" fill="none"/></svg>'''

SOL_SVG = '''<svg viewBox="0 0 520 360" role="img" aria-label="Schéma d’une maison sur un sol argileux : à gauche, sol sec et rétracté avec fissure ; à droite, sol humide qui gonfle.">
<rect width="520" height="360" fill="#f4ecdf"/>
<circle cx="440" cy="50" r="26" fill="#d49a3f"/>
<g stroke="#d49a3f" stroke-width="3" stroke-linecap="round"><path d="M440 8v-6M440 98v6M398 50h-6M488 50h6M410 20l-4-4M470 80l4 4M410 80l-4 4M470 20l4-4"/></g>
<rect x="0" y="170" width="520" height="190" fill="#c98a5b"/>
<rect x="0" y="170" width="520" height="22" fill="#6f8466"/>
<path d="M0 260c60-10 110 8 170 0s120 10 180 0 110 6 170-4v104H0z" fill="#a8512f"/>
<path d="M0 320c70-8 130 6 200 0s130 8 200 0 80 4 120-2v42H0z" fill="#7d3a20"/>
<g fill="#fbf7f0" stroke="#3a2a20" stroke-width="3" stroke-linejoin="round">
<path d="M70 170V105l75-55 75 55v65z"/></g>
<rect x="125" y="130" width="40" height="40" fill="#e3eadc" stroke="#3a2a20" stroke-width="3"/>
<path d="M92 112l16 22-10 14 12 22" stroke="#7a2b12" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M200 192l-14 40 16 30-12 38" stroke="#3a2a20" stroke-width="4" fill="none" stroke-linecap="round"/>
<path d="M40 192l-6 18 8 14" stroke="#3a2a20" stroke-width="3" fill="none" stroke-linecap="round"/>
<g fill="#7aa6c9" opacity=".9"><path d="M340 20q10 16 0 24t-10-8q0-8 10-16z"/><path d="M380 70q8 14 0 20t-8-6q0-6 8-14z"/><path d="M320 80q8 14 0 20t-8-6q0-6 8-14z"/></g>
<path d="M300 170c0-18 20-30 38-30s38 12 38 30" fill="#fbf7f0" stroke="#3a2a20" stroke-width="3"/>
<g stroke="#7aa6c9" stroke-width="3" stroke-linecap="round"><path d="M300 215v40M340 205v50M380 215v40"/></g>
<text x="14" y="352" font-size="15" fill="#fbf7f0" font-family="sans-serif">Sec : l’argile se rétracte</text>
<text x="300" y="352" font-size="15" fill="#fbf7f0" font-family="sans-serif">Humide : elle gonfle</text>
</svg>'''


def head(title, desc, fname):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · {NOM}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#a8512f">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="site">
<div class="bar">
<a class="brand" href="index.html">{LOGO}<span>{NOM}</span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav-main">Menu</button>
<nav class="main" id="nav-main" aria-label="Navigation principale"><ul>
''' + ''.join(
        '<li><a href="%s"%s>%s</a></li>\n' % (f, ' aria-current="page"' if f == fname else '', n)
        for f, n in PAGES[1:]) + '''</ul></nav>
</div>
</header>
<main id="contenu">
'''


def foot():
    return f'''</main>
<footer class="site">
<div class="wrap">
<div class="cols">
<div><h2>{NOM}</h2><p>Un site d’information indépendant et bénévole sur le retrait-gonflement des argiles, pour les habitants de Vence et des Alpes-Maritimes.</p></div>
<div><h2>Sources officielles</h2><ul>
<li><a href="https://www.georisques.gouv.fr/risques/retrait-gonflement-des-argiles" rel="noopener">Géorisques – argiles</a></li>
<li><a href="https://www.service-public.fr/particuliers/recherche?keyword=catastrophe%20naturelle" rel="noopener">service-public.fr – catastrophe naturelle</a></li>
<li><a href="https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006073984" rel="noopener">Légifrance – Code des assurances (art. L125-1)</a></li>
</ul></div>
<div><h2>Nous contacter</h2><p><a href="mailto:{CONTACT}">{CONTACT}</a></p><p><a href="entraide.html#mentions">Mentions et avertissement</a></p></div>
</div>
<small>Information générale, non contractuelle, qui ne constitue pas un conseil juridique personnalisé. Vérifiez votre situation auprès de la préfecture, de votre assureur ou d’un professionnel.</small>
</div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
'''


def page(fname, title, sub, body, desc):
    html = head(title, desc, fname)
    html += f'''<div class="pagehead"><div class="wrap narrow">
<div class="crumbs"><a href="index.html">Accueil</a> › {title}</div>
<h1>{title}</h1><p>{sub}</p></div></div>
<div class="wrap narrow">
{body}
</div>
''' + foot()
    open(os.path.join(OUT, fname), 'w', encoding='utf-8').write(html)


V = '<span class="verify">à vérifier</span>'
AVERT = '<div class="warn"><strong>Information générale.</strong> Cette page ne remplace pas un conseil personnalisé. Vérifiez votre situation auprès de la préfecture, de votre assureur ou d’un professionnel (expert, avocat).</div>'

# ---------- Accueil ----------
home = head('Fissures, argile et sécheresse : vous n’êtes pas seul', 'Comprendre le retrait-gonflement des argiles, vérifier votre adresse et connaître la démarche catastrophe naturelle à Vence et dans les Alpes-Maritimes.', 'index.html')
home += f'''<section class="hero"><div class="wrap grid">
<div>
<span class="kicker">Vence · Alpes-Maritimes</span>
<h1>Des fissures dans votre maison ? Vous n’êtes pas seul.</h1>
<p class="lead">Sécheresses, pluies violentes : les sols argileux se rétractent puis gonflent, et des maisons se fissurent. Ici, on explique calmement, étape par étape, ce qui se passe et ce que vous pouvez faire.</p>
<div class="btns"><a class="btn" href="mon-adresse.html">Vérifier mon adresse</a><a class="btn sec" href="comprendre.html">Comprendre le phénomène</a></div>
</div>
<div>{SOL_SVG}</div>
</div></section>
<div class="wrap">
<h2>Trois façons de commencer</h2>
<div class="cards">
<div class="card"><div class="ico" aria-hidden="true">🔎</div><h3>Comprendre</h3><p>Pourquoi les sols argileux bougent, quelles fissures surveiller, ce qui est sérieux ou non.</p><a class="more" href="comprendre.html">Lire l’explication →</a></div>
<div class="card"><div class="ico" aria-hidden="true">📍</div><h3>Vérifier</h3><p>Saisissez votre adresse : le niveau d’exposition officiel (Géorisques) s’affiche. Rien n’est enregistré.</p><a class="more" href="mon-adresse.html">Tester mon adresse →</a></div>
<div class="card"><div class="ico" aria-hidden="true">🧭</div><h3>Agir</h3><p>La démarche « catastrophe naturelle » pas à pas, avec les délais, puis les recours en cas de refus.</p><a class="more" href="demarche.html">Suivre les étapes →</a></div>
</div>
<div class="note"><strong>Un mot pour vous.</strong> Découvrir des fissures angoisse, surtout quand on a mis des années à acheter sa maison. C’est un problème fréquent, souvent lent, et des solutions existent. Prenez le temps : on avance une étape à la fois.</div>
</div>
<section class="band"><div class="wrap">
<h2 style="margin-top:0">Ici, à Vence</h2>
<p>Vence est classée en exposition <strong>forte</strong> pour une grande partie de son territoire selon la cartographie nationale. Nous suivons les arrêtés de reconnaissance publiés et nous aidons les habitants à se faire entendre, ensemble.</p>
<div class="btns"><a class="btn" href="vence.html">Voir la situation locale</a><a class="btn sec" href="se-faire-entendre.html">Se faire entendre</a><a class="btn sec" href="entraide.html">Partager son expérience</a></div>
</div></section>
<div class="wrap"><div class="warn" style="margin-top:2rem"><strong>À savoir :</strong> ce site est un outil d’information indépendant. Il ne donne pas de conseil juridique personnalisé. Pour votre dossier, rapprochez-vous de la préfecture, de votre assureur ou d’un professionnel.</div></div>
''' + foot()
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(home)

# ---------- Comprendre ----------
page('comprendre.html', 'Comprendre le phénomène', 'Le retrait-gonflement des argiles, expliqué simplement.', f'''
<h2>Ce qui se passe sous la maison</h2>
<p>Certains sols contiennent beaucoup d’argile. L’argile est comme une éponge : <strong>elle gonfle quand elle est humide et se rétracte quand elle sèche</strong>. Sous une maison, le sol ne bouge pas partout de la même façon (près des arbres, sous les zones ensoleillées, près d’un angle). Les fondations suivent ces mouvements <em>inégaux</em>, et les murs se fissurent.</p>
<div class="card" style="padding:0;overflow:hidden">{SOL_SVG}</div>
<h2>Pourquoi cela concerne de plus en plus de monde</h2>
<ul>
<li><strong>Des étés plus secs et plus chauds</strong> font se rétracter les sols en profondeur.</li>
<li><strong>Des pluies plus violentes</strong> (épisodes méditerranéens, dits « cévenols ») réhydratent brutalement le sol : il gonfle vite, et ces va-et-vient fatiguent les fondations.</li>
<li>Les maisons individuelles aux fondations peu profondes sont les plus exposées.</li>
</ul>
<h2>Quelles fissures surveiller ?</h2>
<div class="cards">
<div class="card"><h3>À surveiller</h3><p>Fissures en <strong>escalier</strong> ou obliques, qui s’élargissent, qui traversent le mur de part en part, ou apparaissent autour des portes et fenêtres.</p></div>
<div class="card"><h3>Souvent bénignes</h3><p>Très fines fissures d’enduit (« faïençage »), stables, sans élargissement. Mais notez-les : une photo datée aide.</p></div>
</div>
<div class="note"><strong>Bon réflexe :</strong> photographiez chaque fissure avec un mètre ou une règle à côté, avec la date. Notez ce qui change au fil des semaines. Ce suivi vous servira pour l’assureur et l’expert.</div>
<h2>Que faire à court terme ?</h2>
<ol>
<li>Ne paniquez pas : l’évolution est souvent lente.</li>
<li>Documentez (photos datées, plan simple de la maison, dates des étés secs).</li>
<li>Vérifiez l’exposition de votre adresse : <a href="mon-adresse.html">outil Géorisques</a>.</li>
<li>Déclarez le sinistre à votre assureur dans les délais : <a href="demarche.html">voir la démarche</a>.</li>
<li>Évitez de reboucher les fissures sans avis : cela masque l’évolution.</li>
</ol>
<h2>Prévenir quand on construit ou on achète</h2>
<p>Depuis la loi ELAN (2018), dans les zones d’exposition <strong>moyenne ou forte</strong>, une étude géotechnique est obligatoire pour vendre un terrain constructible et avant de construire. Renseignez-vous auprès de votre mairie et d’un bureau d’études.</p>
<h2>Sources officielles</h2>
<ul>
<li><a href="https://www.georisques.gouv.fr/risques/retrait-gonflement-des-argiles" rel="noopener">Géorisques : dossier retrait-gonflement des argiles</a></li>
<li><a href="https://www.service-public.fr/particuliers/recherche?keyword=catastrophe%20naturelle" rel="noopener">service-public.fr : recherche « catastrophe naturelle »</a></li>
</ul>
{AVERT}
''', 'Comprendre pourquoi les sols argileux gonflent et se rétractent, et comment reconnaître les fissures liées à la sécheresse.')

# ---------- Vence ----------
page('vence.html', 'Vence et Alpes-Maritimes', 'La situation locale, avec des données publiques.', f'''
<h2>Un territoire en exposition forte</h2>
<p>Une grande partie de Vence est classée en aléa fort pour le retrait-gonflement des argiles dans la cartographie nationale. C’est pourquoi nous avons commencé ici. Vérifiez votre propre adresse avec <a href="mon-adresse.html">l’outil dédié</a>.</p>
<h2>Les arrêtés « sécheresse » déjà publiés pour Vence</h2>
<p>La liste ci-dessous provient de la base publique GASPAR (Géorisques).</p>
<div id="arretes-secheresse" data-insee="06157"><p>Chargement…</p></div>
<h2>Demande en cours de la commune</h2>
<p>La commune de Vence a déposé une demande de reconnaissance de l’état de catastrophe naturelle pour la sécheresse. {V} <small>Information à confirmer auprès de la mairie ou de la préfecture : l’état d’avancement n’est pas publié ici.</small></p>
<div class="note">Une demande déposée n’est pas une reconnaissance. Le dossier est instruit par la préfecture puis examiné par une commission interministérielle, qui peut reconnaître, refuser ou ajourner.</div>
<h2>À qui s’adresser</h2>
<div class="cards">
<div class="card"><h3>Mairie de Vence</h3><p>Pour déposer vos constatations (photos, courrier) : la commune les joint au dossier. Demandez le service compétent (risques, urbanisme).</p></div>
<div class="card"><h3>Préfecture des Alpes-Maritimes</h3><p>Instruit les demandes communales. C’est elle qui notifie la décision au maire.</p></div>
<div class="card"><h3>Votre assureur</h3><p>À prévenir dès que vous constatez des désordres. Voir la <a href="demarche.html">démarche</a>.</p></div>
</div>
<p><small>Coordonnées exactes : consultez les sites officiels de la commune et de la préfecture (non reproduits ici pour éviter toute erreur).</small></p>
<h2>Sources</h2>
<ul><li><a href="https://www.georisques.gouv.fr/risques/catastrophes-naturelles" rel="noopener">Géorisques : catastrophes naturelles</a></li><li><a href="https://www.legifrance.gouv.fr/" rel="noopener">Légifrance : arrêtés publiés au Journal officiel</a></li></ul>
{AVERT}
''', 'Exposition aux argiles, arrêtés de catastrophe naturelle sécheresse et contacts utiles à Vence et dans les Alpes-Maritimes.')

# ---------- Mon adresse ----------
page('mon-adresse.html', 'Vérifier mon adresse', 'Le niveau d’exposition officiel pour votre terrain.', f'''
<div class="tool">
<form id="adresse-form" novalidate>
<label for="adresse">Votre adresse</label>
<div class="row"><input type="text" id="adresse" name="adresse" autocomplete="off" placeholder="ex. 12 avenue Henri Isnard, 06140 Vence"><button class="btn" type="submit">Vérifier</button></div>
</form>
<div class="result" id="adresse-resultat" aria-live="polite"></div>
</div>
<div class="note"><strong>Confidentialité :</strong> votre adresse est envoyée directement de votre navigateur aux services publics (géocodage de l’IGN et Géorisques). Ce site n’a pas de serveur et n’enregistre rien.</div>
<h2>Comment lire le résultat</h2>
<ul>
<li><strong>Exposition forte ou moyenne</strong> : sols argileux sensibles. Ce n’est pas un diagnostic de votre maison.</li>
<li><strong>Exposition faible</strong> : sensibilité moindre, mais pas de garantie.</li>
<li>La carte nationale est à petite échelle : seule une <strong>étude de sol</strong> (géotechnique) dit ce qu’il y a sous <em>votre</em> maison.</li>
</ul>
<p><a href="https://www.georisques.gouv.fr/cartes-interactives" rel="noopener">Carte interactive officielle (Géorisques)</a> · <a href="comprendre.html">Comprendre le phénomène</a></p>
{AVERT}
''', 'Entrez votre adresse pour connaître le niveau d’exposition au retrait-gonflement des argiles selon Géorisques.')

# ---------- Démarche ----------
page('demarche.html', 'La démarche catastrophe naturelle', 'Pas à pas, avec les délais à retenir.', f'''
<p>Pour que les dégâts liés à la sécheresse soient indemnisés au titre de la garantie « catastrophe naturelle », un <strong>arrêté interministériel</strong> doit reconnaître l’état de catastrophe naturelle pour votre commune et la période concernée (code des assurances, <a href="https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006073984" rel="noopener">article L.125-1</a>).</p>
<ol class="steps">
<li><h3>Constater et documenter</h3><p>Photos datées, mètre ou règle à côté, plan des fissures, évolution dans le temps. Conservez tout (courriels, devis).</p></li>
<li><h3>Informer la mairie</h3><p>Déposez un courrier avec photos : la commune les joint à sa demande de reconnaissance.</p></li>
<li><h3>La commune demande la reconnaissance</h3><p>Le maire dépose la demande à la préfecture, dans un délai réglementaire après l’événement. {V}</p></li>
<li><h3>Examen par la commission interministérielle</h3><p>Elle rend un avis motivé : reconnaissance, <strong>refus</strong> ou <strong>ajournement</strong> (dossier reporté pour complément).</p></li>
<li><h3>L’arrêté est publié au Journal officiel</h3><p>Depuis la loi du 28 décembre 2021, il indique pour chaque commune la décision motivée ; les refus figurent en annexe. La préfecture notifie la décision au maire.</p></li>
<li><h3>Déclarer le sinistre à l’assureur</h3><p><span class="delai">30 jours après publication au JO</span> {V}<br>Par lettre recommandée ou en ligne, avec vos photos. Vous pouvez aussi prévenir l’assureur plus tôt : n’attendez pas.</p></li>
<li><h3>Expertise et indemnisation</h3><p>L’assureur mandate un expert. Vous pouvez faire vérifier le rapport par votre propre expert. Le code des assurances encadre les délais d’indemnisation. {V}</p></li>
</ol>
<div class="warn"><strong>Points d’attention.</strong> La franchise légale et les délais d’indemnisation évoluent : vérifiez-les dans votre contrat et dans le texte en vigueur sur Légifrance. Le délai de 30 jours court à compter de la publication, pas de la découverte des fissures.</div>
<h2>Sources</h2>
<ul>
<li><a href="https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006073984" rel="noopener">Légifrance : Code des assurances (articles L.125-1 et suivants)</a></li>
<li><a href="https://www.service-public.fr/particuliers/recherche?keyword=catastrophe%20naturelle" rel="noopener">service-public.fr : catastrophe naturelle</a></li>
<li><a href="https://www.georisques.gouv.fr/risques/catastrophes-naturelles" rel="noopener">Géorisques : catastrophes naturelles</a></li>
</ul>
{AVERT}
''', 'La démarche catastrophe naturelle sécheresse pas à pas : arrêté, délais de déclaration, expertise, indemnisation.')

# ---------- Recours ----------
page('recours.html', 'Refus ou ajournement : que faire ?', 'Un refus n’est pas toujours définitif. Voici les pistes.', f'''
<div class="note">Respirez : un refus ou un ajournement n’est pas la fin du chemin. Il existe des suites possibles, mais <strong>les délais sont courts</strong>.</div>
<h2>1. Lire la décision</h2>
<p>L’arrêté publié au Journal officiel (sur Légifrance) mentionne, depuis la loi du 28 décembre 2021, la décision motivée pour chaque commune. Les refus figurent en <strong>annexe II</strong>. La préfecture notifie la décision au maire : demandez-lui la copie et les motifs.</p>
<h2>2. Comprendre la différence</h2>
<div class="cards">
<div class="card"><h3>Refus</h3><p>La commission estime que les critères ne sont pas remplis. Le motif est écrit.</p></div>
<div class="card"><h3>Ajournement</h3><p>Le dossier est repoussé, souvent faute d’éléments. Il peut être réexaminé : ce n’est pas un refus.</p></div>
</div>
<h2>3. Les voies possibles</h2>
<ul>
<li><strong>Recours gracieux ou hiérarchique</strong> auprès de l’administration, par la commune. {V}</li>
<li><strong>Recours devant le tribunal administratif</strong> : <span class="delai">environ 2 mois</span> à compter de la publication ou de la notification. {V} <small>Les sources divergent sur le point de départ : vérifiez-le sans attendre.</small></li>
<li><strong>Nouvelle demande ou réexamen</strong> avec de nouvelles pièces (études, constats), selon les cas. {V}</li>
<li>Se renseigner sur les <strong>garanties de votre contrat</strong> hors CatNat (par exemple dommages aux biens) : un professionnel peut vous orienter.</li>
</ul>
<div class="warn"><strong>Qui peut agir ?</strong> Ce sont d’abord la commune et son maire qui sont destinataires de la décision. Un particulier peut aussi, dans certains cas, saisir le tribunal. Demandez conseil à un avocat ou à une association de sinistrés avant d’engager une procédure.</div>
<h2>Rassembler les pièces utiles</h2>
<ul><li>Photos datées et suivi des fissures</li><li>Rapport d’expert ou étude géotechnique</li><li>Copie de l’arrêté et de la décision motivée</li><li>Courriers échangés avec la mairie et l’assureur</li></ul>
<p>Voir aussi <a href="se-faire-entendre.html">Se faire entendre</a> et <a href="experts.html">Trouver un expert</a>.</p>
{AVERT}
''', 'Que faire en cas de refus ou d’ajournement d’une reconnaissance de catastrophe naturelle sécheresse ? Recours et délais à vérifier.')

# ---------- Se faire entendre ----------
page('se-faire-entendre.html', 'Se faire entendre', 'Seul, on est vite découragé. Ensemble, un dossier pèse davantage.', f'''
<h2>Pourquoi se regrouper</h2>
<p>La reconnaissance repose sur un dossier communal : plus il est documenté, plus il est solide. Des constats précis, venant de plusieurs quartiers, aident la commune à expliquer l’ampleur du phénomène.</p>
<h2>Ce que vous pouvez faire</h2>
<ol>
<li><strong>Écrire à la mairie</strong> avec vos constats (photos, dates, adresse, nature des désordres).</li>
<li><strong>Parler à vos voisins</strong> : des fissures sur plusieurs maisons voisines sont un indice utile.</li>
<li><strong>Demander un rendez-vous</strong> à l’élu chargé des risques ou de l’urbanisme.</li>
<li><strong>Vous rapprocher d’une association</strong> de sinistrés ou de défense des assurés.</li>
<li><strong>Suivre le dossier</strong> : demandez à la mairie où il en est.</li>
</ol>
<h2>Trame de courrier à adapter</h2>
<div class="card"><p><small>Remplacez les passages entre crochets. Ne mettez pas de données personnelles dans un message public.</small></p>
<p>Objet : Désordres sur mon habitation liés à la sécheresse – demande de prise en compte dans le dossier de reconnaissance</p>
<p>Madame, Monsieur le Maire,</p>
<p>Propriétaire de la maison située [adresse], j’ai constaté depuis [date] des fissures [description]. Vous trouverez ci-joint des photos datées. Je vous remercie de bien vouloir les joindre au dossier de demande de reconnaissance de l’état de catastrophe naturelle, et de m’indiquer les suites données.</p>
<p>Dans l’attente, je vous prie d’agréer, Madame, Monsieur le Maire, l’expression de mes respectueuses salutations.</p></div>
<div class="warn"><strong>Respect et sérénité.</strong> Restez factuel et courtois : les agents et élus ne décident pas seuls, et un dossier clair est plus efficace qu’une confrontation.</div>
<p>Voir aussi <a href="recours.html">Refus et recours</a> et <a href="entraide.html">Partager son expérience</a>.</p>
{AVERT}
''', 'Comment se regrouper et se faire entendre de la mairie et des institutions face aux fissures liées à la sécheresse.')

# ---------- Experts ----------
page('experts.html', 'Trouver un expert', 'Qui peut vous aider, et comment bien choisir.', f'''
<h2>Les différents professionnels</h2>
<div class="cards">
<div class="card"><h3>Expert d’assuré</h3><p>Défend vos intérêts face à l’expert de l’assureur. Il chiffre les dégâts et peut contre-expertiser. Rémunéré souvent au pourcentage : demandez les honoraires par écrit.</p></div>
<div class="card"><h3>Bureau d’études géotechniques</h3><p>Étudie le sol (sondages) et indique les causes et les solutions de reprise (par exemple sous-œuvre ou drainage).</p></div>
<div class="card"><h3>Avocat</h3><p>Utile pour un litige ou un recours. Une consultation initiale clarifie vos options. Votre protection juridique peut en couvrir les frais.</p></div>
<div class="card"><h3>Association de sinistrés ou de consommateurs</h3><p>Conseils, retours d’expérience, parfois accompagnement.</p></div>
</div>
<h2>Les questions à poser avant de signer</h2>
<ul>
<li>Combien de dossiers sécheresse avez-vous traités, dans quelle zone ?</li>
<li>Quels sont vos honoraires, et quand sont-ils dus (au résultat, à l’heure, forfait) ?</li>
<li>Êtes-vous inscrit à un registre ou à une organisation professionnelle ? Avez-vous une assurance professionnelle ?</li>
<li>Pouvez-vous me donner une idée du calendrier ?</li>
<li>Quels documents fournissez-vous au final ?</li>
</ul>
<div class="warn"><strong>Prudence.</strong> Méfiez-vous des démarcheurs qui promettent une indemnisation garantie ou demandent un paiement avant tout travail. Comparez au moins deux devis.</div>
<h2>Annuaire local</h2>
<p>Une liste de professionnels intervenant dans les Alpes-Maritimes sera ajoutée ici après vérification (identité, références, tarifs). <em>Aucune recommandation commerciale n’est donnée sans critères publics.</em></p>
<p>Vous êtes professionnel et souhaitez figurer ? <a href="mailto:{CONTACT}">Écrivez-nous</a> avec vos références.</p>
{AVERT}
''', 'Comment choisir un expert d’assuré, un bureau d’études géotechniques ou un avocat pour un sinistre lié aux argiles.')

# ---------- Entraide ----------
page('entraide.html', 'Entraide et ressources', 'Partager, lire, s’appuyer sur les autres.', f'''
<h2>Témoignages</h2>
<p>Lire d’autres histoires aide à se sentir moins seul. Les exemples ci-dessous sont des <strong>illustrations fictives</strong> pour montrer le ton ; les vrais témoignages, modérés et anonymisés, les remplaceront.</p>
<div class="quote">« Quand la première fissure est apparue, j’ai cru que la maison était fichue. En fait, on peut avancer, une étape à la fois. »<cite>Illustration fictive</cite></div>
<div class="quote">« Ce qui m’a aidé, c’est d’avoir écrit à la mairie avec des photos, et de découvrir que des voisins avaient les mêmes fissures. »<cite>Illustration fictive</cite></div>
<h2>Partager votre expérience</h2>
<p>Écrivez-nous quelques lignes : ce que vous avez constaté, les démarches faites, ce qui vous a aidé.</p>
<p><a class="btn" href="mailto:{CONTACT}?subject=T%C3%A9moignage%20Argile%2006">Envoyer un témoignage</a></p>
<div class="note"><strong>Charte :</strong> nous relisons chaque message. Nous publions <em>sans nom, sans adresse, sans numéro de dossier</em>, après votre accord. Pas de mise en cause de personnes, pas de promesse de résultat. Vous pouvez retirer votre témoignage à tout moment.</div>
<h2>Ressources officielles</h2>
<ul>
<li><a href="https://www.georisques.gouv.fr/risques/retrait-gonflement-des-argiles" rel="noopener">Géorisques : retrait-gonflement des argiles</a></li>
<li><a href="https://www.georisques.gouv.fr/cartes-interactives" rel="noopener">Géorisques : cartes interactives</a></li>
<li><a href="https://www.service-public.fr/particuliers/recherche?keyword=catastrophe%20naturelle" rel="noopener">service-public.fr : catastrophe naturelle</a></li>
<li><a href="https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006073984" rel="noopener">Légifrance : Code des assurances, article L.125-1 et suivants</a></li>
</ul>
<h2>Questions fréquentes</h2>
<details><summary>Mes fissures sont-elles forcément dues aux argiles ?</summary><p>Non. D’autres causes existent (défaut de construction, tassement, fuite). Une expertise ou une étude de sol permet de le savoir.</p></details>
<details><summary>L’assurance paie-t-elle sans arrêté de catastrophe naturelle ?</summary><p>La garantie catastrophe naturelle suppose un arrêté. Sans lui, la prise en charge dépend d’autres garanties de votre contrat. Vérifiez auprès de votre assureur.</p></details>
<details><summary>Que faire si l’arrêté est refusé ?</summary><p>Voir <a href="recours.html">Refus et recours</a>.</p></details>
<h2 id="mentions">Mentions et avertissement</h2>
<p>Ce site est une initiative bénévole et indépendante. Il ne représente ni l’État, ni la commune, ni un assureur. Les informations sont générales, rédigées en bonne foi à partir de sources publiques et peuvent être incomplètes ou évoluer : vérifiez toujours auprès des sources officielles. Elles ne constituent pas un conseil juridique personnalisé.</p>
<p>Aucune donnée personnelle n’est collectée ni stockée par ce site. Les outils appellent directement des services publics depuis votre navigateur.</p>
<p>Contact : <a href="mailto:{CONTACT}">{CONTACT}</a></p>
''', 'Témoignages, charte, ressources officielles et questions fréquentes sur le retrait-gonflement des argiles.')
print('ok')
