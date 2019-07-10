### Regional Attention Based Deep Feature for Image Retrieval

the method is based on R-MAC by add context-aware regional attention network

this is a pre-trained single-pass category.

![description](https://user-images.githubusercontent.com/19379550/60946066-d5ee7900-a31f-11e9-9bd5-e4b92b54dcb9.jpg)   

when we get the R-MAC regional feature maps, the pooling weight will be learned from the regional information.
the delf and crow are used the non-parametric model for calculating attention weights, these methods
did not utilize the global context , and used pixed-based attention in feature map space.


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

 