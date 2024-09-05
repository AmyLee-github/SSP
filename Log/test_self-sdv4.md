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
                  isTrain: True                          	[default: None]
                    isVal: False                         	[default: None]
               jpg_method: ['pil', 'cv2']                
                 jpg_prob: 0.0                           
                 jpg_qual: [90, 100]                     
                     load: /hxp/ly/L40/SSP-AI-Generated-Image-Detection/snapshot/sortnet/Net_epoch_best.pth	[default: None]
                 log_name: log3.log                      
                       lr: 0.0001                        
                     name: experiment_name               
               patch_size: 32                            	[default: 32]
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
load model from /hxp/ly/L40/SSP-AI-Generated-Image-Detection/snapshot/sortnet/Net_epoch_best.pth
# Start train
# 结果
## adm
val on: imagenet_ai_0508_adm
ai accu: 0.8263333439826965
nature accu:0.9881666302680969
val on:imagenet_ai_0508_adm, Accuracy:0.9072499871253967
## biggan
val on: imagenet_ai_0419_biggan
ai accu: 0.4623333215713501
nature accu:0.9883333444595337
val on:imagenet_ai_0419_biggan, Accuracy:0.7253333330154419
## glide
val on: imagenet_glide
ai accu: 0.953166663646698
nature accu:0.9883333444595337
val on:imagenet_glide, Accuracy:0.9707499742507935
## midjourney
val on: imagenet_midjourney
ai accu: 0.6725000143051147
nature accu:0.9878333210945129
val on:imagenet_midjourney, Accuracy:0.8301666378974915
## sdv4
val on: imagenet_ai_0419_sdv4
ai accu: 0.9893333315849304
nature accu:0.9866666793823242
val on:imagenet_ai_0419_sdv4, Accuracy:0.9879999756813049
## sdv5
val on: imagenet_ai_0424_sdv5
ai accu: 0.9890000224113464
nature accu:0.9883750677108765
val on:imagenet_ai_0424_sdv5, Accuracy:0.9886875748634338
## vqdm
val on: imagenet_ai_0419_vqdm
ai accu: 0.9526666402816772
nature accu:0.9853333234786987
val on:imagenet_ai_0419_vqdm, Accuracy:0.968999981880188
## wukong
val on: imagenet_ai_0424_wukong
ai accu: 0.9773333072662354
nature accu:0.9894999861717224
val on:imagenet_ai_0424_wukong, Accuracy:0.9834166765213013
## mean
Accuracy:0.9230599999427795
