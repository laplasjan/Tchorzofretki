{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "69237cda-72de-43a0-9db5-324cbd183e41",
   "metadata": {},
   "outputs": [],
   "source": [
    "from PIL import Image\n",
    "import pytesseract\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4b6ad4d8-71e7-45c7-8dba-0f9f0f818409",
   "metadata": {},
   "outputs": [],
   "source": [
    "pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'\n",
    "folder_path = 'C:/Users/jmich/hackYEAH/CLIP/BWTklatki/HY_2024_film_01'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "dced9e26-3eb0-42a8-910e-82ae134a2466",
   "metadata": {},
   "outputs": [],
   "source": [
    "all_words = []\n",
    "\n",
    "for filename in os.listdir(folder_path):\n",
    "    if filename.endswith('.jpg') or filename.endswith('.png'):\n",
    "        image_path = os.path.join(folder_path, filename)\n",
    "\n",
    "        image = Image.open(image_path)\n",
    "\n",
    "        text = pytesseract.image_to_string(image)\n",
    "\n",
    "        words = text.lower().split()\n",
    "        all_words.extend(words)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0813c401-8b86-44af-8782-d9ad13c511c8",
   "metadata": {},
   "source": [
    "### poprawa literówek"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "cb8e119c-b63c-4122-9254-64bdbe5dbd9e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "words = ', '.join(all_words)\n",
    "print(type(words))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3f5f42fe-38b0-4110-b8c2-0513c7d77622",
   "metadata": {},
   "outputs": [],
   "source": [
    "from autocorrect import Speller"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "846d5669-ef88-4276-ab7a-a674d890e5d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "spell = Speller(lang='pl')\n",
    "\n",
    "# Korekta tekstu\n",
    "poprawiony_tekst = spell(words)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "70380551-31ea-4735-a47f-199424ecbfc2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "zadanie_, <, go, [breakwordtraps], >, finta, nagranie, jest, materiałem, instruktażowym, (z, celowo, zastosowanymi, bledami, językowymi), ,, przygotowanym, na, potrzeby, zadania, breakwordtraps, -, hackyeah, 2024, <, mf, ks, cx, clrf, >, zadanie_, finta, <, go, [breakwordtraps], >, za|, <, mf, ks, cx<, clrf, >, zadanie_, <, go, [breakwordtraps], >, finta, zastosowane, modyfikacje, (wtedy):, przerywniki,, <, mf, ks, cx, clrf, >, zadanie_, finta, <, go, [breakwordtraps], >, zastosowane, modyfikacje, (wtedy):, przerywniki,, za, szybkie, tempo,, nadmierne, powtorzenia, <, mf, ks, cx, clrf, >, zadanie_, finta, <, go, [breakwordtraps], >, zastosowane, modyfikacje, (wtedy):, przerywniki,, za, szybkie, tempo,, nadmierne, powtorzenia, <, mf, ks, cx, clrf, >, zadanie_, <, go, [breakwordtraps], >, finta, <, “fe, ks, &&<, clrf, >, kwota, badanych, srodekéw, publicznych, zadanie_, <, go, [breakwordtraps], >, finta, audytem, objelismy@6, podmiotow,, a, toczna, <, me, kb, c<, clav, >, kwota, badanych, srodekéw, publicznych, zadanie_, <, go, [breakwordtraps], >, finta, <, “fe, ks, &&<, clrf, >, kwota, badanych, srodekéw, publicznych, @, zadanie_, finta, ee, go, [breakwordtraps], >, na, <, ™“f, ks, &&<, clrf, >, kwota, badanych, srodekéw, publicznych, ©, zadanie_, finta, <, go, [breakwordtraps], >, toj}około, 100, miliardow, złotych., w, toku, działa, <, “use, cae, >, saturday, miedzy, innymi, niegospode, zadanie_, <, go, [breakwordtraps], >, finta, tokoto, 100, miliardow, złotych., w, toku, działa, <, mks, cm, clrf, >, &, zadanie_, <4, go, [breakwordtraps], >, finta, to}około, 100, miliardow, złotych., w, toku, dzialan, <, mks, mx, chief>, §, zadanie_, <, go, [breakwordtraps], >, finta, to)około, 100, miliardow, złotych., w, toku, działa, <, mks, mx, chief>, §&, zadanie_, finta, <, go, [breakwordtraps], >, niecelowe, wydatkowanie, srodkow,, srodek¢, sq, eee, >, eoudiicznych,, udzielenie, dotacji, podmiotow, 6, zadanie_, finta, <, go, [breakwordtraps], >, <, mf, ks, c<, clrf, >, zadanie_, <, go, [breakwordtraps], >, finta, z, zz, niecelowe, wydatkom, <, me, ks, cx, clrf, >, zadanie_, finta, <, go, [breakwordtraps], >, niecelowe, wydatkowanie, srodkow,, srodkow, <, mks, c<, cle, >, 1, zadanie_, <, go, [breakwordtraps], >, finta, a, ya, niecelowe, wydatkom, la, ee, xe, seoudiicznych,, udzielenie, dotacji, podmiotow, @, zadanie_, <, go, [breakwordtraps], >, finta, <, mf, ks, cx<, clrf, >, zadanie_, <, go, [breakwordtraps], finta, ktore, nie, spełniamy, kryteriow, konkursowy, sala,, eeee, a, sektora, nie, spełniamy, kryteriow, konkursowy, c), zadanie_, finta, a, go, [breakwordtraps], >, ktore, nie, spełniamy, kryteriow, konkursowych, gua,, nee., se, sektora, nie, spełniamy, kryteriow, konkursowy, zadanie_, <, go, [breakwordtraps], >, finta, <, me, ks, c<, clrf, >, zadanie_, finta, <, go, [breakwordtraps], >, ktore, nie, spełniamy, kryteriow, konkursowej, ge,, eee, a, sektora, nie, spełniamy, kryteriow, konkurso, 6, zadanie_, <, go, [breakwordtraps], >, finta, ktore, nie, spełniamy, kryteriow, konkursowy, sale,, eee, se, sektora, nie, spełniamy, kryteriow, konkurso, 6, zadanie_, finta, <<, go, [breakwordtraps], >, tore, nie, spełniamy, ki, kryteriow, konkursowych, sa,, nee., se, sektora, nie, spełniamy, kryteriow, konkursowy, @, zadanie_, <, go, [breakwordtraps], >, finta, ktore, nie, spełniamy, kryteriow, konkursowy, chy, se,, nee, sektora, nie, spełniamy, kryteriow, konkursowy, 6\n"
     ]
    }
   ],
   "source": [
    "print(poprawiony_tekst)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4488e19d-b95b-4a40-98bc-dfde56349ab0",
   "metadata": {},
   "source": [
    "### sprawdzenie, ile słów jest w części wspólnej tych stringów"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c29fc440-6e8b-42fd-a67e-d99ac1dad9f7",
   "metadata": {},
   "source": [
    "### stworzenie \"scenariusza - spójnej narracji tekstowek\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "cb72a2ac-fd08-4a76-8df2-c24f7fe6a64e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Słowa tylko w str1: {'wydatkoy', 'konkursowychy', 'fintax', 'smektore', 'srodke¢', 'dziatan', 'jezykowymi)', 'toj}okoto', 'konkursowyel', 'tojokoto', 'ztotych.', 'materiatem', '(btedy):', 'publicznyct', 'clre', 'taczna', 'sektore', 'claf', 'seektore', 'ciiref>', 'ryteriow', 'srodkéw', 'saterday', 'to}okoto', 'instruktazowym', 'ychy', 'clrfe', 'iniecelowe', 'dziata', 'btedami', 'to)okoto', 'spetniaty'}\n"
     ]
    }
   ],
   "source": [
    "words1 = set(words.split(', '))\n",
    "words2 = set(poprawiony_tekst.split(', '))\n",
    "\n",
    "only_in_str1 = words1 - words2\n",
    "\n",
    "# Wynik\n",
    "print(\"Słowa tylko w str1:\", only_in_str1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "d9054ce9-bf38-4a3d-9fe8-c41309fcd19c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "32\n"
     ]
    }
   ],
   "source": [
    "unique_count = len(only_in_str1)\n",
    "print(unique_count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc7555ca-98d3-4fef-af54-63573a73366b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
