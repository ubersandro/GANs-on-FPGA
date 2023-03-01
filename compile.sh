#!/bin/bash 
vai_c_tensorflow2 -m ./quantize/model_quant.h5 --arch /opt/vitis_ai/compiler/arch/DPUCZDX8G/ULTRA96v2/arch.json -o ./compiled_model -n ganmodel 2>&1 > compilation_log 
