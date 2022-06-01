"""python-docx 基本使用"""

from docx.document import Document
from docx import Document as document_func
from docx.shared import Inches
from docx.shared import Pt
from docx.shared import RGBColor
from docx.enum.dml import MSO_THEME_COLOR_INDEX
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT, WD_TAB_ALIGNMENT, WD_TAB_LEADER, WD_UNDERLINE

def create_document(document: Document):
    # 添加标题
    document.add_heading('0级标题', 0) # 标题级别, 范围 0-9

    # 加粗和斜体样式
    p = document.add_paragraph('A plain paragraph having some ')
    p.add_run('bold').bold = True
    p.add_run(' and some ')
    p.add_run('italic.').italic = True

    document.add_heading('Heading, level 1', level=1)
    document.add_paragraph('Intense quote', style='Intense Quote')

    document.add_paragraph(
        'first item in unordered list', style='List Bullet'
    )
    document.add_paragraph(
        'first item in ordered list', style='List Number'
    )

    document.add_picture('monty-truth.jpeg', width=Inches(1.25))

    records = (
        (3, '101', 'Spam'),
        (7, '422', 'Eggs'),
        (4, '631', 'Spam, spam, eggs, and spam')
    )

    table = document.add_table(rows=1, cols=3)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Qty'
    hdr_cells[1].text = 'Id'
    hdr_cells[2].text = 'Desc'
    for qty, id, desc in records:
        row_cells = table.add_row().cells
        row_cells[0].text = str(qty)
        row_cells[1].text = id
        row_cells[2].text = desc

    document.add_page_break()

    document.save('demo.docx')

    # 解析出一个段落的格式, 包括字体, 字号, 段落, 字体颜色
    # 段落缩进

if __name__ == "__main__":
    document = document_func()
    create_document(document)
