import React from 'react';
import ProfileCard from './ProfileCard';
import ProfileStats from './ProfileStats';
import ProfileActions from './ProfileActions';
import PostCard from './PostCard';
import CommentCard from './CommentCard';
const Main: React.FC = () => {
  return (
    <div className="container mx-auto">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="col-span-1">
          <ProfileCard />
          <ProfileStats />
          <ProfileActions />
        </div>
        <div className="col-span-2">
          <PostCard />
          <CommentCard />
        </div>
      </div>
    </div>
  );
};
export default Main;