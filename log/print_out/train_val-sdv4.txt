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
                     load: None                          
                 log_name: log3.log                      
                       lr: 1e-4                          	[default: 0.0001]
                     name: experiment_name               
               patch_size: 32                            	[default: 32]
                rz_interp: bilinear                      
                save_path: ./snapshot/sortnet/           
                trainsize: 256                           
            val_batchsize: 64                            
             val_interval: 1                             
----------------- End -------------------
# load data...
train on: imagenet_ai_0419_sdv4
val on: imagenet_ai_0508_adm
val on: imagenet_ai_0419_biggan
val on: imagenet_glide
val on: imagenet_midjourney
val on: imagenet_ai_0419_sdv4
val on: imagenet_ai_0424_sdv5
val on: imagenet_ai_0419_vqdm
val on: imagenet_ai_0424_wukong
USE GPU 0
# Start train
# Epoch 01
## 过程
2024-08-31 07:47:43.485223 Epoch [001/030], Step [0001/2668], Total_loss: 0.6219
2024-08-31 07:48:47.683268 Epoch [001/030], Step [0200/2668], Total_loss: 0.0767
2024-08-31 07:50:00.433378 Epoch [001/030], Step [0400/2668], Total_loss: 0.0489
2024-08-31 07:51:12.300389 Epoch [001/030], Step [0600/2668], Total_loss: 0.0149
2024-08-31 07:52:24.086269 Epoch [001/030], Step [0800/2668], Total_loss: 0.0444
2024-08-31 07:53:36.139408 Epoch [001/030], Step [1000/2668], Total_loss: 0.0332
2024-08-31 07:54:48.486089 Epoch [001/030], Step [1200/2668], Total_loss: 0.0245
2024-08-31 07:56:01.286208 Epoch [001/030], Step [1400/2668], Total_loss: 0.0317
2024-08-31 07:57:13.552496 Epoch [001/030], Step [1600/2668], Total_loss: 0.0034
2024-08-31 07:58:26.123407 Epoch [001/030], Step [1800/2668], Total_loss: 0.0012
2024-08-31 07:59:40.347218 Epoch [001/030], Step [2000/2668], Total_loss: 0.0862
2024-08-31 08:00:53.007721 Epoch [001/030], Step [2200/2668], Total_loss: 0.0318
2024-08-31 08:02:05.185606 Epoch [001/030], Step [2400/2668], Total_loss: 0.0076
2024-08-31 08:03:17.503771 Epoch [001/030], Step [2600/2668], Total_loss: 0.0219
2024-08-31 08:03:42.473330 Epoch [001/030], Step [2668/2668], Total_loss: 0.0366
## 结果
### adm
val on: imagenet_ai_0508_adm
ai accu: 0.7839999794960022
nature accu:0.971833348274231
val on:imagenet_ai_0508_adm, Epoch:1, Accuracy:0.8779166340827942
### biggan
val on: imagenet_ai_0419_biggan
ai accu: 0.6154999732971191
nature accu:0.9703333377838135
val on:imagenet_ai_0419_biggan, Epoch:1, Accuracy:0.7929166555404663
### glide
val on: imagenet_glide
ai accu: 0.8849999904632568
nature accu:0.972000002861023
val on:imagenet_glide, Epoch:1, Accuracy:0.9284999966621399
### midjourney
val on: imagenet_midjourney
ai accu: 0.5093333125114441
nature accu:0.9728333353996277
val on:imagenet_midjourney, Epoch:1, Accuracy:0.7410833239555359
### sdv4
val on: imagenet_ai_0419_sdv4
ai accu: 0.9614999890327454
nature accu:0.9693333506584167
val on:imagenet_ai_0419_sdv4, Epoch:1, Accuracy:0.965416669845581
### sdv5
val on: imagenet_ai_0424_sdv5
ai accu: 0.9631250500679016
nature accu:0.967875063419342
val on:imagenet_ai_0424_sdv5, Epoch:1, Accuracy:0.9655000567436218
### vqdm
val on: imagenet_ai_0419_vqdm
ai accu: 0.9208333492279053
nature accu:0.9710000157356262
val on:imagenet_ai_0419_vqdm, Epoch:1, Accuracy:0.9459166526794434
### wukong
val on: imagenet_ai_0424_wukong
ai accu: 0.9430000185966492
nature accu:0.9721666574478149
val on:imagenet_ai_0424_wukong, Epoch:1, Accuracy:0.9575833082199097
### mean
Save state_dict successfully! Best epoch:1.
Epoch:1,Accuracy:0.8995999693870544, bestEpoch:1, bestAccu:0.8995999693870544
# Epoch 02
2024-08-31 08:12:57.185953 Epoch [002/030], Step [0001/2668], Total_loss: 0.0159
2024-08-31 08:14:02.386122 Epoch [002/030], Step [0200/2668], Total_loss: 0.0298
2024-08-31 08:15:09.800478 Epoch [002/030], Step [0400/2668], Total_loss: 0.0179
2024-08-31 08:16:16.790382 Epoch [002/030], Step [0600/2668], Total_loss: 0.0025
2024-08-31 08:17:18.386012 Epoch [002/030], Step [0800/2668], Total_loss: 0.0026
2024-08-31 08:18:21.086085 Epoch [002/030], Step [1000/2668], Total_loss: 0.0015
2024-08-31 08:19:24.586278 Epoch [002/030], Step [1200/2668], Total_loss: 0.0066
2024-08-31 08:20:27.785876 Epoch [002/030], Step [1400/2668], Total_loss: 0.0074
2024-08-31 08:21:30.585950 Epoch [002/030], Step [1600/2668], Total_loss: 0.0014
2024-08-31 08:22:32.885967 Epoch [002/030], Step [1800/2668], Total_loss: 0.0041
2024-08-31 08:23:35.386046 Epoch [002/030], Step [2000/2668], Total_loss: 0.0032
2024-08-31 08:24:38.586047 Epoch [002/030], Step [2200/2668], Total_loss: 0.0351
2024-08-31 08:25:42.286022 Epoch [002/030], Step [2400/2668], Total_loss: 0.0047
2024-08-31 08:26:44.286237 Epoch [002/030], Step [2600/2668], Total_loss: 0.0141
2024-08-31 08:27:04.598567 Epoch [002/030], Step [2668/2668], Total_loss: 0.0004
## adm
val on: imagenet_ai_0508_adm
ai accu: 0.7095000147819519
nature accu:0.996833324432373
val on:imagenet_ai_0508_adm, Epoch:2, Accuracy:0.8531666398048401
## biggan
val on: imagenet_ai_0419_biggan
ai accu: 0.27033331990242004
nature accu:0.9959999918937683
val on:imagenet_ai_0419_biggan, Epoch:2, Accuracy:0.6331666707992554
## glide
val on: imagenet_glide
ai accu: 0.9383333325386047
nature accu:0.9963333010673523
val on:imagenet_glide, Epoch:2, Accuracy:0.9673333168029785
## midjourney
val on: imagenet_midjourney
ai accu: 0.6156666874885559
nature accu:0.996666669845581
val on:imagenet_midjourney, Epoch:2, Accuracy:0.8061666488647461
## sdv4
val on: imagenet_ai_0419_sdv4
ai accu: 0.9626666307449341
nature accu:0.9951666593551636
val on:imagenet_ai_0419_sdv4, Epoch:2, Accuracy:0.9789166450500488
## sdv5
val on: imagenet_ai_0424_sdv5
ai accu: 0.9598750472068787
nature accu:0.9943750500679016
val on:imagenet_ai_0424_sdv5, Epoch:2, Accuracy:0.9771250486373901
## vqdm
val on: imagenet_ai_0419_vqdm
ai accu: 0.8774999976158142
nature accu:0.9963333010673523
val on:imagenet_ai_0419_vqdm, Epoch:2, Accuracy:0.9369166493415833
## wukong
val on: imagenet_ai_0424_wukong
ai accu: 0.9426666498184204
nature accu:0.9958333373069763
val on:imagenet_ai_0424_wukong, Epoch:2, Accuracy:0.969249963760376
## mean
Epoch:2,Accuracy:0.8937299847602844, bestEpoch:1, bestAccu:0.8995999693870544
# Epoch 03-Epoch 28
## Epoch 03
2024-08-31 08:36:34.386178 Epoch [003/030], Step [0001/2668], Total_loss: 0.0083
2024-08-31 08:37:36.588232 Epoch [003/030], Step [0200/2668], Total_loss: 0.0474
2024-08-31 08:38:39.685845 Epoch [003/030], Step [0400/2668], Total_loss: 0.0007
2024-08-31 08:39:42.286852 Epoch [003/030], Step [0600/2668], Total_loss: 0.0124
2024-08-31 08:40:43.886012 Epoch [003/030], Step [0800/2668], Total_loss: 0.0942
2024-08-31 08:41:45.285895 Epoch [003/030], Step [1000/2668], Total_loss: 0.0008
2024-08-31 08:42:47.586213 Epoch [003/030], Step [1200/2668], Total_loss: 0.0015
2024-08-31 08:43:52.701416 Epoch [003/030], Step [1400/2668], Total_loss: 0.0031
2024-08-31 08:44:56.786018 Epoch [003/030], Step [1600/2668], Total_loss: 0.0001
2024-08-31 08:45:58.186031 Epoch [003/030], Step [1800/2668], Total_loss: 0.0025
2024-08-31 08:46:59.708399 Epoch [003/030], Step [2000/2668], Total_loss: 0.0310
2024-08-31 08:48:00.585918 Epoch [003/030], Step [2200/2668], Total_loss: 0.0019
2024-08-31 08:49:03.134159 Epoch [003/030], Step [2400/2668], Total_loss: 0.0246
2024-08-31 08:50:04.985923 Epoch [003/030], Step [2600/2668], Total_loss: 0.0013
2024-08-31 08:50:24.987137 Epoch [003/030], Step [2668/2668], Total_loss: 0.0001
val on: imagenet_ai_0508_adm
ai accu: 0.575166642665863
nature accu:0.9991666674613953
val on:imagenet_ai_0508_adm, Epoch:3, Accuracy:0.7871666550636292
val on: imagenet_ai_0419_biggan
ai accu: 0.25349998474121094
nature accu:0.9983333349227905
val on:imagenet_ai_0419_biggan, Epoch:3, Accuracy:0.6259166598320007
val on: imagenet_glide
ai accu: 0.9483333230018616
nature accu:0.9993333220481873
val on:imagenet_glide, Epoch:3, Accuracy:0.9738333225250244
val on: imagenet_midjourney
ai accu: 0.5478333234786987
nature accu:0.9983333349227905
val on:imagenet_midjourney, Epoch:3, Accuracy:0.7730833292007446
val on: imagenet_ai_0419_sdv4
ai accu: 0.9728333353996277
nature accu:0.9975000023841858
val on:imagenet_ai_0419_sdv4, Epoch:3, Accuracy:0.9851666688919067
val on: imagenet_ai_0424_sdv5
ai accu: 0.9741250276565552
nature accu:0.9983750581741333
val on:imagenet_ai_0424_sdv5, Epoch:3, Accuracy:0.9862500429153442
val on: imagenet_ai_0419_vqdm
ai accu: 0.8796666860580444
nature accu:0.9990000128746033
val on:imagenet_ai_0419_vqdm, Epoch:3, Accuracy:0.9393333196640015
val on: imagenet_ai_0424_wukong
ai accu: 0.934499979019165
nature accu:0.999833345413208
val on:imagenet_ai_0424_wukong, Epoch:3, Accuracy:0.9671666622161865
Epoch:3,Accuracy:0.8840000033378601, bestEpoch:1, bestAccu:0.8995999693870544
## Epoch 04
2024-08-31 08:59:41.685908 Epoch [004/030], Step [0001/2668], Total_loss: 0.0030
2024-08-31 09:00:44.885995 Epoch [004/030], Step [0200/2668], Total_loss: 0.0032
2024-08-31 09:01:46.486707 Epoch [004/030], Step [0400/2668], Total_loss: 0.0029
2024-08-31 09:02:47.385783 Epoch [004/030], Step [0600/2668], Total_loss: 0.0015
2024-08-31 09:03:49.785882 Epoch [004/030], Step [0800/2668], Total_loss: 0.0011
2024-08-31 09:04:51.486480 Epoch [004/030], Step [1000/2668], Total_loss: 0.0902
2024-08-31 09:05:53.685858 Epoch [004/030], Step [1200/2668], Total_loss: 0.0064
2024-08-31 09:06:55.185974 Epoch [004/030], Step [1400/2668], Total_loss: 0.0001
2024-08-31 09:07:57.285897 Epoch [004/030], Step [1600/2668], Total_loss: 0.0018
2024-08-31 09:08:58.586399 Epoch [004/030], Step [1800/2668], Total_loss: 0.0492
2024-08-31 09:10:01.086458 Epoch [004/030], Step [2000/2668], Total_loss: 0.0006
2024-08-31 09:11:03.885785 Epoch [004/030], Step [2200/2668], Total_loss: 0.0072
2024-08-31 09:12:05.785926 Epoch [004/030], Step [2400/2668], Total_loss: 0.0004
2024-08-31 09:13:07.585970 Epoch [004/030], Step [2600/2668], Total_loss: 0.0659
2024-08-31 09:13:28.696345 Epoch [004/030], Step [2668/2668], Total_loss: 0.0002
val on: imagenet_ai_0508_adm
ai accu: 0.6815000176429749
nature accu:0.9984999895095825
val on:imagenet_ai_0508_adm, Epoch:4, Accuracy:0.8399999737739563
val on: imagenet_ai_0419_biggan
ai accu: 0.2436666637659073
nature accu:0.9984999895095825
val on:imagenet_ai_0419_biggan, Epoch:4, Accuracy:0.6210833191871643
val on: imagenet_glide
ai accu: 0.918999969959259
nature accu:0.9979999661445618
val on:imagenet_glide, Epoch:4, Accuracy:0.9584999680519104
val on: imagenet_midjourney
ai accu: 0.5848333239555359
nature accu:0.9976666569709778
val on:imagenet_midjourney, Epoch:4, Accuracy:0.7912499904632568
val on: imagenet_ai_0419_sdv4
ai accu: 0.9708333015441895
nature accu:0.9976666569709778
val on:imagenet_ai_0419_sdv4, Epoch:4, Accuracy:0.984250009059906
val on: imagenet_ai_0424_sdv5
ai accu: 0.9670000672340393
nature accu:0.9980000257492065
val on:imagenet_ai_0424_sdv5, Epoch:4, Accuracy:0.9825000762939453
val on: imagenet_ai_0419_vqdm
ai accu: 0.8766666650772095
nature accu:0.9983333349227905
val on:imagenet_ai_0419_vqdm, Epoch:4, Accuracy:0.9375
val on: imagenet_ai_0424_wukong
ai accu: 0.953666627407074
nature accu:0.9984999895095825
val on:imagenet_ai_0424_wukong, Epoch:4, Accuracy:0.9760833382606506
Epoch:4,Accuracy:0.890239953994751, bestEpoch:1, bestAccu:0.8995999693870544
## Epoch 05
2024-08-31 09:22:39.786374 Epoch [005/030], Step [0001/2668], Total_loss: 0.0302
2024-08-31 09:23:40.508053 Epoch [005/030], Step [0200/2668], Total_loss: 0.0005
2024-08-31 09:24:42.485936 Epoch [005/030], Step [0400/2668], Total_loss: 0.0015
2024-08-31 09:25:44.385887 Epoch [005/030], Step [0600/2668], Total_loss: 0.0014
2024-08-31 09:26:46.386074 Epoch [005/030], Step [0800/2668], Total_loss: 0.0059
2024-08-31 09:27:48.886298 Epoch [005/030], Step [1000/2668], Total_loss: 0.0686
2024-08-31 09:28:50.786022 Epoch [005/030], Step [1200/2668], Total_loss: 0.0035
2024-08-31 09:29:53.694498 Epoch [005/030], Step [1400/2668], Total_loss: 0.0045
2024-08-31 09:30:55.285884 Epoch [005/030], Step [1600/2668], Total_loss: 0.0037
2024-08-31 09:31:57.485867 Epoch [005/030], Step [1800/2668], Total_loss: 0.0002
2024-08-31 09:33:00.649501 Epoch [005/030], Step [2000/2668], Total_loss: 0.0007
2024-08-31 09:34:04.086136 Epoch [005/030], Step [2200/2668], Total_loss: 0.0031
2024-08-31 09:35:07.885848 Epoch [005/030], Step [2400/2668], Total_loss: 0.0008
2024-08-31 09:36:13.686030 Epoch [005/030], Step [2600/2668], Total_loss: 0.0021
2024-08-31 09:36:35.286646 Epoch [005/030], Step [2668/2668], Total_loss: 0.0015
val on: imagenet_ai_0508_adm
ai accu: 0.6621666550636292
nature accu:0.9983333349227905
val on:imagenet_ai_0508_adm, Epoch:5, Accuracy:0.8302499651908875
val on: imagenet_ai_0419_biggan
ai accu: 0.20999999344348907
nature accu:0.9993333220481873
val on:imagenet_ai_0419_biggan, Epoch:5, Accuracy:0.6046666502952576
val on: imagenet_glide
ai accu: 0.9636666774749756
nature accu:0.9986666440963745
val on:imagenet_glide, Epoch:5, Accuracy:0.981166660785675
val on: imagenet_midjourney
ai accu: 0.5805000066757202
nature accu:0.9979999661445618
val on:imagenet_midjourney, Epoch:5, Accuracy:0.7892500162124634
val on: imagenet_ai_0419_sdv4
ai accu: 0.9674999713897705
nature accu:0.9978333115577698
val on:imagenet_ai_0419_sdv4, Epoch:5, Accuracy:0.9826666712760925
val on: imagenet_ai_0424_sdv5
ai accu: 0.9640000462532043
nature accu:0.999250054359436
val on:imagenet_ai_0424_sdv5, Epoch:5, Accuracy:0.9816250205039978
val on: imagenet_ai_0419_vqdm
ai accu: 0.8504999876022339
nature accu:0.9978333115577698
val on:imagenet_ai_0419_vqdm, Epoch:5, Accuracy:0.9241666793823242
val on: imagenet_ai_0424_wukong
ai accu: 0.9304999709129333
nature accu:0.9993333220481873
val on:imagenet_ai_0424_wukong, Epoch:5, Accuracy:0.9649166464805603
Epoch:5,Accuracy:0.8863099813461304, bestEpoch:1, bestAccu:0.8995999693870544
## Epoch 06
2024-08-31 09:45:55.886019 Epoch [006/030], Step [0001/2668], Total_loss: 0.0035
2024-08-31 09:46:57.986299 Epoch [006/030], Step [0200/2668], Total_loss: 0.0343
2024-08-31 09:47:59.585996 Epoch [006/030], Step [0400/2668], Total_loss: 0.0006
2024-08-31 09:49:02.686085 Epoch [006/030], Step [0600/2668], Total_loss: 0.0001
2024-08-31 09:50:05.286325 Epoch [006/030], Step [0800/2668], Total_loss: 0.0007
2024-08-31 09:51:17.187998 Epoch [006/030], Step [1000/2668], Total_loss: 0.0231
2024-08-31 09:52:21.886540 Epoch [006/030], Step [1200/2668], Total_loss: 0.0316
2024-08-31 09:53:27.085981 Epoch [006/030], Step [1400/2668], Total_loss: 0.0020
2024-08-31 09:54:33.586007 Epoch [006/030], Step [1600/2668], Total_loss: 0.0066
2024-08-31 09:55:39.086115 Epoch [006/030], Step [1800/2668], Total_loss: 0.0026
2024-08-31 09:56:46.592148 Epoch [006/030], Step [2000/2668], Total_loss: 0.0802
2024-08-31 09:57:52.211944 Epoch [006/030], Step [2200/2668], Total_loss: 0.0016
2024-08-31 09:58:58.431639 Epoch [006/030], Step [2400/2668], Total_loss: 0.0088
2024-08-31 09:59:59.985919 Epoch [006/030], Step [2600/2668], Total_loss: 0.0010
2024-08-31 10:00:20.257746 Epoch [006/030], Step [2668/2668], Total_loss: 0.0001
val on: imagenet_ai_0508_adm
ai accu: 0.546999990940094
nature accu:0.9991666674613953
val on:imagenet_ai_0508_adm, Epoch:6, Accuracy:0.7730833292007446
val on: imagenet_ai_0419_biggan
ai accu: 0.2004999965429306
nature accu:0.9993333220481873
val on:imagenet_ai_0419_biggan, Epoch:6, Accuracy:0.5999166369438171
val on: imagenet_glide
ai accu: 0.940666675567627
nature accu:0.9994999766349792
val on:imagenet_glide, Epoch:6, Accuracy:0.9700832962989807
val on: imagenet_midjourney
ai accu: 0.5356666445732117
nature accu:0.9990000128746033
val on:imagenet_midjourney, Epoch:6, Accuracy:0.7673333287239075
val on: imagenet_ai_0419_sdv4
ai accu: 0.9726666808128357
nature accu:0.9994999766349792
val on:imagenet_ai_0419_sdv4, Epoch:6, Accuracy:0.9860833287239075
val on: imagenet_ai_0424_sdv5
ai accu: 0.9695000648498535
nature accu:0.9986250400543213
val on:imagenet_ai_0424_sdv5, Epoch:6, Accuracy:0.9840625524520874
val on: imagenet_ai_0419_vqdm
ai accu: 0.8364999890327454
nature accu:0.9986666440963745
val on:imagenet_ai_0419_vqdm, Epoch:6, Accuracy:0.9175833463668823
val on: imagenet_ai_0424_wukong
ai accu: 0.9243333339691162
nature accu:0.9979999661445618
val on:imagenet_ai_0424_wukong, Epoch:6, Accuracy:0.9611666798591614
Epoch:6,Accuracy:0.8744799494743347, bestEpoch:1, bestAccu:0.8995999693870544
## Epoch 07
2024-08-31 10:10:02.885860 Epoch [007/030], Step [0001/2668], Total_loss: 0.0074
2024-08-31 10:11:09.586177 Epoch [007/030], Step [0200/2668], Total_loss: 0.0171
2024-08-31 10:12:23.785792 Epoch [007/030], Step [0400/2668], Total_loss: 0.0006
2024-08-31 10:13:45.685778 Epoch [007/030], Step [0600/2668], Total_loss: 0.0015
2024-08-31 10:14:50.086442 Epoch [007/030], Step [0800/2668], Total_loss: 0.0000
2024-08-31 10:16:00.986098 Epoch [007/030], Step [1000/2668], Total_loss: 0.0014
2024-08-31 10:17:04.585930 Epoch [007/030], Step [1200/2668], Total_loss: 0.0009
2024-08-31 10:18:07.885782 Epoch [007/030], Step [1400/2668], Total_loss: 0.0041
2024-08-31 10:19:12.986483 Epoch [007/030], Step [1600/2668], Total_loss: 0.0002
2024-08-31 10:20:17.885775 Epoch [007/030], Step [1800/2668], Total_loss: 0.0001
2024-08-31 10:21:19.586200 Epoch [007/030], Step [2000/2668], Total_loss: 0.0028
2024-08-31 10:22:22.585932 Epoch [007/030], Step [2200/2668], Total_loss: 0.0012
2024-08-31 10:23:23.087115 Epoch [007/030], Step [2400/2668], Total_loss: 0.0000
2024-08-31 10:24:26.186085 Epoch [007/030], Step [2600/2668], Total_loss: 0.0004
2024-08-31 10:24:46.494752 Epoch [007/030], Step [2668/2668], Total_loss: 0.0011
val on: imagenet_ai_0508_adm
ai accu: 0.6029999852180481
nature accu:0.9990000128746033
val on:imagenet_ai_0508_adm, Epoch:7, Accuracy:0.8009999990463257
val on: imagenet_ai_0419_biggan
ai accu: 0.23983332514762878
nature accu:0.9983333349227905
val on:imagenet_ai_0419_biggan, Epoch:7, Accuracy:0.6190833449363708
val on: imagenet_glide
ai accu: 0.9136666655540466
nature accu:0.9988332986831665
val on:imagenet_glide, Epoch:7, Accuracy:0.956250011920929
val on: imagenet_midjourney
ai accu: 0.5828333497047424
nature accu:0.9984999895095825
val on:imagenet_midjourney, Epoch:7, Accuracy:0.7906666398048401
val on: imagenet_ai_0419_sdv4
ai accu: 0.9789999723434448
nature accu:0.9981666803359985
val on:imagenet_ai_0419_sdv4, Epoch:7, Accuracy:0.9885833263397217
val on: imagenet_ai_0424_sdv5
ai accu: 0.9790000319480896
nature accu:0.999000072479248
val on:imagenet_ai_0424_sdv5, Epoch:7, Accuracy:0.9890000224113464
val on: imagenet_ai_0419_vqdm
ai accu: 0.8815000057220459
nature accu:0.9984999895095825
val on:imagenet_ai_0419_vqdm, Epoch:7, Accuracy:0.9399999976158142
val on: imagenet_ai_0424_wukong
ai accu: 0.9551666378974915
nature accu:0.9993333220481873
val on:imagenet_ai_0424_wukong, Epoch:7, Accuracy:0.9772499799728394
Epoch:7,Accuracy:0.8869799971580505, bestEpoch:1, bestAccu:0.8995999693870544
## Epoch 08
2024-08-31 10:34:11.185909 Epoch [008/030], Step [0001/2668], Total_loss: 0.0149
2024-08-31 10:35:38.386211 Epoch [008/030], Step [0200/2668], Total_loss: 0.0002
2024-08-31 10:36:42.186232 Epoch [008/030], Step [0400/2668], Total_loss: 0.0129
2024-08-31 10:37:45.185893 Epoch [008/030], Step [0600/2668], Total_loss: 0.0038
2024-08-31 10:38:47.486074 Epoch [008/030], Step [0800/2668], Total_loss: 0.0006
2024-08-31 10:39:48.885892 Epoch [008/030], Step [1000/2668], Total_loss: 0.0003
2024-08-31 10:40:49.886008 Epoch [008/030], Step [1200/2668], Total_loss: 0.0005
2024-08-31 10:41:51.485996 Epoch [008/030], Step [1400/2668], Total_loss: 0.0001
2024-08-31 10:42:52.986125 Epoch [008/030], Step [1600/2668], Total_loss: 0.0000
2024-08-31 10:43:54.686057 Epoch [008/030], Step [1800/2668], Total_loss: 0.0025
2024-08-31 10:44:56.886060 Epoch [008/030], Step [2000/2668], Total_loss: 0.0076
2024-08-31 10:45:57.886031 Epoch [008/030], Step [2200/2668], Total_loss: 0.0006
2024-08-31 10:46:59.685990 Epoch [008/030], Step [2400/2668], Total_loss: 0.0000
2024-08-31 10:48:01.933457 Epoch [008/030], Step [2600/2668], Total_loss: 0.0081
2024-08-31 10:48:22.281027 Epoch [008/030], Step [2668/2668], Total_loss: 0.0010
val on: imagenet_ai_0508_adm
ai accu: 0.5083333253860474
nature accu:0.9994999766349792
val on:imagenet_ai_0508_adm, Epoch:8, Accuracy:0.7539166808128357
val on: imagenet_ai_0419_biggan
ai accu: 0.1601666659116745
nature accu:0.9991666674613953
val on:imagenet_ai_0419_biggan, Epoch:8, Accuracy:0.5796666741371155
val on: imagenet_glide
ai accu: 0.8993332982063293
nature accu:0.9996666312217712
val on:imagenet_glide, Epoch:8, Accuracy:0.9494999647140503
val on: imagenet_midjourney
ai accu: 0.4794999957084656
nature accu:0.9986666440963745
val on:imagenet_midjourney, Epoch:8, Accuracy:0.7390833497047424
val on: imagenet_ai_0419_sdv4
ai accu: 0.9603333473205566
nature accu:0.9994999766349792
val on:imagenet_ai_0419_sdv4, Epoch:8, Accuracy:0.9799166321754456
val on: imagenet_ai_0424_sdv5
ai accu: 0.9600000381469727
nature accu:0.9988750219345093
val on:imagenet_ai_0424_sdv5, Epoch:8, Accuracy:0.979437530040741
val on: imagenet_ai_0419_vqdm
ai accu: 0.7339999675750732
nature accu:0.9993333220481873
val on:imagenet_ai_0419_vqdm, Epoch:8, Accuracy:0.8666666746139526
val on: imagenet_ai_0424_wukong
ai accu: 0.9226666688919067
nature accu:0.9993333220481873
val on:imagenet_ai_0424_wukong, Epoch:8, Accuracy:0.9609999656677246
Epoch:8,Accuracy:0.8562799692153931, bestEpoch:1, bestAccu:0.8995999693870544
## Epoch 09
2024-08-31 10:57:28.186078 Epoch [009/030], Step [0001/2668], Total_loss: 0.0236
2024-08-31 10:58:28.885813 Epoch [009/030], Step [0200/2668], Total_loss: 0.0372
2024-08-31 10:59:30.386264 Epoch [009/030], Step [0400/2668], Total_loss: 0.0025
2024-08-31 11:00:31.886109 Epoch [009/030], Step [0600/2668], Total_loss: 0.0015
2024-08-31 11:01:32.885847 Epoch [009/030], Step [0800/2668], Total_loss: 0.0012
2024-08-31 11:02:33.986156 Epoch [009/030], Step [1000/2668], Total_loss: 0.0222
2024-08-31 11:03:35.585863 Epoch [009/030], Step [1200/2668], Total_loss: 0.0010
2024-08-31 11:04:36.585803 Epoch [009/030], Step [1400/2668], Total_loss: 0.0119
2024-08-31 11:05:38.086071 Epoch [009/030], Step [1600/2668], Total_loss: 0.0001
2024-08-31 11:06:39.686106 Epoch [009/030], Step [1800/2668], Total_loss: 0.0030
2024-08-31 11:07:40.585861 Epoch [009/030], Step [2000/2668], Total_loss: 0.0002
2024-08-31 11:08:41.486105 Epoch [009/030], Step [2200/2668], Total_loss: 0.0024
2024-08-31 11:09:42.585942 Epoch [009/030], Step [2400/2668], Total_loss: 0.0115
2024-08-31 11:10:43.385889 Epoch [009/030], Step [2600/2668], Total_loss: 0.0007
2024-08-31 11:11:03.693609 Epoch [009/030], Step [2668/2668], Total_loss: 0.0012
val on: imagenet_ai_0508_adm
ai accu: 0.8246666789054871
nature accu:0.9889999628067017
val on:imagenet_ai_0508_adm, Epoch:9, Accuracy:0.9068333506584167
val on: imagenet_ai_0419_biggan
ai accu: 0.4621666669845581
nature accu:0.9864999651908875
val on:imagenet_ai_0419_biggan, Epoch:9, Accuracy:0.7243333458900452
val on: imagenet_glide
ai accu: 0.9564999938011169
nature accu:0.9908333420753479
val on:imagenet_glide, Epoch:9, Accuracy:0.9736666679382324
val on: imagenet_midjourney
ai accu: 0.668666660785675
nature accu:0.9883333444595337
val on:imagenet_midjourney, Epoch:9, Accuracy:0.828499972820282
val on: imagenet_ai_0419_sdv4
ai accu: 0.9911666512489319
nature accu:0.9906666278839111
val on:imagenet_ai_0419_sdv4, Epoch:9, Accuracy:0.9909166693687439
val on: imagenet_ai_0424_sdv5
ai accu: 0.9898750185966492
nature accu:0.9848750233650208
val on:imagenet_ai_0424_sdv5, Epoch:9, Accuracy:0.987375020980835
val on: imagenet_ai_0419_vqdm
ai accu: 0.953666627407074
nature accu:0.9889999628067017
val on:imagenet_ai_0419_vqdm, Epoch:9, Accuracy:0.9713333249092102
val on: imagenet_ai_0424_wukong
ai accu: 0.9804999828338623
nature accu:0.9869999885559082
val on:imagenet_ai_0424_wukong, Epoch:9, Accuracy:0.9837499856948853
Save state_dict successfully! Best epoch:9.
Epoch:9,Accuracy:0.9235000014305115, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 10
2024-08-31 11:20:11.286424 Epoch [010/030], Step [0001/2668], Total_loss: 0.0065
2024-08-31 11:21:12.133484 Epoch [010/030], Step [0200/2668], Total_loss: 0.0016
2024-08-31 11:22:14.086006 Epoch [010/030], Step [0400/2668], Total_loss: 0.0011
2024-08-31 11:23:15.285924 Epoch [010/030], Step [0600/2668], Total_loss: 0.0059
2024-08-31 11:24:16.586344 Epoch [010/030], Step [0800/2668], Total_loss: 0.0011
2024-08-31 11:25:17.685908 Epoch [010/030], Step [1000/2668], Total_loss: 0.0167
2024-08-31 11:26:19.286053 Epoch [010/030], Step [1200/2668], Total_loss: 0.0052
2024-08-31 11:27:20.785836 Epoch [010/030], Step [1400/2668], Total_loss: 0.0002
2024-08-31 11:28:21.686194 Epoch [010/030], Step [1600/2668], Total_loss: 0.0013
2024-08-31 11:29:22.685918 Epoch [010/030], Step [1800/2668], Total_loss: 0.0044
2024-08-31 11:30:24.886072 Epoch [010/030], Step [2000/2668], Total_loss: 0.0006
2024-08-31 11:31:25.786058 Epoch [010/030], Step [2200/2668], Total_loss: 0.0036
2024-08-31 11:32:27.086005 Epoch [010/030], Step [2400/2668], Total_loss: 0.0025
2024-08-31 11:33:27.986085 Epoch [010/030], Step [2600/2668], Total_loss: 0.0144
2024-08-31 11:33:48.046182 Epoch [010/030], Step [2668/2668], Total_loss: 0.0026
val on: imagenet_ai_0508_adm
ai accu: 0.6793333292007446
nature accu:0.997166633605957
val on:imagenet_ai_0508_adm, Epoch:10, Accuracy:0.8382499814033508
val on: imagenet_ai_0419_biggan
ai accu: 0.2098333239555359
nature accu:0.9978333115577698
val on:imagenet_ai_0419_biggan, Epoch:10, Accuracy:0.6038333177566528
val on: imagenet_glide
ai accu: 0.9599999785423279
nature accu:0.9981666803359985
val on:imagenet_glide, Epoch:10, Accuracy:0.9790832996368408
val on: imagenet_midjourney
ai accu: 0.6398333311080933
nature accu:0.996999979019165
val on:imagenet_midjourney, Epoch:10, Accuracy:0.8184166550636292
val on: imagenet_ai_0419_sdv4
ai accu: 0.984499990940094
nature accu:0.996833324432373
val on:imagenet_ai_0419_sdv4, Epoch:10, Accuracy:0.9906666278839111
val on: imagenet_ai_0424_sdv5
ai accu: 0.9805000424385071
nature accu:0.9975000619888306
val on:imagenet_ai_0424_sdv5, Epoch:10, Accuracy:0.9890000224113464
val on: imagenet_ai_0419_vqdm
ai accu: 0.8898333311080933
nature accu:0.996999979019165
val on:imagenet_ai_0419_vqdm, Epoch:10, Accuracy:0.9434166550636292
val on: imagenet_ai_0424_wukong
ai accu: 0.9628333449363708
nature accu:0.996833324432373
val on:imagenet_ai_0424_wukong, Epoch:10, Accuracy:0.9798333048820496
Epoch:10,Accuracy:0.8966599702835083, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 11
2024-08-31 11:42:57.286191 Epoch [011/030], Step [0001/2668], Total_loss: 0.0021
2024-08-31 11:43:57.985847 Epoch [011/030], Step [0200/2668], Total_loss: 0.0004
2024-08-31 11:44:59.686068 Epoch [011/030], Step [0400/2668], Total_loss: 0.0002
2024-08-31 11:46:00.886039 Epoch [011/030], Step [0600/2668], Total_loss: 0.0002
2024-08-31 11:47:02.785939 Epoch [011/030], Step [0800/2668], Total_loss: 0.0007
2024-08-31 11:48:04.785839 Epoch [011/030], Step [1000/2668], Total_loss: 0.0010
2024-08-31 11:49:05.985898 Epoch [011/030], Step [1200/2668], Total_loss: 0.0090
2024-08-31 11:50:08.286453 Epoch [011/030], Step [1400/2668], Total_loss: 0.0002
2024-08-31 11:51:10.485820 Epoch [011/030], Step [1600/2668], Total_loss: 0.0533
2024-08-31 11:52:12.985925 Epoch [011/030], Step [1800/2668], Total_loss: 0.0196
2024-08-31 11:53:15.032625 Epoch [011/030], Step [2000/2668], Total_loss: 0.0137
2024-08-31 11:54:15.687306 Epoch [011/030], Step [2200/2668], Total_loss: 0.0449
2024-08-31 11:55:16.933514 Epoch [011/030], Step [2400/2668], Total_loss: 0.0067
2024-08-31 11:56:17.985779 Epoch [011/030], Step [2600/2668], Total_loss: 0.0004
2024-08-31 11:56:37.964035 Epoch [011/030], Step [2668/2668], Total_loss: 0.0003
val on: imagenet_ai_0508_adm
ai accu: 0.49283331632614136
nature accu:0.9996666312217712
val on:imagenet_ai_0508_adm, Epoch:11, Accuracy:0.7462499737739563
val on: imagenet_ai_0419_biggan
ai accu: 0.1588333249092102
nature accu:0.9996666312217712
val on:imagenet_ai_0419_biggan, Epoch:11, Accuracy:0.5792499780654907
val on: imagenet_glide
ai accu: 0.922333300113678
nature accu:0.9996666312217712
val on:imagenet_glide, Epoch:11, Accuracy:0.9609999656677246
val on: imagenet_midjourney
ai accu: 0.5456666350364685
nature accu:0.9993333220481873
val on:imagenet_midjourney, Epoch:11, Accuracy:0.7724999785423279
val on: imagenet_ai_0419_sdv4
ai accu: 0.9751666784286499
nature accu:1.0
val on:imagenet_ai_0419_sdv4, Epoch:11, Accuracy:0.987583339214325
val on: imagenet_ai_0424_sdv5
ai accu: 0.971750020980835
nature accu:0.9998750686645508
val on:imagenet_ai_0424_sdv5, Epoch:11, Accuracy:0.9858125448226929
val on: imagenet_ai_0419_vqdm
ai accu: 0.734666645526886
nature accu:0.9994999766349792
val on:imagenet_ai_0419_vqdm, Epoch:11, Accuracy:0.8670833110809326
val on: imagenet_ai_0424_wukong
ai accu: 0.9331666827201843
nature accu:0.9994999766349792
val on:imagenet_ai_0424_wukong, Epoch:11, Accuracy:0.9663333296775818
Epoch:11,Accuracy:0.8633300065994263, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 12
2024-08-31 12:05:43.519822 Epoch [012/030], Step [0001/2668], Total_loss: 0.0012
2024-08-31 12:06:44.486002 Epoch [012/030], Step [0200/2668], Total_loss: 0.0001
2024-08-31 12:07:46.185818 Epoch [012/030], Step [0400/2668], Total_loss: 0.0001
2024-08-31 12:08:47.386023 Epoch [012/030], Step [0600/2668], Total_loss: 0.0004
2024-08-31 12:09:48.285874 Epoch [012/030], Step [0800/2668], Total_loss: 0.0005
2024-08-31 12:10:49.585796 Epoch [012/030], Step [1000/2668], Total_loss: 0.0003
2024-08-31 12:11:51.085909 Epoch [012/030], Step [1200/2668], Total_loss: 0.0003
2024-08-31 12:12:52.286026 Epoch [012/030], Step [1400/2668], Total_loss: 0.0580
2024-08-31 12:13:53.586018 Epoch [012/030], Step [1600/2668], Total_loss: 0.0002
2024-08-31 12:14:54.685905 Epoch [012/030], Step [1800/2668], Total_loss: 0.0031
2024-08-31 12:15:58.908112 Epoch [012/030], Step [2000/2668], Total_loss: 0.0020
2024-08-31 12:17:01.785936 Epoch [012/030], Step [2200/2668], Total_loss: 0.0017
2024-08-31 12:18:03.485892 Epoch [012/030], Step [2400/2668], Total_loss: 0.0068
2024-08-31 12:19:04.785947 Epoch [012/030], Step [2600/2668], Total_loss: 0.0001
2024-08-31 12:19:24.777323 Epoch [012/030], Step [2668/2668], Total_loss: 0.0000
val on: imagenet_ai_0508_adm
ai accu: 0.6071666479110718
nature accu:0.9996666312217712
val on:imagenet_ai_0508_adm, Epoch:12, Accuracy:0.8034166693687439
val on: imagenet_ai_0419_biggan
ai accu: 0.25316667556762695
nature accu:0.9996666312217712
val on:imagenet_ai_0419_biggan, Epoch:12, Accuracy:0.6264166831970215
val on: imagenet_glide
ai accu: 0.9493333101272583
nature accu:0.999833345413208
val on:imagenet_glide, Epoch:12, Accuracy:0.9745833277702332
val on: imagenet_midjourney
ai accu: 0.597000002861023
nature accu:0.9993333220481873
val on:imagenet_midjourney, Epoch:12, Accuracy:0.7981666326522827
val on: imagenet_ai_0419_sdv4
ai accu: 0.9810000061988831
nature accu:0.9994999766349792
val on:imagenet_ai_0419_sdv4, Epoch:12, Accuracy:0.9902499914169312
val on: imagenet_ai_0424_sdv5
ai accu: 0.9777500629425049
nature accu:0.9987500309944153
val on:imagenet_ai_0424_sdv5, Epoch:12, Accuracy:0.9882500171661377
val on: imagenet_ai_0419_vqdm
ai accu: 0.8641666769981384
nature accu:0.9996666312217712
val on:imagenet_ai_0419_vqdm, Epoch:12, Accuracy:0.9319166541099548
val on: imagenet_ai_0424_wukong
ai accu: 0.940833330154419
nature accu:0.9996666312217712
val on:imagenet_ai_0424_wukong, Epoch:12, Accuracy:0.9702500104904175
Epoch:12,Accuracy:0.889519989490509, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 13
2024-08-31 12:28:41.385907 Epoch [013/030], Step [0001/2668], Total_loss: 0.0017
2024-08-31 12:29:42.086026 Epoch [013/030], Step [0200/2668], Total_loss: 0.0022
2024-08-31 12:30:43.885943 Epoch [013/030], Step [0400/2668], Total_loss: 0.0039
2024-08-31 12:31:44.986080 Epoch [013/030], Step [0600/2668], Total_loss: 0.0001
2024-08-31 12:32:47.686092 Epoch [013/030], Step [0800/2668], Total_loss: 0.0004
2024-08-31 12:33:49.186027 Epoch [013/030], Step [1000/2668], Total_loss: 0.0000
2024-08-31 12:34:52.232327 Epoch [013/030], Step [1200/2668], Total_loss: 0.0024
2024-08-31 12:35:53.986664 Epoch [013/030], Step [1400/2668], Total_loss: 0.0012
2024-08-31 12:36:54.785844 Epoch [013/030], Step [1600/2668], Total_loss: 0.0003
2024-08-31 12:37:56.433344 Epoch [013/030], Step [1800/2668], Total_loss: 0.0014
2024-08-31 12:38:57.232901 Epoch [013/030], Step [2000/2668], Total_loss: 0.0002
2024-08-31 12:40:00.234033 Epoch [013/030], Step [2200/2668], Total_loss: 0.0011
2024-08-31 12:41:04.985937 Epoch [013/030], Step [2400/2668], Total_loss: 0.0012
2024-08-31 12:42:05.886042 Epoch [013/030], Step [2600/2668], Total_loss: 0.0048
2024-08-31 12:42:25.919817 Epoch [013/030], Step [2668/2668], Total_loss: 0.0000
val on: imagenet_ai_0508_adm
ai accu: 0.5619999766349792
nature accu:0.9976666569709778
val on:imagenet_ai_0508_adm, Epoch:13, Accuracy:0.7798333168029785
val on: imagenet_ai_0419_biggan
ai accu: 0.2241666615009308
nature accu:0.9981666803359985
val on:imagenet_ai_0419_biggan, Epoch:13, Accuracy:0.6111666560173035
val on: imagenet_glide
ai accu: 0.9443333148956299
nature accu:0.9978333115577698
val on:imagenet_glide, Epoch:13, Accuracy:0.9710833430290222
val on: imagenet_midjourney
ai accu: 0.5730000138282776
nature accu:0.9963333010673523
val on:imagenet_midjourney, Epoch:13, Accuracy:0.7846666574478149
val on: imagenet_ai_0419_sdv4
ai accu: 0.987500011920929
nature accu:0.9979999661445618
val on:imagenet_ai_0419_sdv4, Epoch:13, Accuracy:0.9927499890327454
val on: imagenet_ai_0424_sdv5
ai accu: 0.9846250414848328
nature accu:0.9972500205039978
val on:imagenet_ai_0424_sdv5, Epoch:13, Accuracy:0.9909375309944153
val on: imagenet_ai_0419_vqdm
ai accu: 0.9091666340827942
nature accu:0.9978333115577698
val on:imagenet_ai_0419_vqdm, Epoch:13, Accuracy:0.953499972820282
val on: imagenet_ai_0424_wukong
ai accu: 0.9670000076293945
nature accu:0.9978333115577698
val on:imagenet_ai_0424_wukong, Epoch:13, Accuracy:0.9824166297912598
Epoch:13,Accuracy:0.8876000046730042, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 14
2024-08-31 12:51:30.695021 Epoch [014/030], Step [0001/2668], Total_loss: 0.0007
2024-08-31 12:52:32.185834 Epoch [014/030], Step [0200/2668], Total_loss: 0.0016
2024-08-31 12:53:33.185833 Epoch [014/030], Step [0400/2668], Total_loss: 0.0011
2024-08-31 12:54:35.286050 Epoch [014/030], Step [0600/2668], Total_loss: 0.0021
2024-08-31 12:55:35.905181 Epoch [014/030], Step [0800/2668], Total_loss: 0.0064
2024-08-31 12:56:37.885968 Epoch [014/030], Step [1000/2668], Total_loss: 0.0010
2024-08-31 12:57:39.186294 Epoch [014/030], Step [1200/2668], Total_loss: 0.0004
2024-08-31 12:58:40.585953 Epoch [014/030], Step [1400/2668], Total_loss: 0.0005
2024-08-31 12:59:42.133561 Epoch [014/030], Step [1600/2668], Total_loss: 0.0342
2024-08-31 13:00:43.585823 Epoch [014/030], Step [1800/2668], Total_loss: 0.0000
2024-08-31 13:01:44.986012 Epoch [014/030], Step [2000/2668], Total_loss: 0.0002
2024-08-31 13:02:47.185991 Epoch [014/030], Step [2200/2668], Total_loss: 0.0005
2024-08-31 13:03:47.886091 Epoch [014/030], Step [2400/2668], Total_loss: 0.0318
2024-08-31 13:04:48.986168 Epoch [014/030], Step [2600/2668], Total_loss: 0.0015
2024-08-31 13:05:09.172961 Epoch [014/030], Step [2668/2668], Total_loss: 0.0071
val on: imagenet_ai_0508_adm
ai accu: 0.609833300113678
nature accu:0.9983333349227905
val on:imagenet_ai_0508_adm, Epoch:14, Accuracy:0.8040833473205566
val on: imagenet_ai_0419_biggan
ai accu: 0.33416667580604553
nature accu:0.9975000023841858
val on:imagenet_ai_0419_biggan, Epoch:14, Accuracy:0.6658333539962769
val on: imagenet_glide
ai accu: 0.9326666593551636
nature accu:0.996999979019165
val on:imagenet_glide, Epoch:14, Accuracy:0.9648333191871643
val on: imagenet_midjourney
ai accu: 0.4925000071525574
nature accu:0.9976666569709778
val on:imagenet_midjourney, Epoch:14, Accuracy:0.7450833320617676
val on: imagenet_ai_0419_sdv4
ai accu: 0.9810000061988831
nature accu:0.9979999661445618
val on:imagenet_ai_0419_sdv4, Epoch:14, Accuracy:0.9894999861717224
val on: imagenet_ai_0424_sdv5
ai accu: 0.9808750748634338
nature accu:0.9973750710487366
val on:imagenet_ai_0424_sdv5, Epoch:14, Accuracy:0.9891250729560852
val on: imagenet_ai_0419_vqdm
ai accu: 0.9021666646003723
nature accu:0.9973333477973938
val on:imagenet_ai_0419_vqdm, Epoch:14, Accuracy:0.9497500061988831
val on: imagenet_ai_0424_wukong
ai accu: 0.9568333029747009
nature accu:0.997166633605957
val on:imagenet_ai_0424_wukong, Epoch:14, Accuracy:0.9769999980926514
Epoch:14,Accuracy:0.8897899985313416, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 15
2024-08-31 13:14:12.486181 Epoch [015/030], Step [0001/2668], Total_loss: 0.0002
2024-08-31 13:15:12.885911 Epoch [015/030], Step [0200/2668], Total_loss: 0.0126
2024-08-31 13:16:13.486327 Epoch [015/030], Step [0400/2668], Total_loss: 0.0006
2024-08-31 13:17:15.186070 Epoch [015/030], Step [0600/2668], Total_loss: 0.0001
2024-08-31 13:18:15.985795 Epoch [015/030], Step [0800/2668], Total_loss: 0.0006
2024-08-31 13:19:16.685872 Epoch [015/030], Step [1000/2668], Total_loss: 0.0003
2024-08-31 13:20:17.685931 Epoch [015/030], Step [1200/2668], Total_loss: 0.0003
2024-08-31 13:21:18.585907 Epoch [015/030], Step [1400/2668], Total_loss: 0.0027
2024-08-31 13:22:19.385790 Epoch [015/030], Step [1600/2668], Total_loss: 0.0008
2024-08-31 13:23:20.386050 Epoch [015/030], Step [1800/2668], Total_loss: 0.0002
2024-08-31 13:24:21.586465 Epoch [015/030], Step [2000/2668], Total_loss: 0.0026
2024-08-31 13:25:22.985822 Epoch [015/030], Step [2200/2668], Total_loss: 0.0005
2024-08-31 13:26:23.485875 Epoch [015/030], Step [2400/2668], Total_loss: 0.0004
2024-08-31 13:27:25.186021 Epoch [015/030], Step [2600/2668], Total_loss: 0.0422
2024-08-31 13:27:45.171747 Epoch [015/030], Step [2668/2668], Total_loss: 0.0028
val on: imagenet_ai_0508_adm
ai accu: 0.5883333086967468
nature accu:0.9994999766349792
val on:imagenet_ai_0508_adm, Epoch:15, Accuracy:0.793916642665863
val on: imagenet_ai_0419_biggan
ai accu: 0.23633332550525665
nature accu:0.9993333220481873
val on:imagenet_ai_0419_biggan, Epoch:15, Accuracy:0.6178333163261414
val on: imagenet_glide
ai accu: 0.9455000162124634
nature accu:0.9991666674613953
val on:imagenet_glide, Epoch:15, Accuracy:0.9723333120346069
val on: imagenet_midjourney
ai accu: 0.5776666402816772
nature accu:0.9994999766349792
val on:imagenet_midjourney, Epoch:15, Accuracy:0.7885833382606506
val on: imagenet_ai_0419_sdv4
ai accu: 0.987500011920929
nature accu:0.9991666674613953
val on:imagenet_ai_0419_sdv4, Epoch:15, Accuracy:0.9933333396911621
val on: imagenet_ai_0424_sdv5
ai accu: 0.9858750700950623
nature accu:0.99937504529953
val on:imagenet_ai_0424_sdv5, Epoch:15, Accuracy:0.9926250576972961
val on: imagenet_ai_0419_vqdm
ai accu: 0.8569999933242798
nature accu:0.999833345413208
val on:imagenet_ai_0419_vqdm, Epoch:15, Accuracy:0.9284166693687439
val on: imagenet_ai_0424_wukong
ai accu: 0.965833306312561
nature accu:0.9996666312217712
val on:imagenet_ai_0424_wukong, Epoch:15, Accuracy:0.9827499985694885
Epoch:15,Accuracy:0.8880800008773804, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 16
2024-08-31 13:36:47.686355 Epoch [016/030], Step [0001/2668], Total_loss: 0.1042
2024-08-31 13:37:48.685847 Epoch [016/030], Step [0200/2668], Total_loss: 0.0012
2024-08-31 13:38:50.286023 Epoch [016/030], Step [0400/2668], Total_loss: 0.0006
2024-08-31 13:39:51.185809 Epoch [016/030], Step [0600/2668], Total_loss: 0.0003
2024-08-31 13:40:52.386039 Epoch [016/030], Step [0800/2668], Total_loss: 0.0351
2024-08-31 13:41:53.385955 Epoch [016/030], Step [1000/2668], Total_loss: 0.0000
2024-08-31 13:42:54.686370 Epoch [016/030], Step [1200/2668], Total_loss: 0.0011
2024-08-31 13:43:55.485906 Epoch [016/030], Step [1400/2668], Total_loss: 0.0003
2024-08-31 13:44:56.407655 Epoch [016/030], Step [1600/2668], Total_loss: 0.0002
2024-08-31 13:45:56.886048 Epoch [016/030], Step [1800/2668], Total_loss: 0.0006
2024-08-31 13:46:58.585931 Epoch [016/030], Step [2000/2668], Total_loss: 0.0001
2024-08-31 13:47:59.185983 Epoch [016/030], Step [2200/2668], Total_loss: 0.0003
2024-08-31 13:48:59.585820 Epoch [016/030], Step [2400/2668], Total_loss: 0.0003
2024-08-31 13:50:00.285894 Epoch [016/030], Step [2600/2668], Total_loss: 0.0004
2024-08-31 13:50:20.142931 Epoch [016/030], Step [2668/2668], Total_loss: 0.0002
val on: imagenet_ai_0508_adm
ai accu: 0.48249998688697815
nature accu:0.9986666440963745
val on:imagenet_ai_0508_adm, Epoch:16, Accuracy:0.7405833005905151
val on: imagenet_ai_0419_biggan
ai accu: 0.23116666078567505
nature accu:0.9990000128746033
val on:imagenet_ai_0419_biggan, Epoch:16, Accuracy:0.6150833368301392
val on: imagenet_glide
ai accu: 0.918666660785675
nature accu:0.9993333220481873
val on:imagenet_glide, Epoch:16, Accuracy:0.9589999914169312
val on: imagenet_midjourney
ai accu: 0.48499998450279236
nature accu:0.9988332986831665
val on:imagenet_midjourney, Epoch:16, Accuracy:0.7419166564941406
val on: imagenet_ai_0419_sdv4
ai accu: 0.984499990940094
nature accu:0.9986666440963745
val on:imagenet_ai_0419_sdv4, Epoch:16, Accuracy:0.9915833473205566
val on: imagenet_ai_0424_sdv5
ai accu: 0.9788750410079956
nature accu:0.9986250400543213
val on:imagenet_ai_0424_sdv5, Epoch:16, Accuracy:0.9887500405311584
val on: imagenet_ai_0419_vqdm
ai accu: 0.85916668176651
nature accu:0.9994999766349792
val on:imagenet_ai_0419_vqdm, Epoch:16, Accuracy:0.9293333292007446
val on: imagenet_ai_0424_wukong
ai accu: 0.9584999680519104
nature accu:0.9990000128746033
val on:imagenet_ai_0424_wukong, Epoch:16, Accuracy:0.9787499904632568
Epoch:16,Accuracy:0.8729499578475952, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 17
2024-08-31 13:59:22.308044 Epoch [017/030], Step [0001/2668], Total_loss: 0.0000
2024-08-31 14:00:23.485901 Epoch [017/030], Step [0200/2668], Total_loss: 0.0048
2024-08-31 14:01:24.685808 Epoch [017/030], Step [0400/2668], Total_loss: 0.0014
2024-08-31 14:02:25.385957 Epoch [017/030], Step [0600/2668], Total_loss: 0.0003
2024-08-31 14:03:26.186018 Epoch [017/030], Step [0800/2668], Total_loss: 0.0001
2024-08-31 14:04:27.786394 Epoch [017/030], Step [1000/2668], Total_loss: 0.0001
2024-08-31 14:05:28.485805 Epoch [017/030], Step [1200/2668], Total_loss: 0.0001
2024-08-31 14:06:30.986812 Epoch [017/030], Step [1400/2668], Total_loss: 0.0003
2024-08-31 14:07:36.386003 Epoch [017/030], Step [1600/2668], Total_loss: 0.0005
2024-08-31 14:08:42.185756 Epoch [017/030], Step [1800/2668], Total_loss: 0.0004
2024-08-31 14:09:44.786051 Epoch [017/030], Step [2000/2668], Total_loss: 0.0016
2024-08-31 14:10:46.785946 Epoch [017/030], Step [2200/2668], Total_loss: 0.0001
2024-08-31 14:11:49.885871 Epoch [017/030], Step [2400/2668], Total_loss: 0.0019
2024-08-31 14:12:51.686114 Epoch [017/030], Step [2600/2668], Total_loss: 0.0005
2024-08-31 14:13:12.432154 Epoch [017/030], Step [2668/2668], Total_loss: 0.0008
val on: imagenet_ai_0508_adm
ai accu: 0.5758333206176758
nature accu:0.9991666674613953
val on:imagenet_ai_0508_adm, Epoch:17, Accuracy:0.7874999642372131
val on: imagenet_ai_0419_biggan
ai accu: 0.19033333659172058
nature accu:0.9994999766349792
val on:imagenet_ai_0419_biggan, Epoch:17, Accuracy:0.5949166417121887
val on: imagenet_glide
ai accu: 0.9016666412353516
nature accu:1.0
val on:imagenet_glide, Epoch:17, Accuracy:0.9508333206176758
val on: imagenet_midjourney
ai accu: 0.5831666588783264
nature accu:0.9994999766349792
val on:imagenet_midjourney, Epoch:17, Accuracy:0.7913333177566528
val on: imagenet_ai_0419_sdv4
ai accu: 0.9866666793823242
nature accu:0.9994999766349792
val on:imagenet_ai_0419_sdv4, Epoch:17, Accuracy:0.9930832982063293
val on: imagenet_ai_0424_sdv5
ai accu: 0.9851250648498535
nature accu:0.999625027179718
val on:imagenet_ai_0424_sdv5, Epoch:17, Accuracy:0.9923750758171082
val on: imagenet_ai_0419_vqdm
ai accu: 0.8709999918937683
nature accu:0.9994999766349792
val on:imagenet_ai_0419_vqdm, Epoch:17, Accuracy:0.9352499842643738
val on: imagenet_ai_0424_wukong
ai accu: 0.9621666669845581
nature accu:0.999833345413208
val on:imagenet_ai_0424_wukong, Epoch:17, Accuracy:0.9810000061988831
Epoch:17,Accuracy:0.8828499913215637, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 18
2024-08-31 14:26:39.631887 Epoch [018/030], Step [0001/2668], Total_loss: 0.0002
2024-08-31 14:28:19.010942 Epoch [018/030], Step [0200/2668], Total_loss: 0.0000
2024-08-31 14:29:54.531907 Epoch [018/030], Step [0400/2668], Total_loss: 0.0048
2024-08-31 14:31:34.786551 Epoch [018/030], Step [0600/2668], Total_loss: 0.0018
2024-08-31 14:33:00.123211 Epoch [018/030], Step [0800/2668], Total_loss: 0.0010
2024-08-31 14:34:18.049384 Epoch [018/030], Step [1000/2668], Total_loss: 0.0022
2024-08-31 14:35:39.130274 Epoch [018/030], Step [1200/2668], Total_loss: 0.0172
2024-08-31 14:36:56.534220 Epoch [018/030], Step [1400/2668], Total_loss: 0.0003
2024-08-31 14:38:15.289242 Epoch [018/030], Step [1600/2668], Total_loss: 0.0004
2024-08-31 14:39:35.637599 Epoch [018/030], Step [1800/2668], Total_loss: 0.0364
2024-08-31 14:40:50.432858 Epoch [018/030], Step [2000/2668], Total_loss: 0.0155
2024-08-31 14:42:05.831848 Epoch [018/030], Step [2200/2668], Total_loss: 0.0009
2024-08-31 14:43:26.185964 Epoch [018/030], Step [2400/2668], Total_loss: 0.0100
2024-08-31 14:44:46.165947 Epoch [018/030], Step [2600/2668], Total_loss: 0.0003
2024-08-31 14:45:08.921220 Epoch [018/030], Step [2668/2668], Total_loss: 0.0002
val on: imagenet_ai_0508_adm
ai accu: 0.5463333129882812
nature accu:0.9996666312217712
val on:imagenet_ai_0508_adm, Epoch:18, Accuracy:0.7730000019073486
val on: imagenet_ai_0419_biggan
ai accu: 0.17816665768623352
nature accu:0.999833345413208
val on:imagenet_ai_0419_biggan, Epoch:18, Accuracy:0.5889999866485596
val on: imagenet_glide
ai accu: 0.9126666784286499
nature accu:0.999833345413208
val on:imagenet_glide, Epoch:18, Accuracy:0.956250011920929
val on: imagenet_midjourney
ai accu: 0.5651666522026062
nature accu:0.9994999766349792
val on:imagenet_midjourney, Epoch:18, Accuracy:0.7823333144187927
val on: imagenet_ai_0419_sdv4
ai accu: 0.9889999628067017
nature accu:0.999833345413208
val on:imagenet_ai_0419_sdv4, Epoch:18, Accuracy:0.9944166541099548
val on: imagenet_ai_0424_sdv5
ai accu: 0.9826250672340393
nature accu:0.999250054359436
val on:imagenet_ai_0424_sdv5, Epoch:18, Accuracy:0.9909375309944153
val on: imagenet_ai_0419_vqdm
ai accu: 0.8653333187103271
nature accu:0.999833345413208
val on:imagenet_ai_0419_vqdm, Epoch:18, Accuracy:0.9325833320617676
val on: imagenet_ai_0424_wukong
ai accu: 0.9578333497047424
nature accu:0.999833345413208
val on:imagenet_ai_0424_wukong, Epoch:18, Accuracy:0.9788333177566528
Epoch:18,Accuracy:0.879319965839386, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 19
2024-08-31 14:55:49.634579 Epoch [019/030], Step [0001/2668], Total_loss: 0.0020
2024-08-31 14:57:03.733164 Epoch [019/030], Step [0200/2668], Total_loss: 0.0003
2024-08-31 14:58:17.486237 Epoch [019/030], Step [0400/2668], Total_loss: 0.0454
2024-08-31 14:59:25.932669 Epoch [019/030], Step [0600/2668], Total_loss: 0.0011
2024-08-31 15:00:34.632993 Epoch [019/030], Step [0800/2668], Total_loss: 0.0004
2024-08-31 15:01:44.051226 Epoch [019/030], Step [1000/2668], Total_loss: 0.0023
2024-08-31 15:02:52.250036 Epoch [019/030], Step [1200/2668], Total_loss: 0.0085
2024-08-31 15:04:02.633076 Epoch [019/030], Step [1400/2668], Total_loss: 0.0005
2024-08-31 15:05:10.986115 Epoch [019/030], Step [1600/2668], Total_loss: 0.0001
2024-08-31 15:06:18.885536 Epoch [019/030], Step [1800/2668], Total_loss: 0.0007
2024-08-31 15:07:27.333877 Epoch [019/030], Step [2000/2668], Total_loss: 0.0004
2024-08-31 15:08:36.185772 Epoch [019/030], Step [2200/2668], Total_loss: 0.0001
2024-08-31 15:09:45.231425 Epoch [019/030], Step [2400/2668], Total_loss: 0.0006
2024-08-31 15:10:53.734021 Epoch [019/030], Step [2600/2668], Total_loss: 0.0003
2024-08-31 15:11:16.305548 Epoch [019/030], Step [2668/2668], Total_loss: 0.0305
val on: imagenet_ai_0508_adm
ai accu: 0.6003333330154419
nature accu:1.0
val on:imagenet_ai_0508_adm, Epoch:19, Accuracy:0.800166666507721
val on: imagenet_ai_0419_biggan
ai accu: 0.21033333241939545
nature accu:0.9991666674613953
val on:imagenet_ai_0419_biggan, Epoch:19, Accuracy:0.6047499775886536
val on: imagenet_glide
ai accu: 0.9508333206176758
nature accu:0.999833345413208
val on:imagenet_glide, Epoch:19, Accuracy:0.9753333330154419
val on: imagenet_midjourney
ai accu: 0.6301666498184204
nature accu:0.9994999766349792
val on:imagenet_midjourney, Epoch:19, Accuracy:0.8148333430290222
val on: imagenet_ai_0419_sdv4
ai accu: 0.9768333435058594
nature accu:0.999833345413208
val on:imagenet_ai_0419_sdv4, Epoch:19, Accuracy:0.9883333444595337
val on: imagenet_ai_0424_sdv5
ai accu: 0.9771250486373901
nature accu:0.9998750686645508
val on:imagenet_ai_0424_sdv5, Epoch:19, Accuracy:0.9885000586509705
val on: imagenet_ai_0419_vqdm
ai accu: 0.7976666688919067
nature accu:0.999833345413208
val on:imagenet_ai_0419_vqdm, Epoch:19, Accuracy:0.8987500071525574
val on: imagenet_ai_0424_wukong
ai accu: 0.9494999647140503
nature accu:1.0
val on:imagenet_ai_0424_wukong, Epoch:19, Accuracy:0.9747499823570251
Epoch:19,Accuracy:0.8849899768829346, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 20
2024-08-31 15:21:32.243772 Epoch [020/030], Step [0001/2668], Total_loss: 0.0003
2024-08-31 15:22:39.645839 Epoch [020/030], Step [0200/2668], Total_loss: 0.0002
2024-08-31 15:23:47.436166 Epoch [020/030], Step [0400/2668], Total_loss: 0.0001
2024-08-31 15:24:55.034081 Epoch [020/030], Step [0600/2668], Total_loss: 0.0007
2024-08-31 15:26:03.632944 Epoch [020/030], Step [0800/2668], Total_loss: 0.0268
2024-08-31 15:27:10.885811 Epoch [020/030], Step [1000/2668], Total_loss: 0.0004
2024-08-31 15:28:18.686035 Epoch [020/030], Step [1200/2668], Total_loss: 0.0005
2024-08-31 15:29:25.385919 Epoch [020/030], Step [1400/2668], Total_loss: 0.0006
2024-08-31 15:30:32.986000 Epoch [020/030], Step [1600/2668], Total_loss: 0.0001
2024-08-31 15:31:39.633345 Epoch [020/030], Step [1800/2668], Total_loss: 0.0000
2024-08-31 15:33:44.386467 Epoch [020/030], Step [2000/2668], Total_loss: 0.0023
2024-08-31 15:35:02.107086 Epoch [020/030], Step [2200/2668], Total_loss: 0.0189
2024-08-31 15:36:11.085910 Epoch [020/030], Step [2400/2668], Total_loss: 0.0176
2024-08-31 15:37:17.685765 Epoch [020/030], Step [2600/2668], Total_loss: 0.0004
2024-08-31 15:37:41.112207 Epoch [020/030], Step [2668/2668], Total_loss: 0.0000
val on: imagenet_ai_0508_adm
ai accu: 0.5691666603088379
nature accu:0.9994999766349792
val on:imagenet_ai_0508_adm, Epoch:20, Accuracy:0.784333348274231
val on: imagenet_ai_0419_biggan
ai accu: 0.2303333282470703
nature accu:0.9996666312217712
val on:imagenet_ai_0419_biggan, Epoch:20, Accuracy:0.6150000095367432
val on: imagenet_glide
ai accu: 0.9356666803359985
nature accu:1.0
val on:imagenet_glide, Epoch:20, Accuracy:0.9678333401679993
val on: imagenet_midjourney
ai accu: 0.6101666688919067
nature accu:0.999833345413208
val on:imagenet_midjourney, Epoch:20, Accuracy:0.8050000071525574
val on: imagenet_ai_0419_sdv4
ai accu: 0.9881666302680969
nature accu:0.999833345413208
val on:imagenet_ai_0419_sdv4, Epoch:20, Accuracy:0.9940000176429749
val on: imagenet_ai_0424_sdv5
ai accu: 0.9862500429153442
nature accu:0.999625027179718
val on:imagenet_ai_0424_sdv5, Epoch:20, Accuracy:0.9929375648498535
val on: imagenet_ai_0419_vqdm
ai accu: 0.8654999732971191
nature accu:0.9994999766349792
val on:imagenet_ai_0419_vqdm, Epoch:20, Accuracy:0.9325000047683716
val on: imagenet_ai_0424_wukong
ai accu: 0.9571666717529297
nature accu:0.999833345413208
val on:imagenet_ai_0424_wukong, Epoch:20, Accuracy:0.9785000085830688
Epoch:20,Accuracy:0.8881299495697021, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 21
2024-08-31 15:47:00.486094 Epoch [021/030], Step [0001/2668], Total_loss: 0.0015
2024-08-31 15:48:01.285859 Epoch [021/030], Step [0200/2668], Total_loss: 0.0015
2024-08-31 15:49:02.285978 Epoch [021/030], Step [0400/2668], Total_loss: 0.0010
2024-08-31 15:50:02.886591 Epoch [021/030], Step [0600/2668], Total_loss: 0.0000
2024-08-31 15:51:03.185929 Epoch [021/030], Step [0800/2668], Total_loss: 0.0001
2024-08-31 15:52:03.685856 Epoch [021/030], Step [1000/2668], Total_loss: 0.0000
2024-08-31 15:53:04.285756 Epoch [021/030], Step [1200/2668], Total_loss: 0.0000
2024-08-31 15:54:04.885878 Epoch [021/030], Step [1400/2668], Total_loss: 0.0005
2024-08-31 15:55:05.186016 Epoch [021/030], Step [1600/2668], Total_loss: 0.0000
2024-08-31 15:56:06.233679 Epoch [021/030], Step [1800/2668], Total_loss: 0.0000
2024-08-31 15:57:06.685860 Epoch [021/030], Step [2000/2668], Total_loss: 0.0003
2024-08-31 15:58:06.985812 Epoch [021/030], Step [2200/2668], Total_loss: 0.0000
2024-08-31 15:59:07.385986 Epoch [021/030], Step [2400/2668], Total_loss: 0.0000
2024-08-31 16:00:08.085899 Epoch [021/030], Step [2600/2668], Total_loss: 0.0002
2024-08-31 16:00:28.315922 Epoch [021/030], Step [2668/2668], Total_loss: 0.0000
val on: imagenet_ai_0508_adm
ai accu: 0.534500002861023
nature accu:0.999833345413208
val on:imagenet_ai_0508_adm, Epoch:21, Accuracy:0.7671666741371155
val on: imagenet_ai_0419_biggan
ai accu: 0.17233332991600037
nature accu:0.999833345413208
val on:imagenet_ai_0419_biggan, Epoch:21, Accuracy:0.5860833525657654
val on: imagenet_glide
ai accu: 0.9329999685287476
nature accu:1.0
val on:imagenet_glide, Epoch:21, Accuracy:0.9664999842643738
val on: imagenet_midjourney
ai accu: 0.5801666378974915
nature accu:0.9988332986831665
val on:imagenet_midjourney, Epoch:21, Accuracy:0.7894999980926514
val on: imagenet_ai_0419_sdv4
ai accu: 0.9858333468437195
nature accu:0.9996666312217712
val on:imagenet_ai_0419_sdv4, Epoch:21, Accuracy:0.9927499890327454
val on: imagenet_ai_0424_sdv5
ai accu: 0.9855000376701355
nature accu:0.999750018119812
val on:imagenet_ai_0424_sdv5, Epoch:21, Accuracy:0.9926250576972961
val on: imagenet_ai_0419_vqdm
ai accu: 0.7933333516120911
nature accu:0.999833345413208
val on:imagenet_ai_0419_vqdm, Epoch:21, Accuracy:0.8965833187103271
val on: imagenet_ai_0424_wukong
ai accu: 0.9616666436195374
nature accu:0.9994999766349792
val on:imagenet_ai_0424_wukong, Epoch:21, Accuracy:0.9805833101272583
Epoch:21,Accuracy:0.8763200044631958, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 22
2024-08-31 16:09:27.986407 Epoch [022/030], Step [0001/2668], Total_loss: 0.0003
2024-08-31 16:10:28.986440 Epoch [022/030], Step [0200/2668], Total_loss: 0.0003
2024-08-31 16:11:29.685976 Epoch [022/030], Step [0400/2668], Total_loss: 0.0004
2024-08-31 16:12:30.385790 Epoch [022/030], Step [0600/2668], Total_loss: 0.0003
2024-08-31 16:13:31.986696 Epoch [022/030], Step [0800/2668], Total_loss: 0.0000
2024-08-31 16:14:55.386256 Epoch [022/030], Step [1000/2668], Total_loss: 0.0009
2024-08-31 16:16:32.135816 Epoch [022/030], Step [1200/2668], Total_loss: 0.0101
2024-08-31 16:18:02.584557 Epoch [022/030], Step [1400/2668], Total_loss: 0.0364
2024-08-31 16:19:21.086098 Epoch [022/030], Step [1600/2668], Total_loss: 0.0270
2024-08-31 16:20:44.286609 Epoch [022/030], Step [1800/2668], Total_loss: 0.0051
2024-08-31 16:22:11.986356 Epoch [022/030], Step [2000/2668], Total_loss: 0.0005
2024-08-31 16:23:42.786216 Epoch [022/030], Step [2200/2668], Total_loss: 0.0073
2024-08-31 16:25:11.885923 Epoch [022/030], Step [2400/2668], Total_loss: 0.1176
2024-08-31 16:26:53.785976 Epoch [022/030], Step [2600/2668], Total_loss: 0.0004
2024-08-31 16:27:18.924624 Epoch [022/030], Step [2668/2668], Total_loss: 0.0002
val on: imagenet_ai_0508_adm
ai accu: 0.47833332419395447
nature accu:0.9993333220481873
val on:imagenet_ai_0508_adm, Epoch:22, Accuracy:0.7388333082199097
val on: imagenet_ai_0419_biggan
ai accu: 0.15133333206176758
nature accu:0.9994999766349792
val on:imagenet_ai_0419_biggan, Epoch:22, Accuracy:0.5754166841506958
val on: imagenet_glide
ai accu: 0.9328333139419556
nature accu:0.9996666312217712
val on:imagenet_glide, Epoch:22, Accuracy:0.9662500023841858
val on: imagenet_midjourney
ai accu: 0.5483333468437195
nature accu:0.9993333220481873
val on:imagenet_midjourney, Epoch:22, Accuracy:0.7738333344459534
val on: imagenet_ai_0419_sdv4
ai accu: 0.9878333210945129
nature accu:0.9993333220481873
val on:imagenet_ai_0419_sdv4, Epoch:22, Accuracy:0.9935833215713501
val on: imagenet_ai_0424_sdv5
ai accu: 0.9857500195503235
nature accu:0.99937504529953
val on:imagenet_ai_0424_sdv5, Epoch:22, Accuracy:0.9925625324249268
val on: imagenet_ai_0419_vqdm
ai accu: 0.8548333048820496
nature accu:0.9991666674613953
val on:imagenet_ai_0419_vqdm, Epoch:22, Accuracy:0.9269999861717224
val on: imagenet_ai_0424_wukong
ai accu: 0.968666672706604
nature accu:0.9994999766349792
val on:imagenet_ai_0424_wukong, Epoch:22, Accuracy:0.9840832948684692
Epoch:22,Accuracy:0.8738899827003479, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 23
2024-08-31 16:38:50.286050 Epoch [023/030], Step [0001/2668], Total_loss: 0.0002
2024-08-31 16:40:00.686155 Epoch [023/030], Step [0200/2668], Total_loss: 0.0030
2024-08-31 16:41:03.385775 Epoch [023/030], Step [0400/2668], Total_loss: 0.0005
2024-08-31 16:42:07.886071 Epoch [023/030], Step [0600/2668], Total_loss: 0.0010
2024-08-31 16:43:13.486066 Epoch [023/030], Step [0800/2668], Total_loss: 0.0011
2024-08-31 16:44:16.486847 Epoch [023/030], Step [1000/2668], Total_loss: 0.0007
2024-08-31 16:45:18.785995 Epoch [023/030], Step [1200/2668], Total_loss: 0.0002
2024-08-31 16:46:20.285884 Epoch [023/030], Step [1400/2668], Total_loss: 0.0005
2024-08-31 16:47:22.685805 Epoch [023/030], Step [1600/2668], Total_loss: 0.0003
2024-08-31 16:48:25.385894 Epoch [023/030], Step [1800/2668], Total_loss: 0.0000
2024-08-31 16:49:27.385756 Epoch [023/030], Step [2000/2668], Total_loss: 0.0490
2024-08-31 16:50:29.485950 Epoch [023/030], Step [2200/2668], Total_loss: 0.0000
2024-08-31 16:51:33.533857 Epoch [023/030], Step [2400/2668], Total_loss: 0.0005
2024-08-31 16:52:40.520238 Epoch [023/030], Step [2600/2668], Total_loss: 0.0000
2024-08-31 16:53:02.689571 Epoch [023/030], Step [2668/2668], Total_loss: 0.0000
val on: imagenet_ai_0508_adm
ai accu: 0.5791666507720947
nature accu:0.9994999766349792
val on:imagenet_ai_0508_adm, Epoch:23, Accuracy:0.7893333435058594
val on: imagenet_ai_0419_biggan
ai accu: 0.23616667091846466
nature accu:0.9996666312217712
val on:imagenet_ai_0419_biggan, Epoch:23, Accuracy:0.6179166436195374
val on: imagenet_glide
ai accu: 0.9469999670982361
nature accu:0.9996666312217712
val on:imagenet_glide, Epoch:23, Accuracy:0.9733332991600037
val on: imagenet_midjourney
ai accu: 0.5831666588783264
nature accu:0.9983333349227905
val on:imagenet_midjourney, Epoch:23, Accuracy:0.7907499670982361
val on: imagenet_ai_0419_sdv4
ai accu: 0.9894999861717224
nature accu:0.9994999766349792
val on:imagenet_ai_0419_sdv4, Epoch:23, Accuracy:0.9944999814033508
val on: imagenet_ai_0424_sdv5
ai accu: 0.986875057220459
nature accu:0.999625027179718
val on:imagenet_ai_0424_sdv5, Epoch:23, Accuracy:0.9932500720024109
val on: imagenet_ai_0419_vqdm
ai accu: 0.9041666388511658
nature accu:0.9991666674613953
val on:imagenet_ai_0419_vqdm, Epoch:23, Accuracy:0.9516666531562805
val on: imagenet_ai_0424_wukong
ai accu: 0.9638333320617676
nature accu:0.9994999766349792
val on:imagenet_ai_0424_wukong, Epoch:23, Accuracy:0.9816666841506958
Epoch:23,Accuracy:0.8908199667930603, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 24
2024-08-31 17:05:06.985944 Epoch [024/030], Step [0001/2668], Total_loss: 0.0080
2024-08-31 17:06:31.786505 Epoch [024/030], Step [0200/2668], Total_loss: 0.0022
2024-08-31 17:08:07.985217 Epoch [024/030], Step [0400/2668], Total_loss: 0.0007
2024-08-31 17:09:51.184982 Epoch [024/030], Step [0600/2668], Total_loss: 0.0002
2024-08-31 17:11:43.386667 Epoch [024/030], Step [0800/2668], Total_loss: 0.0005
2024-08-31 17:13:37.903713 Epoch [024/030], Step [1000/2668], Total_loss: 0.0002
2024-08-31 17:15:15.886620 Epoch [024/030], Step [1200/2668], Total_loss: 0.0003
2024-08-31 17:16:56.086757 Epoch [024/030], Step [1400/2668], Total_loss: 0.0000
2024-08-31 17:18:38.699403 Epoch [024/030], Step [1600/2668], Total_loss: 0.0009
2024-08-31 17:20:30.886345 Epoch [024/030], Step [1800/2668], Total_loss: 0.0000
2024-08-31 17:22:13.386040 Epoch [024/030], Step [2000/2668], Total_loss: 0.0007
2024-08-31 17:23:55.586697 Epoch [024/030], Step [2200/2668], Total_loss: 0.0000
2024-08-31 17:25:38.086562 Epoch [024/030], Step [2400/2668], Total_loss: 0.0033
2024-08-31 17:27:38.105839 Epoch [024/030], Step [2600/2668], Total_loss: 0.0005
2024-08-31 17:28:06.993564 Epoch [024/030], Step [2668/2668], Total_loss: 0.0002
val on: imagenet_ai_0508_adm
ai accu: 0.5139999985694885
nature accu:0.999833345413208
val on:imagenet_ai_0508_adm, Epoch:24, Accuracy:0.7569166421890259
val on: imagenet_ai_0419_biggan
ai accu: 0.11866666376590729
nature accu:0.999833345413208
val on:imagenet_ai_0419_biggan, Epoch:24, Accuracy:0.559249997138977
val on: imagenet_glide
ai accu: 0.9120000004768372
nature accu:1.0
val on:imagenet_glide, Epoch:24, Accuracy:0.9559999704360962
val on: imagenet_midjourney
ai accu: 0.5931666493415833
nature accu:0.9996666312217712
val on:imagenet_midjourney, Epoch:24, Accuracy:0.7964166402816772
val on: imagenet_ai_0419_sdv4
ai accu: 0.9808333516120911
nature accu:0.999833345413208
val on:imagenet_ai_0419_sdv4, Epoch:24, Accuracy:0.9903333187103271
val on: imagenet_ai_0424_sdv5
ai accu: 0.9805000424385071
nature accu:0.9998750686645508
val on:imagenet_ai_0424_sdv5, Epoch:24, Accuracy:0.9901875257492065
val on: imagenet_ai_0419_vqdm
ai accu: 0.7684999704360962
nature accu:0.999833345413208
val on:imagenet_ai_0419_vqdm, Epoch:24, Accuracy:0.8841666579246521
val on: imagenet_ai_0424_wukong
ai accu: 0.953499972820282
nature accu:0.999833345413208
val on:imagenet_ai_0424_wukong, Epoch:24, Accuracy:0.9766666293144226
Epoch:24,Accuracy:0.8687999844551086, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 25
2024-08-31 17:42:57.886763 Epoch [025/030], Step [0001/2668], Total_loss: 0.0007
2024-08-31 17:44:28.487428 Epoch [025/030], Step [0200/2668], Total_loss: 0.0004
2024-08-31 17:45:54.786443 Epoch [025/030], Step [0400/2668], Total_loss: 0.0002
2024-08-31 17:47:24.115907 Epoch [025/030], Step [0600/2668], Total_loss: 0.0002
2024-08-31 17:48:49.086684 Epoch [025/030], Step [0800/2668], Total_loss: 0.0006
2024-08-31 17:50:19.986492 Epoch [025/030], Step [1000/2668], Total_loss: 0.0009
2024-08-31 17:51:44.386638 Epoch [025/030], Step [1200/2668], Total_loss: 0.0006
2024-08-31 17:53:15.508888 Epoch [025/030], Step [1400/2668], Total_loss: 0.0002
2024-08-31 17:54:42.086099 Epoch [025/030], Step [1600/2668], Total_loss: 0.0005
2024-08-31 17:56:10.204139 Epoch [025/030], Step [1800/2668], Total_loss: 0.0000
2024-08-31 17:57:36.686574 Epoch [025/030], Step [2000/2668], Total_loss: 0.0005
2024-08-31 17:59:05.286283 Epoch [025/030], Step [2200/2668], Total_loss: 0.0002
2024-08-31 18:00:32.104272 Epoch [025/030], Step [2400/2668], Total_loss: 0.0000
2024-08-31 18:02:00.486676 Epoch [025/030], Step [2600/2668], Total_loss: 0.0166
2024-08-31 18:02:28.590365 Epoch [025/030], Step [2668/2668], Total_loss: 0.0000
val on: imagenet_ai_0508_adm
ai accu: 0.5899999737739563
nature accu:0.9991666674613953
val on:imagenet_ai_0508_adm, Epoch:25, Accuracy:0.7945833206176758
val on: imagenet_ai_0419_biggan
ai accu: 0.1758333295583725
nature accu:1.0
val on:imagenet_ai_0419_biggan, Epoch:25, Accuracy:0.5879166722297668
val on: imagenet_glide
ai accu: 0.9353333115577698
nature accu:0.999833345413208
val on:imagenet_glide, Epoch:25, Accuracy:0.9675832986831665
val on: imagenet_midjourney
ai accu: 0.6344999670982361
nature accu:0.9994999766349792
val on:imagenet_midjourney, Epoch:25, Accuracy:0.8169999718666077
val on: imagenet_ai_0419_sdv4
ai accu: 0.9891666769981384
nature accu:0.9993333220481873
val on:imagenet_ai_0419_sdv4, Epoch:25, Accuracy:0.9942499995231628
val on: imagenet_ai_0424_sdv5
ai accu: 0.9876250624656677
nature accu:0.999500036239624
val on:imagenet_ai_0424_sdv5, Epoch:25, Accuracy:0.9935625195503235
val on: imagenet_ai_0419_vqdm
ai accu: 0.8828333020210266
nature accu:1.0
val on:imagenet_ai_0419_vqdm, Epoch:25, Accuracy:0.9414166808128357
val on: imagenet_ai_0424_wukong
ai accu: 0.9748333096504211
nature accu:0.9991666674613953
val on:imagenet_ai_0424_wukong, Epoch:25, Accuracy:0.9869999885559082
Epoch:25,Accuracy:0.889739990234375, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 26
2024-08-31 18:16:50.486302 Epoch [026/030], Step [0001/2668], Total_loss: 0.0001
2024-08-31 18:18:15.786274 Epoch [026/030], Step [0200/2668], Total_loss: 0.0001
2024-08-31 18:19:44.286961 Epoch [026/030], Step [0400/2668], Total_loss: 0.0003
2024-08-31 18:21:11.786541 Epoch [026/030], Step [0600/2668], Total_loss: 0.0028
2024-08-31 18:22:40.087742 Epoch [026/030], Step [0800/2668], Total_loss: 0.0001
2024-08-31 18:24:07.186714 Epoch [026/030], Step [1000/2668], Total_loss: 0.0042
2024-08-31 18:25:35.392180 Epoch [026/030], Step [1200/2668], Total_loss: 0.0011
2024-08-31 18:27:02.986343 Epoch [026/030], Step [1400/2668], Total_loss: 0.0003
2024-08-31 18:28:29.286539 Epoch [026/030], Step [1600/2668], Total_loss: 0.0005
2024-08-31 18:29:55.905876 Epoch [026/030], Step [1800/2668], Total_loss: 0.0001
2024-08-31 18:31:24.586077 Epoch [026/030], Step [2000/2668], Total_loss: 0.0003
2024-08-31 18:32:49.003040 Epoch [026/030], Step [2200/2668], Total_loss: 0.0006
2024-08-31 18:34:13.685989 Epoch [026/030], Step [2400/2668], Total_loss: 0.0006
2024-08-31 18:35:43.086479 Epoch [026/030], Step [2600/2668], Total_loss: 0.0005
2024-08-31 18:36:11.297937 Epoch [026/030], Step [2668/2668], Total_loss: 0.0001
val on: imagenet_ai_0508_adm
ai accu: 0.5538333058357239
nature accu:0.9994999766349792
val on:imagenet_ai_0508_adm, Epoch:26, Accuracy:0.7766666412353516
val on: imagenet_ai_0419_biggan
ai accu: 0.1899999976158142
nature accu:0.9991666674613953
val on:imagenet_ai_0419_biggan, Epoch:26, Accuracy:0.5945833325386047
val on: imagenet_glide
ai accu: 0.9363332986831665
nature accu:0.9994999766349792
val on:imagenet_glide, Epoch:26, Accuracy:0.9679166674613953
val on: imagenet_midjourney
ai accu: 0.6046666502952576
nature accu:0.9990000128746033
val on:imagenet_midjourney, Epoch:26, Accuracy:0.8018333315849304
val on: imagenet_ai_0419_sdv4
ai accu: 0.9923332929611206
nature accu:0.9993333220481873
val on:imagenet_ai_0419_sdv4, Epoch:26, Accuracy:0.9958333373069763
val on: imagenet_ai_0424_sdv5
ai accu: 0.9923750758171082
nature accu:0.999625027179718
val on:imagenet_ai_0424_sdv5, Epoch:26, Accuracy:0.9960000514984131
val on: imagenet_ai_0419_vqdm
ai accu: 0.8844999670982361
nature accu:0.9994999766349792
val on:imagenet_ai_0419_vqdm, Epoch:26, Accuracy:0.9419999718666077
val on: imagenet_ai_0424_wukong
ai accu: 0.9714999794960022
nature accu:0.9991666674613953
val on:imagenet_ai_0424_wukong, Epoch:26, Accuracy:0.9853333234786987
Epoch:26,Accuracy:0.8870599865913391, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 27
2024-08-31 18:50:38.086628 Epoch [027/030], Step [0001/2668], Total_loss: 0.0000
2024-08-31 18:52:10.998385 Epoch [027/030], Step [0200/2668], Total_loss: 0.0003
2024-08-31 18:53:36.500545 Epoch [027/030], Step [0400/2668], Total_loss: 0.0002
2024-08-31 18:55:05.590892 Epoch [027/030], Step [0600/2668], Total_loss: 0.0002
2024-08-31 18:56:36.185929 Epoch [027/030], Step [0800/2668], Total_loss: 0.0062
2024-08-31 18:57:59.401204 Epoch [027/030], Step [1000/2668], Total_loss: 0.0749
2024-08-31 18:59:32.086568 Epoch [027/030], Step [1200/2668], Total_loss: 0.0004
2024-08-31 19:00:57.602237 Epoch [027/030], Step [1400/2668], Total_loss: 0.0005
2024-08-31 19:02:22.686650 Epoch [027/030], Step [1600/2668], Total_loss: 0.0005
2024-08-31 19:03:56.386009 Epoch [027/030], Step [1800/2668], Total_loss: 0.0001
2024-08-31 19:05:21.885815 Epoch [027/030], Step [2000/2668], Total_loss: 0.0002
2024-08-31 19:06:51.786245 Epoch [027/030], Step [2200/2668], Total_loss: 0.0023
2024-08-31 19:08:19.786085 Epoch [027/030], Step [2400/2668], Total_loss: 0.0098
2024-08-31 19:09:43.812455 Epoch [027/030], Step [2600/2668], Total_loss: 0.0092
2024-08-31 19:10:11.396532 Epoch [027/030], Step [2668/2668], Total_loss: 0.0010
val on: imagenet_ai_0508_adm
ai accu: 0.6003333330154419
nature accu:1.0
val on:imagenet_ai_0508_adm, Epoch:27, Accuracy:0.800166666507721
val on: imagenet_ai_0419_biggan
ai accu: 0.19566667079925537
nature accu:0.999833345413208
val on:imagenet_ai_0419_biggan, Epoch:27, Accuracy:0.5977500081062317
val on: imagenet_glide
ai accu: 0.9359999895095825
nature accu:1.0
val on:imagenet_glide, Epoch:27, Accuracy:0.9679999947547913
val on: imagenet_midjourney
ai accu: 0.621833324432373
nature accu:0.9994999766349792
val on:imagenet_midjourney, Epoch:27, Accuracy:0.8106666803359985
val on: imagenet_ai_0419_sdv4
ai accu: 0.9916666746139526
nature accu:1.0
val on:imagenet_ai_0419_sdv4, Epoch:27, Accuracy:0.9958333373069763
val on: imagenet_ai_0424_sdv5
ai accu: 0.9902500510215759
nature accu:0.999625027179718
val on:imagenet_ai_0424_sdv5, Epoch:27, Accuracy:0.994937539100647
val on: imagenet_ai_0419_vqdm
ai accu: 0.8913333415985107
nature accu:0.999833345413208
val on:imagenet_ai_0419_vqdm, Epoch:27, Accuracy:0.9455833435058594
val on: imagenet_ai_0424_wukong
ai accu: 0.9751666784286499
nature accu:0.9996666312217712
val on:imagenet_ai_0424_wukong, Epoch:27, Accuracy:0.987416684627533
Epoch:27,Accuracy:0.8918399810791016, bestEpoch:9, bestAccu:0.9235000014305115
## Epoch 28
2024-08-31 19:24:42.386501 Epoch [028/030], Step [0001/2668], Total_loss: 0.0000
2024-08-31 19:26:06.386410 Epoch [028/030], Step [0200/2668], Total_loss: 0.0010
2024-08-31 19:27:38.386290 Epoch [028/030], Step [0400/2668], Total_loss: 0.0000
2024-08-31 19:29:06.804353 Epoch [028/030], Step [0600/2668], Total_loss: 0.0000
2024-08-31 19:30:31.886632 Epoch [028/030], Step [0800/2668], Total_loss: 0.0002
2024-08-31 19:32:03.886483 Epoch [028/030], Step [1000/2668], Total_loss: 0.0004
2024-08-31 19:33:29.105880 Epoch [028/030], Step [1200/2668], Total_loss: 0.0006
2024-08-31 19:34:54.486408 Epoch [028/030], Step [1400/2668], Total_loss: 0.0000
2024-08-31 19:36:29.086562 Epoch [028/030], Step [1600/2668], Total_loss: 0.0003
2024-08-31 19:37:53.386153 Epoch [028/030], Step [1800/2668], Total_loss: 0.0001
2024-08-31 19:39:21.799296 Epoch [028/030], Step [2000/2668], Total_loss: 0.0003
2024-08-31 19:40:50.605691 Epoch [028/030], Step [2200/2668], Total_loss: 0.0008
2024-08-31 19:42:14.786530 Epoch [028/030], Step [2400/2668], Total_loss: 0.0003
2024-08-31 19:43:47.986681 Epoch [028/030], Step [2600/2668], Total_loss: 0.0000
2024-08-31 19:44:16.396343 Epoch [028/030], Step [2668/2668], Total_loss: 0.0000
val on: imagenet_ai_0508_adm
ai accu: 0.577833354473114
nature accu:0.999833345413208
val on:imagenet_ai_0508_adm, Epoch:28, Accuracy:0.7888333201408386
val on: imagenet_ai_0419_biggan
ai accu: 0.19583332538604736
nature accu:0.9996666312217712
val on:imagenet_ai_0419_biggan, Epoch:28, Accuracy:0.5977500081062317
val on: imagenet_glide
ai accu: 0.9361666440963745
nature accu:0.9994999766349792
val on:imagenet_glide, Epoch:28, Accuracy:0.9678333401679993
val on: imagenet_midjourney
ai accu: 0.6173333525657654
nature accu:0.999833345413208
val on:imagenet_midjourney, Epoch:28, Accuracy:0.8085833191871643
val on: imagenet_ai_0419_sdv4
ai accu: 0.9919999837875366
nature accu:0.9994999766349792
val on:imagenet_ai_0419_sdv4, Epoch:28, Accuracy:0.9957500100135803
val on: imagenet_ai_0424_sdv5
ai accu: 0.9901250600814819
nature accu:0.9998750686645508
val on:imagenet_ai_0424_sdv5, Epoch:28, Accuracy:0.9950000643730164
val on: imagenet_ai_0419_vqdm
ai accu: 0.8888333439826965
nature accu:1.0
val on:imagenet_ai_0419_vqdm, Epoch:28, Accuracy:0.9444166421890259
val on: imagenet_ai_0424_wukong
ai accu: 0.9749999642372131
nature accu:0.9996666312217712
val on:imagenet_ai_0424_wukong, Epoch:28, Accuracy:0.9873332977294922
Epoch:28,Accuracy:0.8900599479675293, bestEpoch:9, bestAccu:0.9235000014305115
# Epoch 29
2024-08-31 19:58:31.286469 Epoch [029/030], Step [0001/2668], Total_loss: 0.0007
2024-08-31 19:59:53.306917 Epoch [029/030], Step [0200/2668], Total_loss: 0.0002
2024-08-31 20:01:26.986589 Epoch [029/030], Step [0400/2668], Total_loss: 0.0000
2024-08-31 20:02:52.486120 Epoch [029/030], Step [0600/2668], Total_loss: 0.0002
2024-08-31 20:04:21.297713 Epoch [029/030], Step [0800/2668], Total_loss: 0.0028
2024-08-31 20:05:48.787121 Epoch [029/030], Step [1000/2668], Total_loss: 0.0010
2024-08-31 20:07:12.486510 Epoch [029/030], Step [1200/2668], Total_loss: 0.0034
2024-08-31 20:08:42.386441 Epoch [029/030], Step [1400/2668], Total_loss: 0.0003
2024-08-31 20:10:08.686502 Epoch [029/030], Step [1600/2668], Total_loss: 0.0003
2024-08-31 20:11:33.686637 Epoch [029/030], Step [1800/2668], Total_loss: 0.0002
2024-08-31 20:13:05.286295 Epoch [029/030], Step [2000/2668], Total_loss: 0.0016
2024-08-31 20:14:28.286373 Epoch [029/030], Step [2200/2668], Total_loss: 0.0011
2024-08-31 20:15:55.386104 Epoch [029/030], Step [2400/2668], Total_loss: 0.0002
2024-08-31 20:17:25.986532 Epoch [029/030], Step [2600/2668], Total_loss: 0.0003
2024-08-31 20:17:53.890611 Epoch [029/030], Step [2668/2668], Total_loss: 0.0000
## adm
val on: imagenet_ai_0508_adm
ai accu: 0.5945000052452087
nature accu:0.9996666312217712
val on:imagenet_ai_0508_adm, Epoch:29, Accuracy:0.79708331823349
## biggan
val on: imagenet_ai_0419_biggan
ai accu: 0.20866666734218597
nature accu:1.0
val on:imagenet_ai_0419_biggan, Epoch:29, Accuracy:0.6043333411216736
## glide
val on: imagenet_glide
ai accu: 0.9453333020210266
nature accu:0.999833345413208
val on:imagenet_glide, Epoch:29, Accuracy:0.9725832939147949
## midjourney
val on: imagenet_midjourney
ai accu: 0.6266666650772095
nature accu:0.9990000128746033
val on:imagenet_midjourney, Epoch:29, Accuracy:0.812833309173584
## sdv4
val on: imagenet_ai_0419_sdv4
ai accu: 0.9914999604225159
nature accu:0.999833345413208
val on:imagenet_ai_0419_sdv4, Epoch:29, Accuracy:0.9956666827201843
## sdv5
val on: imagenet_ai_0424_sdv5
ai accu: 0.9893750548362732
nature accu:0.9998750686645508
val on:imagenet_ai_0424_sdv5, Epoch:29, Accuracy:0.9946250319480896
## vqdm
val on: imagenet_ai_0419_vqdm
ai accu: 0.8903332948684692
nature accu:1.0
val on:imagenet_ai_0419_vqdm, Epoch:29, Accuracy:0.9451666474342346
## wukong
val on: imagenet_ai_0424_wukong
ai accu: 0.9768333435058594
nature accu:1.0
val on:imagenet_ai_0424_wukong, Epoch:29, Accuracy:0.9884166717529297
## mean
Epoch:29,Accuracy:0.8930699825286865, bestEpoch:9, bestAccu:0.9235000014305115
# Epoch 30
2024-08-31 20:32:19.686208 Epoch [030/030], Step [0001/2668], Total_loss: 0.0007
2024-08-31 20:33:45.814914 Epoch [030/030], Step [0200/2668], Total_loss: 0.0005
2024-08-31 20:35:13.916127 Epoch [030/030], Step [0400/2668], Total_loss: 0.0000
2024-08-31 20:36:40.307177 Epoch [030/030], Step [0600/2668], Total_loss: 0.0001
2024-08-31 20:38:08.386668 Epoch [030/030], Step [0800/2668], Total_loss: 0.0003
2024-08-31 20:39:34.903788 Epoch [030/030], Step [1000/2668], Total_loss: 0.0003
2024-08-31 20:41:02.586748 Epoch [030/030], Step [1200/2668], Total_loss: 0.0002
2024-08-31 20:42:28.786152 Epoch [030/030], Step [1400/2668], Total_loss: 0.0000
2024-08-31 20:43:56.102750 Epoch [030/030], Step [1600/2668], Total_loss: 0.0002
2024-08-31 20:45:22.505555 Epoch [030/030], Step [1800/2668], Total_loss: 0.0002
2024-08-31 20:46:47.786689 Epoch [030/030], Step [2000/2668], Total_loss: 0.0000
2024-08-31 20:48:16.387108 Epoch [030/030], Step [2200/2668], Total_loss: 0.0292
2024-08-31 20:49:41.686625 Epoch [030/030], Step [2400/2668], Total_loss: 0.0000
2024-08-31 20:51:10.209860 Epoch [030/030], Step [2600/2668], Total_loss: 0.0002
2024-08-31 20:51:38.390673 Epoch [030/030], Step [2668/2668], Total_loss: 0.0000
## adm
val on: imagenet_ai_0508_adm
ai accu: 0.5736666321754456
nature accu:0.9996666312217712
val on:imagenet_ai_0508_adm, Epoch:30, Accuracy:0.7866666316986084
## biggan
val on: imagenet_ai_0419_biggan
ai accu: 0.18916666507720947
nature accu:0.999833345413208
val on:imagenet_ai_0419_biggan, Epoch:30, Accuracy:0.5945000052452087
## glide
val on: imagenet_glide
ai accu: 0.9365000128746033
nature accu:0.9994999766349792
val on:imagenet_glide, Epoch:30, Accuracy:0.9679999947547913
## midjourney
val on: imagenet_midjourney
ai accu: 0.6243333220481873
nature accu:0.9993333220481873
val on:imagenet_midjourney, Epoch:30, Accuracy:0.8118333220481873
## sdv4
val on: imagenet_ai_0419_sdv4
ai accu: 0.9923332929611206
nature accu:0.9996666312217712
val on:imagenet_ai_0419_sdv4, Epoch:30, Accuracy:0.9959999918937683
## sdv5
val on: imagenet_ai_0424_sdv5
ai accu: 0.9908750653266907
nature accu:0.999750018119812
val on:imagenet_ai_0424_sdv5, Epoch:30, Accuracy:0.9953125715255737
## vqdm
val on: imagenet_ai_0419_vqdm
ai accu: 0.8834999799728394
nature accu:0.9993333220481873
val on:imagenet_ai_0419_vqdm, Epoch:30, Accuracy:0.9414166808128357
## wukong
val on: imagenet_ai_0424_wukong
ai accu: 0.9761666655540466
nature accu:1.0
val on:imagenet_ai_0424_wukong, Epoch:30, Accuracy:0.9880833029747009
## mean
Epoch:30,Accuracy:0.8896299600601196, bestEpoch:9, bestAccu:0.9235000014305115
