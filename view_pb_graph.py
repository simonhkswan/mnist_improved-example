import tensorflow as tf
import time

# Change the two file paths
pb_file_loc = '../CIFAR10/graphs/cifar_optimized.pb' ##PB FILE PATH##
log_file_loc = '../CIFAR10/graphs/optimized' ##LOG OUTPUT PATH FOR TENSOR BOARD##

fw = tf.summary.FileWriter(log_file_loc)
from tensorflow.python.platform import gfile
with tf.Session() as sess:
	with gfile.FastGFile(pb_file_loc, 'rb') as infile:
		gdef = tf.GraphDef()
		gdef.ParseFromString(infile.read())
		g_in = tf.import_graph_def(gdef)
		fw.add_graph(sess.graph)
time.sleep(5)
print("Output file saved.")

# Then run tensorboard --logdir='./' in the log_file location to view the graph.