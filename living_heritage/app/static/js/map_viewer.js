/* Tongzhou field basemap — Leaflet viewer (vendored 1.9.4, offline-degradable).
 * Data: window.TONGZHOU_MAP (see tongzhou_map.js). Layers:
 *  basemap tiles | waterways | parks | field points | heritage grades |
 *  red-line docs (text only) | grain-trade tracer | day loop
 * Trust tiers: "osm" = OSM-verified coords (solid), "approx" = approximate
 * anchor (hollow) — never present an approx point as surveyed.
 * No boundary geometry is drawn anywhere: OSM has no WH zone polygons for
 * this area (Overpass probe 2026-09-25), so red-line info stays as text. */
(function () {
  "use strict";
  var D = window.TONGZHOU_MAP;
  var el = document.getElementById("map");
  if (!D || !el || typeof L === "undefined") return;

  var ZH = (document.documentElement.lang || "").indexOf("zh") === 0;
  function pick(o, k) { return o[k + (ZH ? "_zh" : "_en")] || o[k + (ZH ? "_en" : "_zh")] || ""; }

  /* TimeDimension (vendored) is used as the spatiotemporal time model:
   * yearly available-times + a current-time cursor that fires `timeload`.
   * The plugin is optional: if it failed to load we fall back to a plain
   * integer year so the page never breaks. */
  var CH = D.chronology || null;
  var HAS_TD = (typeof L.TimeDimension !== "undefined") && !!CH;
  var Y0 = CH ? CH.range[0] : 0, Y1 = CH ? CH.range[1] : 0;
  var mapOpts = { center: [39.887, 116.70], zoom: 12, maxZoom: 19 };
  if (HAS_TD) {
    mapOpts.timeDimension = true;
    mapOpts.timeDimensionOptions = {
      timeInterval: Y0 + "-01-01/" + Y1 + "-12-31",
      timeResolution: "P1Y", useUTC: true
    };
  }
  var map = L.map(el, mapOpts);
  var _year = Y0;
  function availTimes() { var a = []; for (var y = Y0; y <= Y1; y++) a.push(Date.UTC(y, 0, 1)); return a; }
  if (HAS_TD && map.timeDimension) {
    /* merge mode must be one of 'union'|'intersection'|'replace' (v1.1.1 throws
     * otherwise); wrap so a plugin quirk can never abort the whole viewer. */
    try {
      map.timeDimension.setAvailableTimes(availTimes(), "replace");
      map.timeDimension.setCurrentTime(Date.UTC(Y0, 0, 1));
    } catch (err) { HAS_TD = false; }
  }
  function curYear() {
    if (HAS_TD && map.timeDimension) { try { return new Date(map.timeDimension.getCurrentTime()).getUTCFullYear(); } catch (e) {} }
    return _year;
  }
  function setYear(y) {
    y = Math.max(Y0, Math.min(Y1, Math.round(y)));
    _year = y;
    if (HAS_TD && map.timeDimension) {
      try { map.timeDimension.setCurrentTime(Date.UTC(y, 0, 1)); } catch (e) {}
    }
    renderTimeline();
  }
  /* renderTimeline is filled in by the timeline module below; setYear/curYear
   * close over this shared binding so playback can drive the cursor. */
  function renderTimeline() {}


  /* ── base tiles (need network; vectors keep working offline) ── */
  var tiles = L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);
  var tileFailed = false;
  tiles.on("tileerror", function () {
    if (tileFailed) return;
    tileFailed = true;
    var b = document.getElementById("offline-banner");
    if (b) b.hidden = false;
  });

  /* ── style helpers ── */
  var WATER_COLOR = {
    "北运河": "#2f6f9f", "通惠河": "#4a8fb5", "运潮减河": "#6da8c4",
    "温榆河": "#79a6b8", "潮白河": "#5b93b0", "凉水河": "#84b3c6"
  };
  function solid(pt, color) {
    return L.circleMarker(pt, { radius: 5, color: color, fillColor: color, fillOpacity: 0.85, weight: 1.5 });
  }
  function hollow(pt, color) {
    return L.circleMarker(pt, { radius: 5.5, color: color, fillColor: "#fff", fillOpacity: 1, weight: 2, dashArray: "2,2" });
  }
  function trustMark(pt, trust, colorSolid, colorHollow) {
    return trust === "osm" ? solid(pt, colorSolid) : hollow(pt, colorHollow);
  }
  function badge(txt, cls) {
    return '<span class="map-badge ' + cls + '">' + txt + "</span>";
  }
  function popupPoi(p) {
    var h = "<strong>" + p.name + "</strong>";
    if (p.zh) h += "<br>" + p.zh;
    h += "<br>" + badge(p.trust === "osm" ? "OSM" : "approx", p.trust === "osm" ? "tier-osm" : "tier-approx");
    return h;
  }

  /* ── layer: waterways ── */
  var gWater = L.layerGroup();
  Object.keys(D.water).forEach(function (name) {
    var color = WATER_COLOR[name] || "#5b93b0";
    D.water[name].forEach(function (seg) {
      if (seg.length < 2) return;
      gWater.addLayer(L.polyline(seg, { color: color, weight: name === "北运河" ? 3.5 : 2.5, opacity: 0.8 })
        .bindPopup("<strong>" + name + "</strong><br>© OpenStreetMap"));
    });
  });

  /* ── layer: parks ── */
  var gParks = L.layerGroup();
  Object.keys(D.parks).forEach(function (name) {
    gParks.addLayer(L.polygon(D.parks[name], { color: "#4d7a3a", weight: 1, fillColor: "#8fbf6f", fillOpacity: 0.22 })
      .bindPopup("<strong>" + name + "</strong><br>© OpenStreetMap"));
  });

  /* ── layer: field points (OSM-verified + approx anchors) ── */
  var gPois = L.layerGroup();
  D.pois.forEach(function (p) {
    gPois.addLayer(trustMark([p.lat, p.lon], p.trust, "#1f4e5f", "#c07a2d").bindPopup(popupPoi(p)));
  });

  /* ── layer: heritage grades [A] — point + official text, no geometry ── */
  var gHeritage = L.layerGroup();
  (D.layers.heritage || []).forEach(function (h) {
    var pt = [h.lat, h.lon];
    var m = h.level === "national" ? solid(pt, "#a32020")
          : h.level === "unesco" ? solid(pt, "#a9822d")
          : hollow(pt, "#8a8a8a");
    var pop = "<strong>" + pick(h, "name") + "</strong><br>" +
      badge(h.grade + (h.batch ? " · " + h.batch : ""), h.level === "national" ? "grade-guo" : h.level === "unesco" ? "grade-unesco" : "grade-tbd") +
      "<br>" + pick(h, "note") + "<br><em>" + h.src + "</em>";
    gHeritage.addLayer(m.bindPopup(pop));
  });

  /* ── layer: field observations from the DB (link to /fieldwork anchors) ── */
  /* Static mirror: resolve fieldwork page rel-path from <base> (file:// needs ../ form) */
  var BASE = (document.querySelector("base") || {}).href || "/";
  var FIELDWORK_HREF = /zh\/?$/.test(BASE) ? BASE.replace(/zh\/?$/, "") + "fieldwork" : BASE + "fieldwork";
  var gObs = L.layerGroup();
  (D.layers.observations || []).forEach(function (o) {
    var m = o.trust === "osm" ? solid([o.lat, o.lon], "#3c6e47") : hollow([o.lat, o.lon], "#c07a2d");
    var typeLabel = { walk: "走查 walk", food: "食物 food", desk: "案头 desk" }[o.type] || o.type;
    var pop = "<strong>" + (ZH ? o.zh : o.en) + "</strong><br>" +
      (ZH ? o.site_zh : o.site_en) + " · " + o.date + "<br>" + typeLabel + " · " +
      badge("A", "grade-unesco") + " " + badge(o.trust === "osm" ? "OSM" : "approx", "tier-approx") + "<br>" +
      '<a href="' + FIELDWORK_HREF + '#o' + o.id + '">' + (ZH ? "田野记录 →" : "Field record →") + "</a>";
    gObs.addLayer(m.bindPopup(pop));
  });

  /* ── layer: protection red-line — documentation only (no geometry exists) ── */
  var gRedline = L.layerGroup();
  (function () {
    var R = D.layers.redline;
    var list = "";
    (R.docs || []).forEach(function (d) {
      list += "<li>" + (ZH ? d.zh : d.en) + " <em>" + d.src + "</em></li>";
    });
    var pop = "<strong>" + (ZH ? "保护红线 / 缓冲区（文本著录）" : "Protection red-line / buffer (text only)") + "</strong><br>" +
      (ZH ? R.note_zh : R.note_en) + "<ul style='margin:6px 0 0 16px;padding:0'>" + list + "</ul>";
    gRedline.addLayer(L.marker([39.9118, 116.664], {
      icon: L.divIcon({ className: "map-doc-pin", html: "§", iconSize: [18, 18], iconAnchor: [9, 9] })
    }).bindPopup(pop, { maxWidth: 360 }));
  })();

  /* ── layer: grain-trade tracer (numbered dashed chain) ── */
  var gTracer = L.layerGroup();
  (function () {
    var T = D.layers.tracer;
    var pts = T.points.map(function (p) { return [p.lat, p.lon]; });
    gTracer.addLayer(L.polyline(pts, { color: "#7a5c1e", weight: 3, opacity: 0.85, dashArray: "6,6" })
      .bindPopup("<strong>" + pick(T, "name") + "</strong><br>" +
        (ZH ? "线路为概念性漕运链示意，非精确航道。" : "Conceptual grain-trade chain, not a precise channel.")));
    T.points.forEach(function (p) {
      var ic = L.divIcon({ className: "map-tracer-no", html: String(p.no), iconSize: [18, 18], iconAnchor: [9, 9] });
      gTracer.addLayer(L.marker([p.lat, p.lon], { icon: ic }).bindPopup(
        "<strong>" + p.no + " · " + (ZH ? p.zh : p.en) + "</strong><br>" +
        badge(p.trust === "osm" ? "OSM" : "approx", "tier-approx")));
    });
  })();

  /* ── layer: day loop route ── */
  var gRoute = L.layerGroup();
  Object.keys(D.routes).forEach(function (k) {
    var r = D.routes[k];
    gRoute.addLayer(L.polyline(r.points, { color: "#033b4c", weight: 2.5, opacity: 0.9, dashArray: "2,6" })
      .bindPopup("<strong>" + (ZH ? r.name_zh : r.name_en) + "</strong>"));
  });

  /* ── layer: node dossiers (考据档案: 历史演变 / 交融 / 影响) ── */
  /* Every dossier line is segmented from already-vetted field_observations and
   * carries its own source + grade tag; gaps stay flagged, nothing is invented. */
  var LVL = { evolution: ["历史演变", "Evolution"], contact: ["交融", "Contact"], influence: ["影响", "Influence"] };
  var LVL_CLS = { A: "grade-unesco", B: "tier-osm", C: "grade-tbd", D: "grade-tbd" };
  function levelBadge(lv) { return badge("[" + lv + "]", LVL_CLS[lv] || "grade-tbd"); }
  function facetHtml(d, key) {
    var items = d[key] || [];
    if (!items.length) return "";
    var lis = items.map(function (it) {
      return "<li>" + (ZH ? it.zh : it.en) + " " + levelBadge(it.level) +
        (it.src ? "<br><em>" + it.src + "</em>" : "") + "</li>";
    }).join("");
    return "<section class='dossier-facet' id='df-" + key + "'><h4>" + (ZH ? LVL[key][0] : LVL[key][1]) +
      "</h4><ul>" + lis + "</ul></section>";
  }
  function openDossier(d) {
    var panel = document.getElementById("dossier-panel");
    if (!panel) return;
    var t = document.getElementById("dossier-title");
    var s = document.getElementById("dossier-sub");
    var b = document.getElementById("dossier-body");
    if (t) t.textContent = ZH ? d.name_zh : d.name_en;
    if (s) s.textContent = d.lat.toFixed(4) + ", " + d.lon.toFixed(4) + " · " +
      (d.trust === "osm" ? "OSM" : "approx 锚点") + " · 坐标待 GPS 复核";
    if (b) b.innerHTML = facetHtml(d, "evolution") + facetHtml(d, "contact") + facetHtml(d, "influence");
    panel.classList.add("open");
    panel.setAttribute("aria-hidden", "false");
  }
  var gDossier = L.layerGroup();
  (D.dossiers || []).forEach(function (d) {
    var ic = L.divIcon({ className: "map-dossier-pin", html: "档", iconSize: [20, 20], iconAnchor: [10, 10] });
    var mk = L.marker([d.lat, d.lon], { icon: ic });
    mk.bindPopup("<strong>" + (ZH ? d.name_zh : d.name_en) + "</strong><br>" +
      (ZH ? "点选查看考据档案" : "click for the dossier"));
    mk.on("popupopen", function (e) {
      var node = e.popup.getElement();
      var a = node.querySelector(".dossier-open");
      if (a) a.addEventListener("click", function () { openDossier(d); });
    });
    // clicking the marker opens the dossier directly
    mk.on("click", function () { openDossier(d); });
    gDossier.addLayer(mk);
  });

  /* ── defaults + control ── */
  gWater.addTo(map); gParks.addTo(map); gPois.addTo(map); gRoute.addTo(map); gDossier.addTo(map);
  L.control.layers(
    { [ZH ? "街道底图 OSM" : "OSM streets"]: tiles },
    {
      [ZH ? "水系（OSM）" : "Waterways (OSM)"]: gWater,
      [ZH ? "绿地 parks（OSM）" : "Parks (OSM)"]: gParks,
      [ZH ? "田野点位" : "Field points"]: gPois,
      [ZH ? "文保分级 [A]" : "Heritage grades [A]"]: gHeritage,
      [ZH ? "DB 田野观察" : "DB observations"]: gObs,
      [ZH ? "保护红线（文本）" : "Red-line (text)"]: gRedline,
      [ZH ? "漕运 tracer 链" : "Grain-trade tracer"]: gTracer,
      [ZH ? "考据档案（点）" : "Node dossiers"]: gDossier,
      [ZH ? "一日回环" : "Day loop"]: gRoute
    },
    { collapsed: false, position: "topright" }
  ).addTo(map);

  /* fit to Tongzhou working view (triangle), not to full water extent */
  map.fitBounds([[D.view.S, D.view.W], [D.view.N, D.view.E]]);

  /* layer toggle shortcuts under the map */
  var legend = document.getElementById("map-legend");
  if (legend) {
    var rows = [
      ["#1f4e5f", ZH ? "实心 = OSM 已核实坐标" : "Solid = OSM-verified coords"],
      ["#c07a2d", ZH ? "空心 = 近似锚点（待 GPS 钉）" : "Hollow = approximate anchor (GPS pin pending)"],
      ["#a32020", ZH ? "国保点（文本著录）" : "National-site point (text record)"],
      ["#a9822d", ZH ? "UNESCO / A 级来源" : "UNESCO / grade-A source"],
      ["#7a5c1e", ZH ? "虚线 = 漕运 tracer（概念示意）" : "Dashed = grain tracer (conceptual)"],
      ["#033b4c", ZH ? "档 = 考据档案（点选右侧展开）" : "档 = node dossier (click to open)"],
      ["#7b2d8b", ZH ? "● = 时间轴事件（随年代切片显隐）" : "● = timeline event (appears in the year window)"],
      ["#155e63", ZH ? "▮ = 政策（无坐标，横幅著录，不绘几何）" : "▮ = policy (no coords, banner record, no geometry)"]
    ];
    legend.innerHTML = rows.map(function (r) {
      return '<li><i style="background:' + r[0] + '"></i>' + r[1] + "</li>";
    }).join("") +
      "<li><i style='background:#fff;border:1px solid #999'></i>" +
      (ZH ? "无任何边界几何被绘制：OSM 无本区遗产区划数据，红线仅著录官方文本" :
           "No boundary geometry drawn: OSM lacks WH zone data here; red-line = official text only") + "</li>";
  }

  /* dossier panel: close button + Esc */
  var dpanel = document.getElementById("dossier-panel");
  var dclose = document.getElementById("dossier-close");
  function closeDossier() {
    if (!dpanel) return;
    dpanel.classList.remove("open");
    dpanel.setAttribute("aria-hidden", "true");
  }
  if (dclose) dclose.addEventListener("click", closeDossier);
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeDossier(); });

  /* ── 历史进程时间轴动画 · historical-process animation ── */
  /* TimeDimension supplies the yearly time model + `timeload`; the ±window
   * sweep, event-card rail, policy banner and dossier linkage are ours.
   * Policies have no coordinates (Overpass found no boundary geometry) and so
   * are shown only as a text banner — never drawn as a shape. */
  (function () {
    if (!CH) return;
    var EVENTS = CH.events || [];
    var geoEvents = EVENTS.filter(function (e) { return e.lat != null; });
    var policies = EVENTS.filter(function (e) { return e.kind === "policy"; });
    var years = [];
    EVENTS.forEach(function (e) { if (years.indexOf(e.year) < 0) years.push(e.year); });
    years.sort(function (a, b) { return a - b; });

    var chrono = L.layerGroup().addTo(map);
    geoEvents.forEach(function (e) {
      var mk = e.open ? hollow([e.lat, e.lon], "#7b2d8b") : solid([e.lat, e.lon], "#7b2d8b");
      mk.bindPopup("<strong>" + e.year + " · " + (ZH ? e.title_zh : e.title_en) + "</strong><br>" +
        badge("[" + e.level + "]", LVL_CLS[e.level] || "grade-tbd") + "<em><br>" + e.src + "</em><br>" +
        (ZH ? "点选：定位并展开该点档案" : "click: locate + open the dossier"));
      mk.on("click", function () { focusEvent(e); });
      e._marker = mk;
    });

    var winHalf = CH.window || 45, follow = true, speed = 1, timer = null, lastSig = "";
    var elYear = document.getElementById("tl-year"), slider = document.getElementById("tl-slider");
    var playBtn = document.getElementById("tl-play"), banner = document.getElementById("era-banner");
    var rail = document.getElementById("tl-rail");

    if (rail) {
      rail.innerHTML = EVENTS.map(function (e, i) {
        return "<li class='tl-card' data-i='" + i + "'><span class='tl-card-year'>" + e.year + "</span>" +
          "<span class='tl-card-kind " + (e.kind === "policy" ? "kind-policy" : "kind-event") + "'>" +
          (e.kind === "policy" ? (ZH ? "政策" : "policy") : (ZH ? "事件" : "event")) + "</span>" +
          "<span class='tl-card-title'>" + (ZH ? e.title_zh : e.title_en) + "</span>" + levelBadge(e.level) + "</li>";
      }).join("");
      Array.prototype.forEach.call(rail.querySelectorAll(".tl-card"), function (li) {
        li.addEventListener("click", function () { var e = EVENTS[+li.getAttribute("data-i")]; setYear(e.year); focusEvent(e); });
      });
    }

    function dossierFor(site) {
      if (!D.dossiers) return null;
      for (var i = 0; i < D.dossiers.length; i++) if (D.dossiers[i].site === site) return D.dossiers[i];
      return null;
    }
    function focusEvent(e) {
      if (e.lat != null) {
        map.flyTo([e.lat, e.lon], Math.max(map.getZoom(), 13), { duration: 0.6 });
        if (e._marker) e._marker.openPopup();
      }
      var d = dossierFor(e.site);
      if (d) {
        openDossier(d);
        if (e.facet) {
          var f = document.getElementById("df-" + e.facet);
          if (f) { f.classList.remove("flash"); void f.offsetWidth; f.classList.add("flash"); }
        }
      }
    }
    renderTimeline = function () {
      var y = curYear();
      if (elYear) elYear.textContent = y;
      if (slider) slider.value = y;
      var vis = geoEvents.filter(function (e) { return Math.abs(e.year - y) <= winHalf; });
      chrono.clearLayers();
      vis.forEach(function (e) { chrono.addLayer(e._marker); });
      if (rail) Array.prototype.forEach.call(rail.querySelectorAll(".tl-card"), function (li) {
        var e = EVENTS[+li.getAttribute("data-i")];
        li.classList.toggle("active", Math.abs(e.year - y) <= winHalf);
        li.classList.toggle("past", e.year < y - winHalf);
      });
      if (banner) {
        var pol = policies.filter(function (p) { return Math.abs(p.year - y) <= winHalf; })[0];
        if (pol) {
          banner.hidden = false;
          banner.innerHTML = "<span class='era-tag'>" + (ZH ? "政策" : "POLICY") + " · " + pol.year + "</span> " +
            (ZH ? pol.title_zh : pol.title_en) + " <em>" + pol.src + "</em>";
        } else banner.hidden = true;
      }
      if (follow && vis.length) {
        var sig = vis.map(function (e) { return e.year; }).join(",");
        if (sig !== lastSig) {
          lastSig = sig;
          map.fitBounds(vis.map(function (e) { return [e.lat, e.lon]; }), { animate: true, duration: 0.5, maxZoom: 13, padding: [60, 60] });
        }
      } else if (!vis.length) { lastSig = ""; }
    }

    function play() {
      if (timer) return;
      if (curYear() >= Y1) setYear(Y0);
      timer = setInterval(function () { var n = curYear() + 1; if (n > Y1) { pause(); return; } setYear(n); }, Math.max(16, Math.round(45 / speed)));
      if (playBtn) { playBtn.classList.add("playing"); playBtn.setAttribute("aria-pressed", "true"); }
    }
    function pause() {
      if (timer) { clearInterval(timer); timer = null; }
      if (playBtn) { playBtn.classList.remove("playing"); playBtn.setAttribute("aria-pressed", "false"); }
    }
    function neighbor(dir) {
      var y = curYear(), i;
      if (dir > 0) { for (i = 0; i < years.length; i++) if (years[i] > y) return years[i]; return years[years.length - 1]; }
      for (i = years.length - 1; i >= 0; i--) if (years[i] < y) return years[i];
      return years[0];
    }

    if (slider) {
      slider.min = Y0; slider.max = Y1; slider.value = Y0; slider.step = 1;
      slider.addEventListener("input", function () { pause(); setYear(+slider.value); });
    }
    if (playBtn) playBtn.addEventListener("click", function () { timer ? pause() : play(); });
    var prev = document.getElementById("tl-prev"); if (prev) prev.addEventListener("click", function () { pause(); setYear(neighbor(-1)); });
    var next = document.getElementById("tl-next"); if (next) next.addEventListener("click", function () { pause(); setYear(neighbor(1)); });
    var reset = document.getElementById("tl-reset"); if (reset) reset.addEventListener("click", function () { pause(); lastSig = ""; setYear(Y0); });
    var sp = document.getElementById("tl-speed"); if (sp) sp.addEventListener("change", function () { speed = +sp.value; if (timer) { pause(); play(); } });
    var wn = document.getElementById("tl-window"); if (wn) wn.addEventListener("change", function () { winHalf = +wn.value; lastSig = ""; renderTimeline(); });
    var fo = document.getElementById("tl-follow"); if (fo) fo.addEventListener("change", function () { follow = fo.checked; lastSig = ""; });

    if (HAS_TD && map.timeDimension) map.timeDimension.on("timeload", renderTimeline);
    renderTimeline();
  })();
})();
