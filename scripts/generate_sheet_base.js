const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    // Load the HTML file
    const htmlPath = path.resolve(__dirname, '../character_sheet.html');
    const content = fs.readFileSync(htmlPath, 'utf8');
    await page.setContent(content, { waitUntil: 'networkidle0' });

    // Generate PDF
    const pdfPath = path.resolve(__dirname, '../character_sheet_base.pdf');
    await page.pdf({
        path: pdfPath,
        format: 'A4',
        printBackground: true,
        margin: { top: 0, right: 0, bottom: 0, left: 0 }
    });

    // Extract coordinates
    const fields = await page.evaluate(() => {
        const data = [];
        const pages = document.querySelectorAll('.page');
        
        // Helper to get relative coordinates within a page
        // Since we are printing A4, we assume the page elements match the PDF pages exactly
        // But puppeteer prints the whole document.
        // We need to know which "page" element corresponds to which PDF page.
        // Our CSS sets .page to A4 size.
        
        pages.forEach((pageEl, pageIndex) => {
            const pageRect = pageEl.getBoundingClientRect();
            const elements = pageEl.querySelectorAll('[data-field]');
            
            elements.forEach(el => {
                const rect = el.getBoundingClientRect();
                const type = el.getAttribute('data-type') || 'text';
                const multiline = el.hasAttribute('data-multiline');
                let align = el.getAttribute('data-align') || 'left';
                const name = el.getAttribute('data-field');
                
                // Auto-detect alignment based on field name if not set
                if (align === 'left') {
                    if (name.startsWith('attr_') || 
                        name.startsWith('skill_') && name.endsWith('_val') ||
                        ['hp_cur', 'hp_max', 'ip_cur', 'ip_max', 'speed', 'defense', 'reaction_pool', 'xp'].includes(name) ||
                        name.startsWith('inv_wt_') ||
                        name.startsWith('wep_mod_') ||
                        name.startsWith('wep_dmg_') ||
                        name.endsWith('_gp') || name.endsWith('_sp') || name.endsWith('_cp')
                    ) {
                        align = 'center';
                    }
                }

                data.push({
                    name: name,
                    type: type,
                    multiline: multiline,
                    align: align,
                    page: pageIndex, // 0-based
                    x: rect.left - pageRect.left, // Relative to the page container
                    y: rect.top - pageRect.top,   // Relative to the page container
                    width: rect.width,
                    height: rect.height
                });
            });
        });
        return data;
    });

    // Save coordinates
    fs.writeFileSync(path.resolve(__dirname, '../coordinates.json'), JSON.stringify(fields, null, 2));

    await browser.close();
    console.log('PDF generated and coordinates extracted.');
})();
