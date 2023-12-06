import React from 'react';
import { FaGithub } from 'react-icons/fa';
const Logo: React.FC = () => {
  return (
    <div className="flex justify-center items-center h-screen">
      <FaGithub size={100} />
    </div>
  );
};
export default Logo;