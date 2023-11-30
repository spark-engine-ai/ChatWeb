import React from 'react';
const ProfileActions: React.FC = () => {
  return (
    <div className="bg-white rounded-lg shadow p-4 mt-4">
      <button className="bg-blue-500 text-white px-4 py-2 rounded-lg">Like</button>
      <button className="bg-blue-500 text-white px-4 py-2 rounded-lg ml-2">Follow</button>
      <button className="bg-blue-500 text-white px-4 py-2 rounded-lg ml-2">Edit Profile</button>
    </div>
  );
};
export default ProfileActions;