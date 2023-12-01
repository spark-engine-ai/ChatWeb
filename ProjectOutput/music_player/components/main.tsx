import React, { useState } from 'react';
import Player from './player';
import Playlist from './playlist';
const Main: React.FC = () => {
  const [currentSong, setCurrentSong] = useState(null);
  const [previousSong, setPreviousSong] = useState(null);
  const handleSongClick = (song) => {
    setPreviousSong(currentSong);
    setCurrentSong(song);
  };
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h1 className="text-3xl font-bold mb-4">Music Player</h1>
      <Player currentSong={currentSong} previousSong={previousSong} />
      <Playlist handleSongClick={handleSongClick} />
    </div>
  );
};
export default Main;