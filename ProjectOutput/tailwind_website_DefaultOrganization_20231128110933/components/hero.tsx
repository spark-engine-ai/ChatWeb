// components/hero.tsx
import React from 'react';
const Hero: React.FC = () => {
  return (
    <section className="bg-gray-100 py-8">
      <div className="container mx-auto px-4">
        <h2 className="text-3xl font-bold mb-4">Welcome to our Website</h2>
        <p className="text-gray-700">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam
          aliquam, mauris vitae tincidunt fringilla, elit nunc rutrum nunc, eu
          tempor urna nunc id velit. Sed nec diam ac nunc rutrum malesuada.
        </p>
      </div>
    </section>
  );
};
export default Hero;