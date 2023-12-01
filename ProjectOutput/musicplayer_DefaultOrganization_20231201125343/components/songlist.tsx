import React, { useEffect, useState } from 'react';
import { FaMusic } from 'react-icons/fa';
const SongList: React.FC = () => {
  const [songs, setSongs] = useState<{ title: string; composer: string; file: string; image: string }[]>([]);
  useEffect(() => {
    fetch('/music')
      .then((response) => response.json())
      .then((data) => setSongs(data.songs))
      .catch((error) => console.error('Error fetching songs:', error));
  }, []);
  return (
    <div className="max-w-md w-full bg-white rounded-lg shadow-lg p-4">
      <h2 className="text-xl font-bold mb-4">Song List</h2>
      {songs.map((song) => (
        <div key={song.file} className="flex items-center mb-2">
          <img src={`/music/${song.image}`} alt={song.title} className="w-8 h-8 rounded-full mr-2" />
          <FaMusic className="mr-2" />
          {song.title}
        </div>
      ))}
    </div>
  );
};
export default SongList;