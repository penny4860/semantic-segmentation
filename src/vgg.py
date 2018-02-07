# -*- coding: utf-8 -*-

import tensorflow.contrib.slim as slim
import tensorflow as tf

class Vgg16(object):
    def __init__(self, input_tensor):
        rgb = input_tensor - [123.68, 116.779, 103.939]
        # Build convolutional layers only
        self.conv1_1 = slim.conv2d(rgb, 64, [3, 3], scope='vgg_16/conv1/conv1_1')
        self.conv1_2 = slim.conv2d(self.conv1_1, 64, [3, 3], scope='vgg_16/conv1/conv1_2')
        self.pool1 = slim.max_pool2d(self.conv1_2, [2, 2], scope='pool1')
        
        self.conv2_1 = slim.conv2d(self.pool1, 128, [3, 3], scope='vgg_16/conv2/conv2_1')
        self.conv2_2 = slim.conv2d(self.conv2_1, 128, [3, 3], scope='vgg_16/conv2/conv2_2')
        self.pool2 = slim.max_pool2d(self.conv2_2, [2, 2], scope='pool2')
        
        self.conv3_1 = slim.conv2d(self.pool2, 256, [3, 3], scope='vgg_16/conv3/conv3_1')
        self.conv3_2 = slim.conv2d(self.conv3_1, 256, [3, 3], scope='vgg_16/conv3/conv3_2')
        self.conv3_3 = slim.conv2d(self.conv3_2, 256, [3, 3], scope='vgg_16/conv3/conv3_3')
        self.pool3 = slim.max_pool2d(self.conv3_3, [2, 2], scope='pool3')
         
        self.conv4_1 = slim.conv2d(self.pool3, 512, [3, 3], scope='vgg_16/conv4/conv4_1')
        self.conv4_2 = slim.conv2d(self.conv4_1, 512, [3, 3], scope='vgg_16/conv4/conv4_2')
        self.conv4_3 = slim.conv2d(self.conv4_2, 512, [3, 3], scope='vgg_16/conv4/conv4_3')
        self.pool4 = slim.max_pool2d(self.conv4_3, [2, 2], scope='pool4')
         
        self.conv5_1 = slim.conv2d(self.pool4, 512, [3, 3], scope='vgg_16/conv5/conv5_1')
        self.conv5_2 = slim.conv2d(self.conv5_1, 512, [3, 3], scope='vgg_16/conv5/conv5_2')
        self.conv5_3 = slim.conv2d(self.conv5_2, 512, [3, 3], scope='vgg_16/conv5/conv5_3')
        self.pool5 = slim.max_pool2d(self.conv5_3, [2, 2], scope='pool5')
        
        # Use conv2d instead of fully_connected layers.
        self.pool6 = slim.conv2d(self.pool5, 4096, [7, 7], scope='vgg_16/fc6')
#         net = slim.dropout(net, dropout_keep_prob, is_training=is_training,
#                          scope='dropout6')
        self.pool7 = slim.conv2d(self.pool6, 4096, [1, 1], scope='vgg_16/fc7')
        
#         self.layers = {'conv1_1' : self.conv1_1,
#                        'conv1_2' : self.conv1_2,
#                        'conv2_1' : self.conv2_1,
#                        'conv2_2' : self.conv2_2,
#                        'conv3_1' : self.conv3_1,
#                        'conv3_2' : self.conv3_2,
#                        'conv3_3' : self.conv3_3,
#                        'conv4_1' : self.conv4_1,
#                        'conv4_2' : self.conv4_2,
#                        'conv4_3' : self.conv4_3,
#                        'conv5_1' : self.conv5_1,
#                        'conv5_2' : self.conv5_2,
#                        'conv5_3' : self.conv5_3,
#                        
#                        }

    def load_ckpt(self, sess, ckpt='ckpts/vgg_16.ckpt'):
        variables = slim.get_variables(scope='vgg_16')
        init_assign_op, init_feed_dict = slim.assign_from_checkpoint(ckpt, variables)
        sess.run(init_assign_op, init_feed_dict)


if __name__ == '__main__':
    import tensorflow as tf
    import numpy as np
    input_tensor = tf.placeholder(tf.float32, [None, None, None, 3])
    vgg = Vgg16(input_tensor)
    
    np.set_printoptions(linewidth=20000, threshold=1000000, suppress=False)
    np.random.seed(1234)
    
    x = np.random.randn(1, 32, 32, 3)
    # vgg_path = os.path.join('data_tiny', 'vgg')
     
    # tf.set_random_seed(1234)
    with tf.Session() as sess:
        # input_tensor, keep_prob_tensor, layer3, layer4, layer7 = load_vgg(sess, vgg_path)
#         sess.run(tf.global_variables_initializer())
#         pool3_value, pool4_value, pool7_value = sess.run([layer3, layer4, layer7], feed_dict = {input_tensor : x,
#                                                                                                 keep_prob_tensor : 1.0})
        
        sess.run(tf.global_variables_initializer())
        vgg.load_ckpt(sess, ckpt="../data_tiny/vgg/vgg_16.ckpt")
        pool6_value, pool7_value = sess.run([vgg.pool6, vgg.pool7], feed_dict = {input_tensor: x})
        pool6_value = pool6_value.reshape(-1,)
        pool7_value = pool7_value.reshape(-1,)
        print(pool6_value[:3], pool7_value[:3])
        
    
    
    
    
    
    
    
    
    
    
    
