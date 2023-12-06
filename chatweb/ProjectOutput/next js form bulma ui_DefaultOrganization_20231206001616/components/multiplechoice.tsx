import React from 'react';
const MultipleChoice: React.FC = () => {
  return (
    <div className="mb-4">
      <h3 className="text-lg font-bold mb-2">Multiple Choice</h3>
      <label className="block">
        <input type="radio" name="multiple-choice" value="option1" />
        Option 1
      </label>
      <label className="block">
        <input type="radio" name="multiple-choice" value="option2" />
        Option 2
      </label>
      <label className="block">
        <input type="radio" name="multiple-choice" value="option3" />
        Option 3
      </label>
    </div>
  );
};
export default MultipleChoice;