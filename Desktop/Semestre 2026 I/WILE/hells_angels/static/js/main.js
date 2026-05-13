document.addEventListener('DOMContentLoaded', function () {


  const mensajes = document.querySelectorAll('.mensaje');
  mensajes.forEach(msg => {
    setTimeout(() => {
      msg.style.animation = 'slideIn 0.3s ease reverse';
      setTimeout(() => msg.remove(), 300);
    }, 4000);
    msg.addEventListener('click', () => msg.remove());
  });


  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-links a').forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
  });


  const chkLicencia = document.getElementById('id_tiene_licencia');
  const grupoLicencia = document.getElementById('grupo-licencia');
  if (chkLicencia && grupoLicencia) {
    const toggleLicencia = () => {
      grupoLicencia.style.display = chkLicencia.checked ? 'flex' : 'none';
    };
    toggleLicencia();
    chkLicencia.addEventListener('change', toggleLicencia);
  }


  const yearEl = document.getElementById('current-year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
});
