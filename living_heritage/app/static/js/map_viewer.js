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

  var map = L.map(el, { center: [39.887, 116.70], zoom: 12, maxZoom: 19 });

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

  /* ── defaults + control ── */
  gWater.addTo(map); gParks.addTo(map); gPois.addTo(map); gRoute.addTo(map);
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
      ["#7a5c1e", ZH ? "虚线 = 漕运 tracer（概念示意）" : "Dashed = grain tracer (conceptual)"]
    ];
    legend.innerHTML = rows.map(function (r) {
      return '<li><i style="background:' + r[0] + '"></i>' + r[1] + "</li>";
    }).join("") +
      "<li><i style='background:#fff;border:1px solid #999'></i>" +
      (ZH ? "无任何边界几何被绘制：OSM 无本区遗产区划数据，红线仅著录官方文本" :
           "No boundary geometry drawn: OSM lacks WH zone data here; red-line = official text only") + "</li>";
  }
})();
