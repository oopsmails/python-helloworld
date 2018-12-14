import numpy as np
import tensorflow as tf

X_1 = tf.placeholder(tf.float32, name="X_1")
X_2 = tf.placeholder(tf.float32, name="X_2")

multiply = tf.multiply(X_1, X_2, name="multiply")

with tf.Session() as session:
    result = session.run(multiply, feed_dict={X_1: [1, 2, 3], X_2: [4, 5, 6]})
    print(result)

x_input = np.random.sample((1, 2))
print(x_input)

# using a placeholder
x = tf.placeholder(tf.float32, shape=[1, 2], name='X')

dataset = tf.data.Dataset.from_tensor_slices(x)
iterator = dataset.make_initializable_iterator()
get_next = iterator.get_next()

with tf.Session() as sess:
    # feed the placeholder with data
    sess.run(iterator.initializer, feed_dict={x: x_input})
    print(sess.run(get_next))  # output [ 0.52374458  0.71968478]
