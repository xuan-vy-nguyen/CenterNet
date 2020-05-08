mkdir abc

cd ../gdriveAPI

######################
echo 'download image_data'
echo '+ 801_1000'
python download_id_name.py --id 1V-7Tn5xUEAnyfh7eWdeimd9ER0h4e9zY --name ../CenterNet/data/abc/801_1000.zip
echo '+ 601_800'
python download_id_name.py --id 1w4dCsdjF9eVbTf7ETU_QghPXx0WpTkxQ --name ../CenterNet/data/abc/601_800.zip
echo '+ 401_600'
python download_id_name.py --id 1Yok3J4hmjTW_dpJ-1KFqXpLHsdf7BJ_y --name ../CenterNet/data/abc/401_600.zip
echo '+201_400'
python download_id_name.py --id 1CXgItvi4Rn1TKzK7-Ir_OkVoLMOxDoIL --name ../CenterNet/data/abc/201_400.zip
echo '001_200'
python download_id_name.py --id 1lPYbX8LKnit7RCJgC_RtlHkbojU_O7X1 --name ../CenterNet/data/abc/001_200.zip

######################
echo 'unzip data'
cd ../CenterNet/data/abc
unzip -qq 801_1000.zip
unzip -qq 601_800.zip
unzip -qq 401_600.zip
unzip -qq 201_400.zip
unzip -qq 001_200.zip

rm -rf *.zip

######################
echo 'create images folder in abc'
mkdir 'images'
mv images801_1000/* images
mv images601_800/* images
mv images401_600/* images
mv images201_400/* images
mv images000_200/* images

rm -rf images*_**
#####################
echo 'download label'
mkdir 'label'
cd ../../gdriveAPI
python download_id_name.py --id 1SWsjrSNaRp3CVe9h3Fu41ezkvXcGPy0_ --name ../CenterNet/data/abc/label

#####################

echo 'done!'
