import React from 'react';
import { FaGithub } from 'react-icons/fa';
import { MdArrowBack } from 'react-icons/md';

const ButtonRow: React.FC = () => {
  return (
    <>
    <div className="flex justify-center items-center mt-4">
      <div className="flex flex-row">
      <div className="m-4">
        <a href="https://sparkengine.ai" style={{cursor:'pointer'}}>
          <button className="flex items-center rounded px-4 py-2 bg-blue text-white" style={{cursor:'pointer'}}>
            <MdArrowBack size={16} className="mr-2" />
            <span className="font-bold">Go back</span>
          </button>
        </a>
      </div>
        <div className="m-4">
          <a href="https://github.com/spark-engine-ai/ChatWeb" target="_blank" style={{cursor:'pointer'}}>
            <button className="flex items-center border border-white rounded px-4 py-2 bg-black text-white" style={{cursor:'pointer'}}>
              <FaGithub size={20} className="mr-2" />
              <span className="font-bold">Github</span>
            </button>
          </a>
        </div>
      </div>
    </div>
    </>
  );
};
export default ButtonRow;

//<div className="m-4">
//  <a href="#" rel="noopener noreferrer">
//    <button className="flex items-center rounded px-4 py-2 bg-gray text-white">
//      <span className="font-bold">Docs</span>
//    </button>
//  </a>
//</div>
