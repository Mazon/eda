import json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import transparent, Color, black, white
from pypdf import PdfReader, PdfWriter
import io
import os

# Constants
# Puppeteer (96 DPI) to PDF (72 DPI) conversion
# 1 px = 0.75 pt
scale_factor = 0.75

PAGE_HEIGHT = A4[1] # 841.89
PAGE_WIDTH = A4[0] # 595.28

# Helper for colors
dark_red = Color(0.5, 0, 0)

def create_overlay(coordinates, output_buffer):
    c = canvas.Canvas(output_buffer, pagesize=A4)
    
    # Organize fields by page
    fields_by_page = {}
    for field in coordinates:
        p = field['page']
        if p not in fields_by_page:
            fields_by_page[p] = []
        fields_by_page[p].append(field)
    
    # We need to loop through pages to match the base PDF
    # Assuming base PDF has 2 pages
    for page_num in range(2): 
        if page_num in fields_by_page:
            for field in fields_by_page[page_num]:
                # Convert coordinates
                # Puppeteer gives X, Y from Top-Left in px
                # ReportLab needs X, Y from Bottom-Left in pt
                
                x = field['x'] * scale_factor
                width = field['width'] * scale_factor
                height = field['height'] * scale_factor
                
                # Invert Y axis
                # ReportLab Y = PageHeight - (PuppeteerY * scale) - (PuppeteerHeight * scale)
                # Wait, Puppeteer Y is top of element.
                # So bottom of element in PDF coords is:
                y = PAGE_HEIGHT - (field['y'] * scale_factor) - height
                
                name = field['name']
                field_type = field.get('type', 'text')
                is_multiline = field.get('multiline', False)
                
                if field_type == 'checkbox':
                    # Checkbox
                    c.acroForm.checkbox(
                        name=name,
                        tooltip=name,
                        x=x,
                        y=y,
                        size=min(width, height),
                        checked=False,
                        buttonStyle='check',
                        borderStyle='solid',
                        borderWidth=1,
                        borderColor=dark_red,
                        fillColor=white,
                        textColor=black,
                        forceBorder=True
                    )
                else:
                    # Text Field
                    # Check if multiline
                    # If multiline, standard PDF behavior is top-left
                    
                    flags = 0
                    if is_multiline:
                        flags = 4096 # Bit 13: MultiLine

                    # Alignment
                    # ReportLab might not expose alignment directly.
                    # We can try to use 'Q' (Quadding) if it passes **kw to the annotation dict?
                    # Or we just accept left alignment if we can't force it.
                    # But let's try to remove alignment kwarg and see if fieldFlags works.
                    # Actually, if we look at AcroForm.textfield, it might not accept fieldFlags either?
                    # The previous error was on multiline.
                    
                    # Let's try to be conservative.
                    # If I can't set alignment easily via ReportLab's high level API, 
                    # I might have to skip it or find another way.
                    # BUT, usually 'fieldFlags' is the way to set flags.
                    
                    # Reverting to basic call but with fieldFlags if possible? 
                    # Let's check if fieldFlags causes error.

                    c.acroForm.textfield(
                        name=name,
                        tooltip=name,
                        x=x,
                        y=y,
                        width=width,
                        height=height,
                        borderStyle='solid',
                        borderWidth=0,
                        borderColor=transparent,
                        fillColor=transparent, 
                        textColor=black,
                        fontName='Helvetica',
                        fontSize=10,
                        fieldFlags=flags
                    )
        
        c.showPage()
    
    c.save()

def main():
    base_pdf_path = 'character_sheet_base.pdf'
    final_pdf_path = 'build/Character_Sheet.pdf'
    coords_path = 'coordinates.json'
    
    # Read coordinates
    try:
        with open(coords_path, 'r') as f:
            coordinates = json.load(f)
    except FileNotFoundError:
        print("Error: coordinates.json not found. Run the node script first.")
        return

    # Create the overlay PDF in memory
    overlay_buffer = io.BytesIO()
    create_overlay(coordinates, overlay_buffer)
    overlay_buffer.seek(0)
    
    # Merge
    try:
        base_pdf = PdfReader(base_pdf_path)
    except FileNotFoundError:
        print("Error: Base PDF not found.")
        return

    overlay_pdf = PdfReader(overlay_buffer)
    writer = PdfWriter()
    
    # Ensure build dir exists
    if not os.path.exists('build'):
        os.makedirs('build')

    # Iterate through base PDF pages and merge overlay
    # Note: If overlay has fewer pages, we stop merging but keep adding base pages
    num_pages = len(base_pdf.pages)
    
    for i in range(num_pages):
        page = base_pdf.pages[i]
        
        if i < len(overlay_pdf.pages):
            overlay_page = overlay_pdf.pages[i]
            page.merge_page(overlay_page)
        
        writer.add_page(page)
        
    # Write final
    with open(final_pdf_path, 'wb') as f:
        writer.write(f)
        
    print(f"Created interactive PDF at {final_pdf_path}")

if __name__ == "__main__":
    main()
