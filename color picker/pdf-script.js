function convertToPDF() {
    const fileInput = document.getElementById("fileInput");
    if (fileInput.files.length === 0) {
        alert("Please select a file first.");
        return;
    }

    const file = fileInput.files[0];
    const reader = new FileReader();

    reader.onload = function (e) {
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF();
        doc.text(e.target.result, 10, 10);
        doc.save("converted.pdf");
    };

    reader.readAsText(file);
}
