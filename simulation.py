import numpy as np

# Fiziksel Sabitler (PZT-5H Malzemesi Örneği)
d33 = 593e-12  # Piezoelektrik yük katsayısı (C/N)
thickness = 0.002  # Malzeme kalınlığı (m)
permittivity = 3000 * 8.854e-12  # Geçirgenlik

def calculate_energy(force_n, pedestrian_count):
    # Basit voltaj ve enerji hesabı
    voltage = (d33 * force_n * thickness) / permittivity
    energy_per_step = 0.5 * permittivity * (voltage**2)
    return energy_per_step * pedestrian_count

# Örnek: Saatte 1000 kişi, ortalama 750N (75kg) yük
total_energy = calculate_energy(750, 1000)
print(f"Hesaplanan saatlik toplam enerji: {total_energy:.6f} Joule")
