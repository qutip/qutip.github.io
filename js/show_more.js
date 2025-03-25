document.getElementById('show-more-btn').addEventListener('click', function () {
    const collapseElement = document.getElementById('show-more-btn');
    this.textContent = collapseElement.classList.contains('collapsed') ? 'Show More' : 'Show Less';
});