import matplotlib.pyplot as plt
import numpy as np

# TP-72 Engineered Sequence
sequence = """LLKTNTVSAILHRSRLSFPITTSSSPLPATTSSLSTTDNAIRAHPPRDAPDDLRNNRPNNPSGAYFPLGYKD
AAYNWWCGVTPSLADRSVLKHIPFLKDATASLGSLSNTDVGDPYGNRIWRRSLVNLSGKNRALNDFSIDRVG
DDTDDTLVLLHGYGAGLGFFYKNFDPISRIPGLKLYALDLLGLGNSSRPSFKIHAKDRDGKVIDADNWFIDA
LDDWRKARKIDRFTLLGHSLGGYLAVSYALKYPGHLKKLILASPVGIPDDPYAVNSALPDPSDSTLNNDFTV
DNNTTTSTKNGAAVPPRRPYPSWLVWLWDANVSPFSIVRLAGPLGPRFVSGWTSRRFNHLPADDANTLHDYS
FSIFKNKGSGDYALAYILAPGAFARRPVINRINDVGRNPIKGPNGDVVGKDTGIPIVFLYGDNDWLDVAGGL
AADDKLKNVKANILRTGTDDDKANDNGSCKVVIIPKAGHHLYLDNADFFNNILRKDLDDVKDLDKRKRADSS""".replace('\n', '')

# Kyte-Doolittle hydrophobicity scale
kd_scale = {
    'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5,
    'Q': -3.5, 'E': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5,
    'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6,
    'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2
}

# Calculate sliding window hydrophobicity
window_size = 9
hydrophobicity = []
positions = []

for i in range(len(sequence) - window_size + 1):
    window = sequence[i:i+window_size]
    avg_hydro = sum(kd_scale.get(aa, 0) for aa in window) / window_size
    hydrophobicity.append(avg_hydro)
    positions.append(i + window_size // 2)

# Create the plot
plt.figure(figsize=(14, 6), facecolor='white')
plt.plot(positions, hydrophobicity, linewidth=2.5, color='#2E86AB')
plt.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.5)
plt.fill_between(positions, hydrophobicity, 0, 
                 where=np.array(hydrophobicity) > 0, 
                 alpha=0.3, color='#A23B72', label='Hydrophobic')
plt.fill_between(positions, hydrophobicity, 0, 
                 where=np.array(hydrophobicity) < 0, 
                 alpha=0.3, color='#2E86AB', label='Hydrophilic')

# Mark functional domains
plt.axvspan(0, 260, alpha=0.1, color='green', label='Catalytic Core')
plt.axvspan(265, 310, alpha=0.1, color='orange', label='Proline Linker')
plt.axvspan(310, len(sequence), alpha=0.1, color='red', label='WLVW Anchor')

# Styling
plt.xlabel('Residue Position', fontsize=13, fontweight='bold')
plt.ylabel('Hydrophobicity (Kyte-Doolittle)', fontsize=13, fontweight='bold')
plt.title('TP-72 Hydrophobicity Profile\n(Window size = 9 residues)', 
          fontsize=15, fontweight='bold', pad=15)
plt.grid(True, alpha=0.2, linestyle=':')
plt.legend(loc='upper right', framealpha=0.95, fontsize=10)
plt.tight_layout()

# Save the figure
plt.savefig(r'C:\Users\lenovo\Documents\enzem\novel-petase-candidate-trichoderma\images\hydrophobicity_plot.png', 
            dpi=300, bbox_inches='tight')
print("Hydrophobicity plot generated successfully!")
print(f"Total residues: {len(sequence)}")
print(f"Plot saved to: images/hydrophobicity_plot.png")
