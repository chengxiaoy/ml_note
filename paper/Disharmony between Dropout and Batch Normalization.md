Understanding the Disharmony between Dropout and Batch Normalization by Variance Shift
-------

&emsp;&emsp;the paper explained the disharmony between dropout and batch normalization.
Dropout would shift the variance of a specific neural unit when we transfer the state of that network from train to test
BN would maintain its statistical variance, which is accumulated from the entire learning procedure, in the test phase.

##### Dropout for X

- in the train phase x<sub>k</sub> = a<sub>k</sub>x<sub>k</sub>, where a<sub>k</sub> comes from Bernoulli distribution
![Bernouli distribution](https://user-images.githubusercontent.com/19379550/60651540-03977600-9e79-11e9-99ec-8983056d7876.jpg)
- at test time for dropout, scale down the weights by multiple them by a factory of p(dropout retain ratio)
- the same effect is scale up the retained activations by multiplying by the 1/p at train time and not modifying the weights
at test time.


##### Batch Normalization
- normalizing each neuron into zero mean and unit variance
![BN](https://user-images.githubusercontent.com/19379550/60652077-15c5e400-9e7a-11e9-8624-58d6edbb7f72.jpg)
- m is the mini-batch size, and where μ and σ2 would participate in the backpropagation.
- BN accumulates the moving averages of neural means and variances 
![moving](https://user-images.githubusercontent.com/19379550/60653470-aef5fa00-9e7c-11e9-9a0d-e8ec2f742149.jpg)


consider two situations:
1. the BN layer is directly subsequent to the Dropout layer, where X = a<sub>k</sub> 1/p x<sub>k</sub>
2. the feature vector x = (x1 . . . xd ) would be passed into a convolutional layer (or a fully connectedlayer) 
to form the neural response X, so the X = $\sum$ w<sub>i</sub> a<sub>k</sub> 1/p x<sub>k</sub>

![2situation](https://user-images.githubusercontent.com/19379550/60652543-02674880-9e7b-11e9-8a77-6ffdc25bbfe3.jpg)

if we assume the input come from the distribution with c mean and v variance
and a<sub>i</sub>,x<sub>i</sub> are mutually independent

The following is the inference:   

**Figure2(a)**   
![2a](https://user-images.githubusercontent.com/19379550/60653351-7524f380-9e7c-11e9-8943-3b35c3abe2fe.jpg)

**Figure2(b)**    
![2b](https://user-images.githubusercontent.com/19379550/60654008-b8cc2d00-9e7d-11e9-8fa0-557200365825.jpg)
  
conclusion:
1. **Apply Dropout after all BN layers**
2. **Change Dropout into a more variance-stable form** another form of Dropout that amounts to adding a Gaussian distributed 
random variable with zero mean and standard deviation equal to the activation of the unit, i.e., xi + xir 
and r ∼ N (0, 1), we modify r as a uniform distribution that lies in [−β, β], where 0 ≤ β ≤ 1. 
Therefore, each hidden activation would be X = xi + xiri and ri ∼ U(−β,β).
![last](https://user-images.githubusercontent.com/19379550/60654433-97b80c00-9e7e-11e9-930a-cf9dc0dfe9e2.jpg)

 