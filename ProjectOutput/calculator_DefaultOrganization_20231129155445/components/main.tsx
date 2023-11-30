import React from 'react';
import Calculator from './calculator';
import Terminal from './terminal';
const Main: React.FC = () => {
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <Calculator />
      <Terminal />
    </div>
  );
};
export default Main;