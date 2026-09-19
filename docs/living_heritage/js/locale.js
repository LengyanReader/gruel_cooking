// Living Cultural Corridors — locale helper (server-side cookie switch).
(function () {
  var lang = document.documentElement.getAttribute("lang") || "en";
  document.body.classList.add("lang-" + lang);

  document.querySelectorAll(".lang-toggle form").forEach(function (form) {
    form.addEventListener("submit", function () { return true; });
  });
})();