import React, { useEffect, useState } from 'react';
import { FaMusic } from 'react-icons/fa';
interface SongListProps {
  handleSongSelect: (song: string) => void;
}
const SongList: React.FC<SongListProps> = ({ handleSongSelect }) => {
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
        <div
          key={song.file}
          className="flex items-center mb-2 cursor-pointer"
          onClick={() => {
            handleSongSelect(song.file);
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
  );
};
export default SongList;