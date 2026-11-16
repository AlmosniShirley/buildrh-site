/* BUILD RH — script partagé : menu mobile, confort de lecture, formulaire de contact. */
(function () {
  'use strict';

  /* ---------- menu mobile ---------- */
  var menuBtn = document.getElementById('menu-btn');
  var menu = document.getElementById('mobile-menu');
  if (menuBtn && menu) {
    var setMenu = function (open) {
      menu.hidden = !open;
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
      menuBtn.querySelector('.label').textContent = open ? 'Fermer' : 'Menu';
      document.body.classList.toggle('menu-open', open);
      if (open) { var first = menu.querySelector('a'); if (first) first.focus(); }
    };
    menuBtn.addEventListener('click', function () { setMenu(menu.hidden); });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !menu.hidden) { setMenu(false); menuBtn.focus(); }
    });
    window.addEventListener('resize', function () { if (window.innerWidth > 1020 && !menu.hidden) setMenu(false); });
  }

  /* ---------- confort de lecture (repris de l'ancien site) ---------- */
  var KEY = 'buildrh_a11y_v1';
  var state = { size: 'normal', spacing: 'normal', contrast: 'normal', motion: 'normal' };
  try {
    var raw = localStorage.getItem(KEY);
    if (raw) { var p = JSON.parse(raw); for (var k in state) if (p && p[k]) state[k] = p[k]; }
  } catch (e) {}
  function applyA11y() {
    document.documentElement.setAttribute('data-a11y-size', state.size);
    document.body.setAttribute('data-a11y-spacing', state.spacing);
    document.body.setAttribute('data-a11y-contrast', state.contrast);
    document.body.setAttribute('data-a11y-motion', state.motion);
    document.querySelectorAll('.a11y-seg').forEach(function (seg) {
      var c = seg.getAttribute('data-a11y-control');
      seg.querySelectorAll('button').forEach(function (b) {
        b.setAttribute('aria-pressed', b.getAttribute('data-value') === state[c] ? 'true' : 'false');
      });
    });
  }
  function saveA11y() { try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {} }
  applyA11y();

  var aBtn = document.getElementById('a11y-toggle');
  var aPanel = document.getElementById('a11y-panel');
  if (aBtn && aPanel) {
    var setPanel = function (open) { aPanel.hidden = !open; aBtn.setAttribute('aria-expanded', open ? 'true' : 'false'); };
    aBtn.addEventListener('click', function () { setPanel(aPanel.hidden); });
    document.getElementById('a11y-close').addEventListener('click', function () { setPanel(false); aBtn.focus(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !aPanel.hidden) { setPanel(false); aBtn.focus(); } });
    aPanel.querySelectorAll('.a11y-seg button').forEach(function (b) {
      b.addEventListener('click', function () {
        state[b.parentNode.getAttribute('data-a11y-control')] = b.getAttribute('data-value');
        applyA11y(); saveA11y();
      });
    });
    document.getElementById('a11y-reset').addEventListener('click', function () {
      state = { size: 'normal', spacing: 'normal', contrast: 'normal', motion: 'normal' };
      applyA11y(); saveA11y();
    });
  }

  /* ---------- formulaire de contact ----------
     Le site est statique (GitHub Pages) : l'envoi ouvre la messagerie du visiteur
     avec un e-mail pré-rempli. Rien n'est stocké sur le site.
     Destinataires : voir TO / CAP_CC ci-dessous. */
  var TO = 'shirley.chiche@buildrh.co';
  var CAP_CC = 'coralie@ellipse.cn.com';

  document.querySelectorAll('form[data-contact]').forEach(function (form) {
    var radios = form.querySelectorAll('input[name="parcours"]');
    var select = form.querySelector('select[name="besoin"]');
    var warning = form.querySelector('.cap-warning');
    var summary = form.querySelector('.form-error-summary');
    var done = form.parentNode.querySelector('.form-done');

    function current() {
      var r = form.querySelector('input[name="parcours"]:checked');
      return r ? r.value : '';
    }
    function syncParcours() {
      var v = current();
      if (warning) warning.hidden = v !== 'situation';
      if (select) {
        select.querySelectorAll('optgroup').forEach(function (g) {
          var match = !v || g.getAttribute('data-parcours') === v;
          g.disabled = !match;
          g.hidden = !match;
        });
        var opt = select.options[select.selectedIndex];
        if (opt && opt.parentNode.tagName === 'OPTGROUP' && opt.parentNode.disabled) select.value = '';
      }
    }

    // pré-sélection via ?besoin=recrutement|situation ou via un lien #contact-situation
    var params = new URLSearchParams(window.location.search);
    var pre = params.get('besoin');
    if (!pre && /situation/.test(window.location.hash)) pre = 'situation';
    if (!pre && /recrutement/.test(window.location.hash)) pre = 'recrutement';
    if (pre === 'recrutement' || pre === 'situation') {
      var r = form.querySelector('input[name="parcours"][value="' + pre + '"]');
      if (r) r.checked = true;
    }
    radios.forEach(function (r) { r.addEventListener('change', syncParcours); });
    syncParcours();

    // liens internes qui préselectionnent un parcours sur la même page
    document.querySelectorAll('[data-preselect]').forEach(function (a) {
      a.addEventListener('click', function () {
        var r2 = form.querySelector('input[name="parcours"][value="' + a.getAttribute('data-preselect') + '"]');
        if (r2) { r2.checked = true; syncParcours(); }
      });
    });

    function setError(field, msg) {
      var el = form.querySelector('[name="' + field + '"]');
      var err = form.querySelector('#' + form.id + '-' + field + '-err');
      if (el && el.type !== 'radio') el.setAttribute('aria-invalid', msg ? 'true' : 'false');
      if (err) err.textContent = msg || '';
    }

    function validate() {
      var errors = [];
      var data = new FormData(form);
      var checks = [
        ['parcours', !current(), 'Choisissez le type de demande.'],
        ['nom', !String(data.get('nom') || '').trim(), 'Indiquez votre prénom et votre nom.'],
        ['entreprise', !String(data.get('entreprise') || '').trim(), 'Indiquez votre entreprise.'],
        ['role', !String(data.get('role') || '').trim(), 'Indiquez votre rôle.'],
        ['email', !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(String(data.get('email') || '').trim()), 'Indiquez une adresse e-mail valide, par exemple prenom@entreprise.fr.'],
        ['besoin', !data.get('besoin'), 'Choisissez le type de besoin.'],
        ['message', String(data.get('message') || '').trim().length < 10, 'Décrivez la situation en quelques lignes.']
      ];
      checks.forEach(function (c) {
        setError(c[0], c[1] ? c[2] : '');
        if (c[1]) errors.push(c);
      });
      return errors;
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var errors = validate();
      if (errors.length) {
        summary.hidden = false;
        summary.textContent = errors.length === 1
          ? 'Un champ est à compléter : ' + errors[0][2]
          : errors.length + ' champs sont à compléter. Ils sont signalés ci-dessous.';
        var first = errors[0][0] === 'parcours'
          ? form.querySelector('input[name="parcours"]')
          : form.querySelector('[name="' + errors[0][0] + '"]');
        if (first) first.focus();
        return;
      }
      summary.hidden = true;

      var d = new FormData(form);
      var isCap = current() === 'situation';
      var subject = isCap
        ? 'CAP Bascule · Une situation à clarifier · ' + d.get('entreprise')
        : 'BUILD RH · Besoin de recrutement · ' + d.get('entreprise');
      var body = [
        'Bonjour,', '',
        'Type de demande : ' + (isCap ? 'Situation professionnelle sensible (CAP Bascule)' : 'Recrutement ou structuration (BUILD RH)'),
        'Besoin : ' + d.get('besoin'),
        'Urgence : ' + (d.get('urgence') || 'Non précisée'), '',
        'Nom : ' + d.get('nom'),
        'Entreprise : ' + d.get('entreprise'),
        'Rôle : ' + d.get('role'),
        'E-mail : ' + d.get('email'), '',
        'Situation :', String(d.get('message')).trim(), ''
      ].join('\n');

      var href = 'mailto:' + TO + '?' + (isCap ? 'cc=' + encodeURIComponent(CAP_CC) + '&' : '') +
        'subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);

      if (done) {
        var mailLink = done.querySelector('[data-mail-link]');
        if (mailLink) mailLink.href = href;
        var copyBtn = done.querySelector('[data-copy]');
        if (copyBtn) {
          copyBtn.onclick = function () {
            var txt = 'À : ' + TO + (isCap ? '\nCopie : ' + CAP_CC : '') + '\nObjet : ' + subject + '\n\n' + body;
            var ok = function () { copyBtn.textContent = 'Message copié'; };
            if (navigator.clipboard && navigator.clipboard.writeText) {
              navigator.clipboard.writeText(txt).then(ok, function () { window.prompt('Copiez le message :', txt); });
            } else { window.prompt('Copiez le message :', txt); }
          };
        }
        form.hidden = true;
        done.hidden = false;
        var h = done.querySelector('h3');
        if (h) { h.setAttribute('tabindex', '-1'); h.focus(); }
        var back = done.querySelector('[data-back]');
        if (back) back.onclick = function () { done.hidden = true; form.hidden = false; form.querySelector('input,select,textarea').focus(); };
      }
      window.location.href = href;
    });

    // effacer l'erreur dès que le champ est corrigé
    form.addEventListener('input', function (e) {
      var n = e.target.name;
      if (n && e.target.getAttribute('aria-invalid') === 'true') setError(n, '');
    });
    form.addEventListener('change', function (e) {
      if (e.target.name === 'parcours') setError('parcours', '');
      if (e.target.name === 'besoin') setError('besoin', '');
    });
  });
})();
