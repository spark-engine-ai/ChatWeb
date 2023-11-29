import React from 'react';
const Sections = () => {
  return (
    <section className="container mx-auto py-8">
      <div className="grid grid-cols-3 gap-4">
        <div className="bg-gray-200 p-4">
          <h2 className="text-lg font-bold mb-2">Section 1</h2>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </div>
        <div className="bg-gray-200 p-4">
          <h2 className="text-lg font-bold mb-2">Section 2</h2>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </div>
        <div className="bg-gray-200 p-4">
          <h2 className="text-lg font-bold mb-2">Section 3</h2>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </div>
      </div>
    </section>
  );
};
export default Sections;