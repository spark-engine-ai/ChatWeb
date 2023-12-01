import React, { useState, useRef, useEffect } from 'react';
import { FaPlay, FaPause, FaStepForward, FaStepBackward } from 'react-icons/fa';
import useSound from 'use-sound';
const Player: React.FC = () => {
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentSongIndex, setCurrentSongIndex] = useState(0);
  const [duration, setDuration] = useState(0);
  const [currentTime, setCurrentTime] = useState(0);
  const audioRef = useRef<HTMLAudioElement>(null);
  const songs = [
    { title: 'Song 1', composer: 'Composer 1', file: 'song-1.mp3', image: 'song-1.png' },
    { title: 'Song 2', composer: 'Composer 2', file: 'song-2.mp3', image: 'song-2.png' },
    { title: 'Song 3', composer: 'Composer 3', file: 'song-3.mp3', image: 'song-3.png' },
  ];
  const [play, { pause }] = useSound(`/music/${songs[currentSongIndex].file}`, {
    onplay: () => {
      setIsPlaying(true);
      setDuration(audioRef.current?.duration || 0);
    },
    onpause: () => {
      setIsPlaying(false);
    },
    ontimeupdate: () => {
      setCurrentTime(audioRef.current?.currentTime || 0);
    },
    onend: () => {
      handleSkipSong();
    },
  });
  useEffect(() => {
    setDuration(audioRef.current?.duration || 0);
  }, [currentSongIndex]);
  const handlePlayPause = () => {
    if (isPlaying) {
      audioRef.current?.pause();
    } else {
      audioRef.current?.play();
    }
    setIsPlaying(!isPlaying);
  };
  const handleSkipSong = () => {
    setCurrentSongIndex((prevIndex) => (prevIndex + 1) % songs.length);
    setDuration(audioRef.current?.duration || 0);
    setCurrentTime(0);
  };
  const handleGoBackSong = () => {
    setCurrentSongIndex((prevIndex) => (prevIndex - 1 + songs.length) % songs.length);
    setDuration(audioRef.current?.duration || 0);
    setCurrentTime(0);
  };
  const handleSliderChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const time = parseFloat(event.target.value);
    audioRef.current!.currentTime = time;
    setCurrentTime(time);
  };
  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentTime(audioRef.current?.currentTime || 0);
    }, 100);
    return () => {
      clearInterval(interval);
    };
  }, [currentSongIndex]);
  useEffect(() => {
    if (isPlaying) {
      audioRef.current?.play();
    }
  }, [currentSongIndex]);
  return (
    <div className="flex items-center justify-center mb-4">
      <button
        className="bg-blue-500 hover:bg-blue-600 text-white rounded-full p-2 mr-2"
        onClick={handleGoBackSong}
      >
        <FaStepBackward />
      </button>
      <button
        className="bg-blue-500 hover:bg-blue-600 text-white rounded-full p-2 mr-2"
        onClick={handlePlayPause}
      >
        {isPlaying ? <FaPause /> : <FaPlay />}
      </button>
      <button
        className="bg-blue-500 hover:bg-blue-600 text-white rounded-full p-2"
        onClick={handleSkipSong}
      >
        <FaStepForward />
      </button>
      <div className="ml-4">
        <h2 className="text-lg font-bold">{songs[currentSongIndex].title}</h2>
        <p className="text-sm text-gray-500">{songs[currentSongIndex].composer}</p>
      </div>
      <div className="flex items-center ml-4">
        <input
          type="range"
          min="0"
          max={duration}
          step="0.01"
          value={currentTime}
          onChange={handleSliderChange}
        />
        <span className="ml-2">{currentTime.toFixed(2)}</span>
        <span className="ml-2">/{duration.toFixed(2)}</span>
      </div>
      <audio
        ref={audioRef}
        src={`/music/${songs[currentSongIndex].file}`}
        onLoadedMetadata={() => {
          setDuration(audioRef.current?.duration || 0);
        }}
      />
    </div>
  );
};
export default Player;