import React from 'react';
const ProfileStats: React.FC = () => {
  return (
    <div className="bg-white rounded-lg shadow p-4 mt-4">
      <div className="flex justify-between">
        <div>
          <h3 className="text-lg font-bold">Followers</h3>
          <p className="text-gray-600">1000</p>
        </div>
        <div>
          <h3 className="text-lg font-bold">Following</h3>
          <p className="text-gray-600">500</p>
        </div>
        <div>
          <h3 className="text-lg font-bold">Posts</h3>
          <p className="text-gray-600">50</p>
        </div>
      </div>
    </div>
  );
};
export default ProfileStats;