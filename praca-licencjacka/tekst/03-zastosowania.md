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