import streamlit as st
import subprocess
import os
from pathlib import Path
import time

# Page config
st.set_page_config(
    page_title="Manim Animation Player",
    page_icon="🎬",
    layout="wide"
)

# Title and description
st.title("🎬 Manim Animation Player")
st.markdown("### Visualize Mathematical Concepts and CS Algorithms")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    quality = st.selectbox(
        "Video Quality",
        ["low_quality", "medium_quality", "high_quality", "production_quality"],
        index=1
    )
    
    st.markdown("---")
    st.markdown("### 📚 About")
    st.info("This app renders Manim animations from your code. Select a scene and click 'Render' to generate the animation.")

# Main content
tab1, tab2, tab3 = st.tabs(["🎥 Render Animation", "📁 View Rendered Videos", "📝 Code"])

with tab1:
    st.header("Render Manim Animation")
    
    # Scene selection
    scene_name = st.text_input("Scene Name", value="BeautifulIntro", help="Enter the name of the scene class from main.py")
    
    # Render button
    if st.button("🎬 Render Animation", type="primary"):
        with st.spinner(f"Rendering {scene_name}..."):
            try:
                # Define quality flags
                quality_flags = {
                    "low_quality": "-ql",
                    "medium_quality": "-qm",
                    "high_quality": "-qh",
                    "production_quality": "-qp"
                }
                
                # Run manim command
                cmd = f"manim {quality_flags[quality]} main.py {scene_name}"
                
                # Create a placeholder for output
                output_placeholder = st.empty()
                output_placeholder.info(f"Running command: `{cmd}`")
                
                # Run the command
                process = subprocess.Popen(
                    cmd,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    cwd=os.getcwd()
                )
                
                # Wait for completion
                stdout, stderr = process.communicate()
                
                if process.returncode == 0:
                    st.success(f"✅ Successfully rendered {scene_name}!")
                    
                    # Find the rendered video
                    video_path = None
                    quality_map = {
                        "low_quality": "480p15",
                        "medium_quality": "720p30",
                        "high_quality": "1080p60",
                        "production_quality": "1080p60"
                    }
                    
                    video_dir = f"media/videos/main/{quality_map[quality]}"
                    if os.path.exists(video_dir):
                        videos = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]
                        if videos:
                            # Get the most recent video
                            video_path = os.path.join(video_dir, sorted(videos)[-1])
                            
                            st.video(video_path)
                            st.balloons()
                else:
                    st.error("❌ Rendering failed!")
                    with st.expander("Show Error Details"):
                        st.code(stderr if stderr else stdout)
                        
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")

with tab2:
    st.header("Rendered Videos")
    
    # Check for existing videos
    media_path = Path("media/videos/main")
    
    if media_path.exists():
        # Find all quality directories
        quality_dirs = [d for d in media_path.iterdir() if d.is_dir()]
        
        if quality_dirs:
            for quality_dir in quality_dirs:
                st.subheader(f"📂 {quality_dir.name}")
                
                # List all videos in this quality
                videos = list(quality_dir.glob("*.mp4"))
                
                if videos:
                    for video in videos:
                        col1, col2 = st.columns([3, 1])
                        
                        with col1:
                            st.video(str(video))
                        
                        with col2:
                            st.markdown(f"**File:** {video.name}")
                            st.markdown(f"**Size:** {video.stat().st_size / (1024*1024):.2f} MB")
                            st.markdown(f"**Modified:** {time.ctime(video.stat().st_mtime)}")
                else:
                    st.info("No videos found in this quality.")
        else:
            st.warning("No rendered videos found. Render an animation first!")
    else:
        st.warning("No media directory found. Render an animation first!")

with tab3:
    st.header("Current Code - main.py")
    
    # Read and display the main.py file
    try:
        with open("main.py", "r", encoding="utf-8") as f:
            code = f.read()
        
        st.code(code, language="python", line_numbers=True)
        
        st.markdown("---")
        st.info("💡 **Tip:** Edit the code in your IDE and reload this page to see updates.")
        
    except Exception as e:
        st.error(f"Could not read main.py: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Made with ❤️ using Manim & Streamlit</p>
        <p>🎬 Visualizing Mathematics & Computer Science</p>
    </div>
    """,
    unsafe_allow_html=True
)
