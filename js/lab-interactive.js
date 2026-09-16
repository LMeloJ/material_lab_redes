/**
 * Laboratório de Redes - Roteiros Interativos
 * Checklist com localStorage, Barra de Progresso, Cópia de Comandos e Quizzes Didáticos
 */

document.addEventListener('DOMContentLoaded', () => {
  const labId = document.body.getAttribute('data-lab-id') || window.location.pathname.split('/').pop().replace('.html', '');
  
  initChecklist(labId);
  initCodeCopyButtons();
  initQuizzes();
  initFullscreenButton();
});

// 1. CHECKLIST INTERATIVO COM PERSISTÊNCIA EM LOCALSTORAGE
function initChecklist(labId) {
  const taskItems = document.querySelectorAll('.task-item');
  if (taskItems.length === 0) return;

  const storageKey = `lab_redes_check_${labId}`;
  let savedState = {};

  try {
    savedState = JSON.parse(localStorage.getItem(storageKey) || '{}');
  } catch (e) {
    savedState = {};
  }

  const progressBar = document.getElementById('lab-progress-fill');
  const progressText = document.getElementById('lab-progress-text');
  const progressPercent = document.getElementById('lab-progress-percent');

  function updateProgress() {
    let completed = 0;
    taskItems.forEach((item, index) => {
      const checkbox = item.querySelector('.task-checkbox');
      const isDone = checkbox ? checkbox.checked : false;
      if (isDone) {
        completed++;
        item.classList.add('completed');
      } else {
        item.classList.remove('completed');
      }
    });

    const total = taskItems.length;
    const pct = total > 0 ? Math.round((completed / total) * 100) : 0;

    if (progressBar) progressBar.style.width = `${pct}%`;
    if (progressText) progressText.textContent = `${completed} de ${total} etapas concluídas`;
    if (progressPercent) progressPercent.textContent = `${pct}%`;

    // Atualiza status do card na Home caso haja comunicação
    try {
      localStorage.setItem(`lab_status_${labId}`, pct === 100 ? 'done' : (completed > 0 ? 'in_progress' : 'todo'));
    } catch (e) {}
  }

  taskItems.forEach((item, index) => {
    const checkbox = item.querySelector('.task-checkbox');
    const taskId = item.getAttribute('data-task-id') || `task_${index}`;

    // Restaura estado salvo
    if (savedState[taskId]) {
      if (checkbox) checkbox.checked = true;
      item.classList.add('completed');
    }

    // Clique no item todo aciona o checkbox
    item.addEventListener('click', (e) => {
      if (e.target.tagName !== 'INPUT' && e.target.tagName !== 'A' && e.target.tagName !== 'BUTTON') {
        if (checkbox) {
          checkbox.checked = !checkbox.checked;
          checkbox.dispatchEvent(new Event('change'));
        }
      }
    });

    if (checkbox) {
      checkbox.addEventListener('change', () => {
        savedState[taskId] = checkbox.checked;
        localStorage.setItem(storageKey, JSON.stringify(savedState));
        updateProgress();
      });
    }
  });

  // Botões opcionais de Reset / Concluir Tudo
  const resetBtn = document.getElementById('btn-reset-progress');
  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      if (confirm('Deseja reiniciar seu progresso neste roteiro?')) {
        savedState = {};
        localStorage.removeItem(storageKey);
        taskItems.forEach(item => {
          const cb = item.querySelector('.task-checkbox');
          if (cb) cb.checked = false;
        });
        updateProgress();
      }
    });
  }

  const markAllBtn = document.getElementById('btn-mark-all');
  if (markAllBtn) {
    markAllBtn.addEventListener('click', () => {
      taskItems.forEach((item, idx) => {
        const cb = item.querySelector('.task-checkbox');
        const taskId = item.getAttribute('data-task-id') || `task_${idx}`;
        if (cb) cb.checked = true;
        savedState[taskId] = true;
      });
      localStorage.setItem(storageKey, JSON.stringify(savedState));
      updateProgress();
    });
  }

  updateProgress();
}

// 2. CÓPIA DE COMANDOS COM 1 CLIQUE
function initCodeCopyButtons() {
  document.querySelectorAll('.copy-btn').forEach(button => {
    button.addEventListener('click', (e) => {
      e.stopPropagation();
      const codeBlock = button.closest('.code-window')?.querySelector('pre code') || 
                        button.parentElement?.nextElementSibling?.querySelector('code') ||
                        button.closest('.code-window')?.querySelector('pre');
      
      if (!codeBlock) return;

      const codeText = codeBlock.innerText;
      navigator.clipboard.writeText(codeText).then(() => {
        const originalText = button.innerHTML;
        button.innerHTML = '✓ Copiado!';
        button.style.background = '#10b981';
        button.style.color = '#ffffff';

        setTimeout(() => {
          button.innerHTML = originalText;
          button.style.background = '';
          button.style.color = '';
        }, 2000);
      }).catch(err => {
        console.error('Falha ao copiar:', err);
      });
    });
  });
}

// 3. QUIZZES E DESAFIOS DE FIXAÇÃO
function initQuizzes() {
  document.querySelectorAll('.quiz-card').forEach(quiz => {
    const options = quiz.querySelectorAll('.quiz-option');
    const feedback = quiz.querySelector('.quiz-feedback');
    const explainBtn = quiz.querySelector('.btn-reveal-explanation');

    options.forEach(option => {
      option.addEventListener('click', () => {
        const isCorrect = option.getAttribute('data-correct') === 'true';

        // Desabilita as outras opções deste quiz
        options.forEach(opt => {
          opt.style.pointerEvents = 'none';
          if (opt.getAttribute('data-correct') === 'true') {
            opt.classList.add('correct');
          }
        });

        if (!isCorrect) {
          option.classList.add('wrong');
        }

        if (feedback) {
          feedback.style.display = 'block';
          if (isCorrect) {
            feedback.style.background = 'rgba(16, 185, 129, 0.15)';
            feedback.style.color = '#34d399';
            feedback.style.border = '1px solid #10b981';
            feedback.innerHTML = `<strong>🎉 Excelente! Resposta correta.</strong> ${option.getAttribute('data-explanation') || ''}`;
          } else {
            feedback.style.background = 'rgba(239, 68, 68, 0.15)';
            feedback.style.color = '#f87171';
            feedback.style.border = '1px solid #ef4444';
            feedback.innerHTML = `<strong>Atenção:</strong> Resposta incorreta. Revise o conceito acima! ${option.getAttribute('data-explanation') || ''}`;
          }
        }
      });
    });

    if (explainBtn && feedback) {
      explainBtn.addEventListener('click', () => {
        feedback.style.display = feedback.style.display === 'block' ? 'none' : 'block';
      });
    }
  });
}

// 4. BOTÃO ABRIR EM TELA CHEIA / NOVA ABA
function initFullscreenButton() {
  const fullscreenBtns = document.querySelectorAll('.btn-fullscreen');
  fullscreenBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      window.open(window.location.href.replace('iframe=1', ''), '_blank');
    });
  });
}
