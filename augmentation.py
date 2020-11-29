import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import json

class Augmentation():
	def __init__(self,operation=None):
		if operation is None:
			operation = ['Rotation']
		self.operation_list = operation

	def load_data(self,image_dir,label_dir):
		image_list = os.listdir(image_dir)
		label_list = os.listdir(label_dir)
		return(image_list,label_list)

	def get_label_points(self,label_path):
		with open(label_path) as f:
			label_data = json.load(f)
		# label_data = label_object.values()
		px = label_data["all_points_x"]
		py = label_data["all_points_y"]
		poly = [(x + 0.5, y + 0.5) for x, y in zip(px, py)]
		poly = [list(ele) for ele in poly]
		for i, ele in enumerate(poly):
			ele.append(0)
		return(poly)

	def get_transform_matrix(self):
		angle = np.radians(10)
		# transformation matrix for Rotation
		M = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
						[np.sin(angle), np.cos(angle), 0],
						[0, 0, 1]])
		return(M)

	def filtering_points(self,height,width,points):
		filtered_points = []
		for point in points:
			if point[0] < 0 or point[1] < 0 or point[0] > width or point[1] > height:
				pass
			else:
				filtered_points.append(point)
		return(filtered_points)

	def operate_single(self,image_path,label_path):
		transform_matrix = self.get_transform_matrix()
		label_points = self.get_label_points(label_path)
		image = cv2.imread(image_path)
		width, height, channel = image.shape
		points_res = [transform_matrix @ ele for ele in label_points]
		points_res = self.filtering_points(height,width,points_res)
		return(points_res)

	def save_files(self,points,filename,image_path):

		with open(filename) as f:
			label_data = json.load(f)
		label_data["all_points_x"] = [ele[0] for ele in points]
		label_data["all_points_y"] = [ele[1] for ele in points]
		saved = json.dumps(label_data,indent=4)
		with open("output/" + filename, "x") as file:
			file.write(saved)
			file.close()
		img = cv2.imread(image_path)
		cv2.imwrite("output/images/" + "frame0_1" + ".jpg",img)
		return(0)


# json_file = os.path.join("labels/via_region_data.json")
# with open(json_file) as f:
# 	imgs_anns = json.load(f)
#
# dataset_dicts = []
# for idx, v in enumerate(imgs_anns.values()):
# 	if idx == 0:
# 		continue
# 	if idx == 2:
# 		break
# 	record = {}
#
# 	filename = os.path.join("sample_images/frame0_1.jpg")
# 	height, width = cv2.imread(filename).shape[:2]
#
# 	record["file_name"] = filename
# 	record["image_id"] = idx
# 	record["height"] = height
# 	record["width"] = width
#
# 	# annos = v["regions"]
# 	# objs = []
# 	# for _, anno in annos.items():
# 	# 	assert not anno["region_attributes"]
# 	# 	anno = anno["shape_attributes"]
# 	px = v["all_points_x"]
# 	py = v["all_points_y"]
# 	poly = [(x + 0.5, y + 0.5) for x, y in zip(px, py)]
# 	#poly = [p for x in poly for p in x]
#
#
#
#
# # read the input image
# img = cv2.imread("sample_images/frame0_1.jpg")
# # convert from BGR to RGB so we can plot using matplotlib
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# # disable x & y axis
#
# res = []
# for point in poly:
# 	cv2.circle(img,(int(point[0]),int(point[1])),1,(0,0,255),3)
# plt.axis('off')
# # show the image
# plt.imshow(img)
# # plt.show()
# # get the image shape
# rows, cols, dim = img.shape
# #angle from degree to radian
# angle = np.radians(10)
# #transformation matrix for Rotation
# M = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
#             	[np.sin(angle), np.cos(angle), 0],
#             	[0, 0, 1]])
# # apply a perspective transformation to the image
#
# poly = [list(ele) for ele in poly]
#
#
# for i, ele in enumerate(poly):
# 	ele.append(0)
#
#
# #
# # poly = [ele.append(0) for ele in poly]
#
# poly_rot = [M @ ele for ele in poly]
#
# rotated_img = cv2.warpPerspective(img, M, (int(cols),int(rows)))
#
# res = []
# for point in poly_rot:
# 	if point[0] < 0 or point[1] < 0 or point[0] > 704 or point[1] > 576:
# 		pass
# 	else:
# 		cv2.circle(img,(int(point[0]),int(point[1])),1,(0,0,255),3)
#
# # disable x & y axis
# plt.axis('off')
# # show the resulting image
# plt.imshow(rotated_img)
# plt.show()
# # save the resulting image to disk
# plt.imsave("sample_images/frame0_1_rot.jpg", rotated_img)