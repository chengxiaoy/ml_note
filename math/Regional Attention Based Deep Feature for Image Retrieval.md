## attention mechanism in CNN


## Regional Attention Based Deep Feature for Image Retrieval
---------

the method is based on R-MAC by add context-aware regional attention network

this is a pre-trained single-pass category.

![description](https://user-images.githubusercontent.com/19379550/60946066-d5ee7900-a31f-11e9-9bd5-e4b92b54dcb9.jpg)   

when we get the R-MAC regional feature maps, the pooling weight will be learned from the regional information.
_the delf and crow are used the non-parametric model for calculating attention weights, these methods
did not utilize the global context , and used pixed-based attention in feature map space_.


### Regional Attention


![region attention](https://user-images.githubusercontent.com/19379550/60946663-5366b900-a321-11e9-820b-880ba0a4c357.jpg)
![annation](https://user-images.githubusercontent.com/19379550/60946718-7c874980-a321-11e9-8532-e347b81aeb49.jpg)


### context awareness
![context awareness](https://user-images.githubusercontent.com/19379550/60947025-3383c500-a322-11e9-90c2-e813fe5e2d09.jpg)

where ⊕ represents a vector concatenation in the channel space.

### training    

- training the parameters (Wr, Wc, br, bc) of the regional attention network via back-propagating gradients of the cross 
 entropy loss of 􏰂y<sub>I</sub> , while freezing parameters of the off-the-shelf CNN.
- use the ILSVRC ImageNet dataset as the training dataset for meeting the purpose of “pre-trained single-pass”.



### Cross-dimensional Weighting for Aggregated Deep Convolutional Features(crow)
-------
learn alpha and beta as the spatial weights and the channel weights
summary:   
![summary](https://user-images.githubusercontent.com/19379550/60952131-4059e600-a32d-11e9-8c01-ab3b2295b9a7.jpg)

 the spatial weight:
 ![](https://user-images.githubusercontent.com/19379550/60948521-ab072380-a325-11e9-8d1c-e0a233f4c85c.jpg)
 where S<sub>i</sub><sub>j</sub> is the sum across channel per spatial location
 
 
 
 For each channel k we find Qk, the proportion of non-zero responses, and compute the per-channel sparsity, 
 Ξk:Ξk = 1-Q<sub>k</sub>, where Q<sub>k</sub>:
 ![](https://user-images.githubusercontent.com/19379550/60951311-70a08500-a32b-11e9-8d16-d6f08e1373cb.jpg)
 
 
### Large-Scale Image Retrieval with Attentive Deep Local Features
--------

attentive local feature descriptor suitable for large-scale image retrieval, 
referred to as DELF (DEep Local Feature).

architecture as below:   
![](https://user-images.githubusercontent.com/19379550/60952400-c8d88680-a32d-11e9-90a2-ec62b77831d4.jpg)
the innovation of this architecture is that the attention score of the local feature, since 
in this retrieval system, global descriptor is deprecated, a image is represent by several discriminative local feature.

the score function is designed use a 2-layer CNN with a softplus activation at top


### Parameter-Free Spatial Attention Network for Person Re-Identification
-----
parameter-free spatial attention,assigns different importance for different locations
![sa](https://user-images.githubusercontent.com/19379550/60954927-6b930400-a332-11e9-8fb7-7ad82f3586ca.jpg) 


attention mechanism in other domain:   
1. [SCA-CNN: Spatial and Channel-wise Attention in Convolutional Networks for Image Captioning](https://arxiv.org/abs/1611.05594)
