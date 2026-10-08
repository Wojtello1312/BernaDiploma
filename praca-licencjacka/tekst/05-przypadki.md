# ROZDZIAŁ 5. ANALIZA WYBRANYCH PRZYPADKÓW

## 5.1. Kryteria doboru i zakres porównania

Do analizy wybrano Amazon, Zalando oraz Allegro jako przykłady różnych zastosowań AI. Dobór ma charakter celowy i wynika z dostępności materiałów opisujących konkretne rozwiązania. Amazon reprezentuje rekomendacje produktów oraz rozwój konwersacyjnego wspierania zakupów. Zalando pozwala rozpatrzyć znaczenie kontekstu i języka przy poszukiwaniu odzieży. Allegro pokazuje natomiast wykorzystanie modeli językowych do oceny trafności wyszukiwania.

Przypadki nie są identyczne, dlatego nie utworzono rankingu skuteczności analizowanych przedsiębiorstw. Różnią się charakterem funkcji, okresem opisu oraz rodzajem udostępnionych danych. Wspólnym punktem porównania jest sposób łączenia potrzeb odbiorcy z informacją o ofercie. Oceniono także ograniczenia dowodów dotyczących poprawy relacji i efektów sprzedażowych. Tak określony zakres pozwala uniknąć porównywania niezgodnych wskaźników.

Wykorzystano artykuł techniczny dotyczący rekomendacji Amazon oraz oficjalny opis uruchomienia asystenta zakupowego. Dla Zalando podstawę stanowi komunikat z 19 kwietnia 2023 roku. W przypadku Allegro wykorzystano publikację zespołu technicznego z sierpnia 2026 roku. Dokumenty opisują konkretne etapy rozwoju funkcji, a nie pełny stan przedsiębiorstw. Data materiału jest więc istotną częścią interpretacji każdego przypadku.

Analiza obejmuje problem klienta, wykorzystywany mechanizm, źródła informacji oraz zakres udokumentowanych rezultatów. Oddzielono deklaracje firm od wniosków sformułowanych na potrzeby niniejszej pracy, jednak nie przeprowadzono własnego testu działania platform ani badania ich użytkowników. Nie przyjęto również, że publiczny opis ujawnia pełną architekturę techniczną. Brak określonej informacji wskazano jako ograniczenie dostępnego materiału.

## 5.2. Amazon: od podobieństwa produktów do rozmowy zakupowej

Artykuł Lindena, Smitha i Yorka przedstawia sposób tworzenia rekomendacji wykorzystujący podobieństwo produktów. Głównym problemem była obsługa dużej liczby klientów oraz rozbudowanego katalogu oferty. Porównywanie każdego użytkownika ze wszystkimi pozostałymi tworzyło ograniczenia wydajnościowe. Autorzy opisali podejście koncentrujące się na relacjach między przedmiotami (Linden, Smith, York, 2003). Przygotowane powiązania można było wykorzystać do dopasowywania propozycji podczas kontaktu z klientem.

Z perspektywy odbiorcy znaczenie miało ograniczenie wysiłku potrzebnego do odkrycia kolejnych produktów. Rekomendacja mogła wskazywać przedmioty związane z dotychczasowym zainteresowaniem lub historią zakupów. Nie wymagało to ręcznego opisania wszystkich preferencji przez użytkownika, a jednocześnie system korzystał z pośrednich sygnałów, które mogły być niejednoznaczne. Historia zakupu nie wyjaśniała na przykład, czy produkt przeznaczono dla kupującego.

Opisane rozwiązanie pokazuje związek między architekturą techniczną a możliwością prowadzenia personalizacji. Nawet trafna metoda nie spełni zadania, jeśli działa zbyt wolno podczas wizyty. Wydajność jest więc warunkiem udostępnienia propozycji we właściwym momencie procesu zakupowego, nie oznacza jednak automatycznie wzrostu zaufania ani długoterminowej lojalności. Artykuł techniczny nie stanowi samodzielnego dowodu takich skutków relacyjnych.

Inny sposób wspierania zakupów przedstawiono w komunikacie dotyczącym asystenta Rufus. Amazon opisał możliwość zadawania pytań o potrzeby, kategorie oraz konkretne produkty (Amazon, 2024). Wskazano wykorzystanie katalogu, opinii klientów, pytań społeczności i informacji z Internetu. Odpowiedzi miały uwzględniać kontekst prowadzonej rozmowy i pomagać porównywać dostępne możliwości. Był to opis funkcji rozwijanej początkowo w wersji testowej.

Klient może w takim modelu rozpocząć kontakt od określenia planowanej aktywności, ale nie musi znać dokładnej nazwy produktu ani pełnego zestawu parametrów wyszukiwania. Kolejne pytania pozwalają doprecyzować oczekiwania oraz zawęzić listę odpowiednich propozycji. Personalizacja opiera się wtedy także na informacji przekazanej świadomie podczas rozmowy. Jest to inny rodzaj kontekstu niż sama historia wcześniejszych kliknięć.

Oficjalny materiał zaznacza również możliwość występowania błędów generowanej odpowiedzi. Przewidziano przekazywanie opinii przez użytkowników oraz powrót do standardowych wyników wyszukiwania. Elementy te są istotne, ponieważ ograniczają traktowanie rozmowy jako jedynej dostępnej ścieżki, nie dowodzą jednak całkowitego usunięcia ryzyka błędnej rekomendacji. Kontrola jakości pozostaje potrzebna również po udostępnieniu funkcji szerszej grupie odbiorców.

Na stronie źródłowej dodano informację o zmianie nazwy w maju 2026 roku. Wskazano nazwę Alexa for Shopping, zastępującą wcześniejsze określenie Rufus. W niniejszej analizie zachowano nazwę historyczną przy opisie komunikatu uruchomienia z 2024 roku. Takie rozróżnienie pozwala uniknąć mieszania dat oraz kolejnych wersji produktu, jednak nie przyjęto, że wszystkie obecne funkcje były dostępne podczas pierwszego uruchomienia.

Przypadek Amazon pokazuje przejście między dwoma sposobami pozyskiwania kontekstu zakupowego. Pierwszy wykorzystuje relacje między wcześniejszymi interakcjami z produktami. Drugi pozwala dodatkowo opisać potrzebę w bezpośredniej rozmowie z systemem, a oba podejścia mogą ograniczać wysiłek poszukiwania, lecz opierają się na odmiennych przesłankach. Ich skuteczności nie należy oceniać wyłącznie przez fakt zastosowania bardziej rozbudowanej technologii.

## 5.3. Zalando: interpretacja potrzeby w kontekście mody

W zakupach odzieżowych klient często rozpoczyna od okazji, stylu albo oczekiwanego efektu. Parametry katalogowe nie zawsze odpowiadają językowi używanemu podczas opisywania takiej potrzeby, a użytkownik może wiedzieć, na jakie wydarzenie szuka stroju, bez wskazania konkretnego fasonu. Powstaje wtedy potrzeba przełożenia opisu sytuacji na odpowiednie propozycje produktów. Temu problemowi odpowiadał zapowiedziany przez Zalando asystent wykorzystujący ChatGPT (Zalando, 2023).

Komunikat przedstawiał możliwość wyszukiwania przy użyciu własnych słów i określeń związanych z modą. Jako przykład podano pytanie o strój na ślub na Santorini w lipcu. Kontekst obejmował więc rodzaj wydarzenia, miejsce oraz porę roku. Asystent miał przygotować wyjaśnienie i propozycje odpowiadające tak opisanej sytuacji. Przykład prezentuje deklarowany scenariusz funkcji, a nie wynik niezależnego badania jej skuteczności.

W dokumencie zapowiedziano pierwszą wersję dla wybranych klientów na określonych rynkach. Wymieniono Niemcy, Irlandię, Wielką Brytanię oraz Austrię, z obsługą angielskiego i niemieckiego, dlatego nie można na tej podstawie stwierdzać powszechnej dostępności funkcji we wszystkich krajach. Nie jest też uzasadnione przenoszenie opisu bezpośrednio na polską wersję platformy. Zakres pilotażu stanowi część informacji potrzebnych do poprawnej interpretacji materiału.

Szczególnie ważne jest rozróżnienie opisanej funkcji od planowanego rozwoju personalizacji. Powiązanie propozycji z obserwowanymi markami oraz dostępnymi rozmiarami wskazano jako przyszłą możliwość, dlatego nie należy przedstawiać tych elementów jako potwierdzonych funkcji pierwszej wersji. Komunikaty produktowe często łączą opis stanu bieżącego i zamierzeń przedsiębiorstwa. Analiza wymaga oddzielenia obu rodzajów informacji.

Potencjalna korzyść wynika z ograniczenia trudności w przełożeniu potrzeby na język katalogu. Klient może doprecyzować sytuację kolejnym pytaniem zamiast rozpoczynać wyszukiwanie od nowa, nie rozwiązuje to jednak wszystkich problemów charakterystycznych dla sprzedaży odzieży online. Dopasowanie stylu nie oznacza pewności dotyczącej rozmiaru, materiału i komfortu użytkowania. Informacje te nadal wymagają odpowiednich danych produktowych i możliwości sprawdzenia warunków zakupu.

W komunikacie podkreślono zamiar poznawania sposobu korzystania klientów z nowego asystenta. Wskazano również znaczenie prywatności oraz zaufania podczas rozwoju doświadczenia zakupowego. Są to deklaracje określające kierunek projektu, nie wyniki audytu zgodności. Materiał nie dostarcza porównywalnego pomiaru długoterminowej lojalności użytkowników, ani nie pozwala przypisać konkretnego wzrostu sprzedaży samemu asystentowi.

Z perspektywy zarządzania przypadek ten pokazuje znaczenie języka właściwego dla danej kategorii. W modzie potrzeba może być opisana przez okazję i oczekiwany sposób prezentacji. W elektronice większe znaczenie mogą mieć parametry oraz zgodność z posiadanym sprzętem. Skuteczny interfejs powinien zatem odpowiadać sposobowi formułowania pytań przez odbiorców. Jeden ogólny schemat rozmowy nie musi być równie przydatny w każdym sklepie.

## 5.4. Allegro: ocena trafności jako warunek użytecznego dopasowania

Na platformie obejmującej wiele kategorii problemem jest także ocena jakości wyników wyszukiwania, jednak sama liczba kliknięć nie wyjaśnia, czy produkty odpowiadają znaczeniu konkretnego zapytania. Artykuł Marhuli i Sidora opisuje wykorzystanie modeli językowych do wspierania takiej oceny. Przedstawiono narzędzie Relevance Assessment Tool oraz proces przygotowania danych odniesienia (Marhula, Sidor, 2026). Materiał pochodzi od zespołu technicznego przedsiębiorstwa i opisuje jego doświadczenia.

Autorzy zwracają uwagę na niejednoznaczność relacji między zapytaniem a przedstawionym produktem. Oferta może dokładnie odpowiadać potrzebie, stanowić zamiennik albo jedynie produkt uzupełniający. W innych sytuacjach okazuje się nieistotna lub trudna do jednoznacznej oceny. Przygotowanie wspólnych zasad klasyfikacji wymaga więc wiedzy o różnych kategoriach asortymentu, jednak nie wystarcza automatyczne porównanie podobieństwa użytych słów.

Opisany proces wykorzystywał ocenę ludzi oraz rozstrzyganie rozbieżności przez ekspertów. Na tej podstawie przygotowano materiał służący porównywaniu rezultatów modeli językowych. Jest to ważne, ponieważ sam model nie powinien wyznaczać jednocześnie kryterium i oceniać własnej poprawności. Potrzebny pozostaje punkt odniesienia związany z rzeczywistym znaczeniem wyszukiwanego produktu. Dokument pokazuje zatem rolę pracy ludzkiej w przygotowaniu automatycznej oceny.

W tabeli 5.1 przytoczono wybrane wyniki pozwalające porównać trudność rozpoznawania poszczególnych klas trafności.

**Tabela 5.1. Wybrane wyniki oceny klas trafności opisane przez zespół Allegro**

| Klasa relacji produktu do zapytania | Wartość F1 | Liczba przykładów w pokazanym zbiorze |
|---|---:|---:|
| Produkt dokładnie odpowiadający | 0,94 | 10 413 |
| Produkt wysoce zastępowalny | 0,51 | 607 |
| Produkt zastępowalny | 0,33 | 387 |
| Produkt uzupełniający | 0,83 | 719 |
| Produkt nieistotny | 0,52 | 480 |

Źródło: Marhula i Sidor (2026), tabela wyników dla Gemini 3.1 Flash Lite. Przytoczono pięć klas z opublikowanego zestawienia.

Wskaźnik F1 łączy precyzję i kompletność rozpoznawania danej klasy, jednak nie jest miarą zadowolenia klienta ani wzrostu przychodów platformy. W przedstawionym zestawieniu wyniki różnią się między kategoriami relacji produktów. Trudniejsze okazuje się odróżnianie niektórych rodzajów zamienników niż rozpoznawanie dokładnego dopasowania. Wysoki wynik ogólny może więc ukrywać słabości występujące w mniej licznych grupach.

Wybór tego przypadku wymaga zaznaczenia granicy między wyszukiwaniem a personalizacją indywidualną. Dopasowanie do treści zapytania nie musi wykorzystywać profilu konkretnego klienta. Opisane narzędzie wspiera ocenę trafności, a nie bezpośrednią rozmowę zakupową. Jest jednak istotne dla tematu, ponieważ pokazuje warunki rzetelnej oceny dopasowania oferty. Bez odpowiednich kryteriów trudno stwierdzić, czy bardziej złożony system rzeczywiście pomaga użytkownikowi.

Wnioskiem z tego przypadku jest potrzeba łączenia różnych rodzajów pomiaru. Ocena trafności pary zapytanie–produkt dostarcza innych informacji niż wynik testu sprzedażowego. Dane techniczne mogą wskazać błąd niewidoczny w średnim wskaźniku aktywności użytkowników, nie zastępują jednak badania doświadczenia i jakości relacji z platformą. Obie perspektywy powinny wspierać ocenę tej samej funkcji, zachowując odrębne znaczenie wyników.

## 5.5. Porównanie przypadków i wnioski dla zarządzania

Przedstawione rozwiązania różnią się miejscem, w którym AI wspiera kontakt z ofertą. Amazon pokazuje rekomendowanie na podstawie powiązań produktów oraz kontekst rozmowy zakupowej. Zalando koncentruje się na interpretowaniu potrzeby wyrażonej językiem związanym z modą. Allegro przedstawia automatyczną ocenę jakości dopasowania wyników do treści zapytania. W każdym przypadku użyteczność zależy od odpowiedniego połączenia danych i celu zadania.

Tabela 5.2 zestawia rodzaje dostępnych dowodów oraz granice wnioskowania dla analizowanych przypadków.

**Tabela 5.2. Porównanie zakresu dowodów w analizowanych przypadkach**

| Przypadek | Główna funkcja | Potwierdzony zakres materiału | Czego materiał nie rozstrzyga |
|---|---|---|---|
| Amazon, rekomendacje | Dobór powiązanych produktów | Opis metody technicznej z 2003 roku | Aktualnej pełnej architektury i lojalności |
| Amazon, Rufus | Wspieranie zakupów przez rozmowę | Oficjalny opis uruchomienia i funkcji | Niezależnego efektu przyczynowego |
| Zalando | Wyszukiwanie przez opis sytuacji | Zapowiedź pilotażu i zakres scenariuszy | Realizacji wszystkich planowanych funkcji |
| Allegro | Ocena trafności wyszukiwania | Procedura i wybrane wyniki techniczne | Wzrostu zaufania lub retencji klientów |

Źródło: opracowanie własne na podstawie Lindena, Smitha i Yorka (2003), Amazon (2024), Zalando (2023) oraz Marhuli i Sidora (2026).

Pierwszy wniosek dotyczy sposobu pozyskiwania informacji o potrzebie użytkownika. Historia interakcji pozwala ograniczyć konieczność zadawania pytań, lecz bywa niejednoznaczna. Rozmowa umożliwia wyjaśnienie aktualnej sytuacji, ale wymaga wysiłku i poprawnej interpretacji wypowiedzi. Wybór zależy więc od charakteru zadania oraz dostępnego kontekstu, jednak nie ma podstaw do uznania jednego sposobu za najlepszy w każdym zastosowaniu.

Drugi wniosek odnosi się do jakości danych produktowych. Rekomendacja, rozmowa i ocena trafności wymagają informacji pozwalających właściwie rozpoznać ofertę. Błędny opis może prowadzić do nietrafnego dopasowania nawet przy rozbudowanym modelu. Z punktu widzenia sklepu uporządkowanie katalogu stanowi zatem ważny etap przygotowania wdrożenia, jednak nie powinno być traktowane jako zadanie drugorzędne wobec wyboru technologii.

Trzeci wniosek dotyczy ograniczeń dostępnych dowodów skuteczności. Analizowane materiały potwierdzają konkretne mechanizmy lub deklarowane funkcje, lecz nie tworzą wspólnego pomiaru relacji. Nie przedstawiają porównywalnego badania lojalności klientów wszystkich trzech przedsiębiorstw, dlatego nie wyliczono zbiorczego procentowego efektu personalizacji. Takie zestawienie wymagałoby danych o zgodnych definicjach, okresach i grupach odbiorców.

Dla mniejszego sklepu praktyczne znaczenie ma rozpoczęcie od jasno rozpoznanego problemu klienta, na przykład trudności wyboru akcesorium, odnalezienia informacji albo opisania potrzeby. Następnie należy określić dostępne dane i prosty punkt odniesienia dla przyszłej oceny, dlatego dopiero wtedy uzasadniony staje się wybór modelu oraz zakresu automatyzacji. Odwrócenie tej kolejności zwiększa ryzyko wdrożenia funkcji o niewielkiej wartości.

Analiza wspiera również potrzebę pozostawienia klientowi możliwości korekty działania systemu, co dotyczy zmiany zapytania, pominięcia nietrafnej kategorii albo przejścia do zwykłego wyszukiwania. W obsłudze reklamacji znaczenie ma dodatkowo dostęp do pracownika. Kontrola użytkownika nie wyklucza personalizacji, lecz pomaga ograniczać skutki błędnych założeń. Właśnie takie połączenie technologii i odpowiedzialnego procesu sprzyja użyteczności rozwiązań.
