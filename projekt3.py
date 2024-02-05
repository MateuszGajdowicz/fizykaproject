from charges import OscillatingCharge
from field_calculations import MovingChargesField
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import warnings
warnings.filterwarnings("ignore")  # suppress warnings
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import scipy.constants as constants
c = constants.c  # set speed of light constant
charge = OscillatingCharge(pos_charge=True, direction=(1, 0, 0), start_position=(-2e-9, 0, 0), max_speed=0.5*c)
field = MovingChargesField(charge)
t = 0
lim = 50e-9  # 50 nm
grid_size = 101  # number of points along x and z direction
X, Y, Z = np.meshgrid(np.linspace(-lim, lim, grid_size), 0,
                      np.linspace(-lim, lim, grid_size), indexing='ij')
E_total = field.calculate_E(t=t, X=X, Y=Y, Z=Z, pcharge_field='Total', plane=True)
B_total = field.calculate_B(t=t, X=X, Y=Y, Z=Z, pcharge_field='Total', plane=True)
E_acc = field.calculate_E(t=t, X=X, Y=Y, Z=Z, pcharge_field='Acceleration', plane=True)
B_acc = field.calculate_B(t=t, X=X, Y=Y, Z=Z, pcharge_field='Acceleration', plane=True)
E_vel = field.calculate_E(t=t, X=X, Y=Y, Z=Z, pcharge_field='Velocity', plane=True)
B_vel = field.calculate_B(t=t, X=X, Y=Y, Z=Z, pcharge_field='Velocity', plane=True)
im = plt.imshow(E_total[0].T, cmap='viridis', origin='lower', aspect='equal', extent=(-lim, lim, -lim, lim))
im.set_norm(mpl.colors.SymLogNorm(linthresh=1e5, linscale=1, vmin=-1e7, vmax=1e7, base=10))
plt.colorbar(im, label='$E_x$ [N/C]')
plt.xlabel('$x$ [m]')
plt.ylabel('$z$ [m]')
plt.show()
fig, axes = plt.subplots(nrows=1, ncols=3)
ims = [None]*3
ims[0] = axes[0].imshow(E_total[0].T, cmap='viridis', origin='lower', aspect='equal', extent=(-lim, lim, -lim, lim))
ims[1] = axes[1].imshow(E_vel[0].T, cmap='viridis', origin='lower', aspect='equal', extent=(-lim, lim, -lim, lim))
ims[2] = axes[2].imshow(E_acc[0].T, cmap='viridis', origin='lower', aspect='equal', extent=(-lim, lim, -lim, lim))
for i in range(0, 3):
    ims[i].set_norm(mpl.colors.SymLogNorm(linthresh=1e5, linscale=1, vmin=-1e7, vmax=1e7, base=10))

# Add colorbar for E fields
Ecax = inset_axes(axes[2],
                  width="6%",
                  height="100%",
                  loc='lower left',
                  bbox_to_anchor=(1.05, 0., 1, 1),
                  bbox_transform=axes[2].transAxes,
                  borderpad=0,
                  )
plt.colorbar(ims[2], cax=Ecax, label='$E_x$ [N/C]')
axes[1].set_xlabel('$x$ [m]')
axes[0].set_ylabel('$z$ [m]')
plt.tight_layout()
plt.show()
fig, axes = plt.subplots(nrows=1, ncols=3)
ims = [None]*3
ims[0] = axes[0].imshow(E_total[0].T, cmap='viridis', origin='lower', aspect='equal', extent=(-lim, lim, -lim, lim))
ims[1] = axes[1].imshow(E_total[1].T, cmap='viridis', origin='lower', aspect='equal', extent=(-lim, lim, -lim, lim))
ims[2] = axes[2].imshow(E_total[2].T, cmap='viridis', origin='lower', aspect='equal', extent=(-lim, lim, -lim, lim))
for i in range(0, 3):
    ims[i].set_norm(mpl.colors.SymLogNorm(linthresh=1e5, linscale=1, vmin=-1e7, vmax=1e7, base=10))

# Add colorbar for E fields
Ecax = inset_axes(axes[2],
                  width="6%",  # width = 5% of parent_bbox width
                  height="100%",  # height : 50%
                  loc='lower left',
                  bbox_to_anchor=(1.05, 0., 1, 1),
                  bbox_transform=axes[2].transAxes,
                  borderpad=0,
                  )
plt.colorbar(ims[2], cax=Ecax, label='$E$ [N/C]')
axes[1].set_xlabel('$x$ [m]')
axes[0].set_ylabel('$z$ [m]')
plt.tight_layout()
plt.show()
V, Ax, Ay, Az = field.calculate_potentials(t=t, X=X, Y=Y, Z=Z, plane=True)
im = plt.imshow(V.T, cmap='viridis', origin='lower', aspect='equal', extent=(-lim, lim, -lim, lim))
im.set_norm(mpl.colors.LogNorm(vmin=1e-2, vmax=1e0))
plt.colorbar(im, label='$\Phi$ [V]')
plt.xlabel('$x$ [m]')
plt.ylabel('$z$ [m]')
plt.show()