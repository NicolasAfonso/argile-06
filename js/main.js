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
  var liste = document.getElementById('adresse-suggestions');
  var CARTE = 'https://www.georisques.gouv.fr/cartes-interactives';

  var classes = { '1': 'faible', '2': 'moyenne', '3': 'forte' };
  var conseils = {
    forte: 'Ce point est situé en zone d’exposition forte. Cela ne veut pas dire que la maison est abîmée : cela veut dire que les sols argileux y sont sensibles. La page « Comprendre » détaille les bons réflexes.',
    moyenne: 'Ce point est en zone d’exposition moyenne. Surveillez l’apparition de fissures après un été sec.',
    faible: 'Ce point est en zone d’exposition faible. Le risque n’est pas nul, mais il est moindre.',
    nul: 'Aucun aléa significatif n’est signalé pour ce point.'
  };

  // Carte Leaflet : fond IGN + couche officielle d'exposition Géorisques (WMS)
  var map = null, marker = null;
  function initCarte() {
    var box = document.getElementById('carte');
    if (!box || typeof L === 'undefined') return;
    map = L.map(box, { scrollWheelZoom: false }).setView([43.7224, 7.1118], 13);
    L.tileLayer('https://data.geopf.fr/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=GEOGRAPHICALGRIDSYSTEMS.PLANIGNV2&STYLE=normal&TILEMATRIXSET=PM&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}&FORMAT=image/png',
      { maxZoom: 18, attribution: '© IGN – Géoplateforme' }).addTo(map);
    L.tileLayer.wms('https://www.georisques.gouv.fr/services', {
      layers: 'ALEARG', format: 'image/png', transparent: true, version: '1.3.0', opacity: 0.6, maxNativeZoom: 16, maxZoom: 18,
      attribution: 'Exposition : © Géorisques / BRGM'
    }).addTo(map);
    map.on('click', function (e) {
      afficher({ label: 'Point choisi sur la carte', lon: e.latlng.lng, lat: e.latlng.lat });
    });
  }
  initCarte();

  function afficher(p) {
    if (map) {
      if (marker) map.removeLayer(marker);
      marker = L.marker([p.lat, p.lon]).addTo(map);
      if (p.zoom) map.setView([p.lat, p.lon], 15);
    }
    show(out, el('p', {}, 'Recherche de l’exposition pour ', el('strong', {}, p.label), '…'));
    fetch(GEORISQUES + '/rga?latlon=' + p.lon + ',' + p.lat)
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (d) {
        var cl = classes[d.codeExposition] || 'nul';
        if (marker) {
          marker.bindPopup(el('div', {}, el('strong', {}, p.label), el('br', {}), el('span', { 'class': 'badge ' + cl }, d.exposition || 'Non renseigné'))).openPopup();
          document.getElementById('carte').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
        show(out,
          el('p', {}, el('strong', {}, p.label)),
          el('p', {}, el('span', { 'class': 'badge ' + cl }, d.exposition || 'Non renseigné')),
          el('p', {}, conseils[cl]),
          el('p', {}, lien(CARTE, 'Ouvrir la carte officielle Géorisques'), ' pour voir la parcelle en détail.'),
          el('p', {}, el('small', {}, 'Information indicative, issue de l’API Géorisques (cartographie nationale de l’aléa). Elle ne remplace ni une étude de sol, ni la décision de reconnaissance de catastrophe naturelle.'))
        );
      })
      .catch(function () {
        show(out, el('p', { 'class': 'warn' }, 'Le service Géorisques ne répond pas pour le moment. Vous pouvez consulter directement ', lien(CARTE, 'la carte officielle'), '.'));
      });
  }

  // Autocomplétion (service de complétion de la Géoplateforme IGN)
  var suggestions = [], actif = -1, timer = null, requete = 0;
  function fermer() { liste.hidden = true; input.setAttribute('aria-expanded', 'false'); input.removeAttribute('aria-activedescendant'); actif = -1; }
  function choisir(s) {
    input.value = s.fulltext;
    fermer();
    afficher({ label: s.fulltext, lon: s.x, lat: s.y, zoom: true });
  }
  function marquer(i) {
    var items = liste.children;
    for (var k = 0; k < items.length; k++) items[k].setAttribute('aria-selected', k === i ? 'true' : 'false');
    actif = i;
    if (i >= 0) input.setAttribute('aria-activedescendant', items[i].id);
  }
  function dessiner(res) {
    suggestions = res;
    while (liste.firstChild) liste.removeChild(liste.firstChild);
    if (!res.length) { fermer(); return; }
    res.forEach(function (s, i) {
      var li = el('li', { role: 'option', id: 'sugg-' + i, 'aria-selected': 'false' }, s.fulltext);
      li.addEventListener('mousedown', function (e) { e.preventDefault(); choisir(s); });
      liste.appendChild(li);
    });
    liste.hidden = false;
    input.setAttribute('aria-expanded', 'true');
    actif = -1;
  }
  input.addEventListener('input', function () {
    clearTimeout(timer);
    var q = input.value.trim();
    if (q.length < 4) { fermer(); return; }
    timer = setTimeout(function () {
      var n = ++requete;
      fetch('https://data.geopf.fr/geocodage/completion/?type=StreetAddress&maximumResponses=6&text=' + encodeURIComponent(q))
        .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
        .then(function (d) { if (n === requete) dessiner(d.results || []); })
        .catch(function () { fermer(); });
    }, 250);
  });
  input.addEventListener('keydown', function (e) {
    if (liste.hidden) return;
    if (e.key === 'ArrowDown') { e.preventDefault(); marquer((actif + 1) % suggestions.length); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); marquer((actif - 1 + suggestions.length) % suggestions.length); }
    else if (e.key === 'Enter' && actif >= 0) { e.preventDefault(); choisir(suggestions[actif]); }
    else if (e.key === 'Escape') { fermer(); }
  });
  input.addEventListener('blur', fermer);

  // Validation manuelle (sans suggestion choisie)
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    fermer();
    var q = input.value.trim();
    if (q.length < 5) { show(out, el('p', {}, 'Saisissez une adresse plus complète (numéro, rue, commune).')); return; }
    show(out, el('p', {}, 'Recherche de l’adresse…'));
    fetch(GEOCODAGE + '?q=' + encodeURIComponent(q) + '&limit=1')
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (d) {
        var f = (d.features || [])[0];
        if (!f) { show(out, el('p', {}, 'Aucune adresse trouvée. Essayez avec le code postal.')); return; }
        afficher({ label: f.properties.label, lon: f.geometry.coordinates[0], lat: f.geometry.coordinates[1], zoom: true });
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
