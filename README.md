# AR-ioECOG-Pose-Estimation

## Overview  
This repository contains the inference pipeline for markerless EEG electrode localization using stereo video captured by the Microsoft HoloLens 2. It implements a multi-stage deep learning workflow including bounding box detection, super-resolution enhancement, keypoint detection, and 3D triangulation. Pose estimation is performed using a vision-based transformer regression model.

This codebase corresponds to the methods and experiments described in:

**Salim, H.S., et al.**  
*Markerless EEG electrode localization using stereo head-mounted video.*  
*International Journal of Computer Assisted Radiology and Surgery* (2025).  
DOI: [10.1007/s11548-025-03401-5](https://doi.org/10.1007/s11548-025-03401-5)

## License
This code is released under MIT license. See LICENSE.txt.

## Citation
Please cite the following work if this code or method is used:

@article{Salim2025,
  title = {Super-resolution for localizing electrode grids as small,  deformable objects during epilepsy surgery using augmented reality headsets},
  ISSN = {1861-6429},
  url = {http://dx.doi.org/10.1007/s11548-025-03401-5},
  DOI = {10.1007/s11548-025-03401-5},
  journal = {International Journal of Computer Assisted Radiology and Surgery},
  publisher = {Springer Science and Business Media LLC},
  author = {Salim,  Hizirwan S. and Thabit,  Abdullah and Hoogteijling,  Sem and van ’t Klooster,  Maryse A. and van Walsum,  Theo and Zijlmans,  Maeike and Benmahdjoub,  Mohamed},
  year = {2025},
  month = jun 
}
