# Tchorzofretki
Repozytorium grupy z HackYEAH


Grupa złożona z: Przemysława Grzesika, Aleksandra Lewandowsiej, Joanny Michalskiej

Podchodziliśmy do tasków: \
<GO> [BreakWordTraps], FinTax\
Quantum AI, IBM\
Artifficil Inteligence,  Ministerstwo Cyfryzacji\

Metodologia: \
Zamierzamy ykorzystać OpenSourcowy model CLIP wykonany przez OpenAI. Jest to model uczenia transferowego, który został przetrenowany na ogromnym datasecie, dzięki czemu możemy wykorzystać go do 20-stu krótkich filmików.\
Ponieważ CLIP jest trenowany na parach obraz- tekst, podzieliliśmy filmiki na klatki i otagowaliśmy je korzystając z podpowiedzi na pierwszych klatkach odnośnie tego, co tam się znajdowało na filmiku np pierwszy filmik miał: za szybkie temp. przerywniki, nadmierne powtórzenia.\
\
Jak korzystać? \
1. klatki.
2. analiza tekstu
3. ekstrakcja kluczowych słów
4. rozpoznawanie twarzy
5. CLIP.py
6. stronka.py
7. merge.py
8. stronka

Opisy kodu: \
- klatki jest programem, który przygotowuje filmiki w .mp4 do zdjęć klatek w .jpg
