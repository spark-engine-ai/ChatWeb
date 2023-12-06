import React from 'react';

const Info: React.FC = () => {
  return (
    <div className="bg-black p-6 rounded-lg border shadow-lg m-8">
      <h2 className="text-2xl font-semibold text-white mb-8">Welcome to AuRA</h2>
      <p className="text-white mb-4">
        AuRA is a GPT-powered agent pipeline built by the team at <a href="https://sparkengine.ai"><b>Spark Engine</b></a>, dedicated to automating the workflow of React-based applications.
      </p>
      <p className="text-white mb-4">
        Eliminate the need to code 99% of the time by conversing with a powerful team of AIs. Compatible with out-of-the-box frameworks and UI kits, as well as custom configurations for those looking to support their preferences.
      </p>
      <p className="text-white">
        Find your AuRA, and welcome to the new age of development.
      </p>
    </div>
  );
};

export default Info;
