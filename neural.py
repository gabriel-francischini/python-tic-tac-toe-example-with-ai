


class Neuron:

    def __init__(self, weights):
        self.weights = weights

    def evaluate(self, inputs):
        counter = 0
        for index in range(0, len(self.weights)):
            counter += self.weights[index] * inputs[index]

        if counter > 1:
            counter = 1
        if counter < -1:
            counter = -1
        return counter


    



class NeuronLayer():

    def __init__(self, neurons_weights):
        self.neurons = []
        for weights in neurons_weights:
            neuron = Neuron(weights)
            self.append(neurons)

    def evaluate(self, inputs):
        output = [neuron.evaluate(inputs)
                  for neuron in self.neurons]
        return output


class NeuronNetwork():
    def __init__(self, n_inputs=9, n_hidden=2,
                 size_hidden=9, n_output=2, weights):
        copy_weights = list(tuple(weights))

        input_layer = []
        for input_neuron in range(0, size_hidden):
            input_weights = []
            for weight in range(0, n_inputs):
                input_weights.append(copy_weights.pop(0))

            neuron = Neuron(input_weights)
            input_layer.append(neuron)

        hidden_layers = []
        for hidden_layer in range(0, n_hidden):
            hidden_layer = []
            for neuron in range(0, size_hidden):
                input_weights = []
                for weight in range(0, len(input_layer)):
                    input_weights.append(copy_weights.pop(0))

                neuron = Neuron(input_weights)
                hidden_layer.append(neuron)

            hidden_layers.append(hidden_layer)

        output_layer = []
        for output_neuron in range(0, n_output):
            output_weights = []
            for weight in range(0, len(hidden_layers[-1])):
                output_weights.append(copy_weights.pop(0))
            neuron = Neuron(output_weights)
            output_layer.append(neuron)

        self.input_layer = input_layer
        self.hidden_layers = hidden_layers
        self.output_layer = output_layer


    def evaluate(self, inputs):
        intermediary = [neuron.evaluate(inputs) for neuron in self.input_layer]

        for hidden_layer in self.hidden_layers:
            intermediary = [neuron.evaluate(intermediary) for neuron in hidden_layer]

        output = [neuron.evaluate(intermediary) for neuron in self.output_layer]

        return output

