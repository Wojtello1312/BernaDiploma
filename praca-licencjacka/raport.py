from pathlib import Path
from pypdf import PdfReader
from docx import Document
import json,re,zipfile,xml.etree.ElementTree as ET
r=Path(__file__).parent
stats=json.loads((r/'statystyki.json').read_text())
refs=json.loads((r/'zrodla-rejestr.json').read_text())
pdf=PdfReader(r/'Praca_licencjacka_Bernaciak.pdf')
doc=Document(r/'Praca_licencjacka_Bernaciak.docx')
body='\n\n'.join(p.read_text() for p in sorted((r/'tekst').glob('0[0-6]*.md')))
assert 40<=len(pdf.pages)<=50
assert 20<=len(refs)<=30
assert 12<=stats['total']['mean']<=15
assert len(doc.tables)==5
for key,_ in refs:
 assert key in body,(key,'Brak cytowania')
# Check internal package consistency and hyperlink relationships after document composition.
with zipfile.ZipFile(r/'Praca_licencjacka_Bernaciak.docx') as z:
 assert z.testzip() is None
 ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
 root=ET.fromstring(z.read('word/document.xml'))
 rel=ET.fromstring(z.read('word/_rels/document.xml.rels'))
 ids={el.attrib['Id'] for el in rel}
 for el in root.findall('.//w:hyperlink',ns):
  rid=el.attrib.get('{'+ns['r']+'}id')
  if rid:assert rid in ids
# Confirm every final list-of-tables entry points to the actual caption page.
for line in (r/'tekst/08-spis-tabel.md').read_text().splitlines():
 if line.startswith('Tabela '):
  name,page=line.rsplit(' — s. ',1);page=int(page)
  title=name.split('. ',1)[1]
  assert title in (pdf.pages[page-1].extract_text() or '').replace('\n',' ')
status={
'Abadi i in., 2016':'Metadane i abstrakt w arXiv.',
'Adam, Wessel, Benlian, 2021':'Metadane i abstrakt wydawcy w Crossref.',
'Adomavicius, Tuzhilin, 2005':'Metadane w Crossref i abstrakt w OpenAlex.',
'Aguirre i in., 2015':'Potwierdzone metadane. Pełna treść i podstawa szczegółowych odwołań wymagają końcowego sprawdzenia.',
'Amazon, 2024':'Odczytano oficjalny opis funkcji, wraz z aktualizacją dotyczącą nazwy.',
'Bleier, Eisenbeiss, 2015':'Metadane i rozbudowany abstrakt wydawcy w Crossref.',
'Huang, Rust, 2021':'Metadane i abstrakt wydawcy w Crossref. Rok 2021 dotyczy wydania czasopisma, publikacja online nastąpiła wcześniej.',
'Jouppi i in., 2017':'Metadane i abstrakt w arXiv.',
'LeCun, Bengio, Hinton, 2015':'Potwierdzone metadane. Nie odczytano pełnej treści publikacji.',
'Lemon, Verhoef, 2016':'Metadane i abstrakt wydawcy w Crossref.',
'Linden, Smith, York, 2003':'Potwierdzone metadane. Opis metody w pracy wymaga końcowego porównania z pełną publikacją.',
'Luo i in., 2019':'Metadane w Crossref i krótki abstrakt w OpenAlex. Nie odczytano pełnego opisu eksperymentu.',
'Marhula, Sidor, 2026':'Odczytano pełny tekst z oficjalnego repozytorium Allegro. Sprawdzono autorów oraz liczby przytoczone w tabeli 5.1.',
'McCarthy, 2007':'Odczytano stronę wprowadzającą i część Basic Questions na stronie autora w Stanford.',
'Mell, Grance, 2011':'Odczytano oficjalny plik PDF NIST.',
'NIST, 2023':'Odczytano oficjalny plik PDF AI RMF 1.0.',
'OECD, 2019':'Odczytano oficjalną stronę publikacji i opis zakresu. Nie odczytano pełnego raportu.',
'Parlament Europejski i Rada, 2002':'Zidentyfikowano akt. EUR-Lex zwracał blokadę automatycznego odczytu. Treść i aktualność wymagają sprawdzenia.',
'Parlament Europejski i Rada, 2011':'Zidentyfikowano akt i wersję konsolidacji. EUR-Lex blokował odczyt. Sprawdzić art. 6 ust. 1 lit. ea oraz aktualność wersji.',
'Parlament Europejski i Rada, 2016':'Zidentyfikowano RODO. EUR-Lex blokował odczyt. Sprawdzić przywołane art. 4, 5 i 22 w oficjalnym tekście.',
'Parlament Europejski i Rada, 2024':'Zidentyfikowano AI Act. EUR-Lex blokował odczyt. Sprawdzić art. 50, zakres zastosowania i aktualny harmonogram.',
'Paszke i in., 2019':'Metadane i abstrakt w arXiv.',
'Payne, Frow, 2005':'Metadane i abstrakt wydawcy w Crossref.',
'Sejm RP, 2024':'Odczytano oficjalny PDF ustawy z Dziennika Ustaw i sprawdzono art. 399. Nie potwierdzono kompletu ewentualnych późniejszych zmian.',
'Vaswani i in., 2017':'Metadane i abstrakt w arXiv.',
'Zalando, 2023':'Odczytano oficjalny komunikat z 19.04.2023. Odróżniono zapowiedź pilotażu od przyszłych funkcji.'}
report=f'''# Raport przygotowania pracy

## Wynik

Przygotowano pełną wersję roboczą pracy licencjackiej Łukasza Bernaciaka: „Zastosowanie sztucznej inteligencji do personalizacji relacji z klientami sklepów internetowych”.

- PDF: **{len(pdf.pages)} strony**, łącznie ze stroną tytułową, spisami i bibliografią.
- Bibliografia: **{len(refs)} pozycje**, wszystkie przywołane w treści.
- Układ: wstęp, pięć rozdziałów, zakończenie, bibliografia i spis pięciu tabel.
- Średnia długość zdania w tekście głównym: **{stats['total']['mean']:.2f} słowa**.
- Pomiar: {stats['total']['words']} wyrazów i {stats['total']['sentences']} zdań w objętej analizą prozie.

## Podstawa i decyzje redakcyjne

Wykorzystano przygotowane wcześniej pliki Markdown oraz dokument „Bernaciak r1.docx”. Przyjęto nowszy układ pięciu rozdziałów zapowiedziany we wstępie tego dokumentu. Zakres z plików MD włączono do tego układu, zamiast zachowywać dwie sprzeczne numeracje.

Rozdział pierwszy zredagowano ponownie, skracając zdania i upraszczając język. Zachowano tematykę i bezosobowy sposób narracji. Uzupełniono TPU, sieci głębokie, transformery i modele generatywne. Poprawiono nadmierne uogólnienia o procesorach, danych użytkowników i nieuchronnych korzyściach AI. Nie przeniesiono niezweryfikowanych numerów stron ani niespójnej bibliografii z pierwotnego rozdziału.

Nie przeprowadzono ankiety, eksperymentu, testu platform ani badania danych klientów. Rozdział analityczny porównuje materiały wtórne. Wyniki techniczne Allegro pochodzą z wskazanej publikacji i nie zostały przedstawione jako własny pomiar. Hipotezę oceniono jako częściowo wspartą, bez pozornego dowodu powszechnego wzrostu lojalności.

## Sposób pomiaru języka

Zliczono tekst akapitów od wstępu do zakończenia. Pominięto nagłówki, tabelki, podpisy, linie źródeł, bibliografię i spisy. Usunięto nawiasowe odwołania autor–rok. Uwzględniono typowe skróty i zapis numerów podrozdziałów, aby ograniczyć błędny podział na zdania. Wynik jest pomiarem według tego sposobu segmentacji, a nie statystyką programu Word.

| Część | Zdania | Wyrazy | Średnia |
|---|---:|---:|---:|
'''
for a in stats['chapters']:report+=f"| {a['file']} | {a['sentences']} | {a['words']} | {a['mean']:.2f} |\n"
report+='''
## Zakres weryfikacji źródeł

Bibliografia nie jest równoznaczna z pełnotekstową weryfikacją wszystkich pozycji. W części przypadków dostępne były metadane lub abstrakty. Poniższe ograniczenia są rzeczywiste i wymagają uwzględnienia przed uznaniem tekstu za wersję do oddania. Nie dopisywano nieodczytanych cytatów dosłownych ani stron potwierdzających konkretne tezy.

| Pozycja | Sprawdzony materiał i ograniczenie |
|---|---|
'''
for key,_ in refs:report+=f'| {key} | {status[key]} |\n'
report+='''
Najważniejsze do końcowej kontroli są pełne teksty Aguirre i współautorów, Lindena i współautorów oraz LeCuna i współautorów, a także oficjalne teksty czterech przywołanych aktów unijnych. Przy pozycjach dostępnych przez abstrakt nie należy traktować opracowania jako pełnej recenzji metod i wyników całego artykułu.

## Format i sprawdzenie plików

PDF ma stałą, zweryfikowaną liczbę stron, spis treści i spis tabel z numerami stron. Używa kroju Liberation Serif, zbliżonego do Times New Roman, formatu A4 oraz marginesów 3,5 cm z lewej i 2,5 cm z pozostałych stron. Tytuły rozdziałów i podrozdziałów mają odpowiednio 16 i 14 punktów.

DOCX jest wersją edytowalną z krojem Times New Roman 12 pkt i interlinią 1,5. Zawiera pole automatycznego spisu treści z zapisanym wykazem nagłówków. Po otwarciu w Wordzie należy zaktualizować pola przez Ctrl+A i F9. Spis tabel w DOCX zawiera tytuły bez numerów stron, aby nie przenosić paginacji PDF do innego mechanizmu składu. Liczba stron DOCX może się zmienić zależnie od programu, fontów i późniejszej redakcji.

Sprawdzono integralność DOCX, powiązania hiperłączy, pięć tabel, obecność odwołań do wszystkich pozycji bibliografii, numerację spisu tabel w PDF i zgodność zakresu ze strukturą pracy. Nie wykonano kontroli antyplagiatowej. Nie potwierdzono aktualnej wydziałowej instrukcji redakcyjnej ani wzoru strony tytułowej poza danymi z załącznika.

## Pliki

- Praca_licencjacka_Bernaciak.docx — wersja edytowalna.
- Praca_licencjacka_Bernaciak.pdf — wersja o sprawdzonej paginacji.
- Praca_licencjacka_Bernaciak.md — pełny tekst źródłowy.
- tekst/ — osobne części pracy w Markdown.
- statystyki.json — wynik pomiaru zdań.
- zrodla-rejestr.json — identyfikacja 26 pozycji bibliografii.

Dla odczytu źródeł zapisano w szkicu konfiguracji środowiska wymagane domeny sieciowe. Nie potwierdzono publikacji nowej wersji środowiska. Nie zmieniano źródłowych załączników użytkownika.
'''
(r/'Raport_weryfikacji.md').write_text(report)
with zipfile.ZipFile(r/'Praca_licencjacka_Bernaciak_pakiet.zip','w',zipfile.ZIP_DEFLATED) as z:
 for name in ['Praca_licencjacka_Bernaciak.docx','Praca_licencjacka_Bernaciak.pdf','Praca_licencjacka_Bernaciak.md','Raport_weryfikacji.md','statystyki.json','zrodla-rejestr.json']:
  z.write(r/name,name)
 for p in sorted((r/'tekst').glob('*.md')):z.write(p,'tekst/'+p.name)
with zipfile.ZipFile(r/'Praca_licencjacka_Bernaciak_pakiet.zip') as z:assert z.testzip() is None
print(json.dumps({'pages':len(pdf.pages),'sources':len(refs),'mean_sentence_words':stats['total']['mean'],'docx_tables':len(doc.tables),'package_files':len(z.namelist())},ensure_ascii=False))
