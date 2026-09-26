/* Math Clarification — page.js
   Draft notice + share buttons for the server-rendered pages. The language
   switch is server-side (real links), so only the interactive bits live here. */
(function () {
  'use strict';

  var root = document.documentElement;
  var DRAFT_KEY = 'zh-draft-dismissed';

  /* ---------- draft notice: measure, pin, remember dismissal ---------- */
  var draft = document.getElementById('draft');
  function syncBanner() {
    root.style.setProperty('--bh', (draft && !draft.hidden ? draft.offsetHeight : 0) + 'px');
  }
  if (draft) {
    try {
      if (localStorage.getItem(DRAFT_KEY) === '1') { draft.hidden = true; }
    } catch (e) { /* storage may be blocked */ }
    var dismiss = draft.querySelector('.dismiss');
    if (dismiss) {
      dismiss.addEventListener('click', function () {
        draft.hidden = true;
        try { localStorage.setItem(DRAFT_KEY, '1'); } catch (e) { /* ignore */ }
        syncBanner();
      });
    }
    syncBanner();
    window.addEventListener('resize', syncBanner);
  }

  /* ---------- share: copy the page link ---------- */
  var here = location.href;

  function copyFallback(text, done) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); done(); } catch (e) { /* give up */ }
    document.body.removeChild(ta);
  }

  Array.prototype.forEach.call(document.querySelectorAll('.share [data-share="copy"]'), function (el) {
    // Keep the bilingual markup intact: swapping textContent would delete the
    // .p-zh/.p-en spans and freeze the button in one language after one click.
    var rest = el.innerHTML;
    el.addEventListener('click', function () {
      function ok() {
        el.innerHTML = '<span class="p-zh">' + (el.getAttribute('data-done-zh') || '已复制')
          + '</span><span class="p-en">' + (el.getAttribute('data-done-en') || 'Copied')
          + '</span>';
        el.classList.add('done');
        setTimeout(function () {
          el.innerHTML = rest;
          el.classList.remove('done');
        }, 1600);
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(here).then(ok, function () { copyFallback(here, ok); });
      } else {
        copyFallback(here, ok);
      }
    });
  });
})();
