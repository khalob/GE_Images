import boto3, base64
#
client=boto3.client('rekognition')

#It is possible to upload the images to a aws bucket and run detection from there
def detectFire(imageFileName):
	response = client.detect_labels(Image={'S3Object':{'Bucket': 'tba-squad','Name':imageFileName}},MinConfidence=70)
	detectedFeatures=[]
	print (response['Labels'])
	for i in range(len(response['Labels'])):
		"""if detectedFeatures[i][1]=='Fire:
			print("Fire")"""
		#print(i)
		if(detectedFeatures==[]):
			detectedFeatures=[response['Labels'][i]['Name']]
		else:
			detectedFeatures.append(response['Labels'][i]['Name'])
	print(detectedFeatures)
	fireDetected=False
	for i in range(len(detectedFeatures)):
		detectedFeatures[i]=detectedFeatures[i].lower()
		if(detectedFeatures[i]=='fire' or detectedFeatures[i]=="flame" or detectedFeatures[i]=="burn"):
			fireDetected=True
	return fireDetected
def uploadImage(imageFileName):
	s3=boto3.client('s3')
	img=open("images/"+imageFileName,"rb")
	s3.upload_file(imageFileName,'tba-squad',imageFileName)

print("Is there a fire?",detectFire("fire.jpg"))
