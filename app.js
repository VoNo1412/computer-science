const PDFDocument = require('pdfkit');
const express = require("express");
const app = express();

// Define route to generate and download PDF
app.get('/download-pdf', (req, res) => {
    let doc = new PDFDocument();
    
    res.setHeader('Content-Type', 'application/pdf');
    res.setHeader('Content-Disposition', 'attachment; filename=example.pdf');
    doc.pipe(res);

    let data = [
        {
            name: "vono",
            age: 23,
            email: "1412"
        }
    ];

    data.forEach(entry => {
        doc.text(`Name: ${entry.name}`);
        doc.text(`Age: ${entry.age}`);
        doc.text(`Email: ${entry.email}`);
        doc.moveDown(); // Move down for next entry
    });

    doc.end();
});

// Start server
app.listen(3000, () => console.log('Server is running on port 3000'));
