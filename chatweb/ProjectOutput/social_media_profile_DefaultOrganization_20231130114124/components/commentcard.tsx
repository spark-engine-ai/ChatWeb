import React from 'react';
const CommentCard: React.FC = () => {
  return (
    <div className="bg-white rounded-lg shadow p-4 mt-4">
      {/* Commenter name */}
      <h4 className="text-lg font-bold">Jane Smith</h4>
      {/* Comment content */}
      <p className="text-gray-800">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    </div>
  );
};
export default CommentCard;