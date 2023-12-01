import React from 'react';
import useSound from 'use-sound';
export const playlist = [
  { id: 1, title: 'Song 1', artist: 'Artist 1', url: '/music/song-1.mp3' },
  { id: 2, title: 'Song 2', artist: 'Artist 2', url: '/music/song-2.mp3' },
  { id: 3, title: 'Song 3', artist: 'Artist 3', url: '/music/song-3.mp3' },
];
const Playlist: React.FC = ({ handleSongClick }) => {
  return (
    <div className="w-64">
      <h2 className="text-xl font-bold mb-4">Playlist</h2>
      {playlist.map((song) => (
        <div key={song.id} className="mb-2">
          <p className="text-lg font-medium" onClick={() => handleSongClick(song)}>
            {song.title}
          </p>
          <p className="text-gray-500">{song.artist}</p>
        </div>
      ))}
    </div>
  );
};
export default Playlist;
