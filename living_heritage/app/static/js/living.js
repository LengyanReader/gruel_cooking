// 周舟洲粥 Living Cultural Corridors — "living book" behaviours.
// Zero-dependency vanilla JS. Behaviours are progressive enhancements only:
// nothing here is required for content to be readable.
(function () {
  "use strict";

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ── Page-turn entrance: each navigation lands like turning a leaf.
  //    Applied only after first paint so the LCP (hero) is not delayed.
  //    The class is removed when the turn finishes so the persistent
  //    transform never hijacks the sticky nav's positioning context.
  if (!reduce) {
    window.addEventListener("load", function () {
      var body = document.body;
      body.classList.add("page-enter");
      var done = function () { body.classList.remove("page-enter"); body.removeEventListener("animationend", done); };
      body.addEventListener("animationend", done, { once: true });
      setTimeout(done, 1400); // safety net if animationend never fires
    });
  }

  // ── Scroll reveal: chapters surface as they come into view,
  //    as if the reader's steps reveal the next passage.
  var targets = document.querySelectorAll(".reveal");
  if (targets.length && "IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
    );
    targets.forEach(function (el) { io.observe(el); });
  } else {
    targets.forEach(function (el) { el.classList.add("is-visible"); });
  }

  // ── Locale switch: brief leaf-flip feedback before the POST redirect.
  var forms = document.querySelectorAll(".lang-toggle form");
  forms.forEach(function (form) {
    form.addEventListener("submit", function () {
      if (reduce) return; // still allow default submit
      document.body.style.transition = "opacity 0.18s ease";
      document.body.style.opacity = "0";
    });
  });
})();