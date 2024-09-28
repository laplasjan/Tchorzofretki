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
1. klatki.py
2. analiza_tekstu
3. CLIP.py
4. stronka.py
5. merge.py

Opisy kodu: \
- klatki jest programem, który przygotowuje filmiki w .mp4 do zdjęć klatek w .jpg
