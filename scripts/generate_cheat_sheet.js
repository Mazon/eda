const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

(async () => {
    console.log('Generating Cheat Sheet PDF...');
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    // Load the HTML file
    const htmlPath = path.resolve(__dirname, '../cheat_sheet.html');
    const content = fs.readFileSync(htmlPath, 'utf8');
    await page.setContent(content, { waitUntil: 'networkidle0' });

    // Generate PDF
    const pdfPath = path.resolve(__dirname, '../build/Cheat_Sheet.pdf');
    
    // Ensure build directory exists
    const buildDir = path.dirname(pdfPath);
    if (!fs.existsSync(buildDir)){
        fs.mkdirSync(buildDir);
    }

    await page.pdf({
        path: pdfPath,
        format: 'A4',
        printBackground: true,
        margin: { top: 0, right: 0, bottom: 0, left: 0 }
    });

    await browser.close();
    console.log(`PDF generated at: ${pdfPath}`);
})();
