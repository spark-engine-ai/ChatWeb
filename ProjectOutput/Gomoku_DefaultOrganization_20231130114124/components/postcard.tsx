import React from 'react';
const PostCard: React.FC = () => {
  return (
    <div className="bg-white rounded-lg shadow p-4 mt-4">
      {/* Post content */}
      <p className="text-gray-800">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
      {/* Likes */}
      <div className="flex items-center mt-2">
        <svg className="w-4 h-4 text-gray-500 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 8h16M4 16h16"></path>
        </svg>
        <p className="text-gray-600">100 likes</p>
      </div>
      {/* Comments */}
      <div className="flex items-center mt-2">
        <svg className="w-4 h-4 text-gray-500 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
        <p className="text-gray-600">50 comments</p>
      </div>
    </div>
  );
};
export default PostCard;