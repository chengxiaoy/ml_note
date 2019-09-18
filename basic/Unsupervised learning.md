unsupervised learning
------
wikipedia explain:   
A central application of unsupervised learning is in the field of density estimation in statistics
supervised learning intends to infer a conditional probability distribution 
conditioned on the label  of input data;unsupervised learning intends to infer an a priori probability distribution.

most common algorithms:
- clustering
- Anomaly detection
- Neural networks  (Autoencoders/ Deep Belief Nets/ Generative Adversarial Networks/ self-organizing map)
- latent variable models (Expectation-maximization algorithm, blind signal separation)

bind signal separation: the objective is to recover the original component signals from a mixture signal


#### auto-encoder

The fundamental problem with autoencoders, for generation, is that the latent space they convert their inputs to 
and where their encoded vectors lie, may not be continuous, or allow easy interpolation
![image](https://user-images.githubusercontent.com/19379550/64095477-78136600-cd91-11e9-996b-c64e2dc1f086.png)

so it is fine if just replicating the same images.

#### variational auto-encoder
VAE:  their latent spaces are, by design, continuous, allowing easy random sampling and interpolation.    
the encoder not output an encoding vector of size n,rather, outputting two vectors of size n: a vector of means, μ, 
and another vector of standard deviations, σ.
![image](https://user-images.githubusercontent.com/19379550/64095671-11db1300-cd92-11e9-82a0-aa8971a40490.png)
![image](https://user-images.githubusercontent.com/19379550/64095713-31723b80-cd92-11e9-8a2e-dcb9ec586b35.png)


However, since there are no limits on what values vectors μ and σ can take on, the encoder can learn to generate 
very different μ for different classes, clustering them apart, and minimize σ, making sure the encodings themselves 
don’t vary much for the same sample (that is, less uncertainty for the decoder). This allows the decoder to 
efficiently reconstruct the training data.

![image](https://user-images.githubusercontent.com/19379550/64095828-857d2000-cd92-11e9-9e1c-bf271aa4315b.png)

to force this, introduce the Kullback–Leibler divergence (KL divergence) into the loss function.
if only apply the kl divergence loss:
![image](https://user-images.githubusercontent.com/19379550/64095961-e86eb700-cd92-11e9-92d0-13b242959a20.png)

mix the reconstruction loss and kl divergence loss:
![image](https://user-images.githubusercontent.com/19379550/64096022-15bb6500-cd93-11e9-92f3-d3f31455e0ec.png)



the applications :
![image](https://user-images.githubusercontent.com/19379550/64096154-70ed5780-cd93-11e9-8d13-76f8971cfa2d.png)


https://github.com/yzwxx/vae-celebA


all above pic from https://towardsdatascience.com/intuitively-understanding-variational-autoencoders-1bfe67eb5daf

#### variational Inference


变分推断：
https://www.cnblogs.com/yifdu25/p/8181185.html
![image](https://user-images.githubusercontent.com/19379550/64235311-a6787900-cf2a-11e9-95dd-cdfa45d84d86.png)
