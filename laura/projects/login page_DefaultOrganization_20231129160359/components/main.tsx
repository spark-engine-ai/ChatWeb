// components/main.tsx
import React, { useState } from 'react';
import Login from './login';
import Signup from './signup';
const Main: React.FC = () => {
  const [activeTab, setActiveTab] = useState('login');
  const handleTabChange = (tab: string) => {
    setActiveTab(tab);
  };
  return (
    <div className="flex justify-center items-center h-screen">
      <div className="w-96 bg-white shadow-lg rounded-lg p-8">
        <h1 className="text-2xl font-bold mb-6">ChatWeb Login/Signup</h1>
        <div className="flex justify-between mb-6">
          <button
            className={`px-4 py-2 rounded-tl-lg ${
              activeTab === 'login' ? 'bg-blue-500 text-white' : 'bg-gray-200'
            }`}
            onClick={() => handleTabChange('login')}
          >
            Login
          </button>
          <button
            className={`px-4 py-2 rounded-tr-lg ${
              activeTab === 'signup' ? 'bg-blue-500 text-white' : 'bg-gray-200'
            }`}
            onClick={() => handleTabChange('signup')}
          >
            Signup
          </button>
        </div>
        {activeTab === 'login' ? <Login /> : <Signup />}
      </div>
    </div>
  );
};
export default Main;