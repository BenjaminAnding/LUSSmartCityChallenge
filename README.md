# LUSFiber Smart City Challenge

This is a python script that pulls down 100 frames from each of the cameras at each Ambassador Caffrey intersection in Lafayette, Louisiana from the Lafayette Consolidated Government website. "Image Not Available" frames from broken feed are then pruned by comparing RGB data using PIL image tools.  

Files are output in shorthand format of intersection road names followed by datetime format timestamp of data collection time.  

Files are scrutinized using OpenCV tools to find potential car locations (using Harris corners algorithm) and displayed as matte with corners overlayed with console log of number of pixels considered corners. 

This project was part of the winning submission of the LUSFiber Smart City Challenge hackathon in Lafayette, Louisiana. 
