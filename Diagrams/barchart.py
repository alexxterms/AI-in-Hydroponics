import matplotlib.pyplot as plt

# --- Data ---
months = ['M1', 'M2', 'M3', 'M4']
avg_skill = [3.5, 4.5, 5.0, 5.5]

# --- Plotting ---
plt.figure(figsize=(8, 5))
plt.plot(months, avg_skill, marker='o', linestyle='-', color='purple', linewidth=2)

# Titles and labels
plt.title('Track Improvements Over Time')
plt.xlabel('Month')
plt.ylabel('Avg Skill')

# Annotations
plt.annotate('Initial struggle', xy=('M1', 3.5), xytext=('M1', 3.8),
             arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)
plt.annotate('Continued growth', xy=('M4', 5.5), xytext=('M3.8', 5.8),
             arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)

# Grid and layout
plt.grid(True, linestyle='--', alpha=0.5)
plt.ylim(3, 6)  # adjust y-axis for better visual spacing
plt.tight_layout()
plt.show()
