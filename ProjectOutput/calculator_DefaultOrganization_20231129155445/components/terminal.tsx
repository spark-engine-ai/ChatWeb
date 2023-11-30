import React, { useState } from 'react';
const Terminal: React.FC = () => {
  const [history, setHistory] = useState<string[]>([]);
  const handleAddToHistory = (calculation: string) => {
    setHistory((prevHistory) => [...prevHistory, calculation]);
  };
  return (
    <div className="bg-green-200 rounded-lg shadow p-4">
      <h2 className="text-lg font-bold mb-2">Calculation History</h2>
      <ul>
        {history.map((calculation, index) => (
          <li key={index}>{calculation}</li>
        ))}
      </ul>
    </div>
  );
};
export default Terminal;