import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

def update_plot(val):
    try:
        sig_x = float(text_sigx.text)
        sig_y = float(text_sigy.text)
        tau_xy = float(text_tau.text)
        theta_deg = float(text_theta.text)
        theta_rad = np.radians(theta_deg)

        center = (sig_x + sig_y) / 2
        radius = np.sqrt(((sig_x - sig_y) / 2)**2 + tau_xy**2)
        
        sigma_1 = center + radius
        sigma_2 = center - radius
        
        sig_theta = center + ((sig_x - sig_y) / 2) * np.cos(2 * theta_rad) + tau_xy * np.sin(2 * theta_rad)
        tau_theta = -((sig_x - sig_y) / 2) * np.sin(2 * theta_rad) + tau_xy * np.cos(2 * theta_rad)

        ax.clear()
        ax.set_aspect('equal')
        ax.axhline(0, color='black', lw=1)
        ax.axvline(0, color='black', lw=1)
        ax.set_xlabel(r'$\sigma$ (Normal Stress)')
        ax.set_ylabel(r'$\tau$ (Shear Stress)')
        ax.set_title(f"Mohr's Circle (Theta = {theta_deg}°)")

        circle = plt.Circle((center, 0), radius, color='blue', fill=False, lw=2, label='Mohr Circle')
        ax.add_artist(circle)

        ax.plot([sig_x, sig_y], [-tau_xy, tau_xy], 'ro-', label='X-Y Plane')
        
        ax.plot(sig_theta, tau_theta, 'go', markersize=8, label=f'Stress at {theta_deg}°')
        
        limit = max(abs(sigma_1), abs(sigma_2), radius) + 5
        ax.set_xlim(center - radius - 10, center + radius + 10)
        ax.set_ylim(-radius - 10, radius + 10)
        ax.legend(loc='upper right', fontsize='small')
        ax.grid(True, linestyle='--')
        
        plt.draw()
    except ValueError:
        pass 

fig, ax = plt.subplots(figsize=(8, 7))
plt.subplots_adjust(bottom=0.25)

axbox_sx = plt.axes([0.1, 0.1, 0.1, 0.05])
axbox_sy = plt.axes([0.3, 0.1, 0.1, 0.05])
axbox_t  = plt.axes([0.5, 0.1, 0.1, 0.05])
axbox_th = plt.axes([0.75, 0.1, 0.1, 0.05])

text_sigx = TextBox(axbox_sx, r'$\sigma_x$ ', initial="50")
text_sigy = TextBox(axbox_sy, r'$\sigma_y$ ', initial="10")
text_tau  = TextBox(axbox_t, r'$\tau_{xy}$ ', initial="20")
text_theta = TextBox(axbox_th, r'$\theta$ ', initial="30")

text_sigx.on_submit(update_plot)
text_sigy.on_submit(update_plot)
text_tau.on_submit(update_plot)
text_theta.on_submit(update_plot)

update_plot(None)

plt.show()