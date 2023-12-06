import React from 'react';
import { FaGithub } from 'react-icons/fa';
const ButtonRow: React.FC = () => {
  return (
    <div className="flex justify-center items-center mt-4">
      <div className="flex flex-row">
        <div className="m-4">
          <a href="https://github.com/spark-engine-ai/ChatWeb" target="_blank" rel="noopener noreferrer">
            <button className="flex items-center border border-white rounded px-4 py-2 bg-black text-white">
              <FaGithub size={20} className="mr-2" />
              <span className="font-bold">Github</span>
            </button>
          </a>
        </div>
      </div>
    </div>
  );
};
export default ButtonRow;