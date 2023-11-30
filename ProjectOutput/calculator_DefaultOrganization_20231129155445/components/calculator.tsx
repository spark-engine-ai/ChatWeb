import React, { useState } from 'react';
import { evaluate } from 'mathjs';
const Calculator: React.FC = () => {
  const [expression, setExpression] = useState('');
  const [result, setResult] = useState('');
  const handleButtonClick = (value: string) => {
    if (value === '=') {
      handleCalculate();
    } else {
      setExpression((prevExpression) => prevExpression + value);
    }
  };
  const handleCalculate = () => {
    try {
      const calculatedResult = evaluate(expression);
      setResult(calculatedResult.toString());
    } catch (error) {
      setResult('Error');
    }
  };
  return (
    <div className="bg-white rounded-lg shadow p-4 mb-4">
      <div className="mb-4">
        <input
          type="text"
          className="w-full p-2 border border-gray-300 rounded"
          value={expression}
          onChange={(e) => setExpression(e.target.value)}
        />
      </div>
      <div className="flex justify-between mb-4">
        <button
          className="w-1/4 p-2 border border-gray-300 rounded"
          onClick={() => handleButtonClick('1')}
        >
          1
        </button>
        <button
          className="w-1/4 p-2 border border-gray-300 rounded"
          onClick={() => handleButtonClick('2')}
        >
          2
        </button>
        <button
          className="w-1/4 p-2 border border-gray-300 rounded"
          onClick={() => handleButtonClick('3')}
        >
          3
        </button>
        <button
          className="w-1/4 p-2 border border-gray-300 rounded"
          onClick={() => handleButtonClick('+')}
        >
          +
        </button>
      </div>
      <div>
        <button
          className="w-full p-2 bg-green-500 text-white rounded"
          onClick={handleCalculate}
        >
          Calculate
        </button>
      </div>
      <div className="mt-4">
        <input
          type="text"
          className="w-full p-2 border border-gray-300 rounded"
          value={result}
          readOnly
        />
      </div>
    </div>
  );
};
export default Calculator;