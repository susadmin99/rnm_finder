document.addEventListener('DOMContentLoaded', function () {
const toggleButton = document.getElementById('toggleButton');
const episodesList = document.getElementById('episodes');
const hiddenEpisodes = document.querySelectorAll('.hidden');

  function toggleEpisodes() {
    hiddenEpisodes.forEach(item => {
      item.classList.toggle('hidden');
    });

    if (toggleButton.textContent === 'Show Episodes') {
      toggleButton.textContent = 'Hide Episodes';
    } else {
      toggleButton.textContent = 'Show Episodes';
    }
  }

toggleButton.addEventListener('click', toggleEpisodes);

});