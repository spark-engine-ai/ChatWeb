import React, { useState } from 'react';
import Player from './player';
import SongList from './songList';
const Main: React.FC = () => {
  const [showPlaylist, setShowPlaylist] = useState(false);
  const handleTogglePlaylist = () => {
    setShowPlaylist(!showPlaylist);
  };
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h1 className="text-3xl font-bold mb-4">Music Player</h1>
      <div className="border rounded-lg shadow-lg p-4">
        <Player />
      </div>
      <button
        className="bg-blue-500 hover:bg-blue-600 text-white rounded-full p-2 mt-4"
        onClick={handleTogglePlaylist}
      >
        {showPlaylist ? 'Hide Playlist' : 'Show Playlist'}
      </button>
      {showPlaylist && <SongList />}
    </div>
  );
};
export default Main;