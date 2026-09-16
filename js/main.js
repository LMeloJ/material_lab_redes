/**
 * Laboratório de Redes - Script Principal
 * Controle de Tema, Filtros do Cronograma, Detecção de Iframe Canvas e Gerador de Embed
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initIframeDetection();
  initScheduleFilters();
  initCanvasModal();
});

// 1. TEMA DARK / LIGHT
function initTheme() {
  const savedTheme = localStorage.getItem('lab_redes_theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);

  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('lab_redes_theme', next);
      updateThemeIcon(next);
    });
  }
}

function updateThemeIcon(theme) {
  const icon = document.getElementById('theme-icon');
  if (icon) {
    icon.textContent = theme === 'dark' ? '☀️' : '🌙';
  }
}

// 2. DETECÇÃO DE IFRAME DO CANVAS
function initIframeDetection() {
  const isEmbedded = (window.self !== window.top) || window.location.search.includes('iframe=1');
  if (isEmbedded) {
    document.body.classList.add('is-iframe');
    const banner = document.getElementById('iframe-top-banner');
    if (banner) {
      banner.style.display = 'flex';
      const openExternalBtn = document.getElementById('iframe-external-link');
      if (openExternalBtn) {
        openExternalBtn.href = window.location.href.replace('iframe=1', '');
      }
    }
  }
}

// 3. FILTROS E BUSCA DO CRONOGRAMA
function initScheduleFilters() {
  const searchInput = document.getElementById('schedule-search');
  const filterTags = document.querySelectorAll('.filter-tag');
  const cards = document.querySelectorAll('.schedule-card');

  if (!searchInput && filterTags.length === 0) return;

  function filterCards() {
    const query = (searchInput ? searchInput.value : '').toLowerCase().trim();
    const activeTag = document.querySelector('.filter-tag.active');
    const category = activeTag ? activeTag.getAttribute('data-category') : 'all';

    let visibleCount = 0;

    cards.forEach(card => {
      const title = (card.querySelector('.card-title')?.textContent || '').toLowerCase();
      const desc = (card.querySelector('.card-desc')?.textContent || '').toLowerCase();
      const date = (card.querySelector('.card-date')?.textContent || '').toLowerCase();
      const cardCategory = card.getAttribute('data-category') || 'all';

      const matchesQuery = !query || title.includes(query) || desc.includes(query) || date.includes(query);
      const matchesCategory = category === 'all' || cardCategory.includes(category);

      if (matchesQuery && matchesCategory) {
        card.style.display = 'flex';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    const noResults = document.getElementById('no-results-msg');
    if (noResults) {
      noResults.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  }

  if (searchInput) {
    searchInput.addEventListener('input', filterCards);
  }

  filterTags.forEach(tag => {
    tag.addEventListener('click', () => {
      filterTags.forEach(t => t.classList.remove('active'));
      tag.classList.add('active');
      filterCards();
    });
  });
}

// 4. MODAL DO GERADOR DE IFRAME PARA CANVAS
function initCanvasModal() {
  const openBtn = document.getElementById('open-canvas-modal-btn');
  const closeBtn = document.getElementById('close-canvas-modal-btn');
  const modal = document.getElementById('canvas-modal');
  const labSelect = document.getElementById('canvas-lab-select');
  const iframeCode = document.getElementById('canvas-iframe-code');
  const copyBtn = document.getElementById('copy-iframe-btn');

  if (!openBtn || !modal) return;

  openBtn.addEventListener('click', (e) => {
    e.preventDefault();
    modal.classList.add('active');
    updateIframeCode();
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', () => {
      modal.classList.remove('active');
    });
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) modal.classList.remove('active');
  });

  function updateIframeCode() {
    if (!iframeCode) return;
    const selectedLab = labSelect ? labSelect.value : '';
    const currentBase = window.location.href.split('index.html')[0].split('#')[0];
    const targetUrl = selectedLab ? `${currentBase}${selectedLab}` : currentBase;
    
    iframeCode.value = `<iframe src="${targetUrl}" width="100%" height="850" style="border:1px solid #cbd5e1; border-radius:8px; min-height:850px; width:100%;" frameborder="0" allowfullscreen></iframe>`;
  }

  if (labSelect) {
    labSelect.addEventListener('change', updateIframeCode);
  }

  if (copyBtn && iframeCode) {
    copyBtn.addEventListener('click', () => {
      navigator.clipboard.writeText(iframeCode.value).then(() => {
        const original = copyBtn.innerHTML;
        copyBtn.innerHTML = '✓ Copiado com sucesso!';
        copyBtn.style.background = '#10b981';
        setTimeout(() => {
          copyBtn.innerHTML = original;
          copyBtn.style.background = '';
        }, 2200);
      });
    });
  }
}
