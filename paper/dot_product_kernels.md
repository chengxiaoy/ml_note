### why we need dot_product_kernels

_perceptron:classifier implements the linear decision rule_   
(lr,linear_svm)




to deal with non-linear separability, we introduce a kernel   


**polynomial kernels**

this makes a significant difference when K(x,z) is easier to compute that Φ(x)TΦ(z)   

K(X,Z) = (xT,Z)**2 = Φ(x)TΦ(z)  

**how to choose a good kernel**
![practice_list](https://user-images.githubusercontent.com/19379550/59995608-480d5f80-968a-11e9-96de-7b046d4b2a42.jpg)

why rbf-svm is linear separability
![rbf](https://user-images.githubusercontent.com/19379550/59998481-1c8e7300-9692-11e9-813f-777b51b24a9d.jpg)

the segma bigger, the high dimension weight is smaller,
if the segma is smaller, the dimension will be infinity and will be over-fitting