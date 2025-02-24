#from jetson_inference import detectNet
#from jetson_utils import videoSource, videoOutput
import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.loadImage("/home/nvidia/jetson-inference/data/images/fruit_11.jpg")
#save = jetson.utils.saveImageRGBA("test.png")
#display = jetson.utils.videoOutput("display://0")

#while display.IsStreaming():
img = camera
#img = camera.Capture()
#if img is None:
#	continue
detections = net.Detect(img)
for detection in detections:
	print("-- Classid : " + str(detection.ClassID))
	print("-- Confidence : " + str(detection.Confidence))
	print("-- Left : " + str(detection.Left))
	print("-- Top : "  + str(detection.Top))
	print("-- Right : " + str(detection.Right))
	print("-- Bottom : " + str(detection.Bottom))
	print("-- Width : " + str(detection.Right - detection.Left))
	print("-- Height : " + str(detection.Bottom - detection.Top))
	print("-- Area : " + str((detection.Right - detection.Left) *(detection.Bottom - detection.Top)))
	print("-- Center : " + str((detection.Right - detection.Left)/2) + str((detection.Bottom - detection.Top)/2))
#camera.Render(img)
jetson.utils.saveImageRGBA("test.png", img)
	#display.Render(img)
	#display.SetStatus("Object Detection | Network {:.0f}FPS".format(net.GetNetworkFPS()))
