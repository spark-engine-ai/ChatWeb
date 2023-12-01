import React, { useState } from 'react';
import Player from './player';
const Main: React.FC = () => {
  const [selectedSong, setSelectedSong] = useState('');
  const handleSongSelect = (song: string) => {
    setSelectedSong(song);
  };
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h1 className="text-3xl font-bold mb-4">Music Player</h1>
      <div className="border bg-white rounded-lg shadow-lg p-4 flex">
        <Player selectedSong={selectedSong} handleSongSelect={handleSongSelect} />
      </div>
    </div>
  );
};
export default Main;
