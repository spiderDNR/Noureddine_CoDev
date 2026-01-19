# scanner/detector.py
from dataclasses import dataclass


@dataclass
class PodAlert:
    """Alerte concernant l'état d'un Pod Kubernetes.

    Attributs:
        name (str): Le nom du Pod.
        status (str): Le statut actuel du Pod.
    """
    name: str
    status: str


def scan_pods() -> list[PodAlert]:
    """Simulation pour dev local"""
    return [PodAlert("nginx-pod", "Running")]


if __name__ == '__main__':
    print(scan_pods())
