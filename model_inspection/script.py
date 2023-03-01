import tensorflow as tf 

model = tf.keras.models.load_model("/workspace/TESTS/fpga101gan/float/vanilla_gan_generator")

from tensorflow_model_optimization.quantization.keras import vitis_inspect

inspector = vitis_inspect.VitisInspector(target="DPUCZDX8G_ISA1_B1600")
inspector.inspect_model(model, 
                        plot=True, 
                        plot_file="model.svg", 
                        dump_results=True, 
                        dump_results_file="inspect_results.txt", 
                        verbose=0)
