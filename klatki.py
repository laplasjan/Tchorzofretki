{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4161fab1-bec5-4a8d-b299-2f00235d7337",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "e47c1c8d-5d88-463e-83ac-8f9eb52ff116",
   "metadata": {},
   "outputs": [],
   "source": [
    "video_file = \"C:/Users/jmich/hackYEAH/CLIP/BWT/HY_2024_film_01.mp4\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "16d1b19e-4228-46ff-8967-b464b523cbb0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Plik HY_2024_film_01.mp4 nie istnieje.\n"
     ]
    }
   ],
   "source": [
    "def save_frames_from_video(video_path, interval=1):\n",
    "    video_name = os.path.splitext(os.path.basename(video_path))[0]\n",
    "    \n",
    "    # Sprawdź, czy plik wideo istnieje\n",
    "    if not os.path.exists(video_path):\n",
    "        print(f\"Plik {video_path} nie istnieje.\")\n",
    "        return\n",
    "    \n",
    "    output_dir = video_name\n",
    "    if not os.path.exists(output_dir):\n",
    "        os.makedirs(output_dir)\n",
    "    \n",
    "    cap = cv2.VideoCapture(video_path)\n",
    "    \n",
    "    # Sprawdzenie, czy udało się otworzyć plik\n",
    "    if not cap.isOpened():\n",
    "        print(f\"Nie można otworzyć pliku wideo: {video_path}\")\n",
    "        return\n",
    "    \n",
    "    fps = cap.get(cv2.CAP_PROP_FPS)\n",
    "    print(f\"Liczba klatek na sekundę: {fps}\")\n",
    "    \n",
    "    frame_interval = int(fps * interval)\n",
    "    frame_count = 0\n",
    "    saved_frame_count = 0\n",
    "    \n",
    "    while True:\n",
    "        ret, frame = cap.read()\n",
    "        \n",
    "        if not ret:\n",
    "            break\n",
    "        \n",
    "        if frame_count % frame_interval == 0:\n",
    "            frame_filename = os.path.join(output_dir, f\"frame_{saved_frame_count:04d}.jpg\")\n",
    "            cv2.imwrite(frame_filename, frame)\n",
    "            print(f\"Zapisano klatkę: {frame_filename}\")\n",
    "            saved_frame_count += 1\n",
    "        \n",
    "        frame_count += 1\n",
    "    \n",
    "    cap.release()\n",
    "    print(f\"Zapisano {saved_frame_count} klatek w folderze '{output_dir}'.\")\n",
    "\n",
    "# Przykład użycia\n",
    "video_file = \"HY_2024_film_01.mp4\"\n",
    "save_frames_from_video(video_file, interval=1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "0cedebd1-9239-460c-8629-3d32a14ce347",
   "metadata": {},
   "outputs": [],
   "source": [
    "#zdefiniowanie automatu do łącznego stosowania klatkowania filmów\n",
    "def autom(videos):\n",
    "    if isinstance(videos, str):\n",
    "        videos = [videos]\n",
    "    \n",
    "    for video in videos:\n",
    "        save_frames_from_video(video, interval=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "1c3e36a9-b9b7-45b0-a661-441cc76cf040",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Liczba klatek na sekundę: 25.0\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0000.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0001.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0002.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0003.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0004.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0005.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0006.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0007.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0008.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0009.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0010.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0011.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0012.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0013.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0014.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0015.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0016.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0017.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0018.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0019.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0020.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0021.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0022.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0023.jpg\n",
      "Zapisano klatkę: HY_2024_film_20\\frame_0024.jpg\n",
      "Zapisano 25 klatek w folderze 'HY_2024_film_20'.\n"
     ]
    }
   ],
   "source": [
    "#Przykładowy pokaz na jednym z filmów jak działa to zapisywanie do klatki\n",
    "video_files = [\n",
    "    \"C:/Users/jmich/hackYEAH/CLIP/BWT/HY_2024_film_20.mp4\",\n",
    "]\n",
    "autom(video_files)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68000a61-88f5-4518-8970-b940d7439e9b",
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
