import os, pprint
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from klatki import save_frames_from_video
from liczba_osob import detect_faces

app = Flask(__name__)

# Konfiguracja folderu na pliki
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'supersecretkey'

# Funkcja sprawdzająca rozszerzenie pliku
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Strona główna z formularzem
@app.route('/')
def upload_form():
    # Pobieranie listy plików z katalogu uploads
    files = os.listdir(UPLOAD_FOLDER)
    # Renderowanie strony
    return render_template('upload.html', files=files)

# Obsługa przesyłania pliku
@app.route('/upload', methods=['POST'])
def upload_file():
    # Sprawdzanie, czy plik został wysłany w żądaniu
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    
    # Jeśli użytkownik nie wybrał pliku
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    # Sprawdzenie, czy plik ma rozszerzenie 
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)  # Zabezpieczenie nazwy pliku
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # Zapisanie pliku
        flash('File successfully uploaded')
        return redirect(url_for('upload_form'))
    
    flash('Dozwolone filmy tylko w mp4')
    return redirect(request.url)


@app.route('/klatki/<filename>', methods=['POST'])
def przerob_na_zdjęcia_route(filename):
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Wywołanie funkcji do zapisywania klatek z wideo
    folder_path = save_frames_from_video(file_path, interval=1)
    flash(f"Klatki z filmu '{filename}' zostały zapisane.", 'success')

    # Iteracja po plikach w katalogu
    liczba_twarzy_all = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Sprawdź, czy to plik (opcjonalne)
        if os.path.isfile(file_path):
            print(f'Nazwa pliku: {file_path}')
            liczba_twarzy = detect_faces(file_path, 'C:\\HackYeah\\biblioteki\\haarcascade_frontalface_default.xml')
            print(f'wykryto twarzy: {liczba_twarzy}')
            if liczba_twarzy > liczba_twarzy_all:
                liczba_twarzy_all = liczba_twarzy

    # Sprawdź liczbę twarzy i odpowiednio przekaż komunikaty
    if liczba_twarzy_all > 1:
        flash("Znaleziono więcej niż jedną twarz lub lektor zbyt energicznie porusza głową.", 'danger')  # Komunikat typu "danger"
    elif liczba_twarzy_all == 1:
        flash("Znaleziono tylko jedną twarz.", 'success')  # Komunikat typu "success"
    else:
        flash("Nie znaleziono żadnej twarzy.", 'warning')  # Komunikat typu "warning"


    return redirect(url_for('upload_form'))  # Zmiana na odpowiednią trasę po zakończeniu


if __name__ == '__main__':
    # Tworzenie folderu 'uploads', jeśli nie istnieje
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    app.run(debug=True)
