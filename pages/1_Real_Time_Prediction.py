import streamlit as st 
import pages.face_rec as face_rec
from streamlit_webrtc import webrtc_streamer
from streamlit_custom_notification_box import custom_notification_box as scnb
import av
import time

# st.set_page_config(page_title='Predictions')
st.subheader('Real-Time Attendance System')

def AlertBox(wht_msg):
    styles = {'material-icons':{'color': '#FF0000'},
            'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'},
            'notification-text': {'':''},
            'close-button':{'':''},
            'link':{'':''}}

    scnb(icon='info', 
        textDisplay=wht_msg, 
        externalLink='', 
        url='#', 
        styles=styles, 
        key="foo")

# Retrieve the data from Redis Database
with st.spinner('Retrieving Data from Redis DB ...'):    
    redis_face_db = face_rec.retrive_data(name='academy:register')
    st.dataframe(redis_face_db)
    
st.success("Data successfully retrieved from Redis")

# Time settings
waitTime = 30  # Time in seconds
setTime = time.time()
realtimepred = face_rec.RealTimePred()  # Real-time prediction class
face_scan_success = False  # Flag to indicate successful face scan

# Real Time Prediction
# Streamlit WebRTC
# Callback function
def video_frame_callback(frame):
    global setTime, face_scan_success
    
    img = frame.to_ndarray(format="bgr24")  # Convert frame to numpy array
    # Perform face prediction
    pred_img = realtimepred.face_prediction(img, redis_face_db,
                                            'facial_features', ['Name', 'Role'], thresh=0.5)
    
    timenow = time.time()
    difftime = timenow - setTime
    if difftime >= waitTime:
        realtimepred.saveLogs_redis()
        setTime = time.time()  # Reset timer
        st.info('Successfully scanned face!')  # Display info popup
        AlertBox("Tahniah! Kehadiran anda telah direkodkan.")
        face_scan_success = True  # Set flag for successful face scan
        
    # Convert processed image back to VideoFrame
    return av.VideoFrame.from_ndarray(pred_img, format="bgr24")

webrtc_streamer(key="realtimePrediction", video_frame_callback=video_frame_callback,
                rtc_configuration={
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    })
