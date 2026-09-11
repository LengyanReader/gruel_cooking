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

  // ── Reading tide: a thin water-line just under the nav shows
  //    how far along the reader has travelled down the page.
  var tide = document.querySelector(".tide i");
  if (tide) {
    var onScroll = function () {
      var doc = document.documentElement;
      var max = doc.scrollHeight - window.innerHeight;
      var pct = max > 0 ? (window.scrollY / max) * 100 : 0;
      tide.style.width = pct + "%";
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  // ── Chapter scrollspy: build a floating table of contents from
  //    page sections (section-block with an id), highlight the one
  //    currently in view — like the book's own margin notes.
  var blocks = document.querySelectorAll(".section-block[id]");
  if (blocks.length >= 2) {
    var nav = document.createElement("nav");
    nav.className = "chapters";
    nav.setAttribute("aria-label", "In this chapter");
    var title = document.createElement("h4");
    title.textContent = document.documentElement.lang === "zh" ? "本页章节" : "In this chapter";
    nav.appendChild(title);

    var offsets = [];
    blocks.forEach(function (block) {
      var key = block.id;
      var labelEl = block.querySelector(".section-block-title");
      var label = labelEl ? labelEl.textContent.trim() : key;
      var a = document.createElement("a");
      a.href = "#" + key;
      a.textContent = label;
      a.dataset.target = key;
      nav.appendChild(a);
      offsets.push({ key: key, el: block, link: a });
    });
    document.body.appendChild(nav);

    var navVisible = false;
    var spy = function () {
      var half = window.innerHeight * 0.55;
      var current = null;
      offsets.forEach(function (o) {
        var top = o.el.getBoundingClientRect().top;
        if (top <= half) current = o;
      });
      offsets.forEach(function (o) {
        var on = o === current;
        o.link.classList.toggle("is-active", on);
        if (on && !reduce) {
          nav.style.setProperty("--scroll-top", o.link.offsetTop + "px");
        }
      });
      var show = window.scrollY > 260;
      if (show !== navVisible) {
        navVisible = show;
        nav.classList.toggle("is-visible", show);
      }
    };
    window.addEventListener("scroll", spy, { passive: true });
    spy();
  }

  // ── Boat back-to-top: slip upstream again.
  var boat = document.querySelector(".js-boat-top");
  if (boat) {
    var onBoatScroll = function () {
      boat.classList.toggle("is-visible", window.scrollY > 520);
    };
    window.addEventListener("scroll", onBoatScroll, { passive: true });
    onBoatScroll();
    boat.addEventListener("click", function () {
      var behavior = reduce ? "auto" : "smooth";
      window.scrollTo({ top: 0, behavior: behavior });
    });
  }
})();