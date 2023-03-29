# GANs-on-FPGA
This repository hosts the code related to the project "Generative adversarial networks on FPGA" realized in collaboration with NECSTLab (Politecnico di Milano).
The project targets a ULTRA96v2 board by AVNET. The OS image used to run the deep learning model inference is PYNQ DPU 3.0 for ULTRA96v2 and the .xmodel has been produced using Xilinx Vitis AI 2.5.

# Model 
The proposed model is a CNN GAN which is trained to generate grayscale images of clothes out of Gaussian Noise. The training dataset is from Zalando. The model is not very heavy on memory consumption. Training, however, was quite demanding compmutationally speaking. 

# Training 
The noteboook gan-fpga101 contains the training of the model. It has been mutuated from a previous work which was presented during 2022 edition of the Artificial Neural Networks and Deep Learning course at Politecnico di Milano. Credits to lecturer E. Lomurno. 
The model underwent some changes to best fit the DPU architecture made according to the limitations listed in the Vitis AI documentation at https://docs.xilinx.com/r/en-US/ug1414-vitis-ai/Vitis-AI-Overview. These changes hampered the convergence of the conditional GAN model, so the vanilla one was used for compilation and inference acceleration (see training notebook gan-fpga-training-v2-dpu-aware). 
# Quantization 
The model has been quantized using Vitis AI 2.5 quantizer (post training). See the related notebook under /quantization. 

# Inspection and compilation
Results of pre-compilation model inspection  and compilation itself can be inspected looking under the related folders. 

# Inference 
The fpga_model folder hosts a Pynq DPU notebook for inference on the FPGA platform leveraging popular ML libraries (see gandpu). The board used ran Pynq DPU 3.0 Petalinux.
