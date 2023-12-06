import React from 'react';
const Textarea: React.FC = () => {
  return (
    <div className="mb-4">
      <h3 className="text-lg font-bold mb-2">Textarea</h3>
      <textarea
        name="textarea"
        className="border border-gray-300 px-4 py-2 w-full"
        rows={4}
      ></textarea>
    </div>
  );
};
export default Textarea;