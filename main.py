import torch

# 1. Vérification globale de la disponibilité de CUDA
cuda_dispo = torch.cuda.is_available()
print(f"Est-ce que PyTorch voit un GPU ? : {cuda_dispo}")

if cuda_dispo:
    # 2. Afficher le nom de votre carte graphique (ex: RTX 5090)
    nom_gpu = torch.cuda.get_device_name(0)
    print(f"Nom du GPU détecté : {nom_gpu}")
    
    # 3. Vérifier la version de CUDA compilée à l'intérieur de PyTorch
    version_cuda = torch.version.cuda
    print(f"Version de CUDA intégrée à PyTorch : {version_cuda}")
    
    # 4. Test réel : Allocation d'un tenseur sur la mémoire du GPU
    try:
        x = torch.rand(3, 3).cuda()
        print("Succès : Le tenseur a été correctement alloué sur le GPU !")
    except Exception as e:
        print(f"Erreur lors du calcul GPU : {e}")
else:
    print("Attention : PyTorch est configuré en mode CPU uniquement.")

print(torch.__version__)