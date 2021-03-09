import cv2
import argparse
# import orien_lines
import datetime
from imutils.video import VideoStream
from Common_TFOD import detector_utils as detector_utils
import pandas as pd
from datetime import date
import os
import xlrd
from xlwt import Workbook
from xlutils.copy import copy 
import numpy as np

lst1=[]
lst2=[]
ap = argparse.ArgumentParser()
ap.add_argument('-d', '--display', dest='display', type=int,
                        default=1, help='Display the detected images using OpenCV. This reduces FPS')
args = vars(ap.parse_args())

detection_graph, sess = detector_utils.load_inference_graph()

# def save_data(no_of_time_hand_detected, no_of_time_hand_crossed):
#
#     try:
#         today = date.today()
#         today=str(today)
#         #loc = (r'C:\Users\rahul.tripathi\Desktop\result.xls')
#
#         rb = xlrd.open_workbook('result.xls')
#         sheet = rb.sheet_by_index(0)
#         sheet.cell_value(0, 0)
#
#
#         #print(sheet.nrows)
#         q=sheet.cell_value(sheet.nrows-1,1)
#
#         rb = xlrd.open_workbook('result.xls')
#         #rb = xlrd.open_workbook(loc)
#         wb=copy(rb)
#         w_sheet=wb.get_sheet(0)
#
#         if q==today:
#             w=sheet.cell_value(sheet.nrows-1,2)
#             e=sheet.cell_value(sheet.nrows-1,3)
#             w_sheet.write(sheet.nrows-1,2,w+no_of_time_hand_detected)
#             w_sheet.write(sheet.nrows-1,3,e+no_of_time_hand_crossed)
#             wb.save('result.xls')
#         else:
#             w_sheet.write(sheet.nrows,0,sheet.nrows)
#             w_sheet.write(sheet.nrows,1,today)
#             w_sheet.write(sheet.nrows,2,no_of_time_hand_detected)
#             w_sheet.write(sheet.nrows,3,no_of_time_hand_crossed)
#             wb.save('result.xls')
#     except FileNotFoundError:
#         today = date.today()
#         today=str(today)
#
#
#         # Workbook is created
#         wb = Workbook()
#
#         # add_sheet is used to create sheet.
#         sheet = wb.add_sheet('Sheet 1')
#
#         sheet.write(0, 0, 'Sl.No')
#         sheet.write(0, 1, 'Date')
#         sheet.write(0, 2, 'Number of times hand detected')
#         sheet.write(0, 3, 'Number of times hand crossed')
#         m=1
#         sheet.write(1, 0, m)
#         sheet.write(1, 1, today)
#         sheet.write(1, 2, no_of_time_hand_detected)
#         sheet.write(1, 3, no_of_time_hand_crossed)
#
#         wb.save('result.xls')
        
if __name__ == '__main__':
    # Detection confidence threshold to draw bounding box
    score_thresh = 0.55
    
    #vs = cv2.VideoCapture('rtsp://192.168.1.64')
    # vs = VideoStream(0).start()
    cap = cv2.VideoCapture('traffic2.mp4')
    im_width = int(cap.get(3))
    im_height = int(cap.get(4))
    # fourcc = cv2.VideoWriter_fourcc(*'avc1')
    # outfilename = os.path.join("output", "out_" + os.path.basename('traffic2.mp4'))
    # out = cv2.VideoWriter(outfilename, fourcc, 30.0, (im_width, im_height))
    #Oriendtation of machine    
    Orientation= 'bt'


    # Used to calculate fps
    start_time = datetime.datetime.now()
    num_frames = 0

    # im_height, im_width = (None, None)
    # cv2.namedWindow('Collision', cv2.WINDOW_NORMAL)
    def count_no_of_times(lst):
        x=y=cnt=0
        for i in lst:
            x=y
            y=i
            if x==0 and y==1: 
                cnt=cnt+1
        return cnt 
    try:
        # while True:
        #     frame = vs.read()
        #     frame = np.array(frame)
        #     #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #
        #     if im_height == None:
        #         im_height, im_width = frame.shape[:2]
        #
        #     # Convert image to rgb since opencv loads images in bgr, if not accuracy will decrease
        #     try:
        #         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #     except:
        #         print("Error converting to RGB")
        #     #cv2.line(img=frame, pt1=(0, Line_Position1), pt2=(frame.shape[1], Line_Position1), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        #
        #     #cv2.line(img=frame, pt1=(0, Line_Position2), pt2=(frame.shape[1], Line_Position2), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        #
        #     # Run image through tensorflow graph
        #     boxes, scores, classes,num = detector_utils.detect_objects(
        #         frame, detection_graph, sess)
        #     # final_score = np.squeeze(scores)
        #     count1 = 0
        #     for i in range(len(classes)):
        #         if scores is None or scores[i] > score_thresh:
        #             count1 = count1 + 1
        #     num_face_detect = count1
        #     # Line_Position2=orien_lines.drawsafelines(frame,Orientation,Line_Perc1,Line_Perc2)
        #     # Draw bounding boxeses and text
        #     point_1,point_2,ID_1 =detector_utils.get_points_frame(
        #         num_face_detect, score_thresh, scores, boxes, classes, im_width, im_height, frame,Orientation)
        #
        #     midpoints,collectn,height = detector_utils.get_mid_point(point_1,point_2,num_face_detect)
        #     distance = detector_utils.get_distance(midpoints,height,num_face_detect)
        #     close = detector_utils.get_closest(distance,num_face_detect,300)# After Doing some RnD we found this Thresh Hold
        #     detector_utils.draw_box(frame,collectn,close,num_face_detect,scores ,ID_1)
        #
        #     # lst1.append(a)
        #     # lst2.append(b)
        #     # no_of_time_hand_detected=no_of_time_hand_crossed=0
        #     # Calculate Frames per second (FPS)
        #     num_frames += 1
        #     elapsed_time = (datetime.datetime.now() -
        #                     start_time).total_seconds()
        #     fps = num_frames / elapsed_time
        #
        #     if args['display']:
        #
        #         # Display FPS on frame
        #         detector_utils.draw_text_on_image("FPS : " + str("{0:.2f}".format(fps)), frame)
        #         cv2.imshow('Detection', cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        #         if cv2.waitKey(25) & 0xFF == ord('q'):
        #             cv2.destroyAllWindows()
        #             vs.stop()
        #             break
        
        # no_of_time_hand_detected=count_no_of_times(lst2)
        #no_of_time_hand_detected=b
        # no_of_time_hand_crossed=count_no_of_times(lst1)
        #print(no_of_time_hand_detected)
        #print(no_of_time_hand_crossed)
        # save_data(no_of_time_hand_detected, no_of_time_hand_crossed)


        while (cap.isOpened()):
            ret, frame = cap.read()

            # try:
            #     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # except:
            #     print("Error converting to RGB")
            if ret == True:

                boxes, scores, classes, num = detector_utils.detect_objects(
                    frame, detection_graph, sess)
                count1 = 0
                for i in range(len(classes)):
                    if scores is None or scores[i] > score_thresh:
                        count1 = count1 + 1
                num_Vehicle_detect = count1
                point_1, point_2, ID_1 = detector_utils.get_points_frame(
                            num_Vehicle_detect, score_thresh, scores, boxes, classes, im_width, im_height, frame,Orientation)
                midpoints, collectn, height = detector_utils.get_mid_point(point_1, point_2, num_Vehicle_detect)
                distance = detector_utils.get_distance(midpoints,height,num_Vehicle_detect)
                close = detector_utils.get_closest(distance,midpoints,num_Vehicle_detect)# After Doing some RnD we found this Thresh Hold
                # close = set()
                # cv2.line(img=frame, pt1=(840, 620), pt2=(840, 390), color=(0, 0, 255), thickness=2, lineType=8, shift=0)
                pts = np.array([[220,620], [490,390],[840,390], [1100,620]],np.int32)
                cv2.polylines(frame,[pts],True, (255,0,0), 3)
                detector_utils.draw_box(frame,distance,height ,collectn,midpoints,close,num_Vehicle_detect,scores ,ID_1)

                # out.write(frame)
                cv2.imshow('Collision', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        # out.release()
        cv2.destroyAllWindows()

        # print("Average FPS: ", str("{0:.2f}".format(fps)))
        
    except KeyboardInterrupt: 
        no_of_time_hand_detected=count_no_of_times(lst2)
        no_of_time_hand_crossed=count_no_of_times(lst1)
        today = date.today()
        # save_data(no_of_time_hand_detected, no_of_time_hand_crossed)
        # print("Average FPS: ", str("{0:.2f}".format(fps)))