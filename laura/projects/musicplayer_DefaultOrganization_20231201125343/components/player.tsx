import React, { useState, useRef, useEffect } from 'react';
import { FaPlay, FaPause, FaStepForward, FaStepBackward, FaMusic } from 'react-icons/fa';
import useSound from 'use-sound';
interface PlayerProps {
  selectedSong: string;
  handleSongSelect: (song: string) => void;
}
const Player: React.FC<PlayerProps> = ({ selectedSong, handleSongSelect }) => {
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentSongIndex, setCurrentSongIndex] = useState(0);
  const [duration, setDuration] = useState(0);
  const [currentTime, setCurrentTime] = useState(0);
  const [showSongList, setShowSongList] = useState(false);
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
  useEffect(() => {
    if (selectedSong) {
      const index = songs.findIndex((song) => song.file === selectedSong);
      if (index !== -1) {
        setCurrentSongIndex(index);
      }
    }
  }, [selectedSong]);
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
  const formatTime = (time: number) => {
    const minutes = Math.floor(time / 60);
    const seconds = Math.floor(time % 60);
    return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
  };
  return (
    <>
    <div className="flex bg-white flex-col items-center">
      <div className="flex flex-col items-center mb-4">
        <div className="relative w-24 h-24 mb-2">
          <img src={`/music/${songs[currentSongIndex].image}`} alt={songs[currentSongIndex].title} className="w-full h-full rounded-full object-cover" />
        </div>
        <h2 className="text-lg font-bold">{songs[currentSongIndex].title}</h2>
        <p className="text-sm text-gray-500">{songs[currentSongIndex].composer}</p>
      </div>
      <div className="inset-0 flex items-center justify-center">
        <button className="bg-blue-500 hover:bg-blue-600 text-white rounded-full p-2 mr-2" onClick={handleGoBackSong}>
          <FaStepBackward />
        </button>
        <button className="bg-blue-500 hover:bg-blue-600 text-white rounded-full p-2 mr-2" onClick={handlePlayPause}>
          {isPlaying ? <FaPause /> : <FaPlay />}
        </button>
        <button className="bg-blue-500 hover:bg-blue-600 text-white rounded-full p-2" onClick={handleSkipSong}>
          <FaStepForward />
        </button>
      </div>
      <div className="flex items-center mt-4">
        <input type="range" min="0" max={duration} step="0.01" value={currentTime} onChange={handleSliderChange} />
        <span className="ml-2">{formatTime(currentTime)}</span>
        <span className="ml-2">/{formatTime(duration)}</span>
      </div>
      <audio
        ref={audioRef}
        src={`/music/${songs[currentSongIndex].file}`}
        onLoadedMetadata={() => {
          setDuration(audioRef.current?.duration || 0);
        }}
      />
    </div>
    <div className="border-l border-gray-200 p-6 ml-6">
        <div className="p-4">
          <h2 className="text-xl font-bold mb-4">Playlist</h2>
          {songs.map((song) => (
            <div
              key={song.file}
              className="flex items-center mb-2 cursor-pointer"
              onClick={() => {
                handleSongSelect(song.file);
                setIsPlaying(true);
              }}
            >
              <div className="relative w-8 h-8 rounded-full overflow-hidden mr-2">
                <img src={`/music/${song.image}`} alt={song.title} className="w-full h-full object-cover" />
                <div className="absolute inset-0 flex items-center justify-center bg-black bg-opacity-50 transition-opacity opacity-0 hover:opacity-100">
                  <FaMusic className="text-white" />
                </div>
              </div>
              {song.title}
            </div>
          ))}
        </div>
    </div>
    </>
  );
};
export default Player;
