// Menu mobile
(function () {
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('nav-main');
  if (!btn || !nav) return;
  btn.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
})();

var GEOCODAGE = 'https://data.geopf.fr/geocodage/search';
var GEORISQUES = 'https://georisques.gouv.fr/api/v1';

// Construit un élément : el('p', {class:'x'}, 'texte', autreNoeud). Le texte passe toujours par textContent.
function el(tag, attrs) {
  var n = document.createElement(tag);
  Object.keys(attrs || {}).forEach(function (k) { n.setAttribute(k, attrs[k]); });
  for (var i = 2; i < arguments.length; i++) {
    var c = arguments[i];
    n.appendChild(typeof c === 'string' ? document.createTextNode(c) : c);
  }
  return n;
}
function show(box) {
  while (box.firstChild) box.removeChild(box.firstChild);
  for (var i = 1; i < arguments.length; i++) box.appendChild(arguments[i]);
}
function lien(href, texte) { return el('a', { href: href, rel: 'noopener' }, texte); }

// Outil « Mon adresse » : aucune donnée n'est enregistrée ; les appels vont directement aux API publiques.
(function () {
  var form = document.getElementById('adresse-form');
  if (!form) return;
  var input = document.getElementById('adresse');
  var out = document.getElementById('adresse-resultat');
  var CARTE = 'https://www.georisques.gouv.fr/cartes-interactives';

  var classes = { '1': 'faible', '2': 'moyenne', '3': 'forte' };
  var conseils = {
    forte: 'Votre terrain est situé en zone d’exposition forte. Cela ne veut pas dire que votre maison est abîmée : cela veut dire que les sols argileux y sont sensibles. La page « Comprendre » détaille les bons réflexes.',
    moyenne: 'Votre terrain est en zone d’exposition moyenne. Surveillez l’apparition de fissures après un été sec.',
    faible: 'Votre terrain est en zone d’exposition faible. Le risque n’est pas nul, mais il est moindre.',
    nul: 'Aucun aléa significatif n’est signalé pour ce point.'
  };

  function afficher(feat) {
    var c = feat.geometry.coordinates; // [lon, lat]
    show(out, el('p', {}, 'Recherche de l’exposition pour ', el('strong', {}, feat.properties.label), '…'));
    fetch(GEORISQUES + '/rga?latlon=' + c[0] + ',' + c[1])
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (d) {
        var cl = classes[d.codeExposition] || 'nul';
        show(out,
          el('p', {}, el('strong', {}, feat.properties.label)),
          el('p', {}, el('span', { 'class': 'badge ' + cl }, d.exposition || 'Non renseigné')),
          el('p', {}, conseils[cl]),
          el('p', {}, lien(CARTE, 'Ouvrir la carte officielle Géorisques'), ' pour voir votre parcelle en détail.'),
          el('p', {}, el('small', {}, 'Information indicative, issue de l’API Géorisques (cartographie nationale de l’aléa). Elle ne remplace ni une étude de sol, ni la décision de reconnaissance de catastrophe naturelle.'))
        );
      })
      .catch(function () {
        show(out, el('p', { 'class': 'warn' }, 'Le service Géorisques ne répond pas pour le moment. Vous pouvez consulter directement ', lien(CARTE, 'la carte officielle'), '.'));
      });
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var q = input.value.trim();
    if (q.length < 5) { show(out, el('p', {}, 'Saisissez une adresse plus complète (numéro, rue, commune).')); return; }
    show(out, el('p', {}, 'Recherche de l’adresse…'));
    fetch(GEOCODAGE + '?q=' + encodeURIComponent(q) + '&limit=5')
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (d) {
        var f = d.features || [];
        if (!f.length) { show(out, el('p', {}, 'Aucune adresse trouvée. Essayez avec le code postal.')); return; }
        if (f.length === 1 || f[0].properties.score > 0.9) { afficher(f[0]); return; }
        var ul = el('ul', { 'class': 'picker' });
        f.forEach(function (feat) {
          var b = el('button', { type: 'button' }, feat.properties.label);
          b.addEventListener('click', function () { afficher(feat); });
          ul.appendChild(el('li', {}, b));
        });
        show(out, el('p', {}, 'Plusieurs adresses correspondent, choisissez la vôtre :'), ul);
      })
      .catch(function () {
        show(out, el('p', { 'class': 'warn' }, 'La recherche d’adresse est indisponible. Réessayez plus tard ou utilisez la carte officielle.'));
      });
  });
})();

// Page locale : arrêtés CatNat sécheresse déjà publiés pour la commune (code INSEE en data-attribut)
(function () {
  var box = document.getElementById('arretes-secheresse');
  if (!box) return;
  var insee = box.getAttribute('data-insee');
  function cle(s) { return s.split('/').reverse().join(''); }
  function afficherRows(rows, note) {
    rows.sort(function (a, b) { return cle(a.date_debut_evt) < cle(b.date_debut_evt) ? 1 : -1; });
    if (!rows.length) { show(box, el('p', {}, 'Aucun arrêté « sécheresse » trouvé pour cette commune dans la base GASPAR.')); return; }
    var tbody = el('tbody', {});
    rows.forEach(function (x) {
      tbody.appendChild(el('tr', {},
        el('td', {}, x.date_debut_evt + ' au ' + x.date_fin_evt),
        el('td', {}, x.date_publication_jo),
        el('td', {}, x.libelle_risque_jo)));
    });
    var table = el('table', {},
      el('thead', {}, el('tr', {}, el('th', {}, 'Période'), el('th', {}, 'Publication au JO'), el('th', {}, 'Risque'))),
      tbody);
    show(box, el('div', { 'class': 'tablewrap' }, table),
      el('p', {}, el('small', {}, 'Source : API Géorisques, base GASPAR (arrêtés de reconnaissance publiés). ' + note + ' Les refus et les dossiers en cours d’instruction n’y figurent pas.')));
  }
  function filtre(d) { return (d.data || []).filter(function (x) { return /s[ée]cheresse/i.test(x.libelle_risque_jo); }); }
  fetch(GEORISQUES + '/gaspar/catnat?code_insee=' + encodeURIComponent(insee) + '&page=1&page_size=100')
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (d) { afficherRows(filtre(d), 'Données chargées en direct.'); })
    .catch(function () {
      // Repli : copie statique de ces données publiques, datée.
      fetch('data/arretes-secheresse-' + encodeURIComponent(insee) + '.json')
        .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
        .then(function (d) { afficherRows(d.data || [], 'Copie enregistrée le ' + d.extrait_le + ' (le service en direct est indisponible).'); })
        .catch(function () {
          show(box, el('p', { 'class': 'warn' }, 'Impossible de charger la liste pour le moment. Consultez ', lien('https://www.georisques.gouv.fr/risques/catastrophes-naturelles', 'Géorisques'), ' ou ', lien('https://www.legifrance.gouv.fr/', 'Légifrance'), '.'));
        });
    });
})();
