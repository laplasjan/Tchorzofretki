{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c00ff30d-d192-432a-9f3c-66bd4a81a97c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import torch\n",
    "import clip\n",
    "from PIL import Image\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "c7864d2e-55b1-4e48-ab68-fc88285588a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Załadowano 33 obrazów z folderu: C:/Users/jmich/hackYEAH/CLIP/BWTklatki/HY_2024_film_01\n",
      "Embeddingi dla obrazów: tensor([[-0.0086,  0.0109,  0.0104,  ...,  0.0890, -0.0071,  0.0042],\n",
      "        [-0.0333,  0.0261, -0.0015,  ...,  0.0616, -0.0307,  0.0637],\n",
      "        [-0.0213,  0.0285,  0.0139,  ...,  0.0592, -0.0436,  0.0687],\n",
      "        ...,\n",
      "        [-0.0648,  0.0132,  0.0080,  ...,  0.0297, -0.0237,  0.0599],\n",
      "        [-0.0631,  0.0157,  0.0190,  ...,  0.0291, -0.0191,  0.0602],\n",
      "        [-0.0620,  0.0159,  0.0179,  ...,  0.0265, -0.0162,  0.0595]])\n"
     ]
    }
   ],
   "source": [
    "device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n",
    "model, preprocess = clip.load(\"ViT-B/32\", device=device)\n",
    "    \n",
    "folder_path = \"C:/Users/jmich/hackYEAH/CLIP/BWTklatki/HY_2024_film_01\"\n",
    "image_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(('jpg'))]\n",
    "\n",
    "images = [preprocess(Image.open(image_file)).unsqueeze(0) for image_file in image_files]\n",
    "images = torch.cat(images).to(device)\n",
    "text = clip.tokenize([\"powtórzenia\"]).to(device)\n",
    "\n",
    "with torch.no_grad():\n",
    "    image_features = model.encode_image(images)\n",
    "\n",
    "image_features /= image_features.norm(dim=-1, keepdim=True)\n",
    "\n",
    "print(f\"Załadowano {len(image_files)} obrazów z folderu: {folder_path}\")\n",
    "print(\"Embeddingi dla obrazów:\", image_features)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "8ff13e68-536d-46aa-bccd-4f690d65d36e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Label probs: [[1.]]\n"
     ]
    }
   ],
   "source": [
    "with torch.no_grad():\n",
    "    image_features = model.encode_image(image)\n",
    "    text_features = model.encode_text(text)\n",
    "    \n",
    "    logits_per_image, logits_per_text = model(image, text)\n",
    "    probs = logits_per_image.softmax(dim=-1).cpu().numpy()\n",
    "\n",
    "print(\"Label probs:\", probs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "399203e4-2e36-41d4-bac8-932757f86529",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Macierz podobieństw obrazów: tensor([[138.1137]])\n"
     ]
    }
   ],
   "source": [
    "similarity_matrix = image_features @ image_features.T\n",
    "print(\"Macierz podobieństw obrazów:\", similarity_matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4fe6ce01-82ce-41a4-8482-45ec8c8804ad",
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
