import tensorflow as tf

saved_model_dir = 'models/fasterrcnn.pb'
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tf_lite_model = converter.convert()
open('fasterrcnn.tflite', 'wb').write(tf_lite_model)
