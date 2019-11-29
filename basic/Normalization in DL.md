### batch normalization

在across mini-batch的维度上去归一化
具体分为temporal batch normalization(1D)和spatial batch normalization(2D)   
对于cnn 中的feature map应用bn时，是对channel维度上去做normalization，computing statistics
on `(N, H, W)` slices，所以每个location上的方差均值都是一致的,所以称为 Spatial Batch Normalization   
batchNorm是在batch上，对NHW做归一化，对小batchsize效果不好

### layer normalization
针对每一层的神经元都使用 归一化 ，会降低模型表达能力，因为该层所有神经元都会使用同一个转换
layerNorm在通道方向上，对CHW归一化，主要对RNN作用明显；

### weight normalization
对参数做归一化，可以间接对数据进行scale,但是没有shift

### cosine normalization
不在使用点击作为权重和数据之间的计算方式，使用夹角的余弦作为计算结果

### group norm
主要是针对Batch Normalization对小batchsize效果差，GN将channel方向分group，然后每个group内做归一化，算(C//G)*H*W的均值，这样与batchsize无关，不受其约束

### instance norm
instanceNorm在图像像素上，对HW做归一化，用在风格化迁移