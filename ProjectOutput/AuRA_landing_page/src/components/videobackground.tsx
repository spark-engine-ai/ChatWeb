import React from 'react';
const VideoBackground: React.FC = () => {
  return (
    <div className="video-background">
      <video autoPlay muted loop className="w-full h-full object-cover fixed opacity-20">
        <source src="bgvideo.mp4" type="video/mp4" />
      </video>
    </div>
  );
};
export default VideoBackground;