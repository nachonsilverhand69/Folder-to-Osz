import os
import zipfile

base_dir = os.getcwd()

output_dir = os.path.join(base_dir, "Output")
os.makedirs(output_dir, exist_ok=True)

folders = [
    f for f in os.listdir(base_dir)
    if os.path.isdir(os.path.join(base_dir, f)) and f != "Output"
]

total = len(folders)

for i, folder_name in enumerate(folders, start=1):
    folder_path = os.path.join(base_dir, folder_name)
    zip_path = os.path.join(output_dir, f"{folder_name}.zip")


    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)


    os.rename(zip_path, os.path.splitext(zip_path)[0] + ".osz")


    print(f" {i}/{total} processed folders: {folder_name}")

print("\nDone, all files are processed correctly 'Output'")
