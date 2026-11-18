function filterCards(filterValue) {
  document.querySelectorAll('#card-grid > [data-domain]').forEach(card => {
    const isMatch = filterValue === 'all' || card.dataset.domain === filterValue;
    card.classList.toggle('d-none', !isMatch);
  });
}

document.querySelectorAll('[data-bs-toggle="popover"]').forEach(el => new bootstrap.Popover(el));

  function updateReadMore() {
    document.querySelectorAll('.read-more').forEach(link => {
      const desc = link.previousElementSibling;
      const isCut = desc.scrollHeight > desc.clientHeight + 1;
      link.classList.toggle('d-none', !isCut);
    });
  }

  window.addEventListener('load', updateReadMore);
  window.addEventListener('resize', updateReadMore);