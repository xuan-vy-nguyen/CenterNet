import json 
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os

count = 0
lstDir= ['92', '95', '55', '71', '69', '82', '5', '51', '74', '68', '47', '10', '12', '38', '42', '46', '81', '84', '85', '54', '88', '67', '65', '8', '11', '98', '6', '3', '77', '97', '48', '43', '33', '14', '75', '50', '15', '62', '32', '4', '70', '36', '19', '34', '56', '53', '79', '73', '72', '39', '52', '9', '91', '29', '1', '22', '7', '66', '58', '44', '49', '24', '18', '78', '59', '13', '87', '40', '37', '86', '76', '17', '64', '41', '25', '30', '89', '83', '26', '21', '16', '90', '94', '57', '35', '60', '23', '28', '96', '99', '31', '100', '61', '93', '63', '20', '80', '27', '2', '45']

for lsd in lstDir:
	# convert old format to new format
	# {'image_name':[list of bbox]}
    dic_result_demo = {}
    with open('/home/ptthang/aicity20/results_demo_json_4/{}_results_demo.json'.format(lsd),'r') as f:
        file_content = json.load(f)
        for ob in file_content:
            
            image_name = ob['image_name']
            if image_name not in dic_result_demo:
                dic_result_demo[image_name] = []
                # count+=1
            dic_result_demo[image_name].append({
                "category_id": ob["category_id"], 
                "bbox": ob["bbox"], 
                "score": ob["score"]
            })
    # use new format to draw
    os.system('mkdir /home/ptthang/aicity20/average_drawn_4_03/{}'.format(lsd))
    for imgtmp, lsbbox in dic_result_demo.items():
        img= '/home/ptthang/cli/average_image_test/{}/{}'.format(lsd,imgtmp.split('/')[-1])
        print('drawing {}'.format(img))
        source_img = Image.open(img).convert("RGB")
        draw = ImageDraw.Draw(source_img)
        for ob in lsbbox:
            if ob['score'] >= 0.3:
                bbxs = ob['bbox']
                draw.rectangle(((bbxs[0], bbxs[1]), (bbxs[0]+bbxs[2], bbxs[1]+bbxs[3])),outline='red', width=5)
        source_img.save('/home/ptthang/aicity20/average_drawn_4_03/{}/{}'.format(lsd,img.split('/')[-1]))
        print('saved /home/ptthang/aicity20/average_drawn_4_03/{}/{}'.format(lsd,img.split('/')[-1]))
        
# print(count)
# dic_result_demo
