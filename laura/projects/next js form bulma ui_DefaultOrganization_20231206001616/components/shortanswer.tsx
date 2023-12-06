import React from 'react';
const ShortAnswer: React.FC = () => {
  return (
    <div className="mb-4">
      <h3 className="text-lg font-bold mb-2">Short Answer</h3>
      <input
        type="text"
        name="short-answer"
        className="border border-gray-300 px-4 py-2 w-full"
      />
    </div>
  );
};
export default ShortAnswer;