import os
import shutil

# Chemin du répertoire "Downloads"
downloads_path = '/home/frosty/Downloads'

# Chemins des dossiers de destination
picture_path = os.path.join(downloads_path, 'pictures')
document_path = os.path.join(downloads_path, 'documents')
logiciel_path = os.path.join(downloads_path, 'logiciel')
videos_path = os.path.join(downloads_path, 'videos')
zip_path = os.path.join(downloads_path, 'zip')


# Création des dossiers s'ils n'existent pas déjà
for folder_path in [picture_path, document_path, logiciel_path, videos_path]:
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Parcours des fichiers du répertoire "Downloads"
for file_name in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, file_name)

    # Vérification du type de fichier
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(file_name)[1].lower()

        # Déplacement du fichier vers le dossier approprié
        if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.svg']:
            shutil.move(file_path, os.path.join(picture_path, file_name))
        elif file_extension in ['.doc', '.docx', '.pdf', '.txt', '.pptx', '.webp']:
            shutil.move(file_path, os.path.join(document_path, file_name))
        elif file_extension in ['.exe', '.msi', '.deb']:
            shutil.move(file_path, os.path.join(logiciel_path, file_name))
        elif file_extension in ['.mp4', '.avi', '.mov', '.mkv']:
            shutil.move(file_path, os.path.join(videos_path, file_name))
        elif file_extension in ['.zip']:
            shutil.move(file_path, os.path.join(zip_path, file_name))
        