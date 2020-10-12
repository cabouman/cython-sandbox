
import numpy as np
import matplotlib.pyplot as plt

import svmbir

import os
os.chdir("/Users/bouman/PycharmProjects/Data/demo-data")

sino = np.load('sinodata.npy')
weight = np.load('weightdata.npy')

(num_views, num_slices, num_channels) = sino.shape
angles = np.linspace(0, np.pi, num_views, endpoint=False)

x = svmbir.recon(sino, angles, weight, num_threads=20,
    center_offset=-6, img_downsamp=4,
    sigma_x=0.6350, T=0.000478, max_iterations=10)

proj = svmbir.project(angles, x, num_threads=20,
    center_offset=-6, img_downsamp=4)


## display output #################################
imgplot = plt.imshow(x[0])
imgplot.set_cmap('gray')
plt.colorbar()

plt.savefig('recon.png')
plt.show()
plt.close()

imgplot = plt.imshow(np.swapaxes(sino, 0, 1)[0])
imgplot.set_cmap("gray")
plt.colorbar()
plt.savefig("sino.png")
plt.show()
plt.close()

imgplot = plt.imshow(np.swapaxes(sino-proj, 0, 1)[0])
imgplot.set_cmap('gray')
plt.colorbar()
plt.savefig('err_sino.png')
plt.close()