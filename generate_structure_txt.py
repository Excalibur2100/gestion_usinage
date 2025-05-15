import os
from colorama import Fore, Style, init

init(autoreset=True)  # Active les couleurs (Windows & Linux)

def write_structure(root_dir, output_file):
    with open(output_file, "w", encoding="utf-8") as f:

        def walk_dir(current_dir, indent=""):
            items = sorted(os.listdir(current_dir))
            for index, item in enumerate(items):
                path = os.path.join(current_dir, item)
                is_last = index == len(items) - 1
                branch = "└── " if is_last else "├── "
                line_prefix = indent + branch

                if os.path.isdir(path):
                    # Console : couleur bleu pour dossiers
                    print(f"{indent}{Fore.BLUE}{branch}{item}{Style.RESET_ALL}")
                    f.write(f"{line_prefix}{item}/\n")
                    extension = "    " if is_last else "│   "
                    walk_dir(path, indent + extension)
                else:
                    # Console : vert pour fichiers
                    print(f"{indent}{Fore.GREEN}{branch}{item}{Style.RESET_ALL}")
                    f.write(f"{line_prefix}{item}\n")

        print(Fore.CYAN + f"\n📦 Structure de : {root_dir}\n" + Style.RESET_ALL)
        f.write(f"{os.path.basename(root_dir)}/\n")
        walk_dir(root_dir)

if __name__ == "__main__":
    ROOT = "."
    OUTPUT = "structure_projet.txt"

    if os.path.exists(ROOT):
        write_structure(ROOT, OUTPUT)
        print(Fore.YELLOW + f"\n✅ Fichier texte généré : {OUTPUT}" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"\n❌ Dossier introuvable : {ROOT}" + Style.RESET_ALL)
