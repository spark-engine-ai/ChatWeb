// components/features.tsx
import React from 'react';
const Features: React.FC = () => {
  return (
    <section className="bg-white py-8">
      <div className="container mx-auto px-4">
        <h2 className="text-3xl font-bold mb-4">Features</h2>
        <div className="grid grid-cols-3 gap-4">
          <div className="p-4 bg-gray-200">
            <h3 className="text-xl font-bold mb-2">Feature 1</h3>
            <p className="text-gray-700">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            </p>
          </div>
          <div className="p-4 bg-gray-200">
            <h3 className="text-xl font-bold mb-2">Feature 2</h3>
            <p className="text-gray-700">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            </p>
          </div>
          <div className="p-4 bg-gray-200">
            <h3 className="text-xl font-bold mb-2">Feature 3</h3>
            <p className="text-gray-700">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};
export default Features;