// Change background color on hover for the submit button
const submitButton = document.getElementById('submitBtn');

submitButton.addEventListener('mouseenter', function () {
    submitButton.style.backgroundColor = '	#008000'; // New color on hover
});

submitButton.addEventListener('mouseleave', function () {
    submitButton.style.backgroundColor = ''; // Reset to original color
});


// Toggle dark mode
const darkModeToggle = document.getElementById('darkModeToggle');

darkModeToggle.addEventListener('click', function () {
    document.body.classList.toggle('bg-dark');  // Toggle dark background
    document.body.classList.toggle('text-white');  // Toggle text color
    darkModeToggle.classList.toggle('btn-light');  // Toggle button style
    darkModeToggle.classList.toggle('btn-dark');
});


// JavaScript to toggle visibility of the upload section
const toggleButton = document.getElementById('toggleUploadSection');
const uploadSection = document.getElementById('upload-section');

toggleButton.addEventListener('click', function () {
    // Toggle the display style of the upload section between 'none' and 'block'
    if (uploadSection.style.display === 'none') {
        uploadSection.style.display = 'block'; // Show the section
    } else {
        uploadSection.style.display = 'none'; // Hide the section
    }
});

