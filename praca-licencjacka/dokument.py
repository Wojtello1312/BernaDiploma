from pathlib import Path
from docx import Document
from docx.shared import Cm,Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import subprocess,copy,re
root=Path(__file__).parent
# Reference formatting used by pandoc.
ref=Document();sec=ref.sections[0]
sec.page_width=Cm(21);sec.page_height=Cm(29.7)
sec.left_margin=Cm(3.5);sec.right_margin=Cm(2.5);sec.top_margin=Cm(2.5);sec.bottom_margin=Cm(2.5)
for name in ['Normal','Body Text','First Paragraph']:
 st=ref.styles[name] if name in ref.styles else ref.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH);st.font.name='Times New Roman';st.font.size=Pt(12)
 f=st.paragraph_format;f.line_spacing=1.5;f.space_after=Pt(0);f.space_before=Pt(0);f.first_line_indent=Cm(1);f.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY;f.widow_control=True
for name,size in [('Heading 1',16),('Heading 2',14)]:
 st=ref.styles[name];st.font.name='Times New Roman';st.font.size=Pt(size);st.font.bold=True
 f=st.paragraph_format;f.first_line_indent=Cm(0);f.space_before=Pt(14);f.space_after=Pt(8);f.keep_with_next=True
 if name=='Heading 1':f.page_break_before=True
ref.save(root/'format.docx')
subprocess.run(['pandoc',str(root/'Praca_licencjacka_Bernaciak.md'),'--reference-doc='+str(root/'format.docx'),'-o',str(root/'tresc.docx')],check=True)
d=Document(root/'format.docx')
# No default content was created in reference document.
sec=d.sections[0];sec.different_first_page_header_footer=True
p=sec.footer.paragraphs[0];p.alignment=WD_ALIGN_PARAGRAPH.CENTER
fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');p._p.append(fld)
for text,size,bold,after in [
 ('UNIWERSYTET MORSKI W GDYNI',14,False,10),('WYDZIAŁ ZARZĄDZANIA',14,False,20),
 ('Kierunek: Zarządzanie',12,False,0),('Specjalizacja: Informatyka gospodarcza',12,False,72),
 ('Zastosowanie sztucznej inteligencji do personalizacji relacji z klientami sklepów internetowych',18,True,35),
 ('Praca licencjacka',14,False,55),('Łukasz Bernaciak',14,False,0),('Numer indeksu: 50825',12,False,120),('Gdynia 2026',12,False,0)]:
 p=d.add_paragraph();p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.paragraph_format.first_line_indent=Cm(0);p.paragraph_format.space_after=Pt(after)
 r=p.add_run(text);r.font.size=Pt(size);r.bold=bold
p=d.add_paragraph('SPIS TREŚCI','Heading 1')
# A Word TOC field, with readable cached outline. Word recalculates page numbers.
p=d.add_paragraph();p.paragraph_format.first_line_indent=Cm(0)
r=p.add_run();begin=OxmlElement('w:fldChar');begin.set(qn('w:fldCharType'),'begin');r._r.append(begin)
r=p.add_run();instr=OxmlElement('w:instrText');instr.set(qn('xml:space'),'preserve');instr.text=' TOC \\o "1-2" \\h \\z \\u ';r._r.append(instr)
r=p.add_run();sep=OxmlElement('w:fldChar');sep.set(qn('w:fldCharType'),'separate');r._r.append(sep)
for line in (root/'Praca_licencjacka_Bernaciak.md').read_text().splitlines():
 if line.startswith(('# ','## ')):
  p=d.add_paragraph(line.lstrip('# '));p.paragraph_format.first_line_indent=Cm(0);p.paragraph_format.left_indent=Cm(.5 if line.startswith('##') else 0)
  p.paragraph_format.line_spacing=1;p.paragraph_format.space_after=Pt(3)
  for r in p.runs:r.font.size=Pt(10)
r=p.add_run();end=OxmlElement('w:fldChar');end.set(qn('w:fldCharType'),'end');r._r.append(end)
body=Document(root/'tresc.docx')
for i,el in enumerate([x for x in d.element.body if x.tag != qn('w:sectPr')]):
 body.element.body.insert(i,copy.deepcopy(el))
d=body
sec=d.sections[0];sec.different_first_page_header_footer=True
p=sec.footer.paragraphs[0];p.alignment=WD_ALIGN_PARAGRAPH.CENTER
fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');p._p.append(fld)
for table in d.tables:
 table.autofit=False
 for row in table.rows:
  for cell in row.cells:
   for p in cell.paragraphs:
    f=p.paragraph_format;f.first_line_indent=Cm(0);f.space_after=Pt(3);f.space_before=Pt(3);f.line_spacing=1.05;f.alignment=WD_ALIGN_PARAGRAPH.LEFT
    for run in p.runs:run.font.name='Times New Roman';run.font.size=Pt(10)
 for c in table.rows[0].cells:
  for p in c.paragraphs:
   for run in p.runs:run.bold=True
 trpr=table.rows[0]._tr.get_or_add_trPr();rep=OxmlElement('w:tblHeader');trpr.append(rep)
# Captions should remain with the following table, sources use a smaller font.
for p in d.paragraphs:
 if p.text.startswith('Tabela '):
  p.paragraph_format.keep_with_next=True;p.paragraph_format.first_line_indent=Cm(0)
  for r in p.runs:r.font.size=Pt(11)
 if p.text.startswith('Źródło:'):
  p.paragraph_format.first_line_indent=Cm(0);p.paragraph_format.line_spacing=1.0
  for r in p.runs:r.font.size=Pt(9);r.italic=True
for p in d.paragraphs:
 if p.text.startswith('Tabela ') and ' — s. ' in p.text:
  p.text=p.text.split(' — s. ')[0]
  p.paragraph_format.first_line_indent=Cm(0)
settings=d.settings.element
upd=OxmlElement('w:updateFields');upd.set(qn('w:val'),'true');settings.append(upd)
d.core_properties.title='Zastosowanie sztucznej inteligencji do personalizacji relacji z klientami sklepów internetowych'
d.core_properties.author='Łukasz Bernaciak'
d.core_properties.subject='Praca licencjacka – wersja robocza do przeglądu merytorycznego i redakcyjnego'
d.save(root/'Praca_licencjacka_Bernaciak.docx')
print('DOCX zapisany, tabele:',len(d.tables))
