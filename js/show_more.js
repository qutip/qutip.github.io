showMoreElement = document.getElementById('show-more-btn');
if (showMoreElement) {
    showMoreElement.addEventListener('click', function () {
        const collapseElement = document.getElementById('show-more-btn');
        this.textContent = collapseElement.classList.contains('collapsed') ? 'Show More' : 'Show Less';
    });
}