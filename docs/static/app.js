document.addEventListener("DOMContentLoaded", async function() {
  const katexMacros = {
    "\\mat": "\\mathbf{#1}",
    "\\vec": "\\mathbf{#1}",
    "\\rot": "\\mathbf{C}",
    "\\eye": "\\mathbf{I}",
    "\\det": "\\text{det}\\left(#1\\right)",
    "\\tr": "\\text{tr}\\left(#1\\right)",
    "\\rank": "\\text{rank}\\left(#1\\right)",
    "\\quat": "\\mathbf{q}",
    "\\tf": "\\mathbf{T}",
    "\\pos": "\\mathbf{r}",
    "\\vel": "\\mathbf{v}",
    "\\acc": "\\mathbf{a}",
    "\\angvel": "\\mathbf{w}",
    "\\frame": "\\mathcal{F}",
    "\\pt": "\\mathbf{p}",
    "\\vee": "{(#1)^\\times}",
    "\\norm": "{\\left|\\left|#1\\right|\\right|}",
    "\\covar": "{\\mathbf{\\Sigma}}",
    "\\argmin": "\\mathop{\\operatorname{argmin}}\\limits",
    "\\state": "\\mathbf{x}",
    "\\mu": "\\mathbf{x}",
    "\\E": "\\mathbb{E}\\left[#1\\right]",
  };

  // Render KaTeX on an element
  function renderContent(el) {
    if (window.renderMathInElement) {
      renderMathInElement(el, {
        delimiters: [
          { left: "$$", right: "$$", display: true },
          { left: "$", right: "$", display: false }
        ],
        macros: katexMacros
      });
    }
  }

  // Load and inject a note file
  async function loadNote(url) {
    const resp = await fetch(url);
    let html = await resp.text();
    const bodyMatch = html.match(/<body[^>]*>([\s\S]*)<\/body>/i);
    if (bodyMatch) {
      html = bodyMatch[1];
    }
    // Strip outer <div id="content"> wrapper if present (full-wrapper files)
    html = html.replace(/^\s*<div\s+id="content">([\s\S]*)<\/div>\s*$/, "$1");
    const contentEl = document.getElementById("content");
    contentEl.innerHTML = html;
    renderContent(contentEl);
  }

  // Load sidebar
  const sidebarResp = await fetch("static/sidebar.html");
  document.getElementById("sidebar-container").innerHTML = await sidebarResp.text();

  // Load footer
  const footerResp = await fetch("footer.html");
  document.body.insertAdjacentHTML("beforeend", await footerResp.text());

  // Click delegation on sidebar
  document.getElementById("sidebar-container").addEventListener("click", function(e) {
    const link = e.target.closest("a[data-note]");
    if (!link) return;
    e.preventDefault();
    const url = link.getAttribute("href");
    const hash = url.replace(/^notes\//, "").replace(/\.html$/, "");
    history.pushState(null, "", "#" + hash);
    loadNote(url);
    document.querySelectorAll("#sidebar-container a[data-note]").forEach(function(a) {
      a.classList.remove("active");
    });
    link.classList.add("active");
  });

  // Handle back/forward navigation
  window.addEventListener("hashchange", function() {
    const hash = location.hash.slice(1);
    if (!hash) return;
    const link = document.querySelector('#sidebar-container a[href="notes/' + hash + '.html"]');
    if (link) {
      loadNote(link.getAttribute("href"));
      document.querySelectorAll("#sidebar-container a[data-note]").forEach(function(a) {
        a.classList.remove("active");
      });
      link.classList.add("active");
    }
  });

  // Load initial note from URL hash
  if (location.hash) {
    const hash = location.hash.slice(1);
    const link = document.querySelector('#sidebar-container a[href="notes/' + hash + '.html"]');
    if (link) link.click();
  }

  // Render KaTeX on initial content
  renderContent(document.getElementById("content"));
});
