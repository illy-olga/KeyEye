# 👁️ KeyEye

## Description

Ce projet est un keylogger éducatif qui a pour but de vous familiariser avec différentes bibliothèques Python. Il utilise des modules pour capturer l'activité du clavier et de la souris, prendre des captures d'écran et accéder au presse-papiers.

## Objectif

L'objectif principal de ce projet est éducatif. Il vous permet d'explorer et de manipuler différentes bibliothèques Python. Ce projet utilise les bibliothèques suivantes :
- **pynput** : pour écouter les événements du clavier et de la souris.
- **Pillow** : pour prendre des captures d'écran.
- **pyperclip** : pour accéder au contenu du presse-papiers.
- **pyinstaller** : pour convertir le script Python en un exécutable autonome.

## Fonctionnalités

- **Capture de l'activité du clavier** : Enregistre les frappes du clavier dans des fichiers journaux.
- **Capture de l'activité de la souris** : Prend une capture d'écran chaque fois qu'un clic de souris est détecté.
- **Capture d'écran** : Enregistre l'écran lorsqu'un clic est effectué.
- **Surveillance du presse-papiers** : Sauvegarde le contenu du presse-papiers lorsque des modifications sont détectées.

## Utilisation

1. **Cloner le dépôt** :

   ```bash
   git clone https://github.com/illy-olga/KeyEye.git
   cd KeyEye
   
2. **Installer les dépendances** :

   Assurez-vous d'avoir Python et pip installés. Installez les dépendances avec :
   ```bash
   pip install -r requirements.txt
   ```

3. **Exécuter le script** :

   Lancez le script en utilisant Python :
   ```bash
   python KeyEye.py
   ```

4. **Convertir en exécutable (optionnel)** :
   Si vous souhaitez convertir le script Python en exécutable, utilisez PyInstaller :
   ```bash
   pyinstaller KeyEye.py
   ```
   L'exécutable sera généré dans le répertoire dist.

## Avertissement

Ce projet est à des fins éducatives uniquement. Utiliser des keyloggers sans le consentement explicite de la personne concernée est illégal et contraire à l'éthique.









