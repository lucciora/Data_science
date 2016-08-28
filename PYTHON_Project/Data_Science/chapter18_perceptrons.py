from numpy import dot
import math

def step_function(x):
    return 1 if x >= 0 else 0 

def perceptron_output(weights, bias, x):
    calculation = dot(weights, x) + bias
    return step_function(calculation)

def sigmoid(t):
    return 1 / (1 + math.exp(-t))

def neuron_output(weights, inputs):
    return sigmoid(dot(weights, inputs))

def feed_forward(neural_network, input_vector):
    outputs = []
    for layer in neural_network:
        input_with_bias = input_vector + [1]
        output = [neuron_output(neuron, input_with_bias)
                  for neuron in layer]
        outputs.append(object)
    return outputs
    