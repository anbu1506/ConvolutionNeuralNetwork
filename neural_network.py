import numpy as np

class NN:
    weights={}
    biases={}
    neurons_count = []

    forward_cache = {}

    def __init__(self,input_layer_size,no_of_hidden_layers,hidden_layer_size) -> None:
        # self.input_layer_size = input_layer_size
        # self.no_of_hidden_layers = no_of_hidden_layers
        # self.hidden_layer_size = hidden_layer_size
        self.neurons_count.append(input_layer_size)
        for i in range(no_of_hidden_layers):
            self.neurons_count.append(hidden_layer_size)
        self.neurons_count.append(2)
        all_weights=[]
        all_biases=[]
        for i in range(len(self.neurons_count)-1):
            weights = np.random.rand(self.neurons_count[i+1],self.neurons_count[i])
            biases = np.zeros((self.neurons_count[i+1],1))
            self.weights[i] =weights
            self.biases[i] =biases

    def forward_propagation(self,input):
        self.forward_cache["a"] = {}
        self.forward_cache["z"] = {}
        self.forward_cache["a"][0] = input
        for i in range(1,len(self.neurons_count)):
            print(self.weights[i-1],self.forward_cache["a"][i-1])
            self.forward_cache["z"][i] =  np.dot(self.weights[i-1],self.forward_cache["a"][i-1])+self.biases[i-1]
            self.forward_cache["a"][i] = np.tanh(self.forward_cache["z"][i])
        print(self.forward_cache)
    
    def cost_function(self,y):
        m = y.shape[0]  
        epsilon = 1e-15  

        # Clip predicted values to avoid numerical instability
        self.forward_cache["a"][len(self.neurons_count)-1] = np.clip(self.forward_cache["a"][len(self.neurons_count)-1], epsilon, 1 - epsilon)

        # Binary cross-entropy formula
        cost = - (1 / m) * np.sum(y * np.log(self.forward_cache["a"][len(self.neurons_count)-1]) + (1 - y) * np.log(1 - self.forward_cache["a"][len(self.neurons_count)-1]))
        print("the cost is:",cost)
        return cost
    
    
        






input = np.array([1,2,3]).reshape(3,1)

model = NN(3,2,3)
model.forward_propagation(input)
model.cost_function()