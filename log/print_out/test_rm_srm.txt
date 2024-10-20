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
ai accu: 0.734833300113678
nature accu:0.9993333220481873
val on:imagenet_ai_0508_adm, Accuracy:0.8670833110809326
## biggan
val on: imagenet_ai_0419_biggan
ai accu: 0.7754999995231628
nature accu:0.9984999895095825
val on:imagenet_ai_0419_biggan, Accuracy:0.8869999647140503
## glide
val on: imagenet_glide
ai accu: 0.9576666355133057
nature accu:0.999833345413208
val on:imagenet_glide, Accuracy:0.9787499904632568
## midjourney
val on: imagenet_midjourney
ai accu: 0.6426666378974915
nature accu:0.9993333220481873
val on:imagenet_midjourney, Accuracy:0.8209999799728394
## sdv4
val on: imagenet_ai_0419_sdv4
ai accu: 0.9914999604225159
nature accu:0.9994999766349792
val on:imagenet_ai_0419_sdv4, Accuracy:0.9954999685287476
## sdv5
val on: imagenet_ai_0424_sdv5
ai accu: 0.9896250367164612
nature accu:0.999750018119812
val on:imagenet_ai_0424_sdv5, Accuracy:0.994687557220459
## vqdm
val on: imagenet_ai_0419_vqdm
ai accu: 0.9079999923706055
nature accu:0.999833345413208
val on:imagenet_ai_0419_vqdm, Accuracy:0.9539166688919067
## wukong
val on: imagenet_ai_0424_wukong
ai accu: 0.9826666712760925
nature accu:0.9996666312217712
val on:imagenet_ai_0424_wukong, Accuracy:0.9911666512489319
## mean
Accuracy:0.9384799599647522
