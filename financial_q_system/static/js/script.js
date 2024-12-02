document.getElementById("uploadForm")?.addEventListener("submit", function (e) {
    e.preventDefault();
    alert("File uploaded and question submitted!");
});

document.getElementById('fileInput').addEventListener('change', function () {
    const file = this.files[0];
    const displayContent = document.getElementById('displayContent');

    if (file && file.type === "application/pdf") {
        const fileURL = URL.createObjectURL(file);
        displayContent.innerHTML = `<iframe src="${fileURL}" width="100%" height="100%" style="border: none;"></iframe>`;
    } else {
        displayContent.innerHTML = "<p class='text-danger'>Please upload a valid PDF file.</p>";
    }
});


document.getElementById('textInput').addEventListener('input', function () {
    const displayContent = document.getElementById('displayContent');
    displayContent.textContent = this.value;
});


