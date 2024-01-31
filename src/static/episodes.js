document.addEventListener('DOMContentLoaded', function () {
const toggleButton = document.getElementById('toggleButton');
const additionalInfoList = document.getElementById('episodes');
const hiddenItems = document.querySelectorAll('.hidden');

// Function to toggle visibility of additional items
function toggleAdditionalItems() {
    hiddenItems.forEach(item => {
      item.classList.toggle('hidden');
    });

    if (toggleButton.textContent === 'Show Episodes') {
      toggleButton.textContent = 'Hide Episodes';
    } else {
      toggleButton.textContent = 'Show Episodes';
    }
  }


// Event listener for the toggle button
toggleButton.addEventListener('click', toggleAdditionalItems);

});