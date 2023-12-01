import React, { useEffect, useRef, useState } from 'react';
import { FaPlay, FaPause, FaForward, FaBackward } from 'react-icons/fa';
import useSound from 'use-sound';
const Player: React.FC = ({ currentSong, previousSong }) => {
  const audioRef = useRef(null);
  const [duration, setDuration] = useState(0);
  useEffect(() => {
    if (currentSong) {
      audioRef.current.src = currentSong.url;
      audioRef.current.play();
    }
  }, [currentSong]);
  useEffect(() => {
    audioRef.current.addEventListener('loadedmetadata', () => {
      setDuration(audioRef.current.duration);
    });
  }, []);
  const handlePlayPause = () => {
    if (audioRef.current.paused) {
      audioRef.current.play();
    } else {
      audioRef.current.pause();
    }
  };
  const handleSkip = () => {
    audioRef.current.currentTime += 10;
  };
  const handleBack = () => {
    if (previousSong) {
      setCurrentSong(previousSong);
    }
  };
  return (
    <div className="flex flex-col items-center">
      <audio ref={audioRef} />
      <div className="flex items-center">
        <button onClick={handleBack} className="mr-4">
          <FaBackward />
        </button>
        <button onClick={handleSkip} className="mr-4">
          <FaForward />
        </button>
        <button onClick={handlePlayPause}>
          {audioRef.current && !audioRef.current.paused ? <FaPause /> : <FaPlay />}
        </button>
        {currentSong && (
          <p className="text-gray-500 ml-4">
            {Math.floor(audioRef.current.currentTime)} / {Math.floor(duration)}
          </p>
        )}
      </div>
    </div>
  );
};
export default Player;