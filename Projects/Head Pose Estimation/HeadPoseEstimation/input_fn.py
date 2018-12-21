import tensorflow as tf
import os
import numpy as np

def parse_function(filename, label):
    image_string = tf.read_file(filename)

    # Don't use tf.image.decode_image, or the output shape will be undefined
    image = tf.image.decode_jpeg(image_string, channels=1)

    # This will convert to float values in [0, 1]
    image = tf.image.convert_image_dtype(image, tf.float32)

    # image = tf.image.resize_images(image, [64, 64])
    image = tf.image.resize_images(image, [64,64])

    # image = tf.math.l2_normalize(image)

    # convert the label to a one hot vector
    # label = tf.one_hot(label, depth=16)
    # label = label - 1
    return image, label

def input_fn(filenames, labels, batch_size):
    num_samples = len(filenames)
    assert len(filenames) == len(labels), "Filenames and labels should have same length"

    # Create a Dataset serving batches of images and labels
    # We don't repeat for multiple epochs because we always train and evaluate for one epoch
    parse_fn = lambda f, l: parse_function(f, l)

    dataset = (tf.data.Dataset.from_tensor_slices((tf.constant(filenames), tf.constant(labels)))
        .shuffle(num_samples)  # whole dataset into the buffer ensures good shuffling
        .map(parse_fn, num_parallel_calls=4)
        .batch(batch_size)
        .prefetch(1)  # make sure you always have one batch ready to serve
    )

    # Create reinitializable iterator from dataset
    iterator = dataset.make_initializable_iterator()
    # import pdb; pdb.set_trace()
    images, labels = iterator.get_next()
    iterator_init_op = iterator.initializer

    inputs = {'images': images, 'labels': labels, 'iterator_init_op': iterator_init_op}
    return inputs

# with tf.Session() as sess:
#     sess.run(inputs['iterator_init_op'])
#     print(sess.run(tf.shape(inputs['images'])))


