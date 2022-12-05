import fitz
import numpy as np
import cv2
def bts_to_img(bts):
        '''
        :param bts: results from image_to_bts
        '''
        
        buff = np.fromstring(bts, np.uint8)
        buff = buff.reshape(1, -1)
        img = cv2.imdecode(buff, cv2.IMREAD_COLOR)
        return img
def extract_img(file):
    # open the file
    x=0
    pdf_file = fitz.open(file)
    #print("No. of pages:",len(pdf_file))
    # STEP 3
    # iterate over PDF pages
    count1=0
    for page_index in range(len(pdf_file)):
        
        # get the page itself

        page = pdf_file[page_index]
        image_list = page.getImageList()
        
        # printing number of images found in this page
        if image_list:
            #print(f"Total {len(image_list)} images in page {page_index}")
            if(len(image_list)>1):
                count=0
                for image_index, img in enumerate(page.getImageList(), start=2):

                    #print("index",image_index)

                    xref = img[0]  
                    # extract the image bytes
                    base_image = pdf_file.extractImage(xref)
                    #print("!!!",base_image)
                    image_bytes = base_image["image"] 
                    res_img=bts_to_img(image_bytes)  
                    #print("res_img",res_img) 
                    if(count>0):
                        cv2.imwrite("./images/{}.jpg".format(x),res_img)
                        x+=1
                    # get the image extension
                    image_ext = base_image["ext"]
                    count=count+1
                    #print(image_ext)         
        else:
            return ("No images found on page", page_index)


extract_img("./Merico_invoice-Hari_Shyam_Bind(1).pdf")

