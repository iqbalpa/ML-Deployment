import tensorflow as tf

def get_model():
  model = tf.keras.applications.ResNet50(
    include_top=False,
    weights='imagenet',
    input_shape=(300, 300, 3),
  )

  # freeze the layer from pretrained model
  for layer in model.layers:
    layer.trainable = False

  # get the last layer
  last_layer = model.get_layer("conv5_block3_out")
  last_output = last_layer.output

  # create final layer for our classifier
  x = tf.keras.layers.GlobalAveragePooling2D()(last_output)
  x = tf.keras.layers.Dense(1024, activation='relu')(x)
  x = tf.keras.layers.Dense(6, activation='softmax')(x)

  final_model = tf.keras.Model(
    inputs=model.input,
    outputs=x
  )

  final_model.load_weights("./final.weights.h5")

  return final_model
