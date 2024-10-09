# Options
----------------- Options ---------------
                 CropSize: 224                           
                      aug: True                          
                batchsize: 64                            
                blur_prob: 0.0                           
                 blur_sig: [0, 1]                        
                  choices: [0, 0, 0, 0, 1, 0, 0, 0]      
                    epoch: 30                            
                   gpu_id: 0                             
               image_root: /hxp/dataset/genImage         
                  isPatch: True                          
                  isTrain: True                                 [default: None]
                    isVal: False                                [default: None]
               jpg_method: ['pil', 'cv2']                
                 jpg_prob: 0.0                           
                 jpg_qual: [90, 100]                     
                     load: /hxp/ly/SSP-AI-Generated-Image-Detection/snapshots/sd4/Net_epoch_best.pth    [default: None]
                 log_name: log3.log                      
                       lr: 0.0001                        
                     name: experiment_name               
               patch_size: 32                                   [default: 32]
                rz_interp: bilinear                      
                save_path: ./snapshot/sortnet/           
                trainsize: 256                           
            val_batchsize: 64                            
             val_interval: 1                             
----------------- End -------------------
# load data...
val on: imagenet_ai_0508_adm
val on: imagenet_ai_0419_biggan
val on: imagenet_glide
val on: imagenet_midjourney
val on: imagenet_ai_0419_sdv4
val on: imagenet_ai_0424_sdv5
val on: imagenet_ai_0419_vqdm
val on: imagenet_ai_0424_wukong
USE GPU 0
load model from /hxp/ly/SSP-AI-Generated-Image-Detection/snapshots/sd4/Net_epoch_best.pth
# Start train
# 结果
## adm
val on: imagenet_ai_0508_adm
ai accu: 0.8793333172798157
nature accu:0.9916666746139526
val on:imagenet_ai_0508_adm, Accuracy:0.9354999661445618
## biggan
val on: imagenet_ai_0419_biggan
ai accu: 0.5744999647140503
nature accu:0.9929999709129333
val on:imagenet_ai_0419_biggan, Accuracy:0.7837499976158142
## glide
val on: imagenet_glide
ai accu: 0.9818333387374878
nature accu:0.9928333163261414
val on:imagenet_glide, Accuracy:0.9873332977294922
## midjourney
val on: imagenet_midjourney
ai accu: 0.6924999952316284
nature accu:0.9928333163261414
val on:imagenet_midjourney, Accuracy:0.8426666855812073
## sdv4
val on: imagenet_ai_0419_sdv4
ai accu: 0.9904999732971191
nature accu:0.9916666746139526
val on:imagenet_ai_0419_sdv4, Accuracy:0.9910833239555359
## sdv5
val on: imagenet_ai_0424_sdv5
ai accu: 0.9912500381469727
nature accu:0.9927500486373901
val on:imagenet_ai_0424_sdv5, Accuracy:0.9920000433921814
## vqdm
val on: imagenet_ai_0419_vqdm
ai accu: 0.9259999990463257
nature accu:0.9918333292007446
val on:imagenet_ai_0419_vqdm, Accuracy:0.9589166641235352
## wukong
val on: imagenet_ai_0424_wukong
ai accu: 0.9800000190734863
nature accu:0.9936666488647461
val on:imagenet_ai_0424_wukong, Accuracy:0.9868333339691162
## mean
Accuracy:0.9370499849319458