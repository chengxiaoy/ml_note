### GAN 
--------
need read the paper


As suggested in the original GAN paper, rather than training G to mini- mize log(1 − D(x, G(x, z)), we instead train to maximize log D(x, G(x, z)) [24].


### conditional GAN (Conditional Generative Adversarial Nets)
conditional version of GAN, both the generator and the discriminator are conditional on some extra information y. y could be 
any kind of auxiliary information.   
in the generator, z and y are combined in joint hidden representation, In the discriminator x and y are presented as 
inputs and to a discriminative function 


![image](https://user-images.githubusercontent.com/19379550/66732119-19133780-ee8d-11e9-97fb-eee0adf88d6e.png)

### infoGAN (InfoGAN: Interpretable Representation Learning by Information Maximizing Generative Adversarial Nets)
------
the generator may not use the conditional latent code, so and mutual information to the loss,
ensure the generator data is correlative to the conditional latent code.

![image](https://user-images.githubusercontent.com/19379550/66907189-8795f800-f03b-11e9-8e82-c7c199a04339.png)
 
For categorical latent code ci, we use the natural choice of softmax nonlinearity to represent Q(ci|x). For continuous 
latent code cj , there are more options depending on what is the true posterior P (cj |x). In our experiments, we have 
found that simply treating Q(cj |x) as a factored Gaussian is sufficient.






### pixel2pixel (Image-to-Image Translation with Conditional Adversarial Networks)
--------
github: https://phillipi.github.io/pix2pix/.

the hole net architecture :   
![image](https://user-images.githubusercontent.com/19379550/66738701-a496c380-eea1-11e9-85b1-517e16cb7e43.png)



the input is not noise z, so the generator architecture is u-net, an encoder-decoder net with skip connections.

![image](https://user-images.githubusercontent.com/19379550/66738571-6e594400-eea1-11e9-87bc-0584e72e8f8b.png)

The objective of a conditional GAN can be expressed as:   
![image](https://user-images.githubusercontent.com/19379550/66739003-5cc46c00-eea2-11e9-80b4-9bce1421eec4.png)


Previous approaches have found it beneficial to mix the GAN objective with a more traditional loss, such as L2 distance,
 using L1 distance rather than L2 as L1 encourages less blurring.
 ![image](https://user-images.githubusercontent.com/19379550/66739112-96957280-eea2-11e9-9d6b-cb036bd06b72.png)






### DCGAN (UNSUPERVISED REPRESENTATION LEARNING WITH DEEP CONVOLUTIONAL GENERATIVE ADVERSARIAL NETWORKS)
-----
1. this paper guide how to train convolutional GAN, which have be more demonstrated by WGAN    

2. discriminator’s convolutional features as a feature extractor to evaluate the quality for unsupervised representation learning     

3. visualize the filters learnt by GANs and empirically show that specific filters have learned to draw specific objects    

4. generators have interesting vector arithmetic properties allowing for easy manipulation of many semantic qualities of generated samples   
![image](https://user-images.githubusercontent.com/19379550/65681697-037bd080-e08c-11e9-9cb2-56c8dff8471e.png)


### WGAN (Wasserstein GAN)
-----





### Cycle-GAN（Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks）

img2img translation : pix2pix framework which use conditional generative adversarial network
unpaired img2img translation: cycle gan,use a cycle consistency loss as a way of using transitivity to supervise cnn training.


cycle-consistency loss:
![image](https://user-images.githubusercontent.com/19379550/66536259-e85e9580-eb4e-11e9-9dad-19714c3be39b.png)

![image](https://user-images.githubusercontent.com/19379550/66537007-86535f80-eb51-11e9-8aaf-05540dc42af1.png)


Adversarial Loss:
![image](https://user-images.githubusercontent.com/19379550/66536995-7e93bb00-eb51-11e9-98da-c6ccf3e888dd.png)

full objective:
![image](https://user-images.githubusercontent.com/19379550/66537052-af73f000-eb51-11e9-939b-a09ca317f13c.png)


how to evaluate translation effect?

evaluation metrics :
1. AMT perceptual studies to evaluate maps<->aerial photos
2. FCN score to evaluate labels-photo
3. semantic segmentation metrics to evaluate photos-labels


others methods(baseline):    
- CoGAN: learns one GAN generator for domain X and one for domain Y , with tied weights on the first few layers for shared 
latent representations. Translation from X to Y can be achieved by finding a latent representation that generates 
image X and then rendering this latent representation into style Y .     
  
- SimGAN: adversarial loss to train domain x to domain y, regularization term |x- G(x|    

- BiGAN/ALI: 

- pix2pix: conditional GAN


result:
![image](https://user-images.githubusercontent.com/19379550/66555091-abab9200-eb80-11e9-8121-a85aba522a82.png)


### CoGAN (Coupled Generative Adversarial Networks)

CoGAN can learn a joint distribution with just samples drawn from the marginal distributions without paired data.    


architecture:   
![image](https://user-images.githubusercontent.com/19379550/66641776-fa732d80-ec4d-11e9-9f42-56bea6202dff.png)


metric:   
pixel agreement ratios

![image](https://user-images.githubusercontent.com/19379550/66693247-91d19280-ecd9-11e9-9a39-d98146dc9ceb.png)

**CelebFaces Attributes dataset for the experiments**    
randomky sampled two points in the 100 dimensional input noise space and visualized the rendered face images as traveling
 from one point to the other.
![image](https://user-images.githubusercontent.com/19379550/66693422-30122800-ecdb-11e9-9ecd-73a4ab9f010e.png)



Applications
- **unsupervised domain adaptation(UDA)**
- **cross domain Image Transformation** ,let L be the loss of two images, Given g1 and g2, the transformation can be 
achieved by first finding the random vector that generates the query image in the 1st domain z∗ = arg minz L(g1(z), x1). 
After finding z∗, one can apply g2 to obtain the transformed image, x2 = g2(z∗). 