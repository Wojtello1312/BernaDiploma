# WSTĘP

Handel internetowy zmienił sposób poszukiwania produktów oraz kontaktowania się klientów ze sprzedawcami. Oferta jest dostępna przez całą dobę, często z poziomu telefonu komórkowego. Możliwe staje się porównywanie cen, czytanie opinii oraz sprawdzanie dostępności wielu produktów, a jednocześnie duży wybór może utrudniać podjęcie decyzji. Klient potrzebuje więc pomocy w znalezieniu rozwiązania odpowiadającego jego sytuacji. Taką funkcję mogą pełnić odpowiednio zaprojektowane narzędzia personalizacji.

Personalizacja oznacza dopasowanie treści, oferty lub obsługi do informacji dotyczących odbiorcy, jednak nie ogranicza się do wyświetlania imienia w wiadomości wysyłanej przez sklep. Obejmuje również kolejność produktów, dobór komunikatów oraz sposób prowadzenia rozmowy z klientem. Jej znaczenie można rozpatrywać na poszczególnych etapach ścieżki zakupowej. Dopasowanie może ułatwiać wybór produktu, ale także późniejsze korzystanie z pomocy. Relacja ze sklepem nie kończy się bowiem w chwili opłacenia zamówienia.

Rozwój sztucznej inteligencji poszerza możliwości przetwarzania informacji potrzebnych do takiego dopasowania, a system może wykorzystywać historię zakupów, cechy produktów lub treść zadanych pytań. Na tej podstawie tworzone są rekomendacje, przewidywania oraz odpowiedzi kierowane do użytkownika, co jednak nie oznacza pełnego poznania jego potrzeb. Dane zawierają jedynie wybrane ślady zachowania, które wymagają ostrożnej interpretacji. Zakup prezentu nie musi świadczyć o osobistych zainteresowaniach kupującego.

Zastosowanie AI wiąże się również z problemami dotyczącymi prywatności i odpowiedzialności. Trafna sugestia może zostać dobrze przyjęta, natomiast nadmiernie szczegółowa wywołać niepokój, a klient może nie rozumieć, skąd sklep uzyskał informacje wykorzystane podczas kontaktu. Znaczenie ma zatem zarówno użyteczność rozwiązania, jak też sposób jego działania, dlatego korzyści sprzedażowe należy zestawiać z jakością relacji. Sam wzrost liczby kliknięć nie potwierdza jeszcze wzrostu zaufania.

Celem pracy jest analiza zastosowania sztucznej inteligencji do personalizacji relacji z klientami sklepów internetowych. Ocenie podlegają mechanizmy działania, możliwe korzyści oraz ograniczenia wybranych rozwiązań. Uwzględniono perspektywę przedsiębiorstwa i odbiorcy jego oferty. Problem badawczy ujęto następująco: w jaki sposób AI wspiera personalizację relacji w handlu internetowym? Dodatkowo rozpatrzono warunki, od których zależy przydatność takich zastosowań.

Przyjęto cztery pytania szczegółowe. Pierwsze dotyczy mechanizmów wykorzystywanych do dopasowywania oferty, komunikacji oraz obsługi klienta. Drugie odnosi się do różnicy między efektem sprzedażowym a jakością relacji. Trzecie obejmuje ograniczenia techniczne, prawne i etyczne występujące podczas stosowania AI. Czwarte dotyczy wniosków wynikających z porównania wybranych przypadków rynkowych.

Sformułowano hipotezę, że personalizacja wspierana przez AI może poprawiać trafność oferty oraz jakość relacji. Korzyści te zależą jednak od jakości danych i sposobu wdrożenia rozwiązania, przy czym znaczenie mają również przejrzystość działania oraz poszanowanie prywatności klientów. Hipoteza ma charakter warunkowy. Jej ocena nie polega na przyjęciu, że każda personalizacja przynosi pozytywny wynik.

Praca ma charakter teoretyczno-analityczny. Zastosowano przegląd wybranej literatury oraz porównanie opisanych publicznie zastosowań rynkowych. Dobór materiałów jest celowy i obejmuje podstawy technologiczne, marketing oraz ochronę danych. Uwzględniono także dokumenty instytucjonalne i materiały publikowane przez przedsiębiorstwa, jednak nie przeprowadzono własnej ankiety ani eksperymentu z udziałem klientów. Nie wykorzystano również dostępu do wewnętrznych danych analizowanych firm.

Analiza przypadków służy porównaniu problemów biznesowych oraz sposobów wykorzystania danych i algorytmów, jednak nie jest pomiarem udziału AI we wszystkich wynikach finansowych przedsiębiorstwa. Materiały firmowe pozwalają opisywać deklarowane funkcje, lecz wymagają ostrożności przy ocenianiu skuteczności. Wnioski dotyczą zatem przedstawionych zastosowań i dostępnych przesłanek. Ocena hipotezy ma charakter jakościowy, bez statystycznego testowania zależności przyczynowych.

Konstrukcja pracy obejmuje pięć rozdziałów. W pierwszym wyjaśniono podstawowe pojęcia AI oraz technologie wspierające jej rozwój. Drugi dotyczy handlu internetowego, procesu zakupowego i miejsca personalizacji w marketingu. W trzecim omówiono rekomendacje, analitykę predykcyjną, obsługę konwersacyjną i integrację systemów. Rozdział czwarty obejmuje zachowania konsumentów oraz ograniczenia prawne, etyczne i techniczne. W piątym przedstawiono wybrane przypadki oraz wynikające z ich porównania wnioski.

Zakres pracy odpowiada problematyce zarządzania ze specjalnością informatyka gospodarcza. Rozwiązania techniczne opisano w stopniu potrzebnym do oceny ich zastosowań biznesowych, jednak nie przedstawiono instrukcji budowy modeli ani szczegółowej dokumentacji programistycznej. Szczególną uwagę poświęcono powiązaniu działania systemu z potrzebami konkretnego klienta. Taka perspektywa pozwala ocenić personalizację szerzej niż wyłącznie przez wzrost sprzedaży.


# ROZDZIAŁ 1. SZTUCZNA INTELIGENCJA

## 1.1. Definicje i ewolucja pojęcia sztucznej inteligencji

Sztuczna inteligencja jest związana z tworzeniem systemów wykonujących zadania wymagające przetwarzania informacji. Obejmuje między innymi rozpoznawanie wzorców, wnioskowanie, uczenie się oraz analizowanie języka, nie istnieje jednak jeden praktyczny mechanizm odpowiadający wszystkim tym zadaniom. Pod wspólną nazwą występują różne metody, których zastosowanie zależy od problemu. W handlu internetowym mogą one wspierać wyszukiwanie produktów, rekomendacje i obsługę klientów.

McCarthy określał AI jako naukę i inżynierię tworzenia inteligentnych maszyn (McCarthy, 2007). Definicja ta podkreśla zarówno poznawczy, jak i praktyczny charakter rozwijanej dziedziny. Obejmuje badanie sposobów rozwiązywania problemów oraz budowanie systemów wykonujących określone zadania, jednak nie oznacza przy tym, że maszyna musi myśleć dokładnie jak człowiek. Dla przedsiębiorstwa ważniejsza jest przydatność rozwiązania niż podobieństwo jego działania do ludzkiego rozumowania.

W praktyce biznesowej należy oddzielać możliwości konkretnego systemu od ogólnych wyobrażeń dotyczących AI. Program rekomendujący obuwie nie musi rozumieć wszystkich aspektów zachowania konsumenta, lecz może jedynie wykrywać zależności między oglądanymi produktami i wcześniejszymi transakcjami. Zakres jego działania wynika z danych, przyjętego celu i zastosowanej metody. Przekroczenie tych granic zwiększa ryzyko błędnej interpretacji uzyskanego wyniku.

Istotnym obszarem sztucznej inteligencji jest uczenie maszynowe, określane skrótem ML. Polega ono na wyznaczaniu zależności na podstawie przykładów zawartych w danych, a model może uczyć się rozpoznawania kategorii produktu albo przewidywania kolejnego zakupu. Zamiast ręcznie zapisywać wszystkie reguły, określa się sposób uczenia i kryterium oceny, chociaż nadal konieczne pozostaje przygotowanie danych oraz kontrolowanie jakości rozwiązania.

Uczenie maszynowe nie jest więc zewnętrzną technologią wspierającą sztuczną inteligencję. Stanowi jedną z grup metod należących do tego obszaru. Takie rozróżnienie ma znaczenie podczas opisywania infrastruktury wykorzystywanej przez przedsiębiorstwa. Procesor, chmura obliczeniowa i biblioteka programistyczna wspierają wykonywanie obliczeń, natomiast sam model uczenia maszynowego realizuje określone zadanie związane z analizą danych.

W uczeniu nadzorowanym wykorzystywane są przykłady zawierające oczekiwany wynik działania modelu, na przykład wiadomości oznaczone jako pytania dotyczące dostawy albo zwrotu. System uczy się następnie przypisywać podobne kategorie kolejnym zgłoszeniom klientów. W uczeniu nienadzorowanym poszukuje się struktury bez gotowych odpowiedzi dla każdego przykładu. Możliwe staje się na przykład grupowanie podobnych zachowań zakupowych.

Ważnym pojęciem jest także automatyzacja, która nie musi oznaczać wykorzystania AI. Wiadomość wysyłana po opłaceniu zamówienia może wynikać z prostej reguły. Podobnie działa przypomnienie o porzuconym koszyku uruchamiane po określonym czasie. System wykorzystujący ML może dodatkowo wybierać odbiorcę, moment lub treść wiadomości. Różnica dotyczy sposobu wyznaczania działania, a nie samego faktu użycia komputera.

Rozwój AI obejmował podejścia oparte na regułach, danych oraz coraz bardziej rozbudowanych modelach, co nie oznacza całkowitego zastąpienia wcześniejszych metod przez rozwiązania nowsze. W wielu procesach nadal przydatne są proste warunki i ograniczenia biznesowe, a model może ustalać kolejność produktów, natomiast reguła wykluczać towary chwilowo niedostępne. Takie połączenie pozwala dostosować wynik do rzeczywistych warunków sprzedaży.

W kontekście zarządzania ważne jest zatem pytanie o zadanie realizowane przez AI. Huang i Rust rozpatrują jej zastosowania w różnych działaniach marketingowych (Huang, Rust, 2021), przy czym obejmują one przetwarzanie informacji oraz wspieranie decyzji dotyczących kontaktu z odbiorcami. Zastosowanie technologii powinno wynikać z rozpoznanego problemu, a nie samej dostępności narzędzia. W przeciwnym razie można uzyskać kosztowny system o niewielkiej wartości dla klientów.

## 1.2. AI w handlu elektronicznym

Handel elektroniczny obejmuje transakcje, w których zamówienie jest składane przez sieci komputerowe, jednak nie wymaga to elektronicznej postaci samego produktu ani dostarczenia go przez Internet. Zakup odzieży przez stronę sklepu pozostaje przykładem e-commerce, mimo fizycznej dostawy. OECD wskazuje na znaczenie sposobu składania zamówienia przy definiowaniu tego obszaru (OECD, 2019). Rozróżnienie to ułatwia analizę procesów poprzedzających transakcję oraz następujących po niej.

Rozwój handlu internetowego zwiększył znaczenie informacji dostępnych podczas kontaktu ze sklepem. Rejestrowane mogą być zapytania, wyświetlenia produktów, dodania do koszyka i zakupy, jednak nie każda informacja jest równie przydatna przy poznawaniu potrzeb odbiorcy. Samo otwarcie strony produktu może wynikać z pomyłki lub zwykłej ciekawości, dlatego dopiero zestawienie zdarzeń pozwala formułować ostrożne przypuszczenia dotyczące zainteresowania ofertą.

Historia transakcji dostarcza innych informacji niż zachowanie podczas aktualnej wizyty. Poprzedni zakup opisuje podjętą decyzję, ale nie musi odzwierciedlać obecnego celu. Osoba regularnie kupująca książki może właśnie poszukiwać prezentu dla małego dziecka. Nadmierne przywiązanie systemu do jej dawnych wyborów ograniczy użyteczność rekomendacji, dlatego personalizacja powinna uwzględniać możliwość zmiany potrzeb i kontekstu.

Wczesne rekomendacje internetowe nie sprowadzały się wyłącznie do ręcznie zapisanych reguł. Opis systemu Amazon wskazywał na wykorzystanie podobieństwa między kupowanymi produktami (Linden, Smith, York, 2003). Było to rozwiązanie korzystające z obserwowanych wzorców współwystępowania interakcji, dlatego nie należy przedstawiać całej historii rekomendacji jako prostego przejścia od reguł do inteligencji. Rozwijano różne metody, odpowiadające odmiennym warunkom i ograniczeniom technicznym.

Obecnie obszary zastosowania AI można powiązać z etapami działania sklepu internetowego. Przed zakupem system pomaga wyszukać produkt oraz porównać dostępne możliwości. Podczas transakcji może dopasowywać informacje potrzebne do zakończenia zamówienia. Po zakupie wspiera odpowiadanie na pytania i porządkowanie zgłoszeń serwisowych, jednak nie każda z tych funkcji wymaga takiego samego modelu.

Dane wykorzystywane przez systemy mogą przyjmować postać tabel, tekstów lub obrazów. Katalog produktów zawiera ceny, parametry techniczne, opisy oraz fotografie przedmiotów. Opinie klientów dostarczają informacji o doświadczeniach, lecz bywają niepełne i niejednoznaczne. Analiza języka może pomagać porządkować takie materiały według poruszanych tematów, nie gwarantuje jednak prawidłowego rozpoznania ironii lub kontekstu każdej wypowiedzi.

Z perspektywy przedsiębiorstwa AI może usprawniać wykonywanie zadań występujących na dużą skalę, co dotyczy zwłaszcza selekcji informacji oraz ustalania kolejności wielu dostępnych ofert. Sklep z niewielkim asortymentem może jednak osiągać dobre wyniki prostszymi metodami. Koszt zaawansowanej personalizacji nie zawsze znajduje uzasadnienie w wartości dodatkowego dopasowania. Ocena powinna obejmować zarówno korzyści, jak też utrzymanie rozwiązania.

Nie należy również utożsamiać cyfrowego śladu z pełną wiedzą o użytkowniku. Zwykła witryna nie uzyskuje automatycznie informacji o kierunku jego spojrzenia. Pomiar wzroku wymaga odpowiedniego sprzętu lub dodatkowych rozwiązań oraz odrębnej oceny prawnej. Dostępność określonej technologii nie dowodzi jej powszechnego stosowania w sklepach. Opis możliwości powinien pozostawać oddzielony od opisu rzeczywiście udokumentowanego wdrożenia.

## 1.3. Technologie wspierające rozwój AI

Działanie systemów AI zależy od infrastruktury, danych oraz narzędzi wykorzystywanych przez twórców. Samo zwiększenie ilości informacji nie zapewnia jednak poprawy jakości modelu. Dane mogą zawierać błędy, powtórzenia albo nieaktualne opisy oferowanych produktów, a mogą też pomijać określone grupy klientów lub nietypowe sposoby korzystania ze sklepu. Przygotowanie materiału pozostaje zatem równie ważne jak dostępna moc obliczeniowa.

Procesory centralne, określane jako CPU, wykonują wiele różnorodnych zadań systemu komputerowego. Współczesne układy wykorzystują również wielordzeniowość i różne formy przetwarzania równoległego, nie jest więc poprawne traktowanie ich jako urządzeń działających wyłącznie szeregowo. Procesory graficzne, czyli GPU, są natomiast szczególnie przydatne przy niektórych powtarzalnych obliczeniach, co dotyczy między innymi operacji wykonywanych podczas uczenia sieci neuronowych.

Zastosowanie GPU może skracać obliczenia, lecz skala korzyści zależy od konkretnego zadania. Znaczenie mają rozmiar modelu, sposób przygotowania danych oraz dostępna pamięć urządzenia, jednak nie każde rozwiązanie personalizacyjne wymaga własnego serwera wyposażonego w akcelerator. Prosty model rekomendacji może działać na innych zasobach lub jako usługa. Dobór sprzętu powinien wynikać z pomiaru rzeczywistego obciążenia systemu.

Rozwijane są również wyspecjalizowane układy przeznaczone do operacji związanych z uczeniem maszynowym. Przykładem są procesory tensorowe TPU, opisane przez Jouppiego i współautorów (Jouppi i in., 2017). Ich konstrukcję dopasowano do określonych obliczeń wykonywanych przez sieci neuronowe. Pokazuje to rosnące znaczenie sprzętu projektowanego pod konkretne grupy zadań, nie oznacza jednak, że TPU stanowi konieczny element każdego sklepu korzystającego z AI.

Ważną rolę odgrywa chmura obliczeniowa, pozwalająca korzystać z zasobów udostępnianych jako usługa. Definicja NIST wskazuje między innymi dostęp na żądanie oraz elastyczność zasobów (Mell, Grance, 2011). Przedsiębiorstwo może dzięki temu dostosowywać wykorzystanie infrastruktury do bieżącego zapotrzebowania, ale nie musi samodzielnie utrzymywać całego zaplecza technicznego potrzebnego do prowadzenia obliczeń. Nadal odpowiada jednak za właściwe skonfigurowanie usług i kontrolowanie kosztów.

W sklepie internetowym obciążenie może zmieniać się zależnie od sezonu lub promocji. Elastyczna infrastruktura ułatwia obsługę okresów zwiększonego zainteresowania produktami. Rozliczenie usług wymaga jednak uwzględnienia transferu danych, przechowywania informacji i liczby zapytań. Niska cena pojedynczego wywołania modelu może dawać znaczny koszt przy dużym ruchu, dlatego opłacalność należy szacować dla całego procesu, a nie jednej operacji.

Tworzenie modeli wspierają również biblioteki i środowiska programistyczne. TensorFlow oraz PyTorch dostarczają narzędzi do definiowania i wykonywania obliczeń (Abadi i in., 2016; Paszke i in., 2019). Ułatwiają pracę nad modelami, lecz nie zastępują przygotowania danych i oceny wyników. Informacje projektowe są dostępne odpowiednio na stronach tensorflow.org oraz pytorch.org. Wykorzystanie biblioteki nie jest jeszcze dowodem jakości stworzonego z jej pomocą systemu.

Znaczenie ma także integracja infrastruktury z codziennym działaniem przedsiębiorstwa. Model potrzebuje dostępu do aktualnego katalogu oraz informacji o dostępności produktów. Wynik powinien dotrzeć do witryny w czasie akceptowalnym dla użytkownika. Nawet trafna rekomendacja straci wartość, jeśli znacznie opóźni otwarcie strony. Ocena technologii powinna więc obejmować cały przepływ informacji, od danych do kontaktu z klientem.

## 1.4. Sieci neuronowe, transformery i modele generatywne

Uczenie głębokie jest grupą metod wykorzystujących wielowarstwowe sieci neuronowe do analizy danych. Kolejne warstwy przekształcają informacje, tworząc reprezentacje przydatne przy realizacji określonego zadania. W analizie obrazu mogą one pomagać rozpoznawać cechy widocznych produktów. W analizie tekstu wspierają przetwarzanie zależności występujących między słowami. Rozwój tych metod opisują LeCun, Bengio i Hinton (LeCun, Bengio, Hinton, 2015).

Przykładem zastosowania w sklepie może być wyszukiwanie produktów podobnych do przesłanej fotografii. System porównuje cechy obrazu z reprezentacjami fotografii dostępnych w katalogu. Podobieństwo wizualne nie musi jednak oznaczać zgodności rozmiaru, materiału czy przeznaczenia, dlatego wynik analizy obrazu powinien być łączony z danymi opisującymi produkt. Dopiero taki zestaw informacji może ułatwiać podjęcie praktycznej decyzji zakupowej.

Istotną zmianę w przetwarzaniu języka przyniosła architektura transformera. Jej opis przedstawili Vaswani i współautorzy w pracy poświęconej mechanizmowi uwagi (Vaswani i in., 2017). Mechanizm ten pozwala uwzględniać związki między elementami przetwarzanej sekwencji. Znaczenie słowa może być oceniane z uwzględnieniem pozostałych części wypowiedzi. Ułatwia to tworzenie reprezentacji potrzebnych między innymi podczas przetwarzania zapytań tekstowych.

Modele generatywne mogą tworzyć tekst, obrazy lub inne rodzaje treści. W handlu internetowym wykorzystuje się je między innymi do prowadzenia rozmów, a klient może opisać potrzebę zwykłym językiem, zamiast wybierać wiele oddzielnych filtrów. System interpretuje wypowiedź i przygotowuje odpowiedź dopasowaną do dostępnego kontekstu. Jakość odpowiedzi zależy jednak również od informacji, którymi model rzeczywiście dysponuje.

Płynność wypowiedzi nie stanowi gwarancji prawdziwości podanych informacji, a model może wygenerować nieistniejącą cechę produktu lub błędnie opisać zasady zwrotu. W zastosowaniu sklepowym potrzebne jest więc powiązanie odpowiedzi z aktualnymi dokumentami. Wykorzystywane materiały mogą obejmować katalog, regulamin oraz informacje o konkretnym zamówieniu. Takie ograniczenie zmniejsza zakres swobodnego generowania, choć nie usuwa wszystkich możliwych błędów.

W praktyce należy rozdzielać zadania językowe od podejmowania decyzji wywołujących skutki finansowe, a model może przygotować odpowiedź dotyczącą zwrotu, ale zatwierdzenie operacji wymaga kontroli uprawnień. Podobnie sugestia produktu nie powinna samodzielnie zmieniać zawartości opłaconego zamówienia. Możliwości techniczne trzeba połączyć z jasno określoną odpowiedzialnością za działanie systemu, dzięki czemu AI może wspierać obsługę, zachowując przewidywalność procesu zakupowego.


# ROZDZIAŁ 2. PERSONALIZACJA W MARKETINGU CYFROWYM

## 2.1. Rozwój handlu internetowego i przebieg procesu zakupowego

Poszukiwanie produktu w Internecie może rozpocząć się poza stroną konkretnego sklepu. Klient korzysta z wyszukiwarki, porównywarki, mediów społecznościowych albo polecenia innej osoby. Na każdym z tych etapów otrzymuje informacje wpływające na dalszą decyzję, dlatego sama witryna sprzedażowa jest częścią szerszego otoczenia zakupowego. Jej skuteczność zależy także od zgodności informacji przekazywanych w pozostałych kanałach.

OECD opisuje handel elektroniczny jako obszar obejmujący różne modele i uczestników rynku (OECD, 2019). Obok sklepów prowadzonych przez pojedyncze przedsiębiorstwa funkcjonują platformy skupiające wielu sprzedawców. W takim modelu klient ocenia zarówno platformę, jak też konkretnego dostawcę produktu. Zadowolenie z wyszukiwania może współistnieć z niezadowoleniem dotyczącym realizacji zamówienia. Personalizacja interfejsu nie usuwa problemów związanych z jakością pozostałych etapów obsługi.

Proces zakupowy można rozpatrywać od rozpoznania potrzeby do oceny otrzymanego produktu. Początkowo klient może znać jedynie problem wymagający rozwiązania, bez określenia konkretnej marki. Następnie porównuje dostępne możliwości, analizując ceny, cechy oraz warunki dostawy, a dopiero później wybiera ofertę i podejmuje decyzję o złożeniu zamówienia. Po zakupie ocenia zgodność produktu z oczekiwaniami oraz jakość kontaktu ze sprzedawcą.

W rzeczywistości proces ten nie zawsze przebiega w sposób uporządkowany i liniowy, a użytkownik może wracać do wcześniejszych etapów, zmieniać urządzenie albo odkładać decyzję. Czasami porównuje produkty online, lecz kupuje je później w sklepie stacjonarnym. Innym razem ogląda produkt na miejscu, a zamówienie składa przez Internet, dlatego pojedyncza sesja na stronie nie przedstawia całej relacji z klientem.

Lemon i Verhoef podkreślają znaczenie doświadczenia budowanego przez różne punkty kontaktu (Lemon, Verhoef, 2016), przy czym obejmuje ono etapy poprzedzające zakup, sam zakup oraz późniejsze interakcje. Z tej perspektywy personalizacja powinna wspierać ciągłość doświadczenia, a nie jedynie pojedynczy komunikat. Propozycja zakupu kolejnego produktu może być niewłaściwa, gdy poprzednia reklamacja pozostaje nierozwiązana. Znajomość historii kontaktu powinna zatem pomagać również w powstrzymywaniu zbędnych działań sprzedażowych.

Poszczególne etapy wiążą się z odmiennym rodzajem potrzeb informacyjnych. Przed zakupem ważne mogą być porównanie parametrów i wyjaśnienie różnic pomiędzy wariantami. Podczas finalizacji zamówienia większe znaczenie mają koszty dostawy oraz przewidywany termin odbioru. Później klient potrzebuje informacji o użytkowaniu, zwrocie albo zgłoszeniu problemu. Dopasowanie treści powinno odnosić się do tak rozpoznanego zadania.

Tabela 2.1 przedstawia potrzeby klienta oraz przykładowe sposoby dopasowania na kolejnych etapach relacji.

**Tabela 2.1. Personalizacja na kolejnych etapach relacji z klientem**

| Etap | Potrzeba odbiorcy | Możliwe dopasowanie | Ryzyko błędnego działania |
|---|---|---|---|
| Rozpoznanie potrzeby | Określenie odpowiedniej kategorii | Pytania pomocnicze i dobór treści | Zbyt wczesne ograniczenie wyboru |
| Porównanie ofert | Zrozumienie różnic | Kolejność produktów i zestawienie cech | Promowanie marży zamiast przydatności |
| Zakup | Sprawne złożenie zamówienia | Informacje zgodne z aktualnym koszykiem | Zbędne sugestie utrudniające finalizację |
| Obsługa po zakupie | Rozwiązanie konkretnej sprawy | Odpowiedź uwzględniająca zamówienie | Błędne rozpoznanie uprawnień klienta |
| Kolejny kontakt | Utrzymanie użytecznej relacji | Dopasowana częstotliwość komunikacji | Natarczywość i spadek zaufania |

Źródło: opracowanie własne na podstawie Lemon i Verhoefa (2016).

Zestawienie pokazuje, że ten sam mechanizm nie będzie właściwy w każdej sytuacji. Odbiorca poszukujący inspiracji może doceniać różnorodne propozycje związane z jego zainteresowaniami. Osoba zgłaszająca uszkodzenie produktu oczekuje przede wszystkim sprawnego rozwiązania konkretnego problemu. W drugim przypadku dodatkowa oferta może zostać odebrana jako brak zainteresowania reklamacją. Wartość personalizacji zależy więc od właściwego rozpoznania momentu kontaktu.

## 2.2. Rola personalizacji w zarządzaniu relacjami z klientami

Personalizacja jest jednym ze sposobów dostosowywania działań marketingowych do odbiorców przedsiębiorstwa. Jej celem może być ułatwienie wyboru, poprawa komunikacji albo podtrzymanie zainteresowania ofertą, ale nie należy traktować jej jako samodzielnej strategii rozwiązującej wszystkie problemy sklepu. Dopasowany komunikat nie zastąpi dobrej jakości produktu i terminowej dostawy. Powinien wspierać szerszy sposób zarządzania relacjami z klientami.

Podejście CRM obejmuje procesy związane z budowaniem i utrzymywaniem takich relacji, jednak nie jest to wyłącznie nazwa programu przechowującego kontakty oraz historię transakcji. Payne i Frow przedstawiają CRM jako podejście wymagające powiązania różnych procesów organizacyjnych (Payne, Frow, 2005). Obejmuje ono między innymi tworzenie wartości oraz zarządzanie informacją. System informatyczny wspiera te działania, ale nie określa samodzielnie ich celu.

W praktyce personalizacja wymaga połączenia wiedzy o kliencie z odpowiednią decyzją działania. Informacja o wcześniejszym zakupie może pomóc dobrać akcesorium pasujące do produktu. Wiadomość o nierozwiązanej reklamacji powinna natomiast wpływać na sposób prowadzenia kolejnego kontaktu. Samo zgromadzenie danych nie gwarantuje ich właściwego wykorzystania przez przedsiębiorstwo, dlatego potrzebne są reguły określające, kiedy dane rzeczywiście służą klientowi.

Należy odróżnić personalizację od segmentacji odbiorców. Segmentacja polega na podziale klientów według wybranych cech lub podobnych zachowań. Jedną grupę mogą tworzyć osoby kupujące regularnie produkty określonej kategorii. Skierowanie wspólnej oferty do takiej grupy nie musi jeszcze oznaczać indywidualnego dopasowania. Personalizacja może uwzględniać bardziej szczegółowy kontekst konkretnego kontaktu.

Odrębnym rozwiązaniem jest dostosowanie dokonywane samodzielnie przez użytkownika. Klient może wybrać ulubione kategorie, rozmiar odzieży albo częstotliwość otrzymywania wiadomości, dzięki czemu preferencja jest zadeklarowana, zamiast zostać wyłącznie przewidziana przez algorytm. Oba podejścia można łączyć, zachowując możliwość poprawienia błędnego założenia systemu. Deklaracja użytkownika może też pomóc ograniczyć problem braku wcześniejszych danych.

Korzyści przedsiębiorstwa i klienta nie zawsze są jednakowe. Sklep może dążyć do zwiększania wartości koszyka, podczas gdy klient chce ograniczyć wydatki. Zbyt silne ukierunkowanie rekomendacji na marżę może pogarszać trafność otrzymywanych propozycji. Z kolei całkowite pominięcie kosztów prowadzenia działalności utrudnia utrzymanie usługi, dlatego potrzebne jest jawne określenie kompromisów podczas projektowania sposobu rekomendowania produktów.

Praktyczne znaczenie ma również częstotliwość kontaktu. Dopasowanie tematu wiadomości nie usprawiedliwia wysyłania jej zbyt często. Kilka trafnych propozycji może pomagać, natomiast codzienne przypomnienia mogą wywoływać zniecierpliwienie. Ocena personalizacji powinna obejmować także rezygnacje z komunikacji i zgłoszone skargi. W ten sposób uwzględnia się koszty relacyjne niewidoczne w samym wskaźniku otwarć.

Przyjęta w pracy perspektywa zakłada podporządkowanie personalizacji rzeczywistym zadaniom odbiorcy. Wartość rozwiązania ujawnia się wtedy, gdy zmniejsza wysiłek albo poprawia jakość informacji. Dodatkowa sprzedaż może towarzyszyć takiej zmianie, ale nie stanowi jej jedynego uzasadnienia. Odpowiednie dopasowanie powinno również pozwalać zakończyć kontakt po rozwiązaniu sprawy. Utrzymywanie użytkownika w interfejsie za wszelką cenę nie jest tożsame z dobrą obsługą.

## 2.3. Metody i narzędzia personalizacji

Najprostsze metody personalizacji wykorzystują wcześniej ustalone warunki oraz dane podane przez klienta. Sklep może wyświetlać odpowiednią wersję językową lub zapamiętać wybrany sposób dostawy, a także pomijać produkty, które nie występują w zadeklarowanym rozmiarze. Rozwiązania tego rodzaju bywają przydatne bez zastosowania zaawansowanych modeli uczenia maszynowego. Ich zaletą jest przewidywalność oraz stosunkowo łatwe wyjaśnienie sposobu działania.

Bardziej złożone dopasowanie wykorzystuje historię zachowania i zależności wykrywane w danych. Kolejność ofert może zależeć od oglądanych kategorii, cen albo wcześniejszych zakupów. Model porównuje dostępne informacje z podobnymi sytuacjami zaobserwowanymi w przeszłości. Wynik ma charakter przewidywania, a nie pewnej wiedzy o intencjach użytkownika, dlatego powinien pozostawiać możliwość samodzielnego wyszukania innych produktów.

Personalizacja może dotyczyć także samego sposobu prezentowania informacji. Osobie porównującej urządzenia przydatne będzie zestawienie parametrów technicznych w uporządkowanej tabeli. Klient poszukujący inspiracji może natomiast lepiej wykorzystać przykłady zastosowania danego produktu, jednak nie chodzi wówczas o zmianę jego cech, lecz formy przedstawienia oferty. Treść musi pozostawać zgodna z rzeczywistymi właściwościami przedmiotu sprzedaży.

W działaniach marketingowych stosuje się również dopasowywanie komunikacji poza stroną sklepu, obejmujące wiadomości elektroniczne, powiadomienia aplikacji lub reklamy kierowane do odbiorców. Skuteczność takiego kontaktu zależy od treści, chwili i miejsca jego wyświetlenia. Bleier i Eisenbeiss analizują właśnie znaczenie kontekstu personalizowanej reklamy internetowej (Bleier, Eisenbeiss, 2015). Wyników dotyczących reklamy nie należy jednak automatycznie przenosić na całą obsługę klienta.

Przykładem ilustracyjnym może być ponowne pokazanie wcześniej oglądanego plecaka. Wiadomość wysłana podczas aktywnego porównywania ofert może ułatwić powrót do produktu. Ta sama propozycja po zakończeniu zakupu może okazać się zbędna lub irytująca. Przydatniejsze byłoby wtedy wyjaśnienie sposobu konserwacji albo dopasowanie akcesorium. Przykład pokazuje znaczenie aktualności informacji, nie przedstawia wyniku badania konkretnej firmy.

Dobór narzędzi powinien uwzględniać źródło i jakość wykorzystywanych danych. Dane deklarowane pochodzą bezpośrednio z informacji przekazanych przez klienta. Dane obserwowane opisują jego działania podczas korzystania z usługi. Dane wywnioskowane stanowią rezultat analizy i mogą zawierać błędne przypuszczenia. Rozróżnienie tych kategorii ułatwia ocenę, jak pewna jest podstawa danego dopasowania.

Błąd może powstać również podczas łączenia informacji z różnych urządzeń. Z jednego konta lub komputera mogą korzystać członkowie tej samej rodziny. Algorytm potraktuje wtedy odmienne potrzeby jako historię jednego użytkownika. Podobny problem występuje przy zakupach realizowanych służbowo i prywatnie. Udostępnienie możliwości zmiany profilu zainteresowań pomaga ograniczyć takie nieporozumienia.

Istotnym elementem projektu jest także porównanie rozwiązania z prostym punktem odniesienia. Może nim być lista popularnych produktów albo standardowa kolejność wyników wyszukiwania, dlatego dopiero różnica względem takiego wariantu pokazuje dodatkową wartość personalizacji. Sam fakt działania modelu nie przesądza, że poprawia on doświadczenie użytkownika. Szczegółowe metody oceny omówiono w kolejnych częściach pracy.

## 2.4. Oczekiwania klientów i granice dopasowania

Oczekiwania klientów są zróżnicowane, dlatego nie należy przypisywać wszystkim identycznych preferencji. Część odbiorców docenia podpowiedzi, a inni wolą samodzielnie przeglądać pełną ofertę, przy czym znaczenie ma charakter zakupu, wcześniejsze doświadczenie oraz wrażliwość przetwarzanych informacji. Rekomendowanie książki może być oceniane inaczej niż sugerowanie produktu związanego ze zdrowiem. Różny może być też poziom akceptacji dla wykorzystywania historii zachowania.

Badania nad paradoksem personalizacji wskazują na napięcie między dopasowaniem a prywatnością. Aguirre i współautorzy analizują znaczenie zbierania informacji oraz działań budujących zaufanie (Aguirre i in., 2015). Samo zwiększanie szczegółowości danych nie zapewnia zatem lepszego odbioru reklamy, przy czym ważne jest również to, czy sposób ich pozyskania jest zrozumiały. Klient ocenia nie tylko propozycję, lecz także warunki powstania komunikatu.

Odbiorca może oczekiwać wygody bez konieczności ujawniania dużej liczby informacji osobistych. Te dwa cele bywają trudne do pełnego pogodzenia w jednym rozwiązaniu. Możliwe jest jednak ograniczanie zakresu danych do potrzeb konkretnej funkcji. Rekomendacja oparta na aktualnie oglądanym produkcie nie zawsze wymaga długiej historii użytkownika. Taki wariant może stanowić użyteczny punkt wyjścia dla nowych klientów.

Zrozumiałość działania systemu pomaga ustalić granice właściwych oczekiwań. Informacja, że propozycja wynika z poprzednich zakupów, pozwala ocenić jej podstawę. Możliwość ukrycia nietrafnej kategorii daje natomiast praktyczną kontrolę nad dalszym dopasowaniem, jednak samo obszerne wyjaśnienie regulaminowe nie zastępuje takich funkcji w interfejsie. Przejrzystość powinna być związana z rzeczywistą możliwością działania użytkownika.

Oczekiwania dotyczą również ciągłości obsługi po wystąpieniu problemu, a klient może zaakceptować rozmowę z botem, jeśli uzyska poprawną odpowiedź. Trudniej utrzymać pozytywną ocenę, gdy system powtarza te same nieskuteczne wskazówki, dlatego w takiej sytuacji ważna staje się możliwość przekazania sprawy pracownikowi. Personalizacja powinna zmniejszać konieczność ponownego przedstawiania historii całego zgłoszenia.

Nie każda deklaracja zadowolenia przekłada się na długotrwałą relację ze sklepem. Na powrót klienta wpływają także cena, dostępność produktu i doświadczenia konkurencyjnych ofert. Ocena oczekiwań wymaga więc zestawienia wypowiedzi z odpowiednimi danymi o zachowaniu. W pracy nie przyjęto jednej miary przedstawiającej wszystkie aspekty relacji. Poszczególne wskaźniki interpretowane są zgodnie z celem konkretnego zastosowania.

Przedsiębiorstwo powinno również uwzględniać użytkowników, którzy nie chcą korzystać z personalizacji. Zachowanie użytecznej wyszukiwarki, filtrów i standardowej obsługi ogranicza ich wykluczenie. Rezygnacja z dopasowania nie powinna sama w sobie uniemożliwiać podstawowego zakupu. Z perspektywy zarządzania oznacza to potrzebę projektowania różnych ścieżek kontaktu. Dobre doświadczenie wynika z dostępności odpowiednich możliwości, a nie obowiązkowego używania jednego mechanizmu.


# ROZDZIAŁ 3. ZASTOSOWANIA AI W PERSONALIZACJI RELACJI Z KLIENTAMI

## 3.1. Systemy rekomendacyjne i sposoby dopasowywania produktów

System rekomendacyjny porządkuje dostępne możliwości, aby ułatwić odbiorcy znalezienie odpowiednich produktów, prezentując propozycje na stronie głównej, karcie produktu albo po zakończeniu zakupu. Wybór miejsca ma znaczenie, ponieważ zmienia się aktualne zadanie użytkownika. Innej pomocy potrzebuje osoba rozpoczynająca przeglądanie, a innej klient porównujący dwa modele, dlatego ocena rekomendacji powinna uwzględniać kontekst ich wyświetlenia.

Jedną z podstawowych metod jest filtrowanie oparte na treści produktów. System wykorzystuje cechy przedmiotów, takie jak kategoria, materiał, przeznaczenie albo parametry techniczne. Następnie wyszukuje podobieństwa względem produktów odpowiadających dotychczasowym preferencjom użytkownika. Osobie przeglądającej lekkie plecaki turystyczne można zaproponować modele o zbliżonych właściwościach. Skuteczność takiego podejścia zależy między innymi od jakości opisów w katalogu.

Odmiennym rozwiązaniem jest filtrowanie współpracujące, wykorzystujące wzorce interakcji z wieloma produktami. Zależności mogą dotyczyć podobnych użytkowników albo przedmiotów wybieranych w zbliżonych sytuacjach. System nie musi wtedy opierać się wyłącznie na szczegółowych opisach asortymentu. Potrzebuje natomiast odpowiedniego materiału pokazującego wcześniejsze zachowania i wybory klientów. Podstawowe podejścia oraz ich ograniczenia omawiają Adomavicius i Tuzhilin (Adomavicius, Tuzhilin, 2005).

Wariant opisany przez twórców rekomendacji Amazon wykorzystuje podobieństwo między produktami. Zamiast każdorazowo porównywać klienta ze wszystkimi użytkownikami, można korzystać z przygotowanych powiązań przedmiotów. Następnie dobiera się propozycje na podstawie produktów związanych z daną osobą. Rozwiązanie odpowiadało problemowi skali dużego katalogu oraz licznej grupy klientów (Linden, Smith, York, 2003), nie stanowi jednak opisu wszystkich współczesnych mechanizmów stosowanych przez Amazon.

Podejścia hybrydowe łączą kilka rodzajów informacji potrzebnych do tworzenia rekomendacji. Wykorzystywane mogą być cechy produktów, historia interakcji oraz aktualny kontekst wizyty, co pozwala ograniczać słabości pojedynczej metody, choć zwiększa złożoność rozwiązania. Trudniejsze staje się także ustalenie przyczyny konkretnej propozycji przedstawionej klientowi. Projekt wymaga więc równoczesnej kontroli trafności, szybkości oraz możliwości wyjaśnienia wyniku.

Częstym problemem jest zimny start, czyli niedostatek danych o użytkowniku lub produkcie. Nowy klient nie ma historii zakupów, a świeżo dodany produkt nie zebrał interakcji. System może wtedy wykorzystać deklarowane preferencje, opis przedmiotu albo ogólną popularność. Możliwe jest również dopasowanie wyłącznie do aktualnie oglądanej kategorii, dlatego nie należy przedstawiać zimnego startu jako problemu, którego żadne narzędzie nie potrafi ograniczyć.

Drugie ograniczenie dotyczy nadmiernego powtarzania produktów podobnych do wcześniej oglądanych. Klient otrzymuje trafne, lecz bardzo wąskie propozycje, przez co trudniej odkrywa alternatywy, a system może także utrwalać popularność produktów, które już wcześniej często pokazywano. Powstaje zależność między ekspozycją oferty a danymi służącymi do kolejnego uczenia. W ocenie warto więc uwzględniać różnorodność oraz dostępność mniej oczywistych możliwości.

W tabeli 3.1 porównano podstawy działania oraz ograniczenia najważniejszych podejść do rekomendowania produktów.

**Tabela 3.1. Porównanie podstawowych podejść rekomendacyjnych**

| Podejście | Główna podstawa dopasowania | Przydatność | Ograniczenie |
|---|---|---|---|
| Oparte na treści | Cechy produktów i preferencje | Dopasowanie do opisanych wymagań | Zależność od jakości katalogu |
| Współpracujące | Wzorce interakcji użytkowników | Wykrywanie powiązań zakupowych | Niedostatek danych i popularność |
| Hybrydowe | Połączenie kilku rodzajów informacji | Obsługa różnych sytuacji zakupowych | Większa złożoność oceny i utrzymania |
| Regułowe jako punkt odniesienia | Warunki ustalone przez sklep | Proste i przewidywalne dopasowanie | Ograniczona elastyczność reguł |

Źródło: opracowanie własne na podstawie Adomaviciusa i Tuzhilina (2005) oraz Lindena, Smitha i Yorka (2003).

Trafność rekomendacji można oceniać na danych historycznych albo podczas działania sklepu. Pierwszy wariant pozwala porównywać modele przed udostępnieniem ich klientom, nie pokazuje jednak wszystkich skutków zmiany sposobu prezentowania oferty. Kliknięcie może oznaczać zainteresowanie, ale nie dowodzi zadowolenia z kupionego produktu, dlatego wyniki techniczne trzeba zestawiać z miarami odpowiadającymi celowi biznesowemu i relacyjnemu.

## 3.2. Analityka predykcyjna i dobór działań marketingowych

Analityka predykcyjna służy przewidywaniu zdarzeń na podstawie zależności rozpoznanych w danych. W sklepie może dotyczyć prawdopodobieństwa zakupu, ponownego kontaktu albo rezygnacji z relacji. Wynik modelu pozwala uporządkować sytuacje wymagające uwagi przedsiębiorstwa, nie oznacza jednak, że przewidywane zdarzenie nastąpi z pewnością. Decyzja klienta pozostaje zależna także od okoliczności niewidocznych dla sklepu.

Dobrym przykładem jest przewidywanie zainteresowania ponownym zakupem produktu zużywalnego, a wykorzystywane mogą być odstępy między wcześniejszymi zamówieniami oraz cechy konkretnej kategorii. Na tej podstawie sklep ustala moment przedstawienia przypomnienia o dostępności produktu. Odbiorca może jednak kupić zapas wcześniej albo skorzystać z innego sprzedawcy. Prognoza wymaga więc oceny, czy kontakt rzeczywiście pomaga, zamiast jedynie zwiększać liczbę wiadomości.

Innym zastosowaniem jest rozpoznawanie sygnałów wskazujących na możliwą utratę klienta. Dłuższa przerwa w zakupach może uzasadniać sprawdzenie jakości dotychczasowej obsługi, nie powinna jednak automatycznie prowadzić do wysłania rabatu każdej nieaktywnej osobie. Powodem przerwy może być sezonowość produktu albo naturalnie rzadka potrzeba zakupowa. Właściwa reakcja zależy więc od interpretacji wyniku w kontekście działalności sklepu.

Huang i Rust wskazują szerokie możliwości wykorzystania AI w działaniach marketingowych (Huang, Rust, 2021), przy czym obejmują one analizowanie informacji i wspieranie wyboru odpowiednich działań wobec odbiorców. W praktyce należy jednak oddzielić przewidywanie zachowania od przewidywania skutku interwencji. Klient prawdopodobnie dokonujący zakupu nie musi potrzebować dodatkowej zachęty cenowej. Przyznanie mu rabatu może obniżyć marżę bez zmiany decyzji zakupowej.

Ocena modelu wymaga poprawnego podziału danych używanych podczas jego przygotowania. Informacje powstałe po przewidywanym zdarzeniu nie powinny pomagać w odtwarzaniu wcześniejszej decyzji. Przykładowo potwierdzenie płatności nie może służyć do przewidywania zakupu przed złożeniem zamówienia. Taki błąd tworzyłby pozornie wysoką skuteczność rozwiązania na danych historycznych. Podczas rzeczywistego działania sklepu odpowiednia informacja nie byłaby jeszcze dostępna.

Znaczenie ma również zmiana warunków rynkowych i zachowań odbiorców. Model przygotowany przed zmianą asortymentu może gorzej oceniać zainteresowanie nowymi kategoriami. Sezon promocji tworzy inne wzorce niż okres standardowych cen i dostaw, dlatego potrzebne jest monitorowanie jakości po wdrożeniu oraz możliwość ponownego uczenia. Sam poprawny wynik jednorazowego testu nie kończy pracy nad systemem.

Analityka predykcyjna może też wspierać obsługę bez bezpośredniego zwiększania liczby komunikatów marketingowych. Sygnały opóźnienia dostawy mogą skłonić sklep do wcześniejszego poinformowania klienta. Rozpoznanie powtarzających się pytań pozwala poprawić opis produktu lub instrukcję użytkowania. Takie działania zmniejszają wysiłek odbiorcy i mogą ograniczać liczbę późniejszych zgłoszeń. Wartość wyniku ujawnia się wtedy przez rozwiązany problem, a nie wyłącznie dodatkową transakcję.

Przy podejmowaniu decyzji warto uwzględniać koszt błędnego przewidywania. Niepotrzebne przypomnienie o zakupie zwykle ma inne konsekwencje niż błędna ocena reklamacji. W procesach dotyczących praw klienta potrzebna jest szczególna kontrola decyzji, a model może pomagać porządkować zgłoszenia, lecz nie powinien zastępować rozpatrzenia istotnych okoliczności. Zakres automatyzacji należy dostosować do skutków potencjalnej pomyłki.

## 3.3. Chatboty, voiceboty i personalizacja obsługi

Rozmowa z klientem dostarcza informacji, których nie widać w samym rejestrze kliknięć, a użytkownik może wyjaśnić przeznaczenie produktu, ograniczenie budżetu albo powód niezadowolenia. Chatbot wykorzystuje kanał tekstowy, natomiast voicebot umożliwia kontakt głosowy, jednak nie każdy taki system korzysta z generatywnej sztucznej inteligencji. Część rozwiązań działa według przygotowanych scenariuszy i określonych wariantów odpowiedzi.

Personalizacja obsługi pojawia się wtedy, gdy odpowiedź uwzględnia właściwy kontekst konkretnej sprawy. Może nim być numer zamówienia, etap dostawy lub wcześniej zgłoszony problem, dzięki czemu klient nie musi wielokrotnie podawać tych samych informacji. Warunkiem pozostaje jednak poprawna identyfikacja sprawy oraz odpowiedni dostęp do danych. System nie powinien ujawniać informacji o zamówieniu osobie, która nie ma do nich uprawnień.

W prostych zgłoszeniach przydatne bywają krótkie, jednoznaczne odpowiedzi oparte na danych systemowych, co dotyczy statusu przesyłki, godzin kontaktu albo sposobu pobrania dokumentu sprzedaży. Bardziej złożone pytania wymagają interpretacji kilku informacji i uwzględnienia wyjątków. W takich sytuacjach potrzebna jest możliwość przekazania rozmowy do pracownika. Personalizacja powinna ułatwiać to przekazanie wraz z dotychczasowym kontekstem zgłoszenia.

Badanie Luo i współautorów pokazuje znaczenie ujawnienia, że rozmówcą jest chatbot (Luo i in., 2019). Wskazuje ono, że sposób przedstawienia systemu może wpływać na zachowanie odbiorców, nie stanowi jednak uzasadnienia dla ukrywania automatycznego charakteru obsługi. Wdrożenie wymaga uwzględnienia obowiązków informacyjnych oraz długoterminowego zaufania klientów. Wynik pojedynczego badania sprzedażowego nie rozstrzyga wszystkich kwestii prawnych i etycznych.

Adam, Wessel i Benlian analizują zachowanie użytkowników w kontakcie z chatbotami obsługowymi (Adam, Wessel, Benlian, 2021). Ich perspektywa wskazuje na znaczenie sposobu projektowania interakcji z systemem. Nie wystarcza zatem samo udostępnienie mechanizmu generującego odpowiedzi na pytania, przy czym ważne są czytelność rozmowy, oczekiwania odbiorcy oraz charakter wykonywanego zadania. Zachowania zaobserwowane w określonym badaniu należy interpretować w jego granicach.

Błędy generatywnego chatbota mogą być trudne do rozpoznania przez klienta. Odpowiedź bywa poprawna językowo, mimo że zawiera nieprawdziwe informacje o produkcie. Szczególnie ryzykowne są pomyłki dotyczące bezpieczeństwa użytkowania, płatności lub uprawnień konsumenta. System powinien korzystać z zatwierdzonych materiałów i sygnalizować brak pewnej odpowiedzi, dlatego konieczne jest również monitorowanie zgłoszeń ujawniających powtarzające się problemy.

W kontakcie głosowym dochodzą ograniczenia rozpoznawania mowy i warunków prowadzenia rozmowy. Hałas, niewyraźna wypowiedź lub nietypowa nazwa produktu mogą powodować błędną interpretację. Powtarzanie pełnego numeru zamówienia przez telefon bywa uciążliwe dla użytkownika, dlatego dobór kanału powinien uwzględniać charakter informacji i potrzeby odbiorcy. Udostępnienie alternatywy tekstowej może poprawiać dostępność całego procesu obsługi.

Ocena chatbota nie powinna ograniczać się do liczby rozmów zakończonych bez pracownika, a klient może przerwać kontakt dlatego, że nie otrzymał skutecznej pomocy. Niski udział przekazań nie musi więc oznaczać wysokiej jakości rozwiązania. Potrzebne są również dane o rozwiązaniu sprawy, ponownych zgłoszeniach i zadowoleniu. Miarę efektywności należy powiązać z rzeczywistym wynikiem dla odbiorcy.

## 3.4. Personalizowane treści i oferty dynamiczne

Treści prezentowane przez sklep mogą zmieniać się zależnie od potrzeb i kontekstu. Inny opis korzyści będzie przydatny początkującemu użytkownikowi, a inny osobie znającej kategorię. Możliwe jest także dopasowanie języka, kolejności informacji oraz sposobu przedstawienia parametrów, co nie oznacza dowolności w opisywaniu produktu. Każda wersja powinna zachowywać zgodność z jego rzeczywistymi właściwościami i warunkami zakupu.

Generatywna AI może pomagać przygotowywać różne wersje tekstów na podstawie zatwierdzonych danych, co wymaga ograniczenia informacji wejściowych do materiałów opisujących rzeczywisty asortyment. Nie należy pozwalać modelowi swobodnie dopisywać certyfikatów, funkcji albo gwarantowanych rezultatów użycia. Kontrola jest szczególnie ważna przy produktach związanych ze zdrowiem i bezpieczeństwem. Odpowiedzialność za komunikat pozostaje po stronie podmiotu przedstawiającego ofertę klientowi.

Oferta dynamiczna może obejmować zmianę kolejności produktów, zestawu akcesoriów albo komunikatu promocyjnego, jednak nie każda taka zmiana jest personalizacją ceny. Cena może zmieniać się z powodu popytu lub dostępności, jednakowo dla wszystkich odbiorców. Personalizacja ceny dotyczy natomiast dopasowania do konkretnej osoby na podstawie informacji o niej. Rozróżnienie to ma znaczenie zarówno analityczne, jak i prawne.

Przykład ilustracyjny może dotyczyć osoby poszukującej laptopa do pracy podczas podróży. System eksponuje wtedy masę urządzenia, czas pracy baterii oraz warunki gwarancji. Innym odbiorcom ten sam produkt można przedstawić przez parametry ekranu i zastosowania domowe. Cena oraz rzeczywiste cechy pozostają niezmienione. Personalizacja dotyczy wyboru informacji potrzebnych w określonym kontekście zakupowym.

Ryzyko pojawia się wtedy, gdy dopasowanie służy wykorzystywaniu podatności konkretnego odbiorcy. Dotyczy to między innymi nadmiernej presji czasowej lub ukrywania istotnych warunków, a system może zwiększać prawdopodobieństwo zakupu, jednocześnie pogarszając jakość decyzji klienta. Ocena nie powinna więc kończyć się na wyniku krótkiej kampanii. Należy uwzględniać skargi, zwroty oraz konsekwencje dla późniejszego zaufania.

Spójność komunikatów jest równie ważna jak trafność pojedynczej wersji tekstu. Strona produktu, chatbot i wiadomość potwierdzająca zakup powinny przekazywać zgodne informacje. Inaczej klient otrzyma różne odpowiedzi dotyczące tej samej dostawy lub usługi. Problem ten rośnie wraz z liczbą niezależnie generowanych treści. Wspólne źródło danych produktowych pomaga ograniczać rozbieżności między kanałami kontaktu.

## 3.5. Integracja z platformą i ocena rezultatów

Wdrożenie personalizacji wymaga połączenia modelu z procesami działającymi już w przedsiębiorstwie. Podstawę stanowią katalog produktów, informacje o dostępności oraz dane dotyczące interakcji, przy czym ważne są również system zamówień, obsługa reklamacji i narzędzia komunikacji marketingowej. Model nie powinien działać jako odizolowany element oceniający nieaktualny obraz sklepu. Jego wynik musi odpowiadać rzeczywistym warunkom obsługi klienta.

Przepływ informacji można przedstawić jako kilka powiązanych etapów. Najpierw określa się dopuszczalne dane i sposób rejestrowania zdarzeń. Następnie przygotowuje się cechy potrzebne modelowi oraz wybiera odpowiednie działanie. Wynik trafia do witryny lub systemu obsługi przez ustalony interfejs. Reakcja użytkownika może później służyć ocenie jakości, zgodnie z przyjętymi zasadami przetwarzania.

Tabela 3.2 porządkuje proponowane miary oceny i wskazuje ryzyko ich niewłaściwego interpretowania.

**Tabela 3.2. Proponowane kryteria oceny wdrożenia personalizacji**

| Cel | Przykładowa miara | Potrzebne doprecyzowanie | Możliwe błędne odczytanie |
|---|---|---|---|
| Ułatwienie wyboru | Użyteczność rekomendacji | Sposób zebrania oceny | Kliknięcie jako pełna satysfakcja |
| Sprawniejszy zakup | Współczynnik konwersji | Akcja i mianownik | Wzrost jako dowód lojalności |
| Lepsza obsługa | Rozwiązane zgłoszenia | Kryterium rozwiązania | Brak przekazania jako sukces |
| Trwalsza relacja | Ponowne zakupy | Okres i grupa klientów | Każdy powrót jako efekt AI |
| Bezpieczeństwo | Potwierdzone incydenty | Rodzaj i skala naruszenia | Brak zgłoszeń jako brak ryzyka |
| Akceptacja komunikacji | Rezygnacje i skargi | Kanał oraz liczba odbiorców | Wysokie otwarcia jako zgoda na wszystko |

Źródło: opracowanie własne na podstawie Payne’a i Frow (2005), Lemon i Verhoefa (2016) oraz NIST (2023).

Podczas porównywania wariantów można wykorzystać test A/B z odpowiednim podziałem użytkowników. Jeden wariant przedstawia dotychczasowy sposób działania, drugi zawiera badaną zmianę. Należy wcześniej określić główną miarę, czas obserwacji oraz sposób oceny skutków ubocznych. Jednoczesna zmiana wielu elementów utrudnia przypisanie wyniku konkretnemu mechanizmowi. W niniejszej pracy nie przeprowadzono takiego testu, lecz wskazano jego funkcję oceniającą.

Istotna jest również możliwość bezpiecznego działania podczas awarii modelu lub usługi zewnętrznej. Sklep powinien zachować podstawowe wyszukiwanie, zakup i dostęp do informacji o zamówieniu. Zapasowy wariant może korzystać z ogólnych rekomendacji albo standardowej kolejności produktów. Klient nie powinien tracić możliwości wykonania podstawowej czynności przez niedostępność personalizacji. Takie rozwiązanie ogranicza wpływ awarii na ciągłość obsługi.

NIST zaleca zarządzanie ryzykiem AI przez cały cykl działania systemu (NIST, 2023). Obejmuje ono odpowiedzialność, poznanie kontekstu, pomiar oraz reagowanie na problemy. W przedsiębiorstwie należy wskazać osoby zatwierdzające zmiany i analizujące reklamacje. Powinny one mieć możliwość wyłączenia funkcji powodującej nieakceptowalne skutki dla klientów.

# ROZDZIAŁ 4. ZACHOWANIA KONSUMENTÓW ORAZ UWARUNKOWANIA PERSONALIZACJI

## 4.1. Wpływ dopasowania na decyzje zakupowe

Duży wybór produktów może pomagać klientowi, ale jednocześnie zwiększać wysiłek potrzebny do porównania. Rekomendacje ograniczają liczbę propozycji oglądanych na pierwszym etapie poszukiwania, a użytkownik może szybciej odnaleźć kategorię odpowiadającą jego potrzebie i określonemu budżetowi. Korzyść zależy jednak od jakości selekcji dokonanej przez system. Pominięcie istotnych alternatyw może ułatwić decyzję pozornie, kosztem jej trafności.

Kolejność ofert wpływa na to, z jakimi informacjami odbiorca zetknie się najpierw. Produkty umieszczone wysoko otrzymują większą szansę zauważenia podczas krótkiej wizyty. Wynik rekomendacji nie jest więc neutralnym odzwierciedleniem wszystkich dostępnych możliwości. Stanowi wybór dokonany według określonego celu i sposobu oceny produktów, dlatego ważne jest rozróżnienie trafności oferty od jej wartości dla sprzedawcy.

Personalizacja może zmniejszać koszt poszukiwania informacji potrzebnych do podjęcia decyzji. Klient nie musi za każdym razem rozpoczynać od pełnej listy asortymentu. Możliwe staje się także przedstawienie wyjaśnienia odpowiadającego aktualnie rozpatrywanemu problemowi, jednak zbyt silne dopasowanie może ograniczyć kontakt z nowymi kategoriami. Potrzebna pozostaje możliwość samodzielnego zmieniania filtrów oraz przeglądania szerszej oferty.

Badania reklamy personalizowanej pokazują znaczenie czasu i miejsca przedstawienia komunikatu (Bleier, Eisenbeiss, 2015). Dopasowana treść nie wywołuje jednakowego skutku w każdej sytuacji kontaktu. Wynik może zależeć od etapu poszukiwania informacji i celu korzystania ze strony, nie jest więc uzasadnione uznawanie większej szczegółowości za zawsze korzystną. Projekt powinien uwzględniać zarówno informacyjność komunikatu, jak też odczuwaną przez odbiorcę natarczywość.

W ocenie decyzji zakupowych należy rozdzielać zainteresowanie, zamiar i faktyczne zachowanie. Kliknięcie rekomendacji informuje o wejściu w kontakt z ofertą. Deklaracja chęci zakupu opisuje nastawienie, lecz nie potwierdza przeprowadzenia transakcji. Zakup z kolei nie przesądza o późniejszym zadowoleniu z produktu. Każdy z tych wyników odpowiada innemu etapowi relacji.

Porównanie sprzedaży przed wdrożeniem i po nim również wymaga ostrożności. W tym samym czasie mogły zmienić się ceny, kampanie reklamowe lub asortyment. Na wyniki mogła wpłynąć sezonowość albo sytuacja konkurencyjnego sklepu. Bez odpowiedniego punktu odniesienia trudno oddzielić wpływ personalizacji od pozostałych czynników. Wnioski przyczynowe powinny być zatem słabsze niż przy poprawnie zaprojektowanym eksperymencie.

Przydatna jest także ocena jakości decyzji z perspektywy samego kupującego. Mniejsza liczba porzuconych koszyków może oznaczać łatwiejszy zakup, ale nie wyjaśnia jego trafności. Należy sprawdzać, czy nie rośnie liczba zwrotów albo skarg dotyczących opisu. Dobre dopasowanie powinno ograniczać rozbieżność między oczekiwaniem a otrzymanym produktem. Takie podejście pozwala uwzględnić skutki widoczne dopiero po zakończeniu transakcji.

## 4.2. Zaangażowanie, satysfakcja, zaufanie i lojalność

Zaangażowanie opisuje aktywność odbiorcy, lecz jego znaczenie zależy od przyjętej miary. Dłuższy czas na stronie może oznaczać zainteresowanie albo trudność znalezienia informacji. Większa liczba kontaktów z obsługą może wynikać z nierozwiązanego problemu, jednak sam wzrost aktywności nie pozwala zatem ocenić jakości relacji. Wskaźniki należy interpretować wraz z kontekstem konkretnego zadania użytkownika.

Satysfakcja odnosi się do oceny doświadczenia względem oczekiwań klienta, obejmując produkt, obsługę lub cały przebieg zamówienia. Personalizacja jest tylko jednym z elementów wpływających na taką ocenę. Trafna rekomendacja nie zrównoważy każdej sytuacji związanej z opóźnieniem albo uszkodzeniem przesyłki. Znaczenie ma zgodność doświadczeń w różnych punktach kontaktu opisanych przez Lemon i Verhoefa (2016).

Zaufanie wiąże się z przekonaniem, że sklep działa w sposób wiarygodny i przewidywalny. W kontekście AI obejmuje również odpowiednie posługiwanie się informacjami o odbiorcy. Klient może akceptować wykorzystanie danych potrzebnych do realizacji zamówienia, a jednocześnie może nie oczekiwać ich zastosowania do szczegółowego przewidywania sytuacji osobistej. Niespodziewane wykorzystanie informacji może osłabiać ocenę nawet poprawnie działającego systemu.

Paradoks personalizacji polega na współwystępowaniu możliwej korzyści i poczucia utraty prywatności. Zbieranie informacji pomaga dopasować komunikat, ale może też zwiększać niepokój odbiorcy. Aguirre i współautorzy analizują tę zależność z uwzględnieniem sposobu pozyskiwania danych (Aguirre i in., 2015). Wnioskiem dla zarządzania jest potrzeba budowania zaufania równolegle z rozwijaniem dopasowania, jednak sam wzrost zdolności przewidywania nie zapewnia akceptacji klienta.

Lojalność może oznaczać postawę wobec sklepu albo rzeczywiste powtarzanie zakupów. Te dwa aspekty nie zawsze występują jednocześnie u konkretnej osoby. Klient może wracać z powodu niskiej ceny mimo przeciętnej oceny obsługi, ale może również wysoko oceniać sklep, lecz nie mieć potrzeby kolejnego zakupu. W badaniu trzeba więc jasno określić, jaki wymiar lojalności jest rozpatrywany.

Wskaźnik powrotów wymaga dodatkowo ustalenia okresu oraz rodzaju oferowanych produktów. Oczekiwanie kolejnego zakupu w ciągu miesiąca jest inne dla żywności i mebli. Porównywanie takich kategorii bez odpowiedniego kontekstu może prowadzić do błędnych wniosków. Podobnie zmiana liczby klientów nie wyjaśnia samodzielnie jakości ich relacji, dlatego potrzebne jest powiązanie wyników z charakterem działalności przedsiębiorstwa.

Z punktu widzenia CRM personalizacja powinna wspierać tworzenie wartości w dłuższym okresie (Payne, Frow, 2005), co oznacza uwzględnianie kosztu utraty zaufania oraz niezadowolenia po zakupie. Krótkotrwała poprawa sprzedaży może współistnieć ze wzrostem rezygnacji z komunikacji, dlatego ocena powinna obejmować zestaw uzupełniających się miar. Jedna liczba nie wystarcza do opisania całej relacji klienta ze sklepem.

## 4.3. Prywatność, profilowanie i obowiązki informacyjne

Podstawowe znaczenie dla przetwarzania danych osobowych w Unii Europejskiej ma RODO. Definicja danych osobowych obejmuje informacje dotyczące zidentyfikowanej lub możliwej do zidentyfikowania osoby. Identyfikator użytkownika może zatem mieć taki charakter także bez podania jego nazwiska. Ocena zależy od możliwości powiązania informacji z konkretnym człowiekiem. Zasady przetwarzania określa między innymi art. 5 rozporządzenia (Parlament Europejski i Rada, 2016).

W personalizacji szczególnie ważne są ograniczenie celu oraz minimalizacja zakresu danych. Przedsiębiorstwo powinno określić, do czego potrzebuje informacji i dlaczego wybrany zakres jest odpowiedni. Możliwość technicznego zebrania danych nie stanowi samodzielnego uzasadnienia ich przetwarzania. Historię zakupów należy rozpatrywać inaczej niż informacje zbierane dla konkretnej reklamacji. Każdy cel wymaga właściwej oceny podstawy prawnej i obowiązków wobec klienta.

RODO przewiduje różne podstawy przetwarzania, dlatego nie każda operacja musi opierać się na zgodzie, a jednocześnie posiadanie jednej podstawy nie oznacza dowolności dalszego wykorzystywania informacji. Przykładowo realizacja zamówienia nie uzasadnia automatycznie wszystkich przyszłych działań marketingowych, dlatego konieczne jest uwzględnienie rzeczywistego celu i warunków konkretnej operacji. Ogólna zgoda na regulamin nie zastępuje całej wymaganej analizy prawnej.

Profilowanie ma w RODO określone znaczenie związane z automatyczną oceną czynników osobowych. Może dotyczyć między innymi preferencji, zainteresowań albo zachowania konkretnej osoby, jednak nie każde uporządkowanie produktów według popularności jest więc profilowaniem klienta. Ważne jest to, czy przetwarzanie odnosi się do danych osobowych i ich oceny. Definicję zawarto w art. 4 pkt 4 rozporządzenia.

Odrębnego rozpatrzenia wymaga art. 22 dotyczący określonych decyzji podejmowanych wyłącznie automatycznie, przy czym znaczenie mają skutki prawne albo podobnie istotny wpływ na osobę. Nie można zakładać, że każda zwykła rekomendacja spełnia te warunki. Z drugiej strony poważniejsze rozstrzygnięcia wymagają dokładnej oceny sposobu działania systemu. Sam udział modelu nie przesądza więc ani o stosowaniu przepisu, ani o jego braku.

Cookies i podobne mechanizmy należy analizować także w kontekście przepisów komunikacji elektronicznej. Na poziomie unijnym znaczenie ma dyrektywa o prywatności i łączności elektronicznej. W Polsce odpowiednie regulacje zawiera Prawo komunikacji elektronicznej, w tym art. 399 (Parlament Europejski i Rada, 2002; Sejm RP, 2024). Należy odróżnić dostęp do informacji na urządzeniu od późniejszego przetwarzania danych osobowych. Wyjątki dotyczące niezbędnych operacji nie obejmują automatycznie każdego narzędzia marketingowego.

Klient powinien otrzymywać informacje umożliwiające zrozumienie najważniejszych zasad przetwarzania jego danych. Rozbudowany dokument nie spełni praktycznej funkcji, jeżeli komunikaty pozostają niejasne. Szczególnie istotne jest czytelne wyjaśnienie celu oraz dostępnych praw. Interfejs powinien umożliwiać wykonanie wyboru bez niepotrzebnego utrudniania rezygnacji. Takie rozwiązanie łączy formalny obowiązek z rzeczywistą kontrolą użytkownika.

Personalizacja ceny wymaga dodatkowo uwzględnienia obowiązków informacyjnych wynikających z prawa konsumenckiego. Dyrektywa 2011/83/UE przewiduje informację o cenie spersonalizowanej na podstawie zautomatyzowanego podejmowania decyzji. Obowiązek wskazano w art. 6 ust. 1 lit. ea, w odpowiednim zakresie stosowania, co nie oznacza obowiązku nazywania każdej promocji ceną indywidualnie dopasowaną (Parlament Europejski i Rada, 2011). Trzeba najpierw ustalić, jaki mechanizm rzeczywiście zastosowano w ofercie.

Kolejnym punktem odniesienia jest rozporządzenie dotyczące sztucznej inteligencji, określane jako AI Act, przy czym obejmuje ono różne obowiązki zależne od rodzaju systemu i roli podmiotu. Samo wykorzystanie AI w sklepie nie przesądza o klasyfikacji wysokiego ryzyka. Dla systemów przeznaczonych do interakcji z ludźmi znaczenie ma między innymi art. 50. Należy uwzględniać przewidziane warunki, wyjątki oraz harmonogram stosowania przepisów (Parlament Europejski i Rada, 2024).

Przywołane regulacje służą wskazaniu problemów związanych z personalizacją, a nie ocenie zgodności konkretnych przedsiębiorstw. Taka ocena wymagałaby dostępu do dokumentacji i rzeczywistego przebiegu przetwarzania informacji. W analizie przypadków nie przyjęto zatem, że sama dostępność funkcji dowodzi zgodności prawnej, ani nie uznano każdego wykorzystania danych za naruszenie prywatności. Ocenie podlegają rozpoznane mechanizmy i związane z nimi wymagania.

## 4.4. Problemy etyczne i negatywne efekty personalizacji

Ocena etyczna wykracza poza samo stwierdzenie zgodności z konkretnym przepisem. Działanie może być formalnie dopuszczalne, a mimo to odbierane jako niesprawiedliwe. Dotyczy to zwłaszcza sytuacji, gdy klient nie rozumie przyczyny przedstawionej propozycji. Sklep powinien rozpatrywać, czy personalizacja pomaga podejmować świadomą decyzję, przy czym ważne jest także zachowanie możliwości odmowy i wyboru innych rozwiązań.

Efekt inwigilacji oznacza poczucie, że przedsiębiorstwo wie o użytkowniku zbyt wiele. Może pojawić się przy wyjątkowo szczegółowej reklamie albo przypomnieniu dotyczącym wrażliwego tematu, co nie oznacza automatycznie wykazania naruszenia prawa przez sklep. Jest jednak sygnałem problemu z akceptacją sposobu wykorzystywania informacji. Badania paradoksu personalizacji uzasadniają uwzględnienie takiej reakcji w projektowaniu komunikacji (Aguirre i in., 2015).

Innym zagrożeniem jest zawężanie prezentowanego wyboru na podstawie dotychczasowych zainteresowań. W pracy określa się je roboczo jako bańkę zakupową, a klient może stale otrzymywać podobne propozycje, mimo zmiany swoich potrzeb. Nie jest to jednak nieunikniona cecha każdego systemu rekomendacyjnego. Stopień różnorodności zależy również od celu i zasad doboru ofert.

Sposób oceny modelu może utrwalać istniejące nierówności w dostępie do widoczności. Produkty często pokazywane otrzymują więcej interakcji, które później wspierają ich dalszą ekspozycję. Nowe oferty mają wtedy trudniejszy start nawet przy dobrej jakości. Dla klienta oznacza to ryzyko pomijania wartościowych alternatyw. Dla sprzedawców działających na platformie może oznaczać nierówny dostęp do odbiorców.

Możliwa jest również stronniczość wynikająca z niereprezentatywnych danych używanych podczas uczenia, a model może gorzej obsługiwać nietypowe zapytania albo rzadziej występujące potrzeby zakupowe. Wysoki wynik średni może ukrywać problemy dotyczące mniejszej grupy użytkowników, dlatego ocena powinna uwzględniać różne kategorie, języki i scenariusze korzystania ze sklepu. Takie podejście odpowiada szerszemu zarządzaniu ryzykiem przedstawionemu przez NIST (2023).

Granica między pomocą a manipulacją zależy między innymi od celu projektowanego działania. Wyjaśnienie różnic między produktami wspiera samodzielną ocenę dostępnych możliwości. Ukrywanie kosztów albo wywoływanie sztucznej presji ogranicza jakość tej oceny. Personalizacja może zwiększać skuteczność obu rodzajów działań, dlatego wymaga kontroli, jednak nie jest z natury ani rozwiązaniem korzystnym, ani narzędziem szkodliwym w każdej sytuacji.

## 4.5. Cyberbezpieczeństwo i bariery wdrożenia

Personalizacja zwiększa znaczenie przepływu informacji między różnymi częściami infrastruktury sklepu. System rekomendacyjny może korzystać z katalogu, danych zachowania oraz usług zewnętrznych. Chatbot może dodatkowo otrzymywać dostęp do informacji o konkretnym zamówieniu. Każde połączenie wymaga określenia uprawnień i zakresu przekazywanych danych. Rozbudowanie funkcji bez odpowiedniej kontroli może zwiększać skutki potencjalnego naruszenia.

Podstawowe cele bezpieczeństwa obejmują poufność, integralność oraz dostępność informacji. Poufność oznacza ograniczenie dostępu do danych do właściwych osób i systemów. Integralność dotyczy ochrony przed nieuprawnioną zmianą, na przykład ceny lub statusu zamówienia. Dostępność pozwala korzystać z usługi wtedy, gdy jest potrzebna klientowi. Wszystkie te obszary mają znaczenie dla utrzymania zaufania do sklepu.

System generatywny wprowadza dodatkowe ryzyko związane z interpretowaniem otrzymywanego tekstu. Treść opisu produktu lub wiadomości może próbować zmienić sposób działania asystenta. Materiał zewnętrzny powinien być traktowany jako dane, a nie uprawnione polecenie administracyjne. Szczególnie ważne jest ograniczenie możliwości wykonywania operacji dotyczących zamówień i płatności. Rozmowa językowa nie może zastępować niezależnej kontroli dostępu do takich czynności.

Należy także chronić informacje trafiające do dzienników systemowych i narzędzi analitycznych. Zapis całej rozmowy może zawierać dane osobowe niewymagane do późniejszej oceny jakości. Okres przechowywania powinien odpowiadać celowi, a dostęp pozostawać odpowiednio ograniczony. Kontrola jakości nie uzasadnia automatycznie gromadzenia każdego szczegółu kontaktu. Bezpieczeństwo wymaga powiązania działań technicznych z zasadami zarządzania informacją.

Do barier wdrożenia należą również koszty, jakość katalogu oraz kompetencje organizacji. Nieuporządkowane opisy produktów utrudniają zarówno rekomendacje, jak też odpowiedzi generowane przez asystenta. Brak wspólnego identyfikatora produktu komplikuje łączenie informacji pochodzących z różnych systemów, dlatego w takiej sytuacji zakup bardziej rozbudowanego modelu nie rozwiązuje podstawowego problemu. Konieczne może być wcześniejsze uporządkowanie procesów i danych przedsiębiorstwa.

W małym sklepie ważne staje się porównanie kosztu utrzymania z oczekiwanym efektem. Opłaty za usługę, integracja oraz kontrola odpowiedzi tworzą łączne obciążenie organizacji. Wdrożenie powinno zaczynać się od zadania o czytelnej wartości i ograniczonym ryzyku, na przykład pomocy w wyszukiwaniu informacji lub rekomendacji akcesoriów. Rozszerzanie zakresu wymaga wyników uzasadniających kolejne nakłady.

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


# ZAKOŃCZENIE

Celem pracy była analiza zastosowania sztucznej inteligencji do personalizacji relacji z klientami sklepów internetowych. Omówiono mechanizmy dopasowywania oferty, komunikacji oraz obsługi, a także ich najważniejsze ograniczenia. Rozważania objęły podstawy techniczne, perspektywę marketingową oraz uwarunkowania prawne i etyczne, a uzupełnieniem była analiza wybranych materiałów dotyczących Amazon, Zalando oraz Allegro. Pozwoliło to powiązać ogólne pojęcia z konkretnymi problemami występującymi w praktyce.

W odpowiedzi na główne pytanie wskazano kilka sposobów wspierania personalizacji przez AI. Systemy rekomendacyjne ograniczają liczbę ofert wymagających samodzielnego przejrzenia przez klienta. Analityka predykcyjna pomaga rozpoznawać sytuacje uzasadniające określony rodzaj kontaktu. Chatboty oraz asystenci zakupowi umożliwiają wyrażenie potrzeby przy użyciu naturalnego języka. Modele mogą również wspierać przygotowanie treści oraz ocenę trafności wyników wyszukiwania.

Pierwsze pytanie szczegółowe dotyczyło mechanizmów wykorzystywanych do takiego dopasowania. Wskazano znaczenie cech produktów, wzorców wcześniejszych interakcji oraz kontekstu bieżącej rozmowy. Każde źródło informacji ma inne zalety i ograniczenia interpretacyjne. Historia zakupu nie ujawnia wszystkich intencji, a deklaracja klienta może wymagać doprecyzowania. Personalizacja powinna zatem opierać się na odpowiednim połączeniu informacji z celem zadania.

Drugie pytanie obejmowało różnicę między efektem sprzedażowym a jakością relacji. Analiza wykazała potrzebę odrębnego traktowania konwersji, satysfakcji, zaufania i lojalności. Poprawa jednego wskaźnika nie przesądza o analogicznej zmianie pozostałych aspektów. Większa liczba kliknięć może współistnieć z natarczywością komunikacji albo niezadowoleniem po zakupie. Ocena korzyści wymaga więc zestawu miar odpowiadających rzeczywistym celom przedsiębiorstwa i klienta.

Trzecie pytanie dotyczyło ograniczeń technicznych, prawnych oraz etycznych. Za istotne uznano jakość danych, integrację systemów, kontrolę błędów i ciągłość obsługi. W obszarze prawnym znaczenie mają cel przetwarzania, właściwa podstawa oraz obowiązki informacyjne. Ocena etyczna obejmuje natomiast przejrzystość, możliwość wyboru i unikanie nadmiernej presji, jednak sama dostępność technologii nie rozstrzyga, czy jej użycie będzie odpowiednie w danej sytuacji.

Czwarte pytanie odnosiło się do wniosków z porównania przypadków. Materiały Amazon pokazały różnicę między rekomendowaniem produktów a wspieraniem wyboru przez rozmowę. Przypadek Zalando ujawnił znaczenie języka i kontekstu charakterystycznego dla konkretnej kategorii zakupowej. Publikacja Allegro podkreśliła potrzebę oceny trafności wykraczającej poza ogólne wskaźniki aktywności. Wspólnym warunkiem użyteczności pozostaje jakość powiązania danych z rzeczywistą potrzebą odbiorcy.

Przyjęta hipoteza znalazła częściowe wsparcie w przeprowadzonej analizie. Literatura i przypadki wskazują mechanizmy mogące poprawiać trafność oferty oraz ułatwiać kontakt. Uzasadniają także znaczenie jakości danych, prywatności i przejrzystości dla oceny personalizacji. Dostępny materiał nie pozwala jednak potwierdzić powszechnego wzrostu długoterminowej lojalności dzięki AI. W tym zakresie wniosek pozostaje warunkowy i wymaga dalszych badań empirycznych.

Ograniczenie pracy wynika przede wszystkim z wykorzystania materiałów wtórnych o różnym charakterze, ponieważ publikacje naukowe, opisy techniczne i komunikaty firmowe odpowiadają na odmienne pytania. Nie dysponowano jednolitymi danymi pozwalającymi porównać efekty wszystkich analizowanych rozwiązań, nie przeprowadzono również własnego eksperymentu ani reprezentatywnego badania opinii konsumentów. Z tego względu wnioski dotyczą wskazanych mechanizmów oraz zakresu dostępnych dowodów.

Dalsze badania mogłyby porównać doświadczenia klientów korzystających z różnych wariantów personalizacji. Przydatne byłoby połączenie pomiaru zachowania z oceną zaufania i odczuwanej kontroli. Warto także analizować skutki dopasowania w dłuższym okresie oraz różnych kategoriach produktów. Takie podejście pozwoliłoby lepiej oddzielić chwilową reakcję od trwałej jakości relacji. Istotne pozostaje również uwzględnienie osób rezygnujących z personalizacji lub kontaktu z chatbotem.

Z perspektywy zarządzania najważniejsze jest powiązanie wdrożenia z konkretną potrzebą klienta. Technologia powinna zmniejszać jego wysiłek, poprawiać jakość informacji i ułatwiać rozwiązanie sprawy, co wymaga kontroli wyników oraz współpracy zespołów technicznych, marketingowych i obsługowych. Personalizacja oparta na AI może wtedy wspierać relacje w handlu internetowym. Jej wartość zależy jednak od sposobu wykorzystania, a nie samego zastosowania algorytmu.


# BIBLIOGRAFIA

1. Abadi, M. i in. (2016). TensorFlow: A System for Large-Scale Machine Learning. W: 12th USENIX Symposium on Operating Systems Design and Implementation, s. 265–283. https://arxiv.org/abs/1605.08695

2. Adam, M., Wessel, M., Benlian, A. (2021). AI-based chatbots in customer service and their effects on user compliance. Electronic Markets, 31, s. 427–445. https://doi.org/10.1007/s12525-020-00414-7

3. Adomavicius, G., Tuzhilin, A. (2005). Toward the Next Generation of Recommender Systems: A Survey of the State-of-the-Art and Possible Extensions. IEEE Transactions on Knowledge and Data Engineering, 17(6), s. 734–749. https://doi.org/10.1109/TKDE.2005.99

4. Aguirre, E., Mahr, D., Grewal, D., de Ruyter, K., Wetzels, M. (2015). Unraveling the Personalization Paradox: The Effect of Information Collection and Trust-Building Strategies on Online Advertisement Effectiveness. Journal of Retailing, 91(1), s. 34–49. https://doi.org/10.1016/j.jretai.2014.09.005

5. Amazon (2024). Amazon announces Rufus, a new generative AI-powered conversational shopping experience. About Amazon, tekst R. Mehty i T. Chilimbiego. https://www.aboutamazon.com/news/retail/amazon-rufus (dostęp: 08.10.2026). Strona zawiera późniejszą informację o zmianie nazwy w maju 2026 roku.

6. Bleier, A., Eisenbeiss, M. (2015). Personalized Online Advertising Effectiveness: The Interplay of What, When, and Where. Marketing Science, 34(5), s. 669–688. https://doi.org/10.1287/mksc.2015.0930

7. Huang, M.-H., Rust, R. T. (2021). A Strategic Framework for Artificial Intelligence in Marketing. Journal of the Academy of Marketing Science, 49, s. 30–50. https://doi.org/10.1007/s11747-020-00749-9

8. Jouppi, N. P. i in. (2017). In-Datacenter Performance Analysis of a Tensor Processing Unit. W: Proceedings of the 44th Annual International Symposium on Computer Architecture, s. 1–12. https://doi.org/10.1145/3079856.3080246; wersja autorska: https://arxiv.org/abs/1704.04760

9. LeCun, Y., Bengio, Y., Hinton, G. (2015). Deep Learning. Nature, 521, s. 436–444. https://doi.org/10.1038/nature14539

10. Lemon, K. N., Verhoef, P. C. (2016). Understanding Customer Experience Throughout the Customer Journey. Journal of Marketing, 80(6), s. 69–96. https://doi.org/10.1509/jm.15.0420

11. Linden, G., Smith, B., York, J. (2003). Amazon.com Recommendations: Item-to-Item Collaborative Filtering. IEEE Internet Computing, 7(1), s. 76–80. https://doi.org/10.1109/MIC.2003.1167344

12. Luo, X., Tong, S., Fang, Z., Qu, Z. (2019). Frontiers: Machines vs. Humans: The Impact of Artificial Intelligence Chatbot Disclosure on Customer Purchases. Marketing Science. https://doi.org/10.1287/mksc.2019.1192

13. Marhula, J., Sidor, M. (2026). Automating Search Relevance Assessment at Scale with LLM-as-a-Judge. Allegro Tech, 20.08.2026. https://blog.allegro.tech/2026/08/automating-search-relevance-llm-as-a-judge.html (dostęp: 08.10.2026). Odczytano także źródło publikacji w oficjalnym repozytorium github.com/allegro/blog.

14. McCarthy, J. (2007). What Is Artificial Intelligence? Stanford University, wersja z 12.11.2007. https://www-formal.stanford.edu/jmc/whatisai/whatisai.html (dostęp: 08.10.2026).

15. Mell, P., Grance, T. (2011). The NIST Definition of Cloud Computing. NIST Special Publication 800-145. https://doi.org/10.6028/NIST.SP.800-145

16. NIST (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. https://doi.org/10.6028/NIST.AI.100-1

17. OECD (2019). Unpacking E-commerce: Business Models, Trends and Policies. Paris: OECD Publishing. https://doi.org/10.1787/23561431-en

18. Parlament Europejski i Rada (2002). Dyrektywa 2002/58/WE z dnia 12 lipca 2002 r. dotycząca przetwarzania danych osobowych i ochrony prywatności w sektorze łączności elektronicznej. Dz.U. UE L 201, s. 37–47, ze zmianami. https://eur-lex.europa.eu/eli/dir/2002/58/oj

19. Parlament Europejski i Rada (2011). Dyrektywa 2011/83/UE z dnia 25 października 2011 r. w sprawie praw konsumentów. Dz.U. UE L 304, s. 64–88, ze zmianami. Wykorzystana identyfikacja tekstu skonsolidowanego: 02011L0083-20220528. https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:02011L0083-20220528

20. Parlament Europejski i Rada (2016). Rozporządzenie (UE) 2016/679 z dnia 27 kwietnia 2016 r. w sprawie ochrony osób fizycznych w związku z przetwarzaniem danych osobowych i w sprawie swobodnego przepływu takich danych oraz uchylenia dyrektywy 95/46/WE. Dz.U. UE L 119, s. 1–88. https://eur-lex.europa.eu/eli/reg/2016/679/oj

21. Parlament Europejski i Rada (2024). Rozporządzenie (UE) 2024/1689 z dnia 13 czerwca 2024 r. w sprawie ustanowienia zharmonizowanych przepisów dotyczących sztucznej inteligencji. Dz.U. UE L, 2024/1689. https://eur-lex.europa.eu/eli/reg/2024/1689/oj

22. Paszke, A. i in. (2019). PyTorch: An Imperative Style, High-Performance Deep Learning Library. Advances in Neural Information Processing Systems, 32. https://arxiv.org/abs/1912.01703

23. Payne, A., Frow, P. (2005). A Strategic Framework for Customer Relationship Management. Journal of Marketing, 69(4), s. 167–176. https://doi.org/10.1509/jmkg.2005.69.4.167

24. Sejm RP (2024). Ustawa z dnia 12 lipca 2024 r. – Prawo komunikacji elektronicznej. Dz.U. 2024, poz. 1221. https://dziennikustaw.gov.pl/D2024000122101.pdf

25. Vaswani, A. i in. (2017). Attention Is All You Need. Advances in Neural Information Processing Systems, 30. https://arxiv.org/abs/1706.03762

26. Zalando (2023). Zalando to launch a fashion assistant powered by ChatGPT. Zalando Corporate, 19.04.2023. https://corporate.zalando.com/en/technology/zalando-launch-fashion-assistant-powered-chatgpt (dostęp: 08.10.2026).


# SPIS TABEL

Tabela 2.1. Personalizacja na kolejnych etapach relacji z klientem — s. 12

Tabela 3.1. Porównanie podstawowych podejść rekomendacyjnych — s. 18

Tabela 3.2. Proponowane kryteria oceny wdrożenia personalizacji — s. 23

Tabela 5.1. Wybrane wyniki oceny klas trafności opisane przez zespół Allegro — s. 34

Tabela 5.2. Porównanie zakresu dowodów w analizowanych przypadkach — s. 35
